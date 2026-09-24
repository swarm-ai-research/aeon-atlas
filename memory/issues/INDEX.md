# Issues

## Open

| ID | Title | Severity | Category | Detected |
|----|-------|----------|----------|----------|
| ISS-007 | scheduler quiet windows — heartbeat missed dispatch; recovery reset 09-24 (2nd ~41.7h quiet window: 09-23 all three + 09-24 08:00 missed after 2/3 recovery), 36h self-check breached twice (recurrence of ISS-005/006) | high | unknown | 2026-09-22 |

## Resolved

| ID | Title | Severity | Fix PR | Resolved |
|----|-------|----------|--------|----------|
| ISS-006 | scheduler quiet ~36.5h — heartbeat missed all three 2026-09-16 slots (fresh recurrence of ISS-005) | high | — (self-resolved; 3 consecutive clean heartbeat slots 09-17 08:00 → 20:00, dispatch path recovered) | 2026-09-17 |
| ISS-005 | scheduler quiet ~65h — heartbeat missed 6 slots + atlas/atlas-layers missed 08-30 Sunday slots | high | — (self-resolved; 3 consecutive clean heartbeat slots 09-04 14:00 → 09-05 08:00, dispatch path recovered) | 2026-09-05 |
| ISS-003 | atlas not dispatching on its weekly Sunday 04:00 slot (2 consecutive misses) | medium | — (self-resolved; atlas dispatched cleanly 2026-08-09, PR #— / cron-state) | 2026-08-09 |
| ISS-004 | heartbeat hung on its 2026-08-06 14:00 slot and missed 20:00 (~24h monitoring gap) | medium | — (self-resolved; transient one-off hang, 3 clean slots 08-07) | 2026-08-07 |
| ISS-001 | heartbeat recorded failed on every run (29 consecutive) despite executing | critical | — (self-resolved; recorder now classifies heartbeat successes) | 2026-07-26 |
| ISS-002 | atlas-layers not dispatching on its weekly Sunday 05:00 slot (2 consecutive misses) | medium | — (self-resolved; dispatched cleanly 2026-07-26, PR #17) | 2026-07-26 |
