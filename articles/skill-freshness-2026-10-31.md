# Skill Freshness — 2026-10-31

**Verdict:** 🔴 FRESHNESS_STALE — 3 upstream article dependencies missing for fleet-state

*Audited 26 enabled skills · 31 dependencies checked · 3 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| fleet-state | `articles/fork-cohort-*.md` | articles (weekly) | MISSING | 🔴 MISSING |
| fleet-state | `articles/fork-release-*.md` | articles (weekly) | MISSING | 🔴 MISSING |
| fleet-state | `articles/contributor-spotlight-*.md` | articles (weekly) | MISSING | 🔴 MISSING |

## What this means per consumer

> **fleet-state** — depends on 5 files; 3 flagged. Worst: `articles/fork-cohort-*.md`, `articles/fork-release-*.md`, `articles/contributor-spotlight-*.md` — all missing (threshold 192h, class articles/weekly). fleet-state synthesises fork-cohort + fork-release-tracker + contributor-spotlight into a weekly fleet digest; when these three upstream articles are absent, fleet-state's Monday synthesis will either run silently on stale data or produce an incomplete digest with no community narrative. Producers `fork-cohort`, `fork-release-tracker`, and `contributor-spotlight` are weekly/Sunday skills — last Sunday was 2026-10-25 and no articles landed in `articles/`. Suggested action: Check `fork-cohort`, `fork-release-tracker`, and `contributor-spotlight` run history with `./scripts/skill-runs --skill fork-cohort --hours 168`.

## Healthy consumers

- ecosystem-pulse — 1 dep (own article 120h old, all fresh)
- fleet-skill-adoption — 1 dep (own article 144h old, all fresh)
- fork-contributor-leaderboard — 1 dep (own article 144h old, all fresh)
- fork-health-score — 1 dep (own article 120h old, all fresh)
- fork-skill-gap — 1 dep (own article 144h old, all fresh)
- operator-scorecard — 1 cross-skill dep (fork-contributor-leaderboard 144h, within 192h threshold, all fresh)
- skill-freshness — 1 dep (own article 24h old, all fresh)
- skill-leaderboard — 1 dep (own article 144h old, all fresh)

+ 17 more all-fresh consumers (atlas, atlas-layers, atlas-improve, heartbeat, skill-health, api-health-probe, ai-framework-watch, fork-cohort, fork-release-tracker, contributor-spotlight, fork-first-run-alert, skill-evals, skill-update-check, fleet-scorecard, fork-skill-digest, fork-health-score, follow-up-patrol, workflow-security-audit).

## Source status

- `aeon.yml`: 245+ entries, 26 enabled
- Implicit references discovered: 31
- Explicit `chains: consume:` edges: 0 (all chains commented out)
- Files not yet on disk (skipped — implicit references that never existed): 8

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
