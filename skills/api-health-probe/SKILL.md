---
name: API Health Probe
description: Proactively probe the external API hosts the fleet depends on and alert on state transitions, before they show up as skill failures
var: ""
tags: [meta]
---
> **${var}** — Optional single host to probe (e.g. `api.coingecko.com`). If empty, probes the full registry.

## Purpose

`skill-health` audits skills *after* a run fails. This skill probes the actual third-party hosts directly, on its own schedule, so an outage or slowdown is visible **before** it causes a wave of skill failures — and so a later skill-health CRITICAL can be triaged instantly as "known API outage" instead of "unknown, investigate."

## Data sources

1. **`memory/api-health/registry.md`** — Operator-curated (or self-seeded) list of hosts to probe: `host | probe_url | used_by (skill names)`.
2. **`memory/api-health/state.json`** — Last run's per-host status, for transition detection.
3. **`memory/issues/INDEX.md`** — To avoid filing a duplicate of an issue skill-health already opened for the same host.

## Steps

### 1. Load or seed the registry

Read `memory/api-health/registry.md`. If it doesn't exist, seed it once:
- Grep `skills/*/SKILL.md` for recognizable external API hostnames (e.g. `api.coingecko.com`, `geckoterminal.com`, `api.telegram.org`, `discord.com/api`, `hooks.slack.com`, `arxiv.org`, `hn.algolia.com`) and the skill(s) that mention each.
- Write one row per distinct host with a cheap, side-effect-free `probe_url` (a documented health/ping endpoint, or the lightest read-only endpoint available — never an endpoint that posts, writes, or spends a rate-limit budget meaningfully).
- Log `API_PROBE_REGISTRY_SEEDED — N hosts` to `memory/logs/${today}.md` and note in the run output that the operator should review and curate the list (drop hosts, fix probe URLs, add ones the grep missed).

If `${var}` is set, filter the registry to that one host (error and stop if it's not present).

### 2. Probe each host

For each row, issue a `curl -sS -o /dev/null -w "%{http_code} %{time_total}" --max-time 8 "<probe_url>"`. Classify:

| Status | Condition |
|---|---|
| **UP** | 2xx/3xx within 8s |
| **SLOW** | 2xx/3xx but `time_total > 3` |
| **DOWN** | non-2xx/3xx, timeout, or connection error |

If curl fails outright (sandbox blocking outbound bash network), fall back to WebFetch on the same `probe_url` and classify from what it returns; if WebFetch also can't be used to determine reachability, mark the host `UNKNOWN` for this run rather than guessing.

### 3. Diff against previous state

Load `memory/api-health/state.json` (empty map if missing — first run, not a failure). For each host, compare new status to previous. A host is **notable** this run only if its status *changed* (e.g. UP→DOWN, DOWN→UP, UP→SLOW, SLOW→UP) — steady-state UP or steady-state DOWN (already known) is not notable on its own.

### 4. Reconcile with memory/issues/

Only if `memory/issues/INDEX.md` already exists (same precondition guard as skill-health — do not create it):

- For each host that transitioned **to DOWN**: check open issues for one already naming this host in `root_cause` or `affected_skills`. If found, append `Update YYYY-MM-DD: api-health-probe confirms <host> still DOWN` to that ISS file and do not file a new one. If not found, file a new issue: `severity: medium`, `category: api-change` (or `rate-limit`/`timeout` if the probe error clearly indicates one), `detected_by: api-health-probe`, `affected_skills` = the `used_by` list from the registry row.
- For each host that transitioned **to UP** from a DOWN state that has an open issue naming it: remove it from that issue's `affected_skills`; if the list becomes empty, resolve the issue (`status: resolved`, `resolved_at: now`, move row to Resolved in INDEX.md).

### 5. Persist state

Overwrite `memory/api-health/state.json`:
```json
{
  "last_run_at": "<ISO now>",
  "hosts": {
    "<host>": { "status": "UP|SLOW|DOWN|UNKNOWN", "http_code": 200, "time_total": 0.31, "since": "<ISO of last transition>" }
  }
}
```

### 6. Notify and log

- If no host transitioned this run → do not notify. Log `API_PROBE_NOOP — N hosts, all steady` to `memory/logs/${today}.md`.
- If any host transitioned → `./notify` with one compact message, one line per transition:
  ```
  *API Health*
  🔴 api.coingecko.com → DOWN (used by: token-movers, defi-monitor) → ISS-0NN
  🟢 api.telegram.org → UP (was DOWN since 2026-09-10)
  ```
- Log to `memory/logs/${today}.md`:
  ```
  ### api-health-probe
  - transitions: [<host>: <old>→<new>, ...] or none
  - filed: [ISS-NNN, ...]
  - resolved: [ISS-NNN, ...]
  ```

## Sandbox note

GitHub Actions may block outbound `curl` from bash. If a probe's `curl` call fails to connect at all (not a real 4xx/5xx from the target, but a local connection error), retry that single host via WebFetch on the same `probe_url` before classifying it DOWN — an unreachable sandbox network is not the same signal as a genuinely down API.

## Constraints

- Probes must be read-only and cheap — never call an endpoint that writes, posts, trades, or spends meaningful rate-limit budget just to check liveness.
- Never file a duplicate issue for a host that skill-health (or a prior api-health-probe run) already opened and left open — always check INDEX.md first, same contract as skill-health.
- Do not notify on steady-state runs (nothing transitioned), even if hosts are DOWN — only transitions and the first-ever DOWN are notable.
- If `${var}` names a host not in the registry, say so and stop — do not silently probe an arbitrary URL.
