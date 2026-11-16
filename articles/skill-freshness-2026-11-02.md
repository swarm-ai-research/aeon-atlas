# Skill Freshness — 2026-11-02

**Verdict:** ❌ FRESHNESS_STALE — 4 MISSING dependencies across 2 consumers; fork-cohort articles absent fleet-wide

*Audited 26 enabled skills · 32 dependencies checked · 4 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| fleet-state | `articles/fork-cohort-*.md` | articles (weekly, 192h threshold) | MISSING | ❌ MISSING |
| fleet-state | `articles/fork-release-*.md` | articles (weekly, 192h threshold) | MISSING | ❌ MISSING |
| fleet-state | `articles/contributor-spotlight-*.md` | articles (weekly, 192h threshold) | MISSING | ❌ MISSING |
| contributor-spotlight | `articles/fork-cohort-*.md` | articles (weekly, 192h threshold) | MISSING | ❌ MISSING |

(Sorted by severity desc, then consumer name. OK rows omitted.)

## What this means per consumer

> **fleet-state** — depends on 3 tracked files; all 3 flagged. Worst: `articles/fork-cohort-*.md` — no file on disk (threshold 192h, class articles/weekly). The producers `fork-cohort`, `fork-release-tracker`, and `contributor-spotlight` last ran Sunday 2026-11-01 but left no articles in `articles/`. Suggested action: Check `fork-cohort` run history with `./scripts/skill-runs --skill fork-cohort --hours 168`. fleet-state runs today (Monday 08:00 UTC) and will degrade to `FLEET_STATE_PARTIAL` or `FLEET_STATE_NO_SOURCES` — it reads these articles for transition highlights and release blurbs.

> **contributor-spotlight** — depends on 1 tracked file; 1 flagged. Worst: `articles/fork-cohort-*.md` — no file on disk (threshold 192h, class articles/weekly). **This is a new flag** (not present in prior run 2026-10-31): the Oct 25 fork-cohort article that covered the threshold window on Oct 31 is no longer present, and the expected Nov 1 article was not written. Suggested action: Check `fork-cohort` run history with `./scripts/skill-runs --skill fork-cohort --hours 168`. contributor-spotlight runs next Sunday and will fall back to `memory/topics/fork-cohort-state.json` if present.

## Healthy consumers

- skill-health — 0 tracked cross-skill deps, all fresh.
- api-health-probe — 0 tracked cross-skill deps, all fresh.
- ai-framework-watch — 0 tracked cross-skill deps, all fresh.
- ecosystem-pulse — 0 tracked cross-skill deps, all fresh.
- fork-cohort — 0 tracked cross-skill deps, all fresh.
- fork-release-tracker — 0 tracked cross-skill deps, all fresh.
- fork-first-run-alert — 0 tracked cross-skill deps, all fresh.
- operator-scorecard — 1 dep (`articles/fork-contributor-leaderboard-*.md`, 24h old, threshold 192h). ✅

+ 16 more all-fresh consumers (skill-evals, skill-update-check, fleet-scorecard, skill-leaderboard, fork-contributor-leaderboard, follow-up-patrol, fork-skill-digest, fork-skill-gap, fleet-skill-adoption, fork-health-score, workflow-security-audit, atlas, atlas-layers, atlas-improve, skill-freshness, heartbeat).

## Source status

- `aeon.yml`: 228 entries, 26 enabled
- Implicit references discovered: 28
- Explicit `chains: consume:` edges: 0 (all chains commented out)
- Files not yet on disk (skipped — implicit refs that never existed, producers disabled): 4

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes and filename dates — this skill measures nothing it does not also report.*
