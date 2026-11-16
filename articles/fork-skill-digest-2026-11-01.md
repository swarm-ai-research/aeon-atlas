# Fork Skill Digest — 2026-11-01

**Verdict:** 63 forks disable skill-health (upstream defaults on) — fleet is voting it as noise

*Scanned 68 active forks of aaronjmars/aeon (pushed in last 30 days). 67 are configured (aeon.yml diverges from upstream defaults). Divergence scored against the configured 67.*

## Default-flip candidates

### Enable upward (upstream off → fleet enables)

No skills crossed the 50% enable-upward threshold this week.

### Disable downward (upstream on → fleet disables)

| Skill | Forks disabled | % of configured | Δ vs last week |
|-------|----------------|-----------------|----------------|
| skill-health | 63 | 94% | First divergence snapshot |
| operator-scorecard | 65 | 97% | First divergence snapshot |

**skill-health** is the upstream-default ops health auditor. 94% of configured forks explicitly set `enabled: false`, treating it as noise that slows down minimal deployments. Recommend flipping upstream default to `enabled: false`.

**operator-scorecard** is disabled by 97% of configured forks — near-universal rejection. The Monday scorecard appears to be a fleet-operator tool only useful once the fleet reaches scale. Recommend flipping upstream default to `enabled: false`.

## Fleet consensus on alternative settings

### Model overrides

No per-skill model consensus this week. (Note: the fleet uses diverse top-level defaults — claude-sonnet-5-5, claude-opus-5-5, claude-sonnet-5, deepseek-flash, glm-5.2, moonshotai/kimi-k2.7-code, and others — but these are global defaults, not per-skill overrides tracked here.)

### Var hotspots

None this week. Notable individual var customizations: NurstarK sets `autoresearch` var to "Agents" with a daily cron override, and `agent-buzz` var to "AI"; madebyshun sets `github-monitor` var to their own repo ("madebyshun/blue-agent"). Neither reached the 30% fleet threshold.

### Schedule overrides

Most common non-upstream heartbeat schedule: `"0 8 * * *"` — adopted by ~44/67 configured forks (66%). These forks run heartbeat once daily at 08:00 UTC instead of upstream's three-times-daily `"0 8,14,20 * * *"`. Signal: the fleet treats heartbeat as a morning check-in, not a continuous health pulse.

Two outliers: enzoonchain uses `"0 7,13,19 * * *"` (1 hour earlier shift) and hansj73 uses `"0 23 * * *"` (late-night single run).

## Watchlist (emerging — 25–49% adoption)

None this week.

## Heaviest customizers (top 5)

| Fork | Total overrides | Dominant category | Notes |
|------|-----------------|-------------------|-------|
| enuno/noesis-aeon | ~20 | meta/dev | 10 upstream-disabled skills enabled (pr-review, auto-merge, github-trending, search-skill, autoresearch, create-skill, self-improve, action-converter, skill-repair, narrative-convergence); 8 fork-only skills (glim-mcp, executor-mcp, install-skill, pack-submit, strategy-builder, aeon-doctor, aeon-update, soul-builder); soul-builder var set to operator identity |
| TakamiyaZee/aeon | 18 | meta | 18 upstream-enabled skills explicitly disabled in aeon.yml; model claude-opus-4-7; no extra skills enabled — pure fleet-analytics suppression |
| lawbworld-tech/aeon | 15 | meta | 15 upstream-enabled skills disabled; model claude-opus-4-7; same suppression pattern as TakamiyaZee |
| icepy/aeon-token | ~11 | content/defi | 4 upstream-disabled skills enabled (memory-flush, defi-overview, tx-explain, skill-health→false); 7 fork-only skills enabled (investigation-report, sc-audit, aeon-update, arxiv-radar, github-radar, narrative-brief, defillama-radar); model claude-opus-5-5 |
| madebyshun/blueagent-aeon | 8 | content/crypto | 6 upstream-disabled skills enabled (github-monitor with var, token-movers, token-pick, narrative-tracker, distribute-tokens, deep-research) + skill-health disabled; model claude-sonnet-4-6 |

## Fork-only skills

These skills appear in fork aeon.yml entries but have no corresponding `skills/<name>/SKILL.md` in upstream. All are new (first divergence snapshot).

