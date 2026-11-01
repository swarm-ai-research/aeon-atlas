# Skill Leaderboard — 2026-11-01

**Verdict:** Domimueller85/aeon shipped aeon-update — not in upstream (now adopted by 5 configured forks independently)

*Scanned 68 active forks of aaronjmars/aeon (pushed in last 30 days). 62 are configured (aeon.yml diverges from upstream defaults). Leaderboard scored against the configured 62.*

## Top Skills (configured fleet)

| Rank | Skill | Forks | % Configured | var | model | sched | Δ vs last week |
|------|-------|-------|--------------|-----|-------|-------|----------------|
| 1 | heartbeat | 62 | 100% | 0 | 0 | 0 | — |
| 2 | auto-workflow | 45 | 72.6% | 0 | 0 | 0 | NEW |
| 3 | skill-enabler | 8 | 12.9% | 0 | 0 | 0 | NEW |
| 4 | fleet-skill-adoption | 7 | 11.3% | 0 | 0 | 0 | NEW |
| 4 | token-movers | 7 | 11.3% | 0 | 0 | 0 | ↓2 |
| 6 | narrative-tracker | 6 | 9.7% | 0 | 0 | 0 | ↓3 |
| 7 | aeon-update ★ | 5 | 8.1% | 0 | 0 | 0 | ↓1 |
| 7 | skill-health | 5 | 8.1% | 0 | 0 | 0 | ↓2 |
| 9 | auto-merge | 4 | 6.5% | 0 | 0 | 0 | NEW |
| 9 | token-pick | 4 | 6.5% | 0 | 0 | 0 | ↓5 |
| 11 | autoresearch | 3 | 4.8% | 0 | 0 | 0 | — |
| 11 | cost-report | 3 | 4.8% | 0 | 0 | 0 | — |
| 11 | defi-monitor | 3 | 4.8% | 0 | 0 | 0 | — |
| 11 | defi-overview | 3 | 4.8% | 0 | 0 | 0 | — |
| 11 | digest | 3 | 4.8% | 0 | 0 | 0 | — |

*(★ = fork-only skill not in upstream. Top 15 by forks_enabled. Δ relative to 2026-10-25 snapshot.)*

## What the fleet is telling us

### Promote
none this week — no upstream-disabled skill has reached the 25% configured-fleet threshold (auto-workflow leads at 72.6% but is `workflow_dispatch`-only, excluded from Promote per methodology)

### Match
none this week — insufficient model-override data across the full 62-fork sample to confirm ≥2 forks independently settling on the same model

### Sunset (review for removal or better docs)
The following upstream skills had zero configured-fork enables in this scan (sample, not exhaustive — full enumeration requires per-skill tree inspection):

- **smithery-manifest** — niche submission workflow; no fork adoption detected
- **pvr-watchlist** — private vuln reporting; likely operator-specific; no fork adoption detected
- **pvr-triage-monitor** — companion to pvr-watchlist; same pattern
- **sparkleware-catalog** — Sparkleware-ecosystem specific; no independent fork adoption
- **show-hn-draft** / **product-hunt-launch** — both workflow_dispatch launch-prep skills; adoption by 0xMal0u only as a bundle

*(Capped at 5 candidates. Meta and dev-tagged skills excluded. Operator overrides take precedence — these are heuristic signals, not removal recommendations.)*

### Fleet-only skills
Skills enabled by ≥1 configured fork but absent from upstream `skills/`:

| Skill | Forks | Notable adopters |
|-------|-------|-----------------|
| aeon-update | 5 | Domimueller85, enuno/noesis-aeon, icepy/aeon-token, njfyanf9-a11y, Svector-anu |
| investigation-report | 3 | czijian729-oss, Domimueller85, icepy/aeon-token |
| sc-audit | 3 | czijian729-oss, Domimueller85, icepy/aeon-token |
| soul-builder | 3 | Domimueller85, enuno/noesis-aeon, njfyanf9-a11y |
| onchain-monitor | 2 | czijian729-oss, Domimueller85 |
| price-alert | 2 | czijian729-oss, Domimueller85 |
| picks-tracker | 2 | czijian729-oss, Domimueller85 |
| higgsfield | 2 | amritmirch, Domimueller85 |
| glim-mcp | 2 | Domimueller85, enuno/noesis-aeon |
| executor-mcp | 2 | Domimueller85, enuno/noesis-aeon |
| install-skill | 2 | Domimueller85, enuno/noesis-aeon |
| pack-submit | 2 | Domimueller85, enuno/noesis-aeon |
| strategy-builder | 2 | Domimueller85, enuno/noesis-aeon |
| aeon-doctor | 2 | Domimueller85, enuno/noesis-aeon |
| idea-forge | 2 | Domimueller85, enuno/noesis-aeon |
| skill-article | 2 | Domimueller85, enuno/noesis-aeon |
| shiplog | 2 | Domimueller85, njfyanf9-a11y |
| base-mcp | 2 | 00288, Domimueller85 |
| bd-radar | 2 | Domimueller85, rohitctrl |

## Week-over-week

**Snapshot date:** 2026-11-01 vs 2026-10-25

**Rising (≥+3 ranks):** none — auto-workflow, skill-enabler, and fleet-skill-adoption are *new entries*, not risers from prior ranking

**Falling (≥-3 ranks):**
- narrative-tracker: rank 3 → 6 (−3; displaced by new entrants)
- token-pick: rank 4 → 9 (−5; displaced by new entrants)

**New entries:** auto-workflow (rank 2, 72.6%), skill-enabler (rank 3, 12.9%), fleet-skill-adoption (rank 4, 11.3%), auto-merge (rank 9, 6.5%)

**Dropouts:** none — all prior top-41 skills retain ≥1 configured-fork enable

**Fleet growth:** 64 → 68 active forks (+4); configured count held steady at 62 (template/unreadable absorbed the new forks)

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 62 | 91.2% |
| Template (untouched aeon.yml — heartbeat only) | 5 | 7.4% |
| Unreadable (no tree / 404) | 1 | 1.5% |
| **Total active forks** | **68** | **100%** |

Template forks: gitlawbounty, youpsla, antfleet-ops, abhirajprasad, takanafur

## Source status

- Trees fetched: 67 / 68 (unifirer/aeon returned 404)
- aeon.yml readable: 67 / 68
- Rate-limited: 0
- Fork-only skill files detected (enabled): 19 distinct skill slugs across 11 forks
- Most active fleet fork: Domimueller85/aeon (80+ skills enabled, 43 fork-only)

---
*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork counts as "configured" if its `aeon.yml` differs from upstream defaults on `enabled`, `model`, `var`, or `schedule` for any skill. Untouched templates are excluded from leaderboard math.*
