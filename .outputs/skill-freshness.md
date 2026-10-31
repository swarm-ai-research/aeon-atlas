*Skill Freshness — 2026-10-31*
🔴 FRESHNESS_STALE — 3 of 31 deps flagged across 1 of 26 enabled consumers

Worst:
- fleet-state ← articles/fork-cohort-*.md (MISSING, class articles/weekly, sev MISSING)
- fleet-state ← articles/fork-release-*.md (MISSING, class articles/weekly, sev MISSING)
- fleet-state ← articles/contributor-spotlight-*.md (MISSING, class articles/weekly, sev MISSING)

Action: Check fork-cohort, fork-release-tracker, contributor-spotlight run history with ./scripts/skill-runs --hours 168. Sunday producers (last run expected 2026-10-25) left no articles on disk — fleet-state's Monday synthesis may be running blind.
Full: articles/skill-freshness-2026-10-31.md
