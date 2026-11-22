# Fork Skill Digest — 2026-11-22

**Verdict:** 58 forks disable operator-scorecard (upstream defaults on) — fleet is voting it as noise

*Scanned 61 active forks of aaronjmars/aeon (pushed in last 30 days). 59 are configured (aeon.yml diverges from upstream defaults). Divergence scored against the configured 59.*

## Default-flip candidates

### Enable upward (upstream off → fleet enables)

No skills crossed the 50% enable-upward threshold this week.

### Disable downward (upstream on → fleet disables)

| Skill | Forks disabled | % of configured | Δ vs last week |
|-------|----------------|-----------------|----------------|
| operator-scorecard | 58 | 98.3% | — |
| skill-health | 55 | 93.2% | — |

Both signals remain stable. 98% of the configured fleet explicitly sets `operator-scorecard: { enabled: false }`. 93% do the same for `skill-health`. These are not drift — they are consensus. Upstream ships them on; the fleet turns them off.

## Fleet consensus on alternative settings

### Model overrides

None this week. Fleet overwhelmingly uses the upstream default model (`claude-opus-4-8`). One exception: `Boodszw/Boodszw_Bread` overrides operator-scorecard to `claude-sonnet-4-6`, but that is a single fork — well below the 40% consensus threshold.

### Var hotspots

None this week.

### Schedule overrides

None this week.

## Watchlist (emerging — 25–49% adoption)

None this week. The most broadly adopted upstream-disabled skill is `narrative-convergence` (enabled in ~4 configured forks, ~7%) and `memory-flush` (~4 forks, ~7%). Both are far below the 25% emergence threshold.

## Heaviest customizers (top 5)

| Fork | Total overrides | Dominant category | Notes |
|------|-----------------|-------------------|-------|
| Domimueller85/aeon | ~76 | fork-only | 34 upstream-disabled skills enabled + 42 fork-only skills; content, crypto, and infra mix; skill-health and operator-scorecard both kept on (matches upstream) |
| enuno/noesis-aeon | ~23 | fork-only | 12 upstream-disabled skills enabled + 10 fork-only (executor-mcp, glim-mcp, install-skill, soul-builder, aeon-doctor, aeon-update, strategy-builder, skill-article, idea-forge, pack-submit); meta-heavy |
| njfyanf9-a11y/aeon-njfyanf9-a11y | ~13 | meta | fork-fleet, spawn-instance, fleet-control, auto-merge, auto-workflow, memory-flush, narrative-convergence enabled; 4 fork-only (aeon-doctor, aeon-update, shiplog, soul-builder) |
| icepy/aeon-token | ~13 | fork-only | token/defi stack (token-movers, defi-overview, tx-explain, unlock-monitor) + 6 fork-only (sc-audit, aeon-update, arxiv-radar, github-radar, narrative-brief, defillama-radar, onchain-monitor, price-alert) |
| Kodawari10/aeon | ~10 | content | article, digest, monitor-polymarket, reply-maker, write-tweet, skill-repair, pm-manipulation, memory-flush enabled; keeps skill-health on; 1 fork-only (mention-radar) |

## Fork-only skills

New entries this week (not in prior snapshot):

**Domimueller85/aeon** (new heavy customizer):
`compute-resell`, `deploy-uni-hook`, `arc-studio`, `base-mcp`, `bd-radar`, `competitor-monitor`, `cortx-reliability`, `create-prove`, `executor-mcp`, `feedback-builder`, `finance-district-mcp`, `glim-mcp`, `higgsfield`, `hunter-22`, `inbox-triage`, `investigation-report`, `mention-radar`, `miroshark-matchday`, `onchain-monitor`, `picks-tracker`, `posthog-errors`, `price-alert`, `remotion`, `rightstack`, `robinhood-mcp`, `sc-audit`, `send-email`, `seo-audit`, `shiplog`, `skill-article`, `soul-builder`, `spend-watch`, `strategy-builder`, `submit-hook`, `taskmarket-delegate`, `video-script`, `weekly-aeoncard`, `you-web-search`, `idea-forge`, `install-skill`, `pack-submit`, `aeon-doctor`, `aeon-update`

**domosta/aeon** (new active fork):
`flovia`, `revenue-alert`, `onchain-monitor` (without hyphen), `investigation-report`

**hypurr-inc/aeon** (new active fork):
`hyperliquid-market-monitor`

