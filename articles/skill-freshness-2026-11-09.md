# Skill Freshness — 2026-11-09

**Verdict:** 🔴 FRESHNESS_STALE — 4 MISSING upstream articles preventing 2 consumers from running with fresh data

*Audited 26 enabled skills · 32 dependencies checked · 4 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| fleet-state | `articles/fork-cohort-*.md` | articles (weekly) | 9d — never produced | 🔴 MISSING |
| fleet-state | `articles/fork-release-*.md` | articles (weekly) | 9d — never produced | 🔴 MISSING |
| fleet-state | `articles/contributor-spotlight-*.md` | articles (weekly) | 9d — never produced | 🔴 MISSING |
| contributor-spotlight | `articles/fork-cohort-*.md` | articles (weekly) | 9d — never produced | 🔴 MISSING |

## What this means per consumer

> **fleet-state** — depends on 3 upstream articles; all 3 flagged MISSING (first seen 2026-10-31, now 9 days). No file matching `articles/fork-cohort-*.md`, `articles/fork-release-*.md`, or `articles/contributor-spotlight-*.md` exists on disk. Producers `fork-cohort`, `fork-release-tracker`, and `contributor-spotlight` are all enabled (weekly Sunday cadence) — `fork-cohort` has been stuck since 2026-10-25 (`last_status: dispatched`, no `last_success`; ISS-011). The Nov 8 Sunday window passed with no fork-cohort article produced. Suggested action: Check `fork-cohort` run history with `./scripts/skill-runs --skill fork-cohort --hours 168`.

> **contributor-spotlight** — depends on 1 upstream article; 1 flagged MISSING (first seen 2026-11-02, now 7 days). No file matching `articles/fork-cohort-*.md` exists on disk. The producer `fork-cohort` (weekly Sunday, enabled) has never produced an article in this instance due to ISS-011 scheduler issue. Suggested action: Check `fork-cohort` run history with `./scripts/skill-runs --skill fork-cohort --hours 168`.

## Healthy consumers

- skill-health — 0 cross-skill deps, all fresh.
- api-health-probe — 0 cross-skill deps, all fresh.
- ai-framework-watch — 0 cross-skill deps, all fresh.
- ecosystem-pulse — 0 cross-skill deps, all fresh.
- operator-scorecard — 1 dep (`articles/fork-contributor-leaderboard-*.md`, 1d old, OK).
- fork-cohort — 0 cross-skill deps, all fresh.
- fork-release-tracker — 0 cross-skill deps, all fresh.
- skill-evals — 0 cross-skill deps, all fresh.

+ 16 more all-fresh consumers.

## Source status

- `aeon.yml`: 200+ entries, 26 enabled
- Implicit references discovered: 32
- Explicit `chains: consume:` edges: 0
- Files not yet on disk (skipped — implicit references that never existed): 24

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
