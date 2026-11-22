# Skill Leaderboard — 2026-11-22

**Verdict:** defi-overview jumped from rank 8 to rank 2 this week

*Scanned 61 active forks of aaronjmars/aeon (pushed in last 30 days). 55 are configured (aeon.yml diverges from upstream defaults). Leaderboard scored against the configured 55.*

## Top Skills (configured fleet)

| Rank | Skill | Forks | % Configured | var | model | sched | Δ vs last week |
|------|-------|-------|--------------|-----|-------|-------|----------------|
| 1 | heartbeat | 55 | 100% | 0 | 0 | 55 | — |
| 2 | aeon-update ★ | 5 | 9.1% | 1 | 0 | 0 | ↑2 |
| 2 | defi-overview | 5 | 9.1% | 0 | 0 | 1 | ↑6 |
| 4 | narrative-tracker | 5 | 9.1% | 0 | 0 | 0 | ↓1 |
| 5 | memory-flush | 4 | 7.3% | 0 | 0 | 4 | ↑3 |
| 6 | auto-merge | 4 | 7.3% | 1 | 0 | 0 | ↓1 |
| 6 | github-monitor | 4 | 7.3% | 1 | 0 | 0 | ↑3 |
| 6 | narrative-convergence | 4 | 7.3% | 1 | 0 | 0 | ↑3 |
| 9 | auto-workflow | 4 | 7.3% | 0 | 0 | 0 | ↓1 |
| 9 | skill-health | 4 | 7.3% | 0 | 0 | 0 | ↓1 |
| 11 | autoresearch | 3 | 5.5% | 2 | 0 | 1 | ↓3 |
| 12 | digest | 3 | 5.5% | 1 | 0 | 1 | ↓3 |
| 13 | aeon-doctor ★ | 3 | 5.5% | 1 | 0 | 0 | ↑8 |
| 13 | monitor-polymarket | 3 | 5.5% | 0 | 1 | 0 | ↑8 |
| 13 | soul-builder ★ | 3 | 5.5% | 1 | 0 | 0 | ↓3 |

(★ = fork-only skill not present in upstream. Full table shows 15 ranked skills; heartbeat included for completeness but excluded from verdict signals per methodology.)

## What the fleet is telling us

### Promote
None this week — highest adoption is 9.1% (defi-overview, aeon-update, narrative-tracker), well below the 25% promote threshold.

### Match
None this week — no skill shows ≥2 configured forks independently overriding to the same model value.

### Sunset (review for removal or better docs)
1. **morning-brief** — 3 forks last run → 0 this run; inactive operators have dropped off entirely
2. **telegram-digest** — 0 configured-fork enables across both runs
3. **github-issues** — 0 configured-fork enables
4. **rss-digest** — 0 configured-fork enables
5. **paper-digest** — 0 configured-fork enables

### Fleet-only skills
Skills not in upstream but enabled by ≥1 configured fork:
- **aeon-update** — 5 forks (njfyanf9-a11y, icepy/aeon-token, Svector-anu, Domimueller85, enuno/noesis-aeon) — weekly upstream-sync PR opener; highest-adoption fork-only skill
- **aeon-doctor** — 3 forks (njfyanf9-a11y, Domimueller85, enuno/noesis-aeon) — config linter
- **soul-builder** — 3 forks (njfyanf9-a11y, Domimueller85, enuno/noesis-aeon) — SOUL.md generator
- **glim-mcp** — 2 forks (Domimueller85, enuno/noesis-aeon) — live-data research MCP
- **executor-mcp** — 2 forks (Domimueller85, enuno/noesis-aeon)
- **install-skill** — 2 forks (Domimueller85, enuno/noesis-aeon) — community skill pack installer
- **pack-submit** — 2 forks (Domimueller85, enuno/noesis-aeon)
- **strategy-builder** — 2 forks (Domimueller85, enuno/noesis-aeon)
- **shiplog** — 2 forks (njfyanf9-a11y, Domimueller85)
- **base-mcp** — 2 forks (00288, Domimueller85)
- *Single-fork:* bankr-space-worker (anondevv69), lawb-pool-monitor (lawbworld-tech), mine-bean (damo-nu11), bounty-hunter (airdropia), spodumene-reverse-flotation (duan521127), hyperliquid-market-monitor (hypurr-inc), flovia (domosta), revenue-alert (domosta), arxiv-radar (icepy), defillama-radar (icepy), and 20+ more from Domimueller85's highly-activated fork

## Week-over-week

**Rising** (moved up ≥3 ranks):
- defi-overview: rank 8 → rank 2 (↑6) — 3 forks last run → 5 this run
- aeon-doctor ★: rank 19 → rank 13 (↑8) — 2 forks → 3
- monitor-polymarket: rank 19 → rank 13 (↑8) — 2 forks → 3
- fork-fleet: rank 19 → rank ~16 (↑3) — 2 forks → 3
- skill-repair: rank 19 → rank ~16 (↑3) — 2 forks → 3
- github-monitor: rank 8 → rank 6 (↑3) — 3 forks → 4
- narrative-convergence: rank 8 → rank 6 (↑3) — 3 forks → 4
- memory-flush: rank 8 → rank 5 (↑3) — 3 forks → 4

**Falling** (moved down ≥3 ranks):
- token-movers: rank 2 → rank ~16 (↓9) — 7 forks → 3
- token-pick: rank 4 → rank ~16 (↓7) — 4 forks → 3
- autoresearch: rank 8 → rank 11 (↓3)
- soul-builder ★: rank 8 → rank 13 (↓3)
- digest: rank 8 → rank 12 (↓3)

**New entries:** No entirely new skills this week; defi-overview, monitor-polymarket, fork-fleet, skill-repair all rise from the rank-19 group.

**Dropouts** (were ranked, forks_enabled now 0):
- morning-brief: rank 8 last run → 0 configured-fork enables this run (operators who had it active fell out of the 30-day window)
- cost-report: rank 8 last run → 1 fork this run (dropped from group)

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 55 | 90.2% |
| Template (untouched aeon.yml) | 6 | 9.8% |
| Unreadable (no tree / no yml / rate-limited) | 0 | 0.0% |
| **Total active forks** | 61 | 100% |

## Source status

- Trees fetched: 61 / 61
- aeon.yml readable: 61 / 61
- Rate-limited: 0
- Fork-only skill files inspected: ~35 unique fork-only skill names across the fleet

---
*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork counts as "configured" if its `aeon.yml` differs from upstream defaults on `enabled`, `model`, `var`, or `schedule` for any skill. Untouched templates are excluded from leaderboard math.*
