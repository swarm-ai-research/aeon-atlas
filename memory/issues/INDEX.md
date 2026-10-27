# Issues

## Open

| ID | Title | Severity | Category | Detected |
|----|-------|----------|----------|----------|

_No open issues._

## Resolved

| ID | Title | Severity | Fix PR | Resolved |
|----|-------|----------|--------|----------|
| ISS-010 | api.semanticscholar.org keyless 429 — NOT a real transition: host was already in the registry's Excluded section (seed 10-26, keyless rate-limit, re-enable w/ x-api-key). Surfaced only by a seed-time duplicate active-table row. Opened in error, closed **wontfix**; registry active-table dupe removed and host dropped from state.json. Run was otherwise a NOOP (25 active hosts all steady UP) → no notification | low | — (config; registry deduped, no code/API change) | 2026-10-27 |
| ISS-009 | scheduler quiet window (ISS-005→008 lineage) — DEGRADED 10-16 08:00 (full 10-15 blackout → 36h self-check fired ~36.6h, NOTIFIED), de-escalated 🟡 WATCH 10-16 14:00. Cond (a) heartbeat 3-slot clean progression COMPLETE 10-16 08:00→14:00→20:00, held clean through 10-24. Cond (b) cohort recovery: atlas ✅ 10-18 (13/13, PR #33), atlas-layers ✅ **recovered 10-25 05:00 slot** (06:14→06:17, 16/17, PR #34, first success since 09-27 / ~28d frozen). Both conditions met → resolved. Native-`schedule:` jitter persists as known characteristic (atlas dropped its 10-25 04:00 slot, within tolerance; heartbeat slots still ~1-2h late) — fresh miss after close = new issue per convention. Durable offset-cron / external-dispatch backstop remains recommended operator-action | high | — (self-resolved; heartbeat 3-slot bar met 10-16 + cohort recovery confirmed atlas 10-18 / atlas-layers 10-25) | 2026-10-25 |
| ISS-008 | scheduler quiet window — heartbeat dropped slots 10-01→10-06 (incl. 10-05 20:00 HUNG run) + atlas-improve 10-01 monthly + atlas/atlas-layers 10-04 Sunday slots → scheduler-wide; P0/DEGRADED 10-06 cleared 10-07; self-resolve bar reset 4× then self-resolved on 3 consecutive clean slots 10-07 08:00 → 14:00 → 20:00 with P0 clear throughout; durable offset-cron / external-dispatch backstop still recommended | high | — (self-resolved; 3 consecutive clean heartbeat slots 10-07 08:00 → 20:00, dispatch path recovered) | 2026-10-07 |
| ISS-007 | scheduler quiet windows — heartbeat missed dispatches (recurrence of ISS-005/006); self-resolved on 7th recovery attempt: 3 consecutive clean slots 09-29 08:00 → 14:00 → 20:00; heartbeat-cadence-specific (cohort clean 09-27), 08:00 slot the weak point; durable fix (redundant morning-offset cron / external dispatch) still recommended | high | — (self-resolved; 3 consecutive clean heartbeat slots 09-29 08:00 → 20:00, dispatch path recovered) | 2026-09-29 |
| ISS-006 | scheduler quiet ~36.5h — heartbeat missed all three 2026-09-16 slots (fresh recurrence of ISS-005) | high | — (self-resolved; 3 consecutive clean heartbeat slots 09-17 08:00 → 20:00, dispatch path recovered) | 2026-09-17 |
| ISS-005 | scheduler quiet ~65h — heartbeat missed 6 slots + atlas/atlas-layers missed 08-30 Sunday slots | high | — (self-resolved; 3 consecutive clean heartbeat slots 09-04 14:00 → 09-05 08:00, dispatch path recovered) | 2026-09-05 |
| ISS-003 | atlas not dispatching on its weekly Sunday 04:00 slot (2 consecutive misses) | medium | — (self-resolved; atlas dispatched cleanly 2026-08-09, PR #— / cron-state) | 2026-08-09 |
| ISS-004 | heartbeat hung on its 2026-08-06 14:00 slot and missed 20:00 (~24h monitoring gap) | medium | — (self-resolved; transient one-off hang, 3 clean slots 08-07) | 2026-08-07 |
| ISS-001 | heartbeat recorded failed on every run (29 consecutive) despite executing | critical | — (self-resolved; recorder now classifies heartbeat successes) | 2026-07-26 |
| ISS-002 | atlas-layers not dispatching on its weekly Sunday 05:00 slot (2 consecutive misses) | medium | — (self-resolved; dispatched cleanly 2026-07-26, PR #17) | 2026-07-26 |
