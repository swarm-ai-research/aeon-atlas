# Skill Freshness — 2026-11-20

**Verdict:** 🔴 FRESHNESS_STALE — 5 of 32 deps flagged across 3 of 26 enabled consumers

*Audited 26 enabled skills · 32 dependencies checked · 5 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| fleet-state | `articles/fork-cohort-*.md` | articles/weekly | — (never written) | 🔴 MISSING |
| fleet-state | `articles/fork-release-*.md` | articles/weekly | — (never written) | 🔴 MISSING |
| fleet-state | `articles/contributor-spotlight-*.md` | articles/weekly | — (never written) | 🔴 MISSING |
| contributor-spotlight | `articles/fork-cohort-*.md` | articles/weekly | — (never written) | 🔴 MISSING |
| operator-scorecard | `articles/fork-contributor-leaderboard-*.md` | articles/weekly | 12d (288h) | 🟡 WARN |

## What this means per consumer

> **fleet-state** — depends on 3 files; all 3 flagged. Worst: `articles/fork-cohort-*.md`, `articles/fork-release-*.md`, and `articles/contributor-spotlight-*.md` — all MISSING. The producers `fork-cohort`, `fork-release-tracker`, and `contributor-spotlight` are enabled weekly skills but have never written output to `articles/`. First flagged: 2026-10-31 (20 days persistent). Suggested action: Check `fork-cohort` run history with `./scripts/skill-runs --skill fork-cohort --hours 168`.

> **contributor-spotlight** — depends on 1 file; 1 flagged. Worst: `articles/fork-cohort-*.md` last updated never (MISSING, threshold 192h, class articles/weekly). `contributor-spotlight` is itself a weekly producer but requires `fork-cohort` articles to pick its spotlight subject — without them it cannot function. First flagged: 2026-11-02 (18 days persistent). Suggested action: Check `fork-cohort` run history with `./scripts/skill-runs --skill fork-cohort --hours 168`.

> **operator-scorecard** — depends on 1 article-class file; 1 flagged. Worst: `articles/fork-contributor-leaderboard-*.md` last updated 2026-11-08 (12 days ago, 288h, threshold 192h, class articles/weekly). Producer `fork-contributor-leaderboard` last ran on 2026-11-08 — one weekly cycle was missed on 2026-11-15. First flagged: 2026-11-17 (3 days). Suggested action: Monitor — one missed run, expected to clear on next producer cadence (Sunday).

## Healthy consumers

- heartbeat — 0 deps, all fresh.
- skill-health — 0 deps, all fresh.
- api-health-probe — 0 deps, all fresh.
- ai-framework-watch — 0 deps tracked, all fresh.
- ecosystem-pulse — 0 deps tracked, all fresh.
- fork-cohort — 0 deps tracked, all fresh.
- fork-release-tracker — 0 deps tracked, all fresh.
- skill-freshness — 0 deps tracked, all fresh.
+ 15 more all-fresh consumers.

## Source status

- `aeon.yml`: ~175 entries, 26 enabled
- Implicit references discovered: 32
- Explicit `chains: consume:` edges: 0
- Files not yet on disk (skipped — implicit references to disabled producers): ~8

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
