*Skill Freshness — 2026-11-17*
🔴 FRESHNESS_STALE — 5 of 32 deps flagged across 3 of 26 enabled consumers

Worst:
- fleet-state ← articles/fork-cohort-*.md (MISSING, 17d persistent, class articles/weekly)
- fleet-state ← articles/fork-release-*.md (MISSING, 17d persistent, class articles/weekly)
- contributor-spotlight ← articles/fork-cohort-*.md (MISSING, 15d persistent, class articles/weekly)
- operator-scorecard ← articles/fork-contributor-leaderboard-*.md (216h, WARN — new flag, missed 2026-11-16 window)

Action: Check fork-cohort run history with ./scripts/skill-runs --skill fork-cohort --hours 504
Full: articles/skill-freshness-2026-11-17.md
