# Fleet-Intelligence Suite (Phase 2 Complete)

## Overview
25 autonomous agent skills enabled across aeon-atlas, forming a comprehensive fleet orchestration and analytics system. 25% of ~100 configured skills now active.

**Status:** Staged for first full weekly run on 2026-09-15, 06:00 UTC.

## Tier 1: Fleet Analytics & Visibility (8 skills)

### Adoption Tracking
- **skill-leaderboard** (Sun 17:00 UTC) — Top-15/bottom-15 most/least adopted skills across POWER+ACTIVE forks
- **fork-skill-digest** (Sun 18:30 UTC) — Weekly divergence digest: where fork fleet disagrees with upstream defaults
- **fork-skill-gap** (Sun 21:00 UTC) — Per-fork inventory of unadopted upstream skills (expansion candidates)
- **fleet-skill-adoption** (Sun 22:00 UTC) — Weekly leaderboard of adoption across fork cohort with WoW deltas

### Community & Velocity
- **fork-contributor-leaderboard** (Sun 17:30 UTC) — Rank community contributors across forks and upstream PRs
- **fork-release-tracker** (Sun 19:30 UTC) — Weekly celebration of fork releases; shipping velocity signal
- **contributor-spotlight** (Sun 20:00 UTC) — Named weekly recognition of one POWER fork developer
- **fork-cohort** (Sun 19:00 UTC) — Foundation: classify 129+ forks by activation stage (COLD/STALE/ACTIVE/POWER)

## Tier 2: Operational Health & Quality (6 skills)

### Core Monitoring
- **heartbeat** (Daily 08:00, 14:00, 20:00 UTC) — Scheduler health, runs successful, early issue detection
- **skill-health** (Daily 18:00 UTC) — Daily health analytics of enabled skills; exit-taxonomy distribution
- **skill-evals** (Sun 06:00 UTC) — Output quality assertions across all tracked skills; weekly quality baseline
- **api-health-probe** (Daily 10:00 UTC) — Proactive monitoring of external API hosts; UP/DOWN/SLOW alerts

### Dependency & Freshness
- **skill-freshness** (Daily 08:00 UTC) — Audit upstream skill dependencies for staleness; prevent bit-rot
- **fork-first-run-alert** (Daily 20:30 UTC) — Named alert when fork completes first workflow run; activation tracking

### Security
- **workflow-security-audit** (Sun 16:00 UTC) — Pre-analytics gate: scan workflows for injection vectors

## Tier 3: Fleet Infrastructure (4 skills)

### Atlas Rendering & Tracking
- **atlas** (Sun 04:00 UTC) — Parse 129+ forks, regenerate atlas.json/md/html; fork inventory
- **atlas-layers** (Sun 05:00 UTC) — Render seven-layer categorical view from atlas + skill-packs data
- **atlas-improve** (Monthly 1st, 06:00 UTC) — Diff 30d atlas changes, pick highest-magnitude surprise, open PR

## Tier 4: Strategic Synthesis & Accountability (3 skills)

### Weekly Digests & Scoring
- **fleet-state** (Mon 08:00 UTC) — Synthesize fork-cohort + fork-release-tracker + contributor-spotlight into one digest with WoW deltas + 12-week trend
- **operator-scorecard** (Mon 10:30 UTC) — Plain-language weekly scorecard: agent health + community growth + economic activity; worst-of-three OK/WATCH/DEGRADED verdict
- **skill-update-check** (Sun 19:00 UTC) — Check imported skills for upstream changes and security regressions

## Schedule Timeline

