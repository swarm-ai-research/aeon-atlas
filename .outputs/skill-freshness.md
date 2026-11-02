*Skill Freshness — 2026-11-02*
❌ FRESHNESS_STALE — 4 of 32 deps flagged across 2 of 26 enabled consumers

Worst:
- fleet-state ← articles/fork-cohort-*.md (MISSING, class articles/weekly, first seen 2026-10-31)
- fleet-state ← articles/fork-release-*.md (MISSING, class articles/weekly, first seen 2026-10-31)
- fleet-state ← articles/contributor-spotlight-*.md (MISSING, class articles/weekly, first seen 2026-10-31)

Action: Check fork-cohort run history — ./scripts/skill-runs --skill fork-cohort --hours 168. All 3 Sunday producers (fork-cohort, fork-release-tracker, contributor-spotlight) left no articles on 2026-11-01. fleet-state runs today and will degrade. New flag: contributor-spotlight now also lacks its fork-cohort input.
Full: articles/skill-freshness-2026-11-02.md