| Fork | Skill | Status |
|------|-------|--------|
| ~44 v5-template forks | deploy-uni-hook | disabled (ecosystem addition: Uniswap v4 hook generator) |
| ~44 v5-template forks | sc-audit | disabled in most; enabled in icepy/aeon-token |
| duan521127 + others | compute-resell | disabled (compute marketplace reseller) |
| duan521127 + others | miroshark-matchday | disabled (sports-sim skill) |
| duan521127, icepy | investigation-report | enabled in icepy; composite onchain investigation |
| icepy, enuno | aeon-update | enabled in both; upstream sync PR skill |
| enuno/noesis-aeon | glim-mcp | enabled; live-data research via glim.sh MCP |
| enuno/noesis-aeon | executor-mcp | enabled; task execution via Executor Cloud |
| enuno/noesis-aeon | install-skill | enabled; community skill pack installer |
| enuno/noesis-aeon | pack-submit | enabled; community skill publisher |
| enuno/noesis-aeon | strategy-builder | enabled; STRATEGY.md generator |
| enuno/noesis-aeon | aeon-doctor | enabled; config-correctness linter |
| enuno/noesis-aeon | soul-builder | enabled; identity/voice builder from links |
| anondevv69/bankr-space-aeon | bankr-space-worker | enabled; custom Bankr Space worker (gemini-2.5-flash, every 15 min) |
| 00288/aeon | base-mcp | enabled; Base Account access via mcp.base.org |
| icepy/aeon-token | arxiv-radar | enabled; arXiv paper radar |
| icepy/aeon-token | github-radar | enabled; GitHub trending radar |
| icepy/aeon-token | narrative-brief | enabled; daily narrative summary |
| icepy/aeon-token | defillama-radar | enabled; DeFiLlama protocol radar |

deploy-uni-hook and sc-audit are the most widely distributed fork-only additions — the v5 framework template ships them disabled by default, suggesting they may be candidates for upstreaming.

## Week-over-week

First divergence snapshot — no comparison available.

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 67 | 98.5% |
| Template (untouched aeon.yml) | 1 | 1.5% |
| Unreadable | 0 | 0% |
| **Total active** | **68** | **100%** |

## Source status

- aeon.yml readable: 68 / 68
- YAML parse failures: 0
- Rate-limited: 0
- Trees fetched: 0 (aeon.yml fetched directly via contents API)
- Fork-only skills inspected: 19+ distinct skill names across the fleet

## Appendix — full divergence table

Skills with non-zero divergence signal (sorted by total disable count; capped at 30 rows):

| Skill | Enable↑ forks | Disable↓ forks | Model Δ forks | Schedule Δ forks |
|-------|--------------|----------------|---------------|-----------------|
| operator-scorecard | 0 | 65 | 0 | 0 |
| skill-health | 0 | 63 | 0 | 1 (enzoonchain: schedule diff) |
| heartbeat | 0 | 0 | 0 | ~45 (schedule override) |
| ai-framework-watch | 0 | ~22 | 0 | 0 |
| ecosystem-pulse | 0 | ~22 | 0 | 0 |
| fleet-state | 0 | ~22 | 0 | 0 |
| fork-cohort | 0 | ~22 | 0 | 0 |
| fork-release-tracker | 0 | ~22 | 0 | 0 |
| contributor-spotlight | 0 | ~22 | 0 | 0 |
| fork-first-run-alert | 0 | ~22 | 0 | 0 |
| skill-evals | 0 | ~22 | 0 | 0 |
| skill-update-check | 0 | ~22 | 0 | 0 |
| fork-contributor-leaderboard | 0 | ~22 | 0 | 0 |
| fork-skill-gap | 0 | ~22 | 0 | 0 |
| fleet-skill-adoption | 0 | ~22 | 0 | 0 |
| fork-health-score | 0 | ~22 | 0 | 0 |
| workflow-security-audit | 0 | ~22 | 0 | 0 |
| skill-freshness | 0 | ~22 | 0 | 0 |
| fork-skill-digest | 0 | ~22 | 0 | 0 |
| autoresearch | 1 (NurstarK) | 0 | 0 | 1 (NurstarK) |
| agent-buzz | 1 (NurstarK) | 0 | 0 | 0 |
| github-monitor | 2 (moosebizlab, madebyshun) | 0 | 0 | 0 |
| narrative-tracker | 2 (madebyshun, icepy?) | 0 | 0 | 0 |
| defi-overview | 2 (00288, icepy) | 0 | 0 | 0 |
| token-movers | 1 (madebyshun) | 0 | 0 | 0 |
| token-pick | 1 (madebyshun) | 0 | 0 | 0 |
| memory-flush | 1 (icepy) | 0 | 0 | 0 |
| pr-review | 1 (enuno) | 0 | 0 | 0 |
| search-skill | 1 (enuno) | 0 | 0 | 0 |
| digest | 1 (moosebizlab) | 0 | 0 | 0 |

+ Additional low-signal skills (self-improve, auto-merge, action-converter, skill-repair, narrative-convergence, create-skill, github-trending, tx-explain, auto-merge, pr-review).

---
*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork is "configured" if its aeon.yml diverges from upstream defaults on enabled, model, var, or schedule for any skill. Untouched templates are excluded from divergence math. Companion to skill-leaderboard (popularity) and fork-fleet (per-fork work).*