| Time (UTC) | Day | Skills |
|-----------|-----|--------|
| 04:00 | Sun | atlas (fork inventory parse) |
| 05:00 | Sun | atlas-layers (categorical rendering) |
| 06:00 | Sun | **skill-evals** (quality baseline gate) |
| 08:00 | Daily | skill-freshness (dependency audit) + api-health-probe upstream check |
| 08:00 | Mon | fleet-state (weekly digest synthesis) |
| 10:00 | Daily | api-health-probe (external health monitoring) |
| 10:30 | Mon | operator-scorecard (accountability + verdict) |
| 16:00 | Sun | workflow-security-audit (security pre-gate) |
| 17:00 | Sun | skill-leaderboard (adoption ranking) |
| 17:30 | Sun | fork-contributor-leaderboard (community ranking) |
| 18:00 | Daily | skill-health (daily health analytics) |
| 18:30 | Sun | fork-skill-digest (divergence tracking) |
| 19:00 | Sun | fork-cohort (fork classification) + skill-update-check (upstream security) |
| 19:30 | Sun | fork-release-tracker (shipping velocity) |
| 20:00 | Sun | contributor-spotlight (weekly recognition) |
| 20:30 | Daily | fork-first-run-alert (activation tracking) |
| 21:00 | Sun | fork-skill-gap (adoption gaps) |
| 22:00 | Sun | fleet-skill-adoption (adoption leaderboard) |

## Deployment History

### Phase 1 (Prior Session)
- Memory consolidation: 100+ daily logs → 4 structured topic files
- Fork-skill-digest enabled for divergence analysis
- Amplitude analytics setup + Protocol Omega personal practice template

### Phase 2a (2026-09-12, Session Continued)
- fork-cohort (data foundation)
- fork-contributor-leaderboard (community visibility)
- fork-health-score (health tier classification)
- workflow-security-audit (security gate)

### Phase 2b
- fork-release-tracker (shipping velocity)
- contributor-spotlight (community recognition)
- skill-freshness (dependency freshness auditing)

### Phase 2c
- skill-evals (quality assertions)
- api-health-probe (external dependency monitoring)
- skill-health (daily health analytics)
- fork-first-run-alert (new fork activation tracking)

### Phase 3
- fleet-state (weekly synthesis)
- operator-scorecard (accountability)
- skill-update-check (upstream security)

## Key Design Decisions

1. **Layered Approach:** Analytics → Health → Synthesis creates progressive visibility from granular metrics to executive summary
2. **Sunday Evening Pipeline:** 16:00-22:00 UTC concentrates weekly analytics, leaving operational monitoring distributed across day
3. **Foundational Dependencies:** fork-cohort runs first (19:00) to seed fork-health-score and contributor-spotlight
4. **Quality Gate:** skill-evals runs earliest (06:00 Sun) to establish baseline before analytics begin
5. **Multi-Model Optimization:** Sonnet 4.6 for compute-intensive tasks (leaderboards, synthesis); default for simple tracking

## Blockers & Dependencies

### Notification Channels (Blocking Alerting)
- Telegram, Discord, Slack channels not configured
- Requires operator API keys: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, DISCORD_WEBHOOK_URL, SLACK_WEBHOOK_URL
- Digests will run but notifications silent until channels activated

### External API Dependencies
- GitHub API (for fork inventory, PR tracking, contributor data)
- Supported via gh CLI in GitHub Actions
- No external blocking dependencies beyond GitHub

## Next Steps (Phase 4 / Future)

Optional enhancements for deeper insight:
1. **fleet-scorecard** — Daily cost + reliability metrics across fork fleet
2. **follow-up-patrol** — Escalation audit: age items in MEMORY.md, alert on overdue CRITICAL/HIGH items
3. **AI framework watch** — Weekly competitive intelligence on 9 AI agent frameworks + peer cohort
4. **ecosystem-entrants** — New fork detection from ecosystem-watch integration

## Success Metrics (First Week: 2026-09-15)

- [ ] skill-evals completes without errors; quality baseline established
- [ ] fork-cohort produces COLD/STALE/ACTIVE/POWER classification
- [ ] All 25 skills complete their first scheduled run
- [ ] fleet-state generates WoW delta comparison (even if 0 change)
- [ ] operator-scorecard produces verdict (OK/WATCH/DEGRADED)
- [ ] Zero timeout errors on dependent skills (fork-contributor-leaderboard depends on fork-cohort)
