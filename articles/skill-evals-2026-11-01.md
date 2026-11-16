# Skill Evals — 2026-11-01

**Verdict:** SKILL_EVALS_OK *(bootstrap — first eval run; no prior baseline)*
**Coverage:** 2/26 (7.7%) *(first run)*
**Diff:** 0 new fail · 0 fixed · 0 still failing · 14 skills first-eval (BOOTSTRAP)

## Action Queue
1. Dispatch skill-health — no output; enabled but `articles/skill-health-*.md` not found
2. Add evals.json entry for skill-freshness — pattern: `STALE|FRESH|stale_deps`
3. Add evals.json entry for ecosystem-pulse — pattern: `ACTIVE|COLD|RECENT`
4. Add evals.json entry for operator-scorecard — pattern: `OK|WATCH|DEGRADED`
5. Add evals.json entry for atlas — pattern: `fork|aeon|atlas`
6. Add evals.json entry for fleet-scorecard — pattern: `scorecard|cost|run`
7. Add evals.json entry for fork-cohort — pattern: `COLD|STALE|ACTIVE|POWER`
8. +18 more uncovered enabled skills — see Coverage Gaps

## Full Results
| Skill | Status | Diff | Root cause | Quality | Words | Last output |
|-------|--------|------|------------|---------|-------|-------------|
| heartbeat | PASS | BOOTSTRAP_NEW | — | unknown | >300 | memory/logs/2026-10-31.md |
| skill-health | NO_OUTPUT | BOOTSTRAP_NEW | no_file_match (articles/skill-health-*.md) | unknown | — | — |
| changelog | STALE | BOOTSTRAP_NEW | stale_file (~7.5mo old); assertions pass | — | >150 | articles/changelog-2026-03-19.md |
| repo-pulse | NO_OUTPUT | BOOTSTRAP_NEW | no_file_match; skill disabled | — | — | — |
| push-recap | NO_OUTPUT | BOOTSTRAP_NEW | no_file_match; skill disabled | — | — | — |
| fork-fleet | NO_OUTPUT | BOOTSTRAP_NEW | no_file_match; skill disabled | — | — | — |
| cost-report | NO_OUTPUT | BOOTSTRAP_NEW | no_file_match; skill disabled | — | — | — |
| repo-article | NO_OUTPUT | BOOTSTRAP_NEW | no_file_match; skill disabled | — | — | — |
| repo-actions | NO_OUTPUT | BOOTSTRAP_NEW | no_file_match; skill disabled | — | — | — |
| deep-research | NO_OUTPUT | BOOTSTRAP_NEW | no_file_match; skill disabled | — | — | — |
| hn-digest | NO_OUTPUT | BOOTSTRAP_NEW | no_file_match; skill disabled | — | — | — |
| rss-digest | NO_OUTPUT | BOOTSTRAP_NEW | no_file_match; skill disabled | — | — | — |
| polymarket | NO_OUTPUT | BOOTSTRAP_NEW | no_file_match; skill disabled | — | — | — |
| token-alert | NO_OUTPUT | BOOTSTRAP_NEW | no_file_match; skill disabled | — | — | — |

**Notes:**
- heartbeat: word count far exceeds min_words (20); required pattern `heartbeat` present; no forbidden patterns found. Quality file absent → `unknown`.
- skill-health: **enabled in aeon.yml**, runs daily at 18:00 UTC, last_success 2026-10-31T18:52:24Z. Output lands in `memory/skill-health/last-report.json`, not `articles/skill-health-*.md` — the evals.json `output_pattern` may be wrong, or the skill simply never writes an article. Requires investigation before firing a FAIL.
- changelog: disabled skill; file from 2026-03-19 is ~7.5 months past its 24h cadence — STALE as expected for a disabled skill. Assertions pass (commit/fix keywords present, no placeholders). No issue filed (disabled + bootstrap).
- Disabled skills (12 of 14): NO_OUTPUT is expected; not counted toward coverage or issue filing.

## Coverage Gaps (enabled in aeon.yml, missing from evals.json)
Skills with existing article outputs (highest-priority gaps):
- skill-freshness — `articles/skill-freshness-*.md` → inferred pattern: `STALE|FRESH|stale_deps`
- ecosystem-pulse — `articles/ecosystem-pulse-*.md` → inferred pattern: `ACTIVE|COLD|RECENT`
- operator-scorecard — `articles/operator-scorecard-*.md` → inferred pattern: `OK|WATCH|DEGRADED`
- fork-health-score — `articles/fork-health-score-*.md` → inferred pattern: `ACTIVE|WARM|STALE|tier`
- fork-skill-gap — `articles/fork-skill-gap-*.md` → inferred pattern: `gap|skill|fork`
- fleet-skill-adoption — `articles/fleet-skill-adoption-*.md` → inferred pattern: `adoption|skill|fork`
- skill-leaderboard — `articles/skill-leaderboard-*.md` → inferred pattern: `rank|leaderboard|skill`
- fork-contributor-leaderboard — `articles/fork-contributor-leaderboard-*.md` → inferred pattern: `contributor|fork|PR`
- workflow-security-audit — `articles/workflow-security-audit-*.md` → inferred pattern: `injection|security|workflow`

Enabled skills with no output yet (add evals.json entry when first output lands):
- atlas, atlas-layers, atlas-improve, api-health-probe, ai-framework-watch, fleet-state, fork-cohort, fork-release-tracker, contributor-spotlight, fork-first-run-alert, skill-evals, skill-update-check, fleet-scorecard, follow-up-patrol, fork-skill-digest

+15 more — total uncovered enabled: 24/26

## Sources
- evals.json=ok · cron-state=ok · skill-health=partial (last-report.json, no per-skill files) · eval-audit=fail (permission-gated; fell back to in-memory coverage check) · prior-article=none (bootstrap)
