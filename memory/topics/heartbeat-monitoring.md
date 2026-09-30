# Heartbeat & Scheduler Monitoring

Aeon's health check runs three times daily: 08:00, 14:00, 20:00 UTC. Monitors skill dispatch success, run outcomes, and system degradation.

## ISS-005 Recovery (2026-09-05)
**Issue:** scheduler quiet ~65h — heartbeat missed 6 slots + atlas/atlas-layers missed 08-30 Sunday slots.
**Status:** Resolved via 3 consecutive clean heartbeat slots (09-04 14:00 → 09-05 08:00); dispatch path recovered.
**Signature:** Recurring intermittent late/skip (heartbeat 89% 238/267, atlas 100% 9/9, atlas-layers 93% 13/14). Each run recovers on dispatch; self-check < 36h threshold → monitor-only, not DEGRADED.

## Monitoring Pattern
- **Metrics:** skill success rate, consecutive failures, time since last success, scheduler anchor drift
- **Thresholds:** 36h staleness trigger, 3 consecutive missed anchors escalation, chronic failure >50% = HIGH
- **Check frequency:** heartbeat runs; filed issues tracked in memory/issues/INDEX.md

## Current Fleet (2026-09-11)
- `heartbeat`: 89% (238/267 runs) — robust, self-healing
- `atlas`: 100% (9/9 recent) — weekly Sunday 04:00 UTC
- `atlas-layers`: 93% (13/14 recent) — weekly Sunday 05:00 UTC
- `atlas-improve`: 100% (3/3 recent) — monthly 1st @ 06:00 UTC
- **0 open issues.** All failures self-resolved or tracked as resolved.

## Scheduler Notes
- 08:00 anchor (most critical): fires ~1–2h late intermittently but recovers
- No 2nd consecutive missed anchor observed since 09-05 recovery
- Next weekly cohort test: 2026-09-13 04:00/05:00 UTC
