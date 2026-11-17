# Skill Freshness — 2026-11-17

**Verdict:** 🔴 FRESHNESS_STALE — 5 deps flagged across 3 consumers; fork-cohort articles persistently missing (17d); fork-contributor-leaderboard slipping past weekly window

*Audited 26 enabled skills · 32 dependencies checked · 5 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| fleet-state | `articles/fork-cohort-*.md` | articles/weekly | MISSING | 🔴 MISSING |
| fleet-state | `articles/fork-release-*.md` | articles/weekly | MISSING | 🔴 MISSING |
| fleet-state | `articles/contributor-spotlight-*.md` | articles/weekly | MISSING | 🔴 MISSING |
| contributor-spotlight | `articles/fork-cohort-*.md` | articles/weekly | MISSING | 🔴 MISSING |
| operator-scorecard | `articles/fork-contributor-leaderboard-*.md` | articles/weekly | 216h | 🟡 WARN |

(Sorted by severity desc, then consumer name.)

## What this means per consumer

> **fleet-state** — depends on 6 files; 3 flagged. Worst: `articles/fork-cohort-*.md` — no matching file on disk (threshold 192h, class articles/weekly). First flagged 2026-10-31 (17 days ago — persistent). Producers `fork-cohort`, `fork-release-tracker`, and `contributor-spotlight` are enabled weekly skills that have never committed an article. fleet-state falls back to state-file-only synthesis but loses narrative context and WoW movement data. Suggested action: Check `fork-cohort` run history with `./scripts/skill-runs --skill fork-cohort --hours 504`. If runs show no executions, verify the Sunday 19:00 UTC slot is correctly wired in `.github/workflows/aeon.yml`.

> **contributor-spotlight** — depends on 2 files; 1 flagged. Worst: `articles/fork-cohort-*.md` — no matching file on disk (threshold 192h, class articles/weekly). First flagged 2026-11-02 (15 days ago — persistent). contributor-spotlight requires a fork-cohort article to pick the POWER cohort roster; with no article it cannot run meaningfully. Suggested action: Check `fork-cohort` run history with `./scripts/skill-runs --skill fork-cohort --hours 336`.

> **operator-scorecard** — depends on 1 article file; 1 flagged. `articles/fork-contributor-leaderboard-*.md` — most recent is `fork-contributor-leaderboard-2026-11-08.md`, age 216h (threshold 192h, class articles/weekly). **New flag this run** — was OK on 2026-11-15 (168h, within window). The Sunday 17:30 UTC `fork-contributor-leaderboard` run has not produced a new article since 2026-11-08, missing the 2026-11-16 window. operator-scorecard will read a 9-day-old leaderboard on its next Monday run. Suggested action: Monitor — one missed run, expected to clear on the next producer cadence (Sunday 2026-11-22). If not cleared by then, check `fork-contributor-leaderboard` run history with `./scripts/skill-runs --skill fork-contributor-leaderboard --hours 336`.

## Healthy consumers

- ai-framework-watch — 1 dep (memory/topics/framework-watch-state.json), all fresh.
- ecosystem-pulse — 2 deps (ecosystem-pulse-state.json, ecosystem-pulse-map.json), all fresh.
- fork-skill-digest — 1 dep (fork-skill-digest-state.json), all fresh.
- fork-skill-gap — 1 dep (fork-skill-gap-state.json), all fresh.
- fleet-skill-adoption — 1 dep (fleet-skill-adoption-state.json), all fresh.
- fork-health-score — 1 dep (fork-health-score-state.json), all fresh.
- skill-leaderboard — 1 dep (skill-leaderboard-state.json), all fresh.
- fork-first-run-alert — 1 dep (fork-first-run-state.json), all fresh.

+ 15 more all-fresh consumers.

## Source status

- `aeon.yml`: 177+ entries parsed, 26 enabled
- Implicit references discovered: 32
- Explicit `chains: consume:` edges: 0 (chains block is commented out)
- Files not yet on disk (skipped — implicit references that never existed): 3 (fork-cohort-state.json, skill-analytics articles, heartbeat articles)

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
