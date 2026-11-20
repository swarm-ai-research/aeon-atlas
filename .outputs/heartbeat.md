Heartbeat complete. Summary below.

## Summary

Ran the `heartbeat` skill for the **2026-11-20 08:00 slot** (executed 09:15 UTC, ~1h15m late — within native-`schedule:` jitter). Soul files are template-only → neutral tone.

**Findings:**
- **P0 — `🔴 DEGRADED`:** `fork-cohort` still 🕸 STUCK (`dispatched` since 2026-10-25, ~25.5d ≫ 45min) → keeps Overall DEGRADED. No failed skills, no `consecutive_failures ≥ 3`, no chronic failures.
- **Scheduler recovering (not a fresh escalation):** two consecutive scheduled heartbeat slots have now landed (11-19 20:00 + 11-20 08:00) — the 11-17→11-19 dark window broke. Self-check ~12.6h (well under 36h). `fork-first-run-alert` recovered. **2 of the 3-slot** ISS-011 resolution bar met; third slot to watch is 11-20 14:00/20:00.
- **P1:** No open GitHub issues; 18 PRs all within the known tracked/bot-managed set — deduped.
- **P2:** Notification channels still 0/3 (Discord secret pending since 09-13) — old, deduped.
- **P3 (within ISS-011):** api-health-probe ~7.9d (dominant daily breach), fleet-scorecard ~5.8d, skill-health ~5.6d, skill-freshness ~3.0d; weekly cohorts stale; follow-up-patrol never-run.

**Notification: NOT sent** — deduped. Same ongoing conditions already notified 11-17/11-18, now *improving*; no full resolution and no fresh P0 escalation → re-notify would be noise (channels would skip anyway).

**Files modified:**
- `docs/status.md` — regenerated (🔴 DEGRADED, 26 skills, Open issues 1, Next run api-health-probe 10:00 UTC)
- `memory/issues/ISS-011.md` — appended 11-20 continuation (recovery signal, close-candidate criteria)
- `memory/issues/INDEX.md` — refreshed ISS-011 row (detected → 2026-11-20)
- `memory/logs/2026-11-20.md` — this run's log

**Verdict:** `HEARTBEAT_OK (attention: DEGRADED, deduped) · STATUS_PAGE=DEGRADED — wrote docs/status.md`

**Follow-up (operator action required):** durable offset-cron / external `workflow_dispatch` backstop for the recurring native-`schedule:` dispatch gap (`skill-repair` disabled). Watch 11-20 14:00 → 20:00 for the third clean slot; clear api-health-probe (~7.9d); fork-cohort next retry Sun 11-22 19:00. The modified files land on `main` via the workflow's auto-commit step.
