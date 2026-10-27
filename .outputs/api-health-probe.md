Probe run complete. Here's the outcome.

## Summary

Ran **api-health-probe** across the full registry (no `${var}` filter).

**Probe result:** All **25 active hosts UP** (HTTP 2xx/3xx, all responding in ~0.03–0.38s — none SLOW, none DOWN). Versus the 2026-10-26 state, **no transitions** → steady-state run → **no notification sent** (per the skill's steady-state rule).

**One anomaly, investigated and dispositioned:** `api.semanticscholar.org` returned HTTP **429** (keyless rate-limit) on two consecutive probes. It initially looked like a first-ever DOWN, but the full registry showed it was **already in the "Excluded — needs a better probe" section** (added on the 2026-10-26 seed, with the `x-api-key` re-enable note). Its 429 is a known, documented, non-liveness signal — not an outage. It got probed only because the seed run **also** left a duplicate row for it in the *active* table. So it's not a real transition, and the actual defect was the registry duplication.

**Actions taken (memory-data writes, not code):**
- `memory/api-health/registry.md` — removed the stale duplicate `api.semanticscholar.org` active-table row; the Excluded-section entry is now the single source of truth.
- `memory/api-health/state.json` — recorded this run's results for the 25 active hosts (all UP); dropped `api.semanticscholar.org` (excluded hosts aren't tracked for transitions).
- `memory/issues/ISS-010.md` + `INDEX.md` — filed ISS-010 during triage, then **closed it `wontfix`** once I found the excluded-section entry; it stands as the audit trail (couldn't `rm` the file — approval-gated in this sandbox). INDEX Open table is back to empty; ISS-010 is under Resolved.
- `memory/logs/2026-10-27.md` — logged `API_PROBE_NOOP — 25 hosts, all steady` with the full investigation.

**Verification:** state.json is valid with 25 hosts and no semanticscholar; registry active table has no leftover gap.

**Follow-up (operator action, carried from the seed):** the excluded hosts need better probes to re-enable liveness tracking — `api.semanticscholar.org` (add `SEMANTIC_SCHOLAR_API_KEY`/`x-api-key`), `eth.llamarpc.com` + `mainnet.base.org` (read-only JSON-RPC POST), `www.reddit.com` (custom User-Agent). No PR opened — these are the skill's own in-place memory writes, not source changes.
