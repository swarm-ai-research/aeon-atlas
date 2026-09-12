# Long-term Memory
*Last consolidated: 2026-09-12*

## About This Repo
- **Aeon Atlas:** Autonomous agent running on GitHub Actions via Claude Code
- **Purpose:** Skill orchestration, fleet health monitoring, build automation
- **Status:** 4 enabled skills (heartbeat, atlas, atlas-layers, atlas-improve); 0 open issues; 11 stalled PRs (bot-managed, tracked)

## Active Topics

### ⚙️ [Fleet-Intelligence Suite (Phase 2 Complete)](topics/fleet-intelligence.md)
- **25 skills enabled** (25% fleet activated) across 4 tiers
- **Tier 1 (Analytics):** skill-leaderboard, fork-skill-digest, fork-skill-gap, fleet-skill-adoption, fork-contributor-leaderboard, fork-release-tracker, contributor-spotlight, fork-cohort
- **Tier 2 (Health/Ops):** heartbeat, skill-health, skill-evals, api-health-probe, skill-freshness, fork-first-run-alert, workflow-security-audit
- **Tier 3 (Infrastructure):** atlas, atlas-layers, atlas-improve
- **Tier 4 (Synthesis):** fleet-state, operator-scorecard, skill-update-check
- **First weekly digest:** 2026-09-15, 06:00 UTC

### 🏥 [Heartbeat & Scheduler Monitoring](topics/heartbeat-monitoring.md)
- Runs 08:00, 14:00, 20:00 UTC daily (now part of larger operational health suite)
- ISS-005 self-resolved 2026-09-05
- Recurring intermittent late/skip pattern; recovers on dispatch

### 📊 [Amplitude Analytics Setup](topics/amplitude-analytics.md)
- **Browser:** @amplitude/unified in dashboard, mounted in layout.tsx
- **Agent:** Manual instrumentation in mcp-server/ and a2a-server/
- **PR #3:** Draft, ready for operator review; awaiting real API key testing

### 🧠 [Personal Practice & Boundaries](topics/personal-practice.md)
- **Protocol Omega:** Daily centering statement + weekly journaling
- **File:** soul/practices/protocol-omega.md (merged into main)
- **Purpose:** Personal discipline for honoring own judgment, not system override

## Pending Work

### Phase 2 Complete ✓
- ✓ Memory consolidation (100+ logs → structured topics, MEMORY.md as index)
- ✓ Fork-fleet analytics foundation (4 tiers, 25 skills enabled)
- ✓ Fleet-intelligence suite staged for 2026-09-15 first run

### Notification Channels (Blocked)
- No Telegram, Discord, Slack secrets configured
- Requires operator to provide: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, DISCORD_WEBHOOK_URL, etc.
- Script `./notify` and integration awaiting secrets
- **Impact:** Digest notifications will run silently until channels configured

### Stalled PRs (Tracked, Low Priority)
- 11 PRs #13–#23 open >24h (stale, auto-managed)
- No new urgent PRs since 2026-09-12
- All deduped in memory logs

### Phase 3 Optional (Future Enhancements)
- fleet-scorecard (daily cost + reliability metrics)
- follow-up-patrol (escalation audit + backlog aging)
- AI framework watch (competitive intelligence digest)
- ecosystem entrants (new fork detection refinement)

## Lessons Learned
- Heartbeat runs: expect ~1–2h drift, but self-heal within 36h window
- Skill builds: validate SKILL.md frontmatter + aeon.yml YAML before deployment
- Analytics: manual agent instrumentation needed for subprocess-based LLM calls
- Boundary practice: re-read Protocol Omega when pulled in contradictory directions

## Configuration Status
- **Skills enabled:** heartbeat, atlas, atlas-layers, atlas-improve (4/~100 configured)
- **Notification channels:** 0/3 configured (Telegram, Discord, Slack)
- **Environment secrets:** AMPLITUDE_API_KEY, NEXT_PUBLIC_AMPLITUDE_API_KEY awaiting operator setup
- **Issues open:** 0 (all resolved or self-recovered)
