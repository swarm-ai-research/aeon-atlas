# Issues

## Open

| ID | Title | Severity | Category | Detected |
|----|-------|----------|----------|----------|
| _none_ | | | | |

## Resolved

| ID | Title | Severity | Fix PR | Resolved |
|----|-------|----------|--------|----------|
| ISS-008 | scheduler quiet window — heartbeat dropped slots 10-01→10-06 (incl. 10-05 20:00 HUNG run) + atlas-improve 10-01 monthly + atlas/atlas-layers 10-04 Sunday slots → scheduler-wide; P0/DEGRADED 10-06 cleared 10-07; self-resolve bar reset 4× then self-resolved on 3 consecutive clean slots 10-07 08:00 → 14:00 → 20:00 with P0 clear throughout; durable offset-cron / external-dispatch backstop still recommended | high | — (self-resolved; 3 consecutive clean heartbeat slots 10-07 08:00 → 20:00, dispatch path recovered) | 2026-10-07 |
| ISS-007 | scheduler quiet windows — heartbeat missed dispatches (recurrence of ISS-005/006); self-resolved on 7th recovery attempt: 3 consecutive clean slots 09-29 08:00 → 14:00 → 20:00; heartbeat-cadence-specific (cohort clean 09-27), 08:00 slot the weak point; durable fix (redundant morning-offset cron / external dispatch) still recommended | high | — (self-resolved; 3 consecutive clean heartbeat slots 09-29 08:00 → 20:00, dispatch path recovered) | 2026-09-29 |
| ISS-006 | scheduler quiet ~36.5h — heartbeat missed all three 2026-09-16 slots (fresh recurrence of ISS-005) | high | — (self-resolved; 3 consecutive clean heartbeat slots 09-17 08:00 → 20:00, dispatch path recovered) | 2026-09-17 |
| ISS-005 | scheduler quiet ~65h — heartbeat missed 6 slots + atlas/atlas-layers missed 08-30 Sunday slots | high | — (self-resolved; 3 consecutive clean heartbeat slots 09-04 14:00 → 09-05 08:00, dispatch path recovered) | 2026-09-05 |
| ISS-003 | atlas not dispatching on its weekly Sunday 04:00 slot (2 consecutive misses) | medium | — (self-resolved; atlas dispatched cleanly 2026-08-09, PR #— / cron-state) | 2026-08-09 |
| ISS-004 | heartbeat hung on its 2026-08-06 14:00 slot and missed 20:00 (~24h monitoring gap) | medium | — (self-resolved; transient one-off hang, 3 clean slots 08-07) | 2026-08-07 |
| ISS-001 | heartbeat recorded failed on every run (29 consecutive) despite executing | critical | — (self-resolved; recorder now classifies heartbeat successes) | 2026-07-26 |
| ISS-002 | atlas-layers not dispatching on its weekly Sunday 05:00 slot (2 consecutive misses) | medium | — (self-resolved; dispatched cleanly 2026-07-26, PR #17) | 2026-07-26 |
