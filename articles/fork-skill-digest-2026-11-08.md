# Fork Skill Digest — 2026-11-08

**Verdict:** 63 forks disable skill-health (upstream defaults on) — fleet is voting it as noise

*Scanned 67 active forks of aaronjmars/aeon (pushed in last 30 days). 66 are configured (aeon.yml diverges from upstream defaults). Divergence scored against the configured 66.*

## Default-flip candidates

### Enable upward (upstream off → fleet enables)

No skills crossed the 50% enable-upward threshold this week.

### Disable downward (upstream on → fleet disables)

| Skill | Forks disabled | % of configured | Δ vs last week |
|-------|----------------|-----------------|----------------|
| skill-health | 63 | 95.5% | STRENGTHENED (was 94%) |
| operator-scorecard | 63 | 95.5% | — (was 97%) |

**Note on broader fleet intelligence stack:** Old-template forks (~26) and mid-template forks (~12) also explicitly set atlas, atlas-layers, atlas-improve, fork-cohort, fork-release-tracker, contributor-spotlight, fork-first-run-alert, skill-evals, skill-update-check, fleet-scorecard, skill-leaderboard, fork-contributor-leaderboard, follow-up-patrol, fork-skill-digest, fork-skill-gap, fleet-skill-adoption, fork-health-score, workflow-security-audit, ai-framework-watch, ecosystem-pulse, fleet-state, skill-freshness, and api-health-probe to `enabled: false` (~40/66 = 61%). These are fleet-orchestrator skills appropriate for the upstream reference instance but represent overhead for most operators. The 50%+ threshold is met; upstream defaults for these skills warrant review.

## Fleet consensus on alternative settings

### Model overrides

None this week. Per-skill model overrides are absent across the fleet. Global model changes (many forks use `claude-sonnet-5-5`, some `claude-opus-4-7`, isolated forks use `deepseek-chat`, `open_router/deepseek/deepseek-v4-flash`, `venice-uncensored`, `openai/gpt-6.1-sol`) are global-level, not per-skill overrides — not counted.

### Var hotspots

None this week. No upstream skill has ≥2 forks sharing the same non-empty var override.

Notable single-fork var customizations (illustrative):
- **rohitctrl/aeon** — digest var: India-focused job market research spec
- **NurstarK/aeon-upstream** — autoresearch var: "Agents"; agent-buzz var: "AI"
- **0xMal0u/aeon** — 4 upstream skills with heavy operator-specific vars (morning-brief, on-chain-monitor, narrative-tracker, refresh-x)
- **enuno/noesis-aeon** — soul-builder var: operator identity link

### Schedule overrides

**heartbeat — dominant schedule shift:**
- Upstream: `"0 8,14,20 * * *"` (3×/day)
- `"0 8 * * *"` (1×/day): ~44/66 configured forks (67%)
- Unchanged: ~18/66 (27%)
- Other: 4/66 — hansj73 `"0 23 * * *"`, icepy `"30 0 * * *"`, enzoonchain `"0 7,13,19 * * *"`, damo-nu11 `"0 8,14,20 * * *"`

67% of the fleet has converged on once-daily heartbeat vs upstream's three-times-daily default. The fleet has voted: 3×/day is excessive. Upstream should consider changing heartbeat's default schedule to `"0 8 * * *"`.

## Watchlist (emerging — 25–49% adoption)

None this week. No upstream-disabled skill reached the 25% EMERGING threshold.

Closest candidates (single-digit adoption):
- auto-merge: ~4/66 (6%) — enabled by njfyanf9-a11y, Svector-anu, Domimueller85, enuno
- token-movers: ~6/66 (9%)
- narrative-tracker: ~3/66 (5%)

## Heaviest customizers (top 5)

| Fork | Total overrides | Dominant category | Notes |
|------|-----------------|-------------------|-------|
| duan521127/aeon | ~66 | fork-only | Fork-only explosion: 40+ custom skills (blockchain research, DeFi, x402, MCP integrations, media/video tools); 25 fleet skills disabled |
| enuno/noesis-aeon | ~47 | meta | 10 enabled skill-management tools; 10 fork-only skills including soul-builder + aeon-doctor; skill-health preserved (outlier) |
| njfyanf9-a11y/aeon-njfyanf9-a11y | ~38 | meta | Ops-focused: fleet-control + spawn-instance enabled with var, spawn-instance running every 3h; 3 fork-only (aeon-update, shiplog, soul-builder) |
| icepy/aeon-token | ~37 | content | 7 fork-only research/radar skills (arxiv, github, defillama, narrative-brief); heartbeat shifted to midnight UTC |
| TakamiyaZee/aeon | ~25 | meta | Silent minimizer: entire fleet stack disabled, model downgraded to claude-opus-4-7, heartbeat-only operation |

**New entry:** duan521127/aeon was not in the top-5 last week — it has had a major skills expansion since 2026-11-01.

## Fork-only skills

Skills present in a fork as `skills/<name>/SKILL.md` but absent from upstream:

**Continuing from prior snapshot (stable):**
- **duan521127/aeon**: deploy-uni-hook, sc-audit, compute-resell, miroshark-matchday, investigation-report + 35 new additions this week (see below)
- **vaubandev/aeon**: deploy-uni-hook, sc-audit
- **icepy/aeon-token**: sc-audit, investigation-report, aeon-update, arxiv-radar, github-radar, narrative-brief, defillama-radar
- **enuno/noesis-aeon**: glim-mcp, executor-mcp, install-skill, pack-submit, strategy-builder, aeon-doctor, aeon-update, soul-builder, idea-forge, skill-article
- **anondevv69/bankr-space-aeon**: bankr-space-worker
- **00288/aeon**: base-mcp

