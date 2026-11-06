## Summary

**skill-freshness** ran for 2026-11-06. Here's what happened:

**Audit scope:** 26 enabled skills · 32 dependencies checked · 4 flagged

**Flagged dependencies (all MISSING):**
| Consumer | Dependency | Severity |
|---|---|---|
| fleet-state | `articles/fork-cohort-*.md` | 🔴 MISSING |
| fleet-state | `articles/fork-release-*.md` | 🔴 MISSING |
| fleet-state | `articles/contributor-spotlight-*.md` | 🔴 MISSING |
| contributor-spotlight | `articles/fork-cohort-*.md` | 🔴 MISSING |

**Fleet verdict:** `FRESHNESS_STALE` — but this is the **same 4-flag fingerprint** as yesterday's run (2026-11-05), and last run was 1 day ago (< 7-day re-emit window). No notification sent.

**Root cause:** `fork-cohort`, `fork-release-tracker`, and `contributor-spotlight` are all enabled on a weekly Sunday cadence but have never produced article files in this instance. `fleet-state` and `contributor-spotlight` both depend on `fork-cohort` articles as upstream inputs.

**Files written:**
- `articles/skill-freshness-2026-11-06.md` — today's report
- `memory/topics/skill-freshness-state.json` — updated `last_run_at`
- `memory/logs/2026-11-06.md` — daily log entry

**Status:** `FRESHNESS_NO_CHANGE` — the gap has been open since Oct 31. If it persists another day (Nov 7), the `first_seen_at` for three of the fleet-state flags will cross the 7-day re-emit threshold and a fresh notification will fire.
