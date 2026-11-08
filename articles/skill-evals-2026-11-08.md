# Skill Evals — 2026-11-08

**Verdict:** SKILL_EVALS_OK
**Coverage:** 2/26 (7.7%) *(same as prior)*
**Diff:** 0 new fail · 0 fixed · 1 still failing · 13 stable

## Action Queue
1. Patch evals.json:skill-health — output_pattern mismatch (skill writes to `memory/skill-health/last-report.json`, not `articles/skill-health-*.md`)
2. Add evals.json entry for skill-freshness — pattern: `STALE|FRESH|stale_deps`
3. Add evals.json entry for ecosystem-pulse — pattern: `ACTIVE|COLD|RECENT`
4. Add evals.json entry for operator-scorecard — pattern: `OK|WATCH|DEGRADED`
5. Add evals.json entry for fork-health-score — pattern: `ACTIVE|WARM|STALE|tier`
6. Add evals.json entry for skill-leaderboard — pattern: `rank|leaderboard|skill`
7. Add evals.json entry for fork-skill-digest — pattern: `digest|skill|fork`
8. +17 more uncovered enabled skills — see Coverage Gaps

## Still Failing
| Skill | Status | Root cause | Issue | Failing since |
|-------|--------|------------|-------|---------------|
| skill-health | NO_OUTPUT | no_file_match (output_pattern mismatch — skill writes `memory/skill-health/last-report.json`) | — | 2026-11-01 |

## Full Results
| Skill | Status | Diff | Root cause | Quality | Words | Last output |
|-------|--------|------|------------|---------|-------|-------------|
| heartbeat | PASS | STABLE | — | unknown | 269 | memory/logs/2026-11-07.md |
| skill-health | NO_OUTPUT | STILL_FAIL | no_file_match (output_pattern mismatch) | — | — | — |
| changelog | STALE | STABLE | stale_file (~7.6mo; disabled) | — | >150 | articles/changelog-2026-03-19.md |
| repo-pulse | NO_OUTPUT | STABLE | no_file_match; skill disabled | — | — | — |
| push-recap | NO_OUTPUT | STABLE | no_file_match; skill disabled | — | — | — |
| fork-fleet | NO_OUTPUT | STABLE | no_file_match; skill disabled | — | — | — |
| cost-report | NO_OUTPUT | STABLE | no_file_match; skill disabled | — | — | — |
| repo-article | NO_OUTPUT | STABLE | no_file_match; skill disabled | — | — | — |
| repo-actions | NO_OUTPUT | STABLE | no_file_match; skill disabled | — | — | — |
| deep-research | NO_OUTPUT | STABLE | no_file_match; skill disabled | — | — | — |
| hn-digest | NO_OUTPUT | STABLE | no_file_match; skill disabled | — | — | — |
| rss-digest | NO_OUTPUT | STABLE | no_file_match; skill disabled | — | — | — |
| polymarket | NO_OUTPUT | STABLE | no_file_match; skill disabled | — | — | — |
| token-alert | NO_OUTPUT | STABLE | no_file_match; skill disabled | — | — | — |

**Notes:**
- heartbeat: file `memory/logs/2026-11-07.md` age ~13h (last modified by skill-health at ~18:31 UTC 11-07); heartbeat's own last logged run was 2026-11-06T21:51 (ISS-011 scheduler quiet window ongoing — heartbeat dropped 11-07 08:00, 14:00, and 20:00 slots). File is not stale per 2× expected_cadence (8h × 2 = 16h, file age < 16h). Contains "heartbeat" (2 occurrences). No forbidden patterns. PASS stands but heartbeat slot health remains a concern under ISS-011.
- skill-health: enabled, runs daily at 18:00 UTC, last run 2026-11-07T18:31. Output writes to `memory/skill-health/last-report.json`, not `articles/skill-health-*.md`. The evals.json `output_pattern` is incorrect. This is an evals.json config bug, not a skill failure. STILL_FAIL (second consecutive run); no ISS filed by skill-evals due to bootstrap exclusion on first run — now persistent, patch evals.json to fix.
- changelog: disabled skill; file ~7.6 months past 24h cadence — STALE as expected. Assertions pass (commit/fix keywords present, no placeholders). No issue filed (disabled + stable stale state).
- Disabled skills (12 of 14): NO_OUTPUT is expected; not counted toward coverage or issue filing.

## Coverage Gaps (enabled in aeon.yml, missing from evals.json)
Skills with existing article outputs (highest-priority):
- skill-freshness — `articles/skill-freshness-*.md` → inferred pattern: `STALE|FRESH|stale_deps`
- ecosystem-pulse — `articles/ecosystem-pulse-*.md` → inferred pattern: `ACTIVE|COLD|RECENT`
- operator-scorecard — `articles/operator-scorecard-*.md` → inferred pattern: `OK|WATCH|DEGRADED`
- fork-health-score — `articles/fork-health-score-*.md` → inferred pattern: `ACTIVE|WARM|STALE|tier`
- skill-leaderboard — `articles/skill-leaderboard-*.md` → inferred pattern: `rank|leaderboard|skill`
- fork-skill-gap — `articles/fork-skill-gap-*.md` → inferred pattern: `gap|skill|fork`
- fork-skill-digest — `articles/fork-skill-digest-*.md` → inferred pattern: `digest|skill|fork`
- workflow-security-audit — `articles/workflow-security-audit-*.md` → inferred pattern: `injection|security|workflow`

Enabled skills with no article output yet:
- atlas, atlas-layers, atlas-improve, api-health-probe, ai-framework-watch, fleet-state, fork-cohort, fork-release-tracker, contributor-spotlight, fork-first-run-alert, skill-evals, skill-update-check, fleet-scorecard, follow-up-patrol, fork-contributor-leaderboard, fleet-skill-adoption

+8 more — total uncovered enabled: 24/26

## Sources
- evals.json=ok · cron-state=ok · skill-health=partial (last-report.json, no per-skill files) · eval-audit=fail (permission-gated; fell back to in-memory coverage check) · prior-article=ok (2026-11-01)