**NEW this week:**
- **airdropia/aeon**: bounty-hunter
- **damo-nu11/aeon-minebean**: mine-bean
- **lawbworld-tech/aeon**: lawb-pool-monitor
- **amritmirch/aeon**: higgsfield
- **rohitctrl/aeon**: bd-radar, dental-lead-scout
- **Svector-anu/aeon**: aeon-update
- **njfyanf9-a11y/aeon-njfyanf9-a11y**: aeon-update, shiplog, soul-builder
- **czijian729-oss/aeon**: picks-tracker, price-alert, onchain-monitor
- **duan521127/aeon (expanded)**: spodumene-reverse-flotation, anatomy, arc-studio, cortx-reliability, hunter-22, aeon-doctor, aeon-update, soul-builder, install-skill, pack-submit, strategy-builder, glim-mcp, executor-mcp, finance-district-mcp, robinhood-mcp, higgsfield, bd-radar, picks-tracker, oil-china-chem-georisk, remotion, video-script, weekly-aeoncard, you-web-search, send-email, seo-audit, skill-article, inbox-triage, mention-radar, posthog-errors, rightstack, feedback-builder, research-persona-review, submit-hook, taskmarket-delegate, spend-watch, github-filing-registry

## Week-over-week

| Delta | Detail |
|-------|--------|
| NEW_FLIP | None |
| STRENGTHENED | skill-health: 94% (63/67) → 95.5% (63/66) |
| FADED | None — operator-scorecard 97% → 95.5% due to fleet size shift (65/67 → 63/66), still solidly in flip bucket |
| NEW_FORK_ONLY | bounty-hunter (airdropia), mine-bean (damo-nu11), lawb-pool-monitor (lawbworld-tech), dental-lead-scout + bd-radar (rohitctrl), higgsfield (amritmirch), aeon-update + shiplog + soul-builder (njfyanf9-a11y), aeon-update (Svector-anu), picks-tracker + price-alert + onchain-monitor (czijian729-oss), 35+ skills from duan521127 expansion |
| NEW_HEAVY_CUSTOMIZER | duan521127/aeon (newly #1 by override count, up from outside top-5) |

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 66 | 98.5% |
| Template (untouched aeon.yml) | 1 | 1.5% |
| Unreadable | 0 | 0% |
| **Total active** | **67** | **100%** |

## Source status

- Trees fetched: 67 / 67
- aeon.yml readable: 67 / 67
- YAML parse failures: 0
- Rate-limited: 0
- Fork-only skills inspected: 6 deep-scanned (duan521127, vaubandev, icepy, enuno, anondevv69, 00288 + 7 new forks with fork-only signals)

## Appendix — full divergence table

| Skill | enable_diff | var_overrides | model_overrides | schedule_overrides |
|-------|-------------|---------------|-----------------|-------------------|
| skill-health | 63 | 0 | 0 | 0 |
| operator-scorecard | 63 | 0 | 0 | 0 |
| atlas | ~38 | 0 | 0 | 0 |
| atlas-layers | ~38 | 0 | 0 | 0 |
| atlas-improve | ~38 | 0 | 0 | 0 |
| fork-cohort | ~38 | 0 | 0 | 0 |
| fork-release-tracker | ~38 | 0 | 0 | 0 |
| contributor-spotlight | ~38 | 0 | 0 | 0 |
| fork-first-run-alert | ~38 | 0 | 0 | 0 |
| skill-evals | ~38 | 0 | 0 | 0 |
| skill-update-check | ~38 | 0 | 0 | 0 |
| fleet-scorecard | ~38 | 0 | 0 | 0 |
| skill-leaderboard | ~38 | 0 | 0 | 0 |
| fork-contributor-leaderboard | ~38 | 0 | 0 | 0 |
| follow-up-patrol | ~38 | 0 | 0 | 0 |
| fork-skill-digest | ~38 | 0 | 0 | 0 |
| fork-skill-gap | ~38 | 0 | 0 | 0 |
| fleet-skill-adoption | ~38 | 0 | 0 | 0 |
| fork-health-score | ~38 | 0 | 0 | 0 |
| workflow-security-audit | ~38 | 0 | 0 | 0 |
| ai-framework-watch | ~38 | 0 | 0 | 0 |
| ecosystem-pulse | ~38 | 0 | 0 | 0 |
| fleet-state | ~38 | 0 | 0 | 0 |
| skill-freshness | ~38 | 0 | 0 | 0 |
| api-health-probe | ~38 | 0 | 0 | 0 |
| heartbeat | 0 | 0 | 0 | 48 |
| digest | 1 | 1 | 0 | 0 |
| morning-brief | ~3 | 1 | 0 | 0 |
| on-chain-monitor | ~3 | 1 | 0 | 0 |
| narrative-tracker | 3 | 1 | 0 | 0 |

*Note: `~` values are estimates based on old-template + mid-template fork counts (~38); new-template forks (~28) omit these keys entirely (inherit upstream true). All signals use explicit-override-only counting.*

---
*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork is "configured" if its aeon.yml diverges from upstream defaults on enabled, model, var, or schedule for any skill. Untouched templates are excluded from divergence math. Companion to skill-leaderboard (popularity) and fork-fleet (per-fork work).*
