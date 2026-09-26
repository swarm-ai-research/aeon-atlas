# Pre-Run Checklist: First Full Fleet-Intelligence Execution
## Target: 2026-09-15, 16:00 AEST (06:00 UTC)

### ✅ Phase 1-4 Skills Status
- [x] 29/~100 skills enabled (29% fleet activation)
- [x] All tier dependencies verified (fork-cohort → fork-health-score → contributor-spotlight)
- [x] Quality gate (skill-evals) scheduled first (06:00 UTC Sunday)
- [x] All SKILL.md files exist for enabled skills
- [x] Schedule gaps verified (no conflicting time slots)

### 🔐 Configuration Checklist
- [ ] **Notification channels** (BLOCKING if digests are to be sent)
  - `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` — optional
  - `DISCORD_WEBHOOK_URL` — optional
  - `SLACK_WEBHOOK_URL` — optional
  - **Impact:** Without these, all digests run silently (no notifications sent)
  - **Fix:** Provide at least one channel secret in GitHub repo settings

- [ ] **GitHub token permissions**
  - `GITHUB_TOKEN` has read access to 129+ forks
  - `GITHUB_TOKEN` has read access to all managed instances (if any) in memory/instances.json
  - **Fix:** Verify GitHub App or PAT has required scopes

- [ ] **Amplitude analytics setup** (optional, monitored separately)
  - `AMPLITUDE_API_KEY` configured for agent instrumentation
  - `NEXT_PUBLIC_AMPLITUDE_API_KEY` configured for browser setup
  - **Impact:** Analytics features gracefully degrade without keys

### 📋 Data Readiness
- [x] **ECOSYSTEM.md** populated with 65+ projects (ecosystem-pulse ready)
- [ ] **memory/instances.json** (optional for fleet-scorecard)
  - Create if managing multi-repo fleet
  - Format: `{ "instances": [{ "repo": "owner/repo", "archived": false }] }`
  - **Impact:** Without this, fleet-scorecard reports only self repo

- [ ] **memory/MEMORY.md follow-up section** (optional for follow-up-patrol)
  - Required if escalation audit should monitor tagged backlog items
  - Format: Standard markdown list with CRITICAL/HIGH/MEDIUM tags

### 🧪 Validation Steps (Run Sunday 2026-09-12 or 2026-09-13)
- [ ] Manually trigger one skill (e.g., `skill-evals`) to verify:
  - Claude can execute the SKILL.md
  - No timeout/sandbox issues
  - Output format is correct
  - Model access is available

- [ ] Check GitHub Actions logs for workflow errors:
  - No permission denied errors
  - No missing secrets in console output
  - Token usage is within rate limits

### 📊 Success Criteria (First Week: 2026-09-15 - 2026-09-22)
- [ ] skill-evals completes without errors; quality baseline established
- [ ] fork-cohort produces COLD/STALE/ACTIVE/POWER classification
- [ ] All 29 skills complete their first scheduled run
- [ ] fleet-state generates WoW delta comparison (even if 0 change)
- [ ] operator-scorecard produces verdict (OK/WATCH/DEGRADED)
- [ ] Zero timeout errors on dependent skills
- [ ] ecosystem-pulse resolves ECOSYSTEM.md projects to GitHub repos
- [ ] ai-framework-watch digests 9 AI frameworks successfully
- [ ] follow-up-patrol validates backlog items (if populated)
- [ ] fleet-scorecard reports costs/reliability without errors

### 🔄 Rollback Plan (if first run fails)
1. **Check logs:** `./scripts/skill-runs --hours 2 --failures`
2. **Identify failing skill:** Review SKILL.md and error context
3. **Disable & investigate:**
   - Set `enabled: false` for the failing skill in aeon.yml
   - Commit + push to branch
   - Re-run (only non-failing skills will execute next time)
4. **Root cause analysis:**
   - Missing secret? Add to GitHub repo settings
   - API change? Check SKILL.md comments for vendor-specific notes
   - Timeout? Check skill complexity vs available time slot
5. **File issue:** Create memory/issues/ISS-NNN.md with category + context

### ⏰ Timeline
- **2026-09-12:** Configuration checklist + optional data setup
- **2026-09-13:** Validation run (manual trigger one skill)
- **2026-09-15, 06:00 UTC / 16:00 AEST:** First full pipeline execution begins
- **2026-09-15 - 2026-09-22:** Monitor runs, collect success metrics

---

**Status:** Awaiting configuration + operator action for notification channels.
**Next step:** Provide at least one notification channel secret to enable digest delivery.
