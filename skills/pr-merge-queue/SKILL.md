---
name: PR Merge Queue
description: Serialize merging of PRs opted into a lightweight merge queue — one at a time, refreshing the next in line against the new base immediately after each merge
var: ""
tags: [dev, meta]
---
> **${var}** — Repo (owner/repo) to target. If empty, uses every repo in memory/watched-repos.md.
> Env: `MERGE_QUEUE_DRY_RUN=1` logs intent without merging or updating branches.

`auto-merge` merges every independently-qualifying PR it finds in one run, up to `MAX_AUTO_MERGE`. That's fine when PRs are unrelated. It is not fine when several open PRs touch the same files (a shared lockfile, `aeon.yml`, a generated catalog) — merging two of them back-to-back means the second lands against a base its own CI never actually saw, and a semantic conflict that CI would have caught ships silently. `pr-merge-queue` is the serialized lane for exactly those PRs: opt in with a label, and this skill merges strictly one at a time, immediately refreshing whichever PR becomes the new head so its checks re-run against the real, current base before it's ever considered for merge.

It does not replace `auto-merge` — most PRs don't need this. It only acts on PRs a human (or another skill) has explicitly labeled `merge-queue`.

Read `memory/MEMORY.md` and `memory/watched-repos.md` for repos to target.
Read the last 2 days of `memory/logs/` to avoid re-logging PRs already merged.

## Safety policy

Same base gates as `auto-merge`, applied only to PRs carrying the `merge-queue` label:

- **Author allowlist**: `author.login` is one of `dependabot[bot]`, `renovate[bot]`, `github-actions[bot]`, or appears under a `## Trusted Authors` section in `memory/watched-repos.md`.
- **Size cap**: `additions + deletions ≤ 500`, unless the PR also carries `auto-merge-large`.
- **Base branch**: `baseRefName` is `main` or `master`.
- **Not a fork**: `isCrossRepository == false`.
- **Not draft**: `isDraft == false`.
- **No opt-out label**: none of {`do-not-merge`, `wip`, `hold`, `needs-review`, `blocked`} present.

A PR failing any of these is evicted from the *internal queue order* (not from GitHub — its `merge-queue` label is left untouched) and re-evaluated fresh next run, as if newly entering the queue.

## Steps

0. **Bootstrap state** — per-repo FIFO order lives in `memory/topics/pr-merge-queue-state.json`:
   ```bash
   mkdir -p memory/topics
   [ -f memory/topics/pr-merge-queue-state.json ] || echo '{"repos":{}}' > memory/topics/pr-merge-queue-state.json
   ```
   Schema:
   ```json
   {
     "repos": {
       "owner/repo": {
         "order": ["owner/repo#12", "owner/repo#15"],
         "attempts": { "owner/repo#12": 1 },
         "last_run": "2026-09-11T10:00:00Z"
       }
     }
   }
   ```

1. **List labeled PRs** per watched repo:
   ```bash
   gh pr list -R owner/repo --label merge-queue --state open \
     --json number,title,author,isDraft,mergeable,mergeStateStatus,reviewDecision,statusCheckRollup,isCrossRepository,labels,additions,deletions,baseRefName,createdAt
   ```

2. **Reconcile queue order**: drop any tracked PR no longer open or no longer labeled `merge-queue`. Append newly-seen labeled PRs to the end, ordered by `createdAt` among themselves. PRs already in `order` keep their recorded position — the queue is FIFO by first-seen, not by GitHub's own ordering.

3. **Act only on the head of the queue.** Every other queued PR waits untouched this run — that serialization is the entire point.
   - If the queue is empty, log `MERGE_QUEUE_EMPTY` and stop for this repo.
   - If the head fails the safety policy (§ above): remove it from `order` (leave its GitHub label alone), log `SKIP:<gate>:<detail>`, and immediately treat the new head (if any) as this run's head — continue to the next step for it instead of stopping.
   - Handle `mergeStateStatus == "UNKNOWN"` with one 3-second retry, same as `auto-merge`; if still `UNKNOWN`, leave it as head untouched this run.

4. **If the head is not yet CLEAN** (behind base, checks still pending, etc.) but passes the safety policy: bring it current so its checks run against today's base —
   ```bash
   gh pr update-branch NUMBER -R owner/repo
   ```
   Log `SKIP:not-clean:<mergeStateStatus>`, increment its attempt counter, and stop for this repo — do not merge this run.

5. **If the head is CLEAN and green** (`mergeStateStatus == "CLEAN"`, `reviewDecision != "CHANGES_REQUESTED"`, every `statusCheckRollup` entry `SUCCESS`/`NEUTRAL`/`SKIPPED`):
   - Unless `MERGE_QUEUE_DRY_RUN=1`: `gh pr merge NUMBER -R owner/repo --squash --delete-branch`.
   - On success: pop it from `order`, clear its attempt counter, and — if another PR is now head — immediately run `gh pr update-branch` on that new head so it starts revalidating against the fresh base without waiting a full cycle.
   - On failure (non-zero exit): log `MERGE_FAIL #N: <stderr≤200 chars>`, increment its attempt counter, leave it as head.

6. **Retry cap** — a head stuck at 3 attempts without merging is almost never a transient CI blip; pop it from `order`, apply label `merge-queue-blocked` (do not remove `merge-queue` — a human clears both when they've dealt with it), and advance to the new head with an immediate `update-branch` as in step 5.

7. **Persist** `memory/topics/pr-merge-queue-state.json`, validated with `jq empty` (restore from a pre-run `.bak` on failure).

8. **Notify** only when something changed this run — a merge, a retry-cap eviction, or both. No state change → log only, no notification.
   ```
   *PR Merge Queue — ${today}*
   ✅ Merged owner/repo#12: PR title (+40/-8) — squash abc1234
   ⏭️ owner/repo#15 promoted to head, branch refreshed against main
   ```
   or, for an eviction:
   ```
   *PR Merge Queue — retry cap*
   owner/repo#12 hit 3 attempts without going CLEAN — evicted, labeled merge-queue-blocked.
   Last state: BEHIND. Investigate manually; remove merge-queue-blocked to re-enter the queue.
   ```

9. **Log to `memory/logs/${today}.md`** under a `### pr-merge-queue` heading: per repo, queue order at start, action taken on the head (`merged` / `updated-branch` / `evicted:<reason>` / `unknown-retry`), and queue order at end.

## Sandbox note

`gh` authenticates via the workflow's `GITHUB_TOKEN` — no curl needed, nothing here depends on outbound bash network. If `gh pr update-branch` or `gh pr merge` fails with `Resource not accessible by integration`, the token lacks the required permission on that repo; log once and notify at most once per 7 days (check `memory/logs/` for a prior identical notification) to avoid alert spam.

## Constraints

- Never act on a PR that isn't labeled `merge-queue` — this skill is strictly opt-in, unlike `auto-merge`'s author-allowlist model.
- Never merge anything but the current head of the queue, even if a later entry is CLEAN and the head is not. Out-of-order merges are exactly the failure mode this skill exists to prevent.
- Never run `gh pr update-branch` across the whole queue in one run — only the head, and only the PR that just became the new head after a merge or eviction. Refreshing idle queue entries wastes CI minutes for no benefit.
- Never remove or add the `merge-queue` label yourself — that's an explicit human/skill signal. Only ever add `merge-queue-blocked` (retry cap) and only ever act on internal queue-state, never GitHub's own PR labels, to represent "not currently head."
- Do not comment on PRs or alter their reviews — merging, branch updates, and the `merge-queue-blocked` label are the only writes this skill makes.
