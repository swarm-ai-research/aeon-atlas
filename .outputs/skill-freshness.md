## Summary

**skill-freshness** ran for 2026-11-20. Verdict: 🔴 FRESHNESS_STALE — no notification (FRESHNESS_NO_CHANGE).

**What was found (26 enabled skills, 32 deps, 5 flagged):**

| Consumer | Dependency | Severity |
|----------|-----------|---------|
| fleet-state | `articles/fork-cohort-*.md` | 🔴 MISSING (20d) |
| fleet-state | `articles/fork-release-*.md` | 🔴 MISSING (20d) |
| fleet-state | `articles/contributor-spotlight-*.md` | 🔴 MISSING (20d) |
| contributor-spotlight | `articles/fork-cohort-*.md` | 🔴 MISSING (18d) |
| operator-scorecard | `articles/fork-contributor-leaderboard-*.md` | 🟡 WARN (12d, threshold 8d) |

**Root issue:** `fork-cohort`, `fork-release-tracker`, and `contributor-spotlight` are enabled weekly skills that have never written articles to `articles/`. This blocks both `fleet-state` and `contributor-spotlight` from functioning. `fork-contributor-leaderboard` missed its 2026-11-15 Sunday run.

**Dedup:** Identical fingerprint to the 2026-11-17 run (3 days ago, within the 7-day re-emit window) → notification suppressed. The dedup window expires 2026-11-24 if issues persist.

**Files written/modified:**
- `articles/skill-freshness-2026-11-20.md` — created
- `memory/topics/skill-freshness-state.json` — updated `last_run_at`
- `memory/logs/2026-11-20.md` — created
