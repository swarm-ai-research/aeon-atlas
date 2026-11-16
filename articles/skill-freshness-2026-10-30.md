# Skill Freshness — 2026-10-30

**Verdict:** ✅ FRESHNESS_OK — all enabled consumers' tracked dependencies are fresh

*Audited 26 enabled skills · 31 dependencies checked · 0 flagged*

## Flagged dependencies

*(none — no consumer has a stale or missing upstream dependency)*

## What this means per consumer

All enabled consumers with tracked cross-skill dependencies resolved cleanly:

- **operator-scorecard** depends on 6 files; 0 flagged. The `articles/fork-contributor-leaderboard-2026-10-25.md` input (5 days old, weekly threshold 8d) is the only resolved article — all other producers (skill-analytics, heartbeat, tweet-allocator, token-report, repo-pulse) are disabled and their article patterns have never been written; those are classified as "never existed" and excluded from the freshness verdict.

- **fleet-state** depends on 6 files; 0 flagged. Three wildcard article patterns (`fork-cohort-*.md`, `fork-release-*.md`, `contributor-spotlight-*.md`) have never been written on disk; three memory/topics/ state files (`fork-release-state.json`, `contributor-spotlight-history.json`) are present and fresh. `fork-cohort-state.json` has never been written; classified as never-existed.

- **contributor-spotlight** depends on 2 files; 0 flagged. `articles/fork-cohort-*.md` and `memory/topics/fork-cohort-state.json` are both never-existed; the skill falls back to live API data gracefully.

- **ecosystem-pulse** depends on 2 files; 0 flagged. `memory/topics/ecosystem-pulse-state.json` and `ecosystem-pulse-map.json` both present and fresh.

## Healthy consumers

- heartbeat — 0 external deps, all fresh.
- skill-health — 0 external deps, all fresh.
- api-health-probe — 0 external deps, all fresh.
- ai-framework-watch — 0 external deps, all fresh.
- ecosystem-pulse — 2 deps, all fresh.
- fleet-state — 6 deps, all fresh (3 article wildcards never existed; 2 state files OK; 1 never-existed state file).
- operator-scorecard — 6 deps, all fresh (5 disabled-producer articles never existed; 1 article OK at 5d/8d threshold).
- contributor-spotlight — 2 deps, all fresh (both never existed).
+ 18 more all-fresh consumers.

## Notable observations (outside scope, for operator awareness)

These are not freshness violations under this skill's methodology (no enabled consumer depends on these files), but are worth noting:

- **workflow-security-audit** — last article on disk is `articles/workflow-security-audit-2026-04-11.md` (202 days old). The skill is `enabled: true` on a weekly Sunday schedule. No enabled consumer reads its articles, so this skill cannot flag it — but `skill-health` should be investigating why this skill has not produced an article since April 2026. The workflow security coverage gap is real.

- **fork-cohort** — no articles have ever been written to `articles/fork-cohort-*.md`. Multiple consumers (fleet-state, contributor-spotlight, fork-contributor-leaderboard) reference this pattern but fall back to state files or live API. The state file `memory/topics/fork-cohort-state.json` also does not exist, meaning these consumers run without cohort context. This is a data-quality concern, not a freshness violation.

- **fleet-state** — no articles have ever been written to `articles/fleet-state-*.md`. Fleet-state is listed as enabled (weekly Monday) but has produced no on-disk output. This is outside this skill's scope (no consumer has a canonical `${today}` dependency on it), but suggests fleet-state has never successfully completed.

## Mtime note

All files were checked out in this GitHub Actions run at `2026-10-30T08:56:51Z`. In a git-checkout environment, all committed files share the same mtime (the checkout timestamp), making `.outputs/` and `memory/topics/` file ages appear as ~2 minutes. Article freshness was cross-validated against filename dates; `.outputs/` and `memory/topics/` verdicts rely on mtime only and would require git history for a more precise assessment. With a shallow clone (depth=1), git-log-based timestamps were not available this run.

## Source status

- `aeon.yml`: 240+ entries parsed, 26 enabled
- Implicit references discovered: 31
- Explicit `chains: consume:` edges: 0 (all chains are commented out in `aeon.yml`)
- Files not yet on disk (skipped — implicit references that never existed): 15

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
