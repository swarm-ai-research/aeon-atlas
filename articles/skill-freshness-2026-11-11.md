# Skill Freshness — 2026-11-11

**Verdict:** 🔴 FRESHNESS_STALE — 4 deps MISSING across 2 consumers; fork-cohort, fork-release-tracker, and contributor-spotlight have never produced articles

*Audited 26 enabled skills · 32 dependencies checked · 4 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| fleet-state | `articles/fork-cohort-*.md` | articles | MISSING | 🔴 MISSING |
| fleet-state | `articles/fork-release-*.md` | articles | MISSING | 🔴 MISSING |
| fleet-state | `articles/contributor-spotlight-*.md` | articles | MISSING | 🔴 MISSING |
| contributor-spotlight | `articles/fork-cohort-*.md` | articles | MISSING | 🔴 MISSING |

## What this means per consumer

> **fleet-state** — depends on 6 files; 3 flagged. Worst: `articles/fork-cohort-*.md` — no matching file on disk (threshold 192h, class articles/weekly). First flagged 2026-10-31 (11 days ago — persistent). Producers `fork-cohort`, `fork-release-tracker`, and `contributor-spotlight` are enabled weekly skills that write articles, but no article has ever been committed. fleet-state falls back to state-file-only synthesis when articles are absent, but loses narrative context and WoW movement data. Suggested action: Check `fork-cohort` run history with `./scripts/skill-runs --skill fork-cohort --hours 336`. If runs show no executions, verify the Sunday 19:00 UTC slot is correctly wired in `.github/workflows/aeon.yml`.

> **contributor-spotlight** — depends on 2 files; 1 flagged. Worst: `articles/fork-cohort-*.md` — no matching file on disk (threshold 192h, class articles/weekly). First flagged 2026-11-02 (9 days ago — persistent). contributor-spotlight requires a fork-cohort article to pick the POWER cohort roster; with no article it cannot run meaningfully. Suggested action: Check `fork-cohort` run history with `./scripts/skill-runs --skill fork-cohort --hours 168`.

## Healthy consumers

- ai-framework-watch — 1 dep (memory/topics/framework-watch-state.json), all fresh.
- ecosystem-pulse — 2 deps (ecosystem-pulse-state.json, ecosystem-pulse-map.json), all fresh.
- fork-skill-digest — 1 dep (fork-skill-digest-state.json), all fresh.
- fork-skill-gap — 1 dep (fork-skill-gap-state.json), all fresh.
- fleet-skill-adoption — 1 dep (fleet-skill-adoption-state.json), all fresh.
- fork-health-score — 1 dep (fork-health-score-state.json), all fresh.
- skill-leaderboard — 1 dep (skill-leaderboard-state.json), all fresh.
- operator-scorecard — 1 dep (articles/fork-contributor-leaderboard-*.md → 2026-11-08), all fresh.

+ 16 more all-fresh consumers.

## Source status

- `aeon.yml`: 177+ entries parsed, 26 enabled
- Implicit references discovered: 32
- Explicit `chains: consume:` edges: 0 (chains block is commented out)
- Files not yet on disk (skipped — implicit references that never existed): 3 (fork-cohort-state.json, skill-analytics articles, heartbeat articles)

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