Persistent fork-only entries from prior snapshot remain active in: `duan521127/aeon`, `enuno/noesis-aeon`, `njfyanf9-a11y/aeon-njfyanf9-a11y`, `icepy/aeon-token`, `vaubandev/aeon`, `airdropia/aeon`, `anondevv69/bankr-space-aeon`, `00288/aeon`, `lawbworld-tech/aeon`, `damo-nu11/aeon-minebean`, `Svector-anu/aeon`.

(These skills exist as `skills/<name>/SKILL.md` in a fork but not in upstream. Surfaces fork experiments worth reviewing for upstreaming.)

## Week-over-week

*Prior snapshot: 2026-11-08 (14 days ago)*

- **DEFAULT_FLIP_DISABLE:** stable — both `skill-health` and `operator-scorecard` remain solidly above 90% across the shrinking active window (67→61 active forks).
- **NEW_HEAVY_CUSTOMIZER:** `Domimueller85/aeon` enters the top 5 (not in prior fingerprints). 76 overrides, 42+ fork-only skills — the most heavily customized fork in the current active window by a wide margin.
- **NEW_FORK_ONLY:** Domimueller85 (42+ skills), domosta (`flovia`, `revenue-alert`, `hyperliquid-market-monitor` from hypurr-inc).
- **FADED:** `TakamiyaZee/aeon` dropped out of top 5 (pushed >30 days ago; exits the active window).

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 59 | 96.7% |
| Template (untouched aeon.yml) | 1 | 1.6% |
| Unreadable | 1 | 1.6% |
| **Total active** | **61** | **100%** |

*Template: `swarm-ai-research/aeon-atlas`. Unreadable: `unifirer/aeon` (no tree).*

## Source status

- Trees fetched: 61 / 61
- aeon.yml readable: 60 / 61
- YAML parse failures: 0
- Rate-limited: 0
- Fork-only skills inspected: 47+ (Domimueller85 tree enumerated; partial coverage on other heavy customizers)

## Appendix — full divergence table

(Skills with at least one non-zero divergence signal, sorted by total override signal desc. Only covers upstream skills that at least one configured fork explicitly overrides.)

| Skill | Enable diff | Var overrides | Model overrides | Schedule overrides |
|-------|-------------|---------------|-----------------|-------------------|
| operator-scorecard | 58 (disabled) | 0 | 0 | 0 |
| skill-health | 55 (disabled) | 0 | 0 | 0 |
| narrative-convergence | 4 (enabled) | 0 | 0 | 0 |
| memory-flush | 4 (enabled) | 0 | 0 | 0 |
| auto-merge | 3 (enabled) | 0 | 0 | 0 |
| auto-workflow | 3 (enabled) | 0 | 0 | 0 |
| narrative-tracker | 3 (enabled) | 0 | 0 | 0 |
| token-movers | 3 (enabled) | 0 | 0 | 0 |
| article | 3 (enabled) | 0 | 0 | 0 |
| digest | 3 (enabled) | 0 | 0 | 0 |
| heartbeat | 1 (disabled) | 0 | 0 | 0 |
| skill-repair | 3 (enabled) | 0 | 0 | 0 |
| defi-overview | 2 (enabled) | 0 | 0 | 0 |
| tx-explain | 2 (enabled) | 0 | 0 | 0 |
| monitor-polymarket | 2 (enabled) | 0 | 0 | 0 |
| write-tweet | 2 (enabled) | 0 | 0 | 0 |
| reply-maker | 2 (enabled) | 0 | 0 | 0 |
| pm-manipulation | 2 (enabled) | 0 | 0 | 0 |
| github-monitor | 2 (enabled) | 0 | 0 | 0 |
| search-skill | 2 (enabled) | 0 | 0 | 0 |
| autoresearch | 2 (enabled) | 0 | 0 | 0 |
| deep-research | 1 (enabled) | 0 | 0 | 0 |
| distribute-tokens | 1 (enabled) | 0 | 0 | 0 |
| token-pick | 2 (enabled) | 0 | 0 | 0 |
| pr-review | 2 (enabled) | 0 | 0 | 0 |
| fork-fleet | 1 (enabled) | 0 | 0 | 0 |
| fleet-control | 1 (enabled) | 0 | 0 | 0 |
| spawn-instance | 1 (enabled) | 0 | 0 | 0 |
| github-trending | 1 (enabled) | 0 | 0 | 0 |
| last30 | 1 (enabled) | 0 | 0 | 0 |

---
*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork is "configured" if its aeon.yml diverges from upstream defaults on enabled, model, var, or schedule for any skill. Untouched templates are excluded from divergence math. Companion to skill-leaderboard (popularity) and fork-fleet (per-fork work).*
