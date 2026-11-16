# Skill Leaderboard — 2026-10-25

**Verdict:** 4 forks enabled `aeon-update` — not in upstream

*Scanned 64 active forks of aaronjmars/aeon (pushed in last 30 days). 62 are configured (aeon.yml diverges from upstream defaults). Leaderboard scored against the configured 62.*

## Top Skills (configured fleet)

| Rank | Skill | Forks | % Configured | var | model | sched | Δ vs last week |
|------|-------|-------|--------------|-----|-------|-------|----------------|
| 1 | heartbeat | 62 | 100% | 0 | 0 | 0 | first snapshot |
| 2 | token-movers | 8 | 12.9% | 0 | 0 | 0 | first snapshot |
| 3 | narrative-tracker | 6 | 9.7% | 0 | 0 | 0 | first snapshot |
| 4 | token-pick | 4 | 6.5% | 0 | 0 | 0 | first snapshot |
| 5 | skill-health | 4 | 6.5% | 0 | 0 | 0 | first snapshot |
| 6 | aeon-update ★ | 4 | 6.5% | 0 | 0 | 0 | first snapshot |
| 7 | autoresearch | 3 | 4.8% | 0 | 0 | 0 | first snapshot |
| 8 | cost-report | 3 | 4.8% | 0 | 0 | 0 | first snapshot |
| 9 | defi-overview | 3 | 4.8% | 0 | 0 | 0 | first snapshot |
| 10 | digest | 3 | 4.8% | 0 | 0 | 0 | first snapshot |
| 11 | github-monitor | 3 | 4.8% | 0 | 0 | 0 | first snapshot |
| 12 | investigation-report ★ | 3 | 4.8% | 0 | 0 | 0 | first snapshot |
| 13 | memory-flush | 3 | 4.8% | 0 | 0 | 0 | first snapshot |
| 14 | morning-brief | 3 | 4.8% | 0 | 0 | 0 | first snapshot |
| 15 | on-chain-monitor | 3 | 4.8% | 0 | 0 | 0 | first snapshot |

★ = fork-only skill (not in upstream)

(15 ranked. 62 configured forks total.)

## What the fleet is telling us

### Promote
none this week — no skill exceeds 25% of configured forks (highest: token-movers at 12.9%)

### Match
none this week — no model override pattern detected across ≥2 forks

### Sunset (review for removal or better docs)
The entire fleet-intelligence suite shipped in this instance has 0 adoption across configured forks. Top 5 candidates for review:

- **api-health-probe** — 0 forks, enabled:true in upstream
- **ai-framework-watch** — 0 forks, enabled:true in upstream
- **ecosystem-pulse** — 0 forks, enabled:true in upstream
- **fleet-state** — 0 forks, enabled:true in upstream
- **fork-cohort** — 0 forks, enabled:true in upstream

Note: all 26 fleet-intelligence skills enabled in this instance have 0 adoption. This likely reflects that most active forks predate the fleet-intelligence suite and haven't updated. Better discoverability (docs, onboard skill) may be more effective than removal.

### Fleet-only skills
Skills built by forks but absent from upstream — sorted by adoption:

- **aeon-update** — 4 forks: bgiesing/pepper-bgiesing, icepy/aeon-token, Svector-anu/aeon, Domimueller85/aeon
- **onchain-monitor** — 3 forks: icepy/aeon-token, czijian729-oss/aeon, Domimueller85/aeon
- **investigation-report** — 3 forks: icepy/aeon-token, czijian729-oss/aeon, Domimueller85/aeon
- **price-alert** — 3 forks: icepy/aeon-token, czijian729-oss/aeon, Domimueller85/aeon
- **sc-audit** — 3 forks: icepy/aeon-token, czijian729-oss/aeon, Domimueller85/aeon
- **aeon-doctor** — 2 forks: bgiesing/pepper-bgiesing, Domimueller85/aeon
- **install-skill** — 2 forks: bgiesing/pepper-bgiesing, Domimueller85/aeon
- **weekly-aeoncard** — 2 forks: bgiesing/pepper-bgiesing, Domimueller85/aeon
- **picks-tracker** — 2 forks: czijian729-oss/aeon, Domimueller85/aeon
- **higgsfield** — 2 forks: amritmirch/aeon, Domimueller85/aeon
- And ~40 skills unique to Domimueller85/aeon (most active fork)

## Week-over-week

First ranked snapshot — no comparison.

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 62 | 97% |
| Template (untouched aeon.yml) | 1 | 2% |
| Unreadable (no tree / no yml / rate-limited) | 1 | 2% |
| **Total active forks** | 64 | 100% |

## Source status

- Trees fetched: 63 / 64
- aeon.yml readable: 63 / 64
- Rate-limited: 0
- Fork-only skill files inspected: ~20 distinct fork-only skill names across the fleet

---
*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork counts as "configured" if its `aeon.yml` differs from upstream defaults on `enabled`, `model`, `var`, or `schedule` for any skill. The single template fork (swarm-ai-research/aeon-atlas) matches this instance's 26-skill fleet-intelligence configuration exactly and is excluded from leaderboard math.*
