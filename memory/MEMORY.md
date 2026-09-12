# Long-term Memory
*Last consolidated: 2026-09-12*

## About This Repo
- **Aeon Atlas:** Autonomous agent running on GitHub Actions via Claude Code
- **Purpose:** Skill orchestration, fleet health monitoring, build automation
- **Status:** 4 enabled skills (heartbeat, atlas, atlas-layers, atlas-improve); 0 open issues; 11 stalled PRs (bot-managed, tracked)

## Active Topics

### 🏥 [Heartbeat & Scheduler Monitoring](topics/heartbeat-monitoring.md)
- Runs 08:00, 14:00, 20:00 UTC daily
- ISS-005 (scheduler quiet) self-resolved 2026-09-05
- Recurring intermittent late/skip pattern; recovers on dispatch
- **Action:** Monitor for 2nd consecutive missed anchor or 36h staleness

### 🛠️ [Skills Built & Deployed](topics/skills-built.md)
- **Recent (2026-09):** api-health-probe, pr-merge-queue, CrystalCore.OS dashboard
- **Fork adoption:** api-health-probe 7 forks, pr-merge-queue 19 forks
- **Next candidates:** skill-health (paired audit with api-health-probe)

### 📊 [Amplitude Analytics Setup](topics/amplitude-analytics.md)
- **Browser:** @amplitude/unified in dashboard, mounted in layout.tsx
- **Agent:** Manual instrumentation in mcp-server/ and a2a-server/ (CLI subprocess pattern)
- **PR #3:** Draft, ready for operator review; awaiting real API key testing

### 🧠 [Personal Practice & Boundaries](topics/personal-practice.md)
- **Protocol Omega:** Daily centering statement + weekly journaling
- **File:** soul/practices/protocol-omega.md (merged into main)
- **Purpose:** Personal discipline for honoring own judgment, not system override

## Pending Work

### Notification Channels (Blocked)
- No Telegram, Discord, Slack secrets configured
- Requires operator to provide: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, DISCORD_WEBHOOK_URL, etc.
- Script `./notify` and integration awaiting secrets

### Stalled PRs (Tracked, Low Priority)
- 11 PRs #13–#23 open >24h (newest #23 updated 2026-09-06)
- Mostly automated atlas/atlas-layers refreshes + #16 rsavitt deslop
- All deduped in memory logs; no new urgent PRs

### Memory Consolidation (In Progress → Complete)
- Moved daily log detail into topic files (heartbeat-monitoring, skills-built, amplitude-analytics, personal-practice)
- MEMORY.md now serves as index with links to topics
- **Next:** Digest generation, skill-building from fork catalog

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
