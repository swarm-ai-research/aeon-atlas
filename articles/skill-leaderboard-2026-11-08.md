# Skill Leaderboard — 2026-11-08

**Verdict:** Domimueller85/aeon shipped aeon-update (and 50+ more) — not in upstream

*Scanned 65 active forks of aaronjmars/aeon (pushed in last 30 days). 64 are configured (aeon.yml diverges from upstream defaults). Leaderboard scored against the configured 64.*

## Top Skills (configured fleet)

| Rank | Skill | Forks | % Configured | var | model | sched | Δ vs last week |
|------|-------|-------|--------------|-----|-------|-------|----------------|
| 1 | heartbeat | 64 | 100% | 0 | 0 | 48 | — |
| 2 | token-movers | 7 | 10.9% | 2 | 0 | 1 | ↑2 |
| 3 | narrative-tracker | 6 | 9.4% | 1 | 1 | 2 | ↑3 |
| 4 | auto-merge | 4 | 6.3% | 2 | 0 | 1 | — |
| 4 | auto-workflow | 4 | 6.3% | 0 | 0 | 0 | ↓4 |
| 4 | skill-health | 4 | 6.3% | 0 | 0 | 1 | ↓3 |
| 4 | token-pick | 4 | 6.3% | 0 | 0 | 0 | — |
| 8 | autoresearch | 3 | 4.7% | 2 | 0 | 1 | — |
| 8 | cost-report | 3 | 4.7% | 0 | 3 | 2 | — |
| 8 | defi-overview | 3 | 4.7% | 2 | 0 | 1 | — |
| 8 | digest | 3 | 4.7% | 2 | 0 | 1 | — |
| 8 | github-monitor | 3 | 4.7% | 2 | 0 | 0 | — |
| 8 | memory-flush | 3 | 4.7% | 0 | 0 | 2 | NEW |
| 8 | morning-brief | 3 | 4.7% | 1 | 1 | 1 | NEW |
| 8 | on-chain-monitor | 3 | 4.7% | 2 | 1 | 2 | — |

*(Top 15. Additional ties at rank 8 excluded: narrative-convergence 3, self-improve 3.)*

## What the fleet is telling us

### Promote
None this week — no skill crossed the 25% configured-fork threshold. Token-movers leads at 10.9%. To promote, a skill needs ≥25% adoption with upstream default of `enabled: false`.

### Match
None this week — no upstream skill had ≥2 configured forks independently override `model:` to the same value. Notable: mine-bean (damo-nu11) uses `claude-haiku-4-5-20251001`; bankr-space-worker (anondevv69) uses `gemini-2.5-flash` — both fork-only, so not applicable to upstream matching.

### Sunset (review for removal or better docs)
1. **star-milestone** — 0 configured-fork adoption; niche milestone announcements, low discoverability
2. **farcaster-digest** — 0 adoption; declining platform signal
3. **channel-recap** — 0 adoption; Telegram-dependent, requires specific channel var setup
4. **remix-tweets** — 0 adoption; marginal utility in an era of native AI writing tools
5. **telegram-digest** — 0 adoption; auth-required setup complexity may be friction point

### Fleet-only skills
Skills built by forks but absent from upstream's `skills/` directory:

| Skill | Forks | Built by |
|-------|-------|----------|
| aeon-update | 5 | enuno, icepy, Svector-anu, njfyanf9-a11y, Domimueller85 |
| investigation-report | 3 | icepy, czijian729-oss, Domimueller85 |
| soul-builder | 3 | enuno, njfyanf9-a11y, Domimueller85 |
| aeon-doctor | 2 | enuno, Domimueller85 |
| bd-radar | 2 | rohitctrl, Domimueller85 |
| executor-mcp | 2 | enuno, Domimueller85 |
| glim-mcp | 2 | enuno, Domimueller85 |
| higgsfield | 2 | amritmirch, Domimueller85 |
| idea-forge | 2 | enuno, Domimueller85 |
| install-skill | 2 | enuno, Domimueller85 |
| onchain-monitor | 2 | czijian729-oss, Domimueller85 |
| pack-submit | 2 | enuno, Domimueller85 |
| picks-tracker | 2 | czijian729-oss, Domimueller85 |
| price-alert | 2 | czijian729-oss, Domimueller85 |
| shiplog | 2 | njfyanf9-a11y, Domimueller85 |
| skill-article | 2 | enuno, Domimueller85 |
| strategy-builder | 2 | enuno, Domimueller85 |
| base-mcp | 2 | 00288, Domimueller85 |

*Additionally, Domimueller85/aeon runs 30+ unique single-fork skills (arc-studio, compute-resell, deploy-uni-hook, finance-district-mcp, hunter-22, miroshark-matchday, remotion, robinhood-mcp, rightstack, sc-audit, seo-audit, taskmarket-delegate, weekly-aeoncard, and more). icepy/aeon-token contributes arxiv-radar, github-radar, narrative-brief, defillama-radar.*

## Week-over-week

**Rising** (≥3 ranks): narrative-tracker jumped from rank 6 → rank 3.

**Falling** (≥3 ranks): auto-workflow fell from rank 2 → rank 6 (adoption collapsed from 45/62 to 4/64 as high-activation forks rotated out of the 30-day window). skill-health fell from rank 7 → rank 6 (steady at 4 forks, ranking shift due to increased competition).

**Dropouts**: skill-enabler (8 forks last week → 0 this week), fleet-skill-adoption (7 forks → 0). Both reflect the same pattern: the cohort of power-users who had these enabled has drifted outside the active-30-day window.

**New entries**: memory-flush and morning-brief entered the top 15 at rank 8 (3 forks each).

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 64 | 98.5% |
| Template (untouched aeon.yml) | 1 | 1.5% |
| Unreadable (no tree / no yml / rate-limited) | 0 | 0% |
| **Total active forks** | **65** | **100%** |

## Source status

- Trees fetched: 65 / 65 (tree check skipped; direct contents call used)
- aeon.yml readable: 65 / 65
- Rate-limited: 0
- Fork-only skill files inspected: 50+ unique fork-only skills detected via aeon.yml parsing

---
*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork counts as "configured" if its `aeon.yml` differs from upstream defaults on `enabled`, `model`, `var`, or `schedule` for any skill. Untouched templates are excluded from leaderboard math.*
