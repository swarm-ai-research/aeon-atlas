# Fleet-Intelligence Suite (Phase 2 Complete)

## Overview
25 autonomous agent skills enabled across aeon-atlas, forming a comprehensive fleet orchestration and analytics system. 25% of ~100 configured skills now active.

**Status:** Staged for first full weekly run on 2026-09-15, 16:00 AEST (06:00 UTC).

## Tier 1: Fleet Analytics & Visibility (8 skills)

### Adoption Tracking
- **skill-leaderboard** (Mon 03:00 AEST / Sun 17:00 UTC) — Top-15/bottom-15 most/least adopted skills across POWER+ACTIVE forks
- **fork-skill-digest** (Mon 04:30 AEST / Sun 18:30 UTC) — Weekly divergence digest: where fork fleet disagrees with upstream defaults
- **fork-skill-gap** (Mon 07:00 AEST / Sun 21:00 UTC) — Per-fork inventory of unadopted upstream skills (expansion candidates)
- **fleet-skill-adoption** (Mon 08:00 AEST / Sun 22:00 UTC) — Weekly leaderboard of adoption across fork cohort with WoW deltas

### Community & Velocity
- **fork-contributor-leaderboard** (Mon 03:30 AEST / Sun 17:30 UTC) — Rank community contributors across forks and upstream PRs
- **fork-release-tracker** (Mon 05:30 AEST / Sun 19:30 UTC) — Weekly celebration of fork releases; shipping velocity signal
- **contributor-spotlight** (Mon 06:00 AEST / Sun 20:00 UTC) — Named weekly recognition of one POWER fork developer
- **fork-cohort** (Mon 05:00 AEST / Sun 19:00 UTC) — Foundation: classify 129+ forks by activation stage (COLD/STALE/ACTIVE/POWER)

## Tier 2: Operational Health & Quality (6 skills)

### Core Monitoring
- **heartbeat** (Daily 18:00, 00:00, 06:00 AEST / 08:00, 14:00, 20:00 UTC) — Scheduler health, runs successful, early issue detection
- **skill-health** (Daily 04:00 AEST / 18:00 UTC) — Daily health analytics of enabled skills; exit-taxonomy distribution
- **skill-evals** (Sun 16:00 AEST / 06:00 UTC) — Output quality assertions across all tracked skills; weekly quality baseline
- **api-health-probe** (Daily 20:00 AEST / 10:00 UTC) — Proactive monitoring of external API hosts; UP/DOWN/SLOW alerts

### Dependency & Freshness
- **skill-freshness** (Daily 18:00 AEST / 08:00 UTC) — Audit upstream skill dependencies for staleness; prevent bit-rot
- **fork-first-run-alert** (Daily 06:30 AEST / 20:30 UTC) — Named alert when fork completes first workflow run; activation tracking

### Security
- **workflow-security-audit** (Sun 02:00 AEST / 16:00 UTC) — Pre-analytics gate: scan workflows for injection vectors

## Tier 3: Fleet Infrastructure (4 skills)

### Atlas Rendering & Tracking
- **atlas** (Sun 14:00 AEST / 04:00 UTC) — Parse 129+ forks, regenerate atlas.json/md/html; fork inventory
- **atlas-layers** (Sun 15:00 AEST / 05:00 UTC) — Render seven-layer categorical view from atlas + skill-packs data
- **atlas-improve** (Monthly 1st, 16:00 AEST / 06:00 UTC) — Diff 30d atlas changes, pick highest-magnitude surprise, open PR

## Tier 4: Strategic Synthesis & Accountability (3 skills)

### Weekly Digests & Scoring
- **fleet-state** (Mon 18:00 AEST / 08:00 UTC) — Synthesize fork-cohort + fork-release-tracker + contributor-spotlight into one digest with WoW deltas + 12-week trend
- **operator-scorecard** (Mon 20:30 AEST / 10:30 UTC) — Plain-language weekly scorecard: agent health + community growth + economic activity; worst-of-three OK/WATCH/DEGRADED verdict
- **skill-update-check** (Mon 05:00 AEST / Sun 19:00 UTC) — Check imported skills for upstream changes and security regressions

## Schedule Timeline

| Time (AEST) | Day | Time (UTC) | Skills |
|-----------|-----|-----------|--------|
| 14:00 | Sun | 04:00 | atlas (fork inventory parse) |
| 15:00 | Sun | 05:00 | atlas-layers (categorical rendering) |
| 16:00 | Sun | 06:00 | **skill-evals** (quality baseline gate) |
| 18:00 | Daily | 08:00 | skill-freshness (dependency audit) + api-health-probe upstream check |
| 18:00 | Mon | 08:00 | fleet-state (weekly digest synthesis) |
| 20:00 | Daily | 10:00 | api-health-probe (external health monitoring) |
| 20:30 | Mon | 10:30 | operator-scorecard (accountability + verdict) |
| 02:00 | Sun→Mon | 16:00 | workflow-security-audit (security pre-gate) |
| 03:00 | Mon | 17:00 | skill-leaderboard (adoption ranking) |
| 03:30 | Mon | 17:30 | fork-contributor-leaderboard (community ranking) |
| 04:00 | Daily | 18:00 | skill-health (daily health analytics) |
| 04:30 | Mon | 18:30 | fork-skill-digest (divergence tracking) |
| 05:00 | Mon | 19:00 | fork-cohort (fork classification) + skill-update-check (upstream security) |
| 05:30 | Mon | 19:30 | fork-release-tracker (shipping velocity) |
| 06:00 | Mon | 20:00 | contributor-spotlight (weekly recognition) |
| 06:30 | Daily | 20:30 | fork-first-run-alert (activation tracking) |
| 07:00 | Mon | 21:00 | fork-skill-gap (adoption gaps) |
| 08:00 | Mon | 22:00 | fleet-skill-adoption (adoption leaderboard) |

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

## Phase 4: Strategic Intelligence & Backlog Management (In Progress)

### Enabled (2 skills)
1. **ai-framework-watch** (Mon 18:30 AEST / 08:30 UTC) — Weekly competitive intelligence digest across 9 AI agent frameworks + peer cohort. Tracks 7d/30d star deltas, releases, breaking changes, momentum signals.
2. **follow-up-patrol** (Tue 21:00 AEST / 11:00 UTC) — Escalation audit: parses MEMORY.md follow-up section + issue tracker, ages items, alerts on overdue CRITICAL/HIGH items (>21d/>14d). Catch-all for open-loop backlog.

### Optional Future Enhancements
1. **fleet-scorecard** — Daily cost + reliability metrics (blocked: needs prefetch integration)
2. **ecosystem-pulse** — Liveness check on watched projects (blocked: needs ECOSYSTEM.md project list)
3. **competitor-launch-radar** — New AI framework launch detection (lower priority: covered by fork analytics)

## Success Metrics (First Week: 2026-09-15)

- [ ] skill-evals completes without errors; quality baseline established
- [ ] fork-cohort produces COLD/STALE/ACTIVE/POWER classification
- [ ] All 25 skills complete their first scheduled run
- [ ] fleet-state generates WoW delta comparison (even if 0 change)
- [ ] operator-scorecard produces verdict (OK/WATCH/DEGRADED)
- [ ] Zero timeout errors on dependent skills (fork-contributor-leaderboard depends on fork-cohort)
