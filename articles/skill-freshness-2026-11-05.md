# Skill Freshness — 2026-11-05

**Verdict:** 🔴 FRESHNESS_STALE — 4 canonical article dependencies missing across 2 consumers; fingerprint unchanged from 2026-11-02 (notification suppressed: FRESHNESS_NO_CHANGE, 3 days within 7-day dedup window).

*Audited 26 enabled skills · 32 dependencies checked · 4 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| fleet-state | `articles/fork-cohort-*.md` | articles/weekly | no file (missing since ≥2026-10-31) | 🔴 MISSING |
| fleet-state | `articles/fork-release-*.md` | articles/weekly | no file (missing since ≥2026-10-31) | 🔴 MISSING |
| fleet-state | `articles/contributor-spotlight-*.md` | articles/weekly | no file (missing since ≥2026-10-31) | 🔴 MISSING |
| contributor-spotlight | `articles/fork-cohort-*.md` | articles/weekly | no file (missing since ≥2026-11-02) | 🔴 MISSING |

*(Sorted by severity desc, then consumer name. OK rows omitted.)*

## What this means per consumer

> **fleet-state** — depends on 4 files; 3 flagged. Worst: `articles/fork-cohort-*.md` — no file on disk matching the pattern (threshold 192h, class articles/weekly). Producer `fork-cohort` last confirmed run: before 2026-10-31 (5+ days without output). `articles/fork-release-*.md` and `articles/contributor-spotlight-*.md` are also absent. fleet-state will synthesize from an empty cohort, producing a degraded digest with no WoW movement data or spotlight summary. Suggested action: Check `fork-cohort` run history with `./scripts/skill-runs --skill fork-cohort --hours 168`.

> **contributor-spotlight** — depends on 1 file; 1 flagged. Worst: `articles/fork-cohort-*.md` — no file on disk (threshold 192h, class articles/weekly). contributor-spotlight picks its weekly POWER fork from this cohort article. Without it the skill falls back to its cohort-state.json accelerator if present — but `memory/topics/fork-cohort-state.json` does not exist on disk either. The skill may silently produce a degraded or empty recognition post. Suggested action: Check `fork-cohort` run history with `./scripts/skill-runs --skill fork-cohort --hours 168`.

## Healthy consumers

- skill-health — 0 article deps audited, all fresh.
- skill-evals — 1 dep (`articles/skill-evals-2026-11-01.md`, ~96h, threshold 192h), OK.
- operator-scorecard — 1 dep (`articles/fork-contributor-leaderboard-2026-11-01.md`, ~96h, threshold 192h), OK.
- fork-skill-digest — 0 article deps (uses state files), all fresh.
- fleet-skill-adoption — 0 article deps (uses state files), all fresh.
- fork-skill-gap — 0 article deps (uses state files), all fresh.
- fork-health-score — 0 article deps (uses state files), all fresh.
+ 18 more all-fresh consumers.

## Source status

- `aeon.yml`: 180+ entries, 26 enabled
- Implicit references discovered: 32
- Explicit `chains: consume:` edges: 0 (all chains commented out)
- Files not yet on disk (skipped — implicit references that never existed): ~15 (disabled-skill outputs: skill-analytics, token-report, repo-pulse, tweet-allocator, heartbeat articles, etc.)

## Dedup note

Fingerprint `5ac877e8fe7ea3c1dab1c72a64c6e50a83097cd9` matches the 2026-11-02 run (3 days ago). Notification suppressed under FRESHNESS_NO_CHANGE. Next re-emit window opens 2026-11-09 (7 days after last notify on 2026-11-02).

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: ages derived from filename dates (git checkout normalizes on-disk mtimes); thresholds are per-class (articles/weekly 192h, articles/daily 28h, .outputs 4h, topics/.md 168h).*
