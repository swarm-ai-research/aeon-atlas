## Summary

Skill-freshness audit complete for 2026-11-05.

**Verdict: 🔴 FRESHNESS_STALE / Status: FRESHNESS_NO_CHANGE**

- **26 enabled consumers** audited · **32 dependencies** checked · **4 flagged** (all MISSING)
- Same 4 items flagged as the 2026-11-02 run — fingerprint `5ac877e8...` unchanged
- **No notification sent** — within 7-day dedup window (3 days since last run); re-emit opens 2026-11-09

**Still-missing dependencies:**
| Consumer | Missing file | Producer | First flagged |
|----------|-------------|----------|---------------|
| fleet-state | `articles/fork-cohort-*.md` | fork-cohort | 2026-10-31 |
| fleet-state | `articles/fork-release-*.md` | fork-release-tracker | 2026-10-31 |
| fleet-state | `articles/contributor-spotlight-*.md` | contributor-spotlight | 2026-10-31 |
| contributor-spotlight | `articles/fork-cohort-*.md` | fork-cohort | 2026-11-02 |

The root cause is `fork-cohort` not producing an article since before Oct 31 — both `fleet-state` and `contributor-spotlight` depend on it. Run `./scripts/skill-runs --skill fork-cohort --hours 168` to investigate.

**Files written:**
- `articles/skill-freshness-2026-11-05.md` (report)
- `memory/topics/skill-freshness-state.json` (updated `last_run_at`)
- `memory/logs/2026-11-05.md` (new)
