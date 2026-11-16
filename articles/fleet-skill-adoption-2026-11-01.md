# Fleet Skill Adoption — 2026-11-01

**Parent:** aeonfun/aeon · **Upstream skills:** 87
**Active forks measured:** 7/80 (POWER + ACTIVE; 0 unreadable aeon.yml) · **Source:** live
**Note:** 80-fork cap applied (sorted by stargazers desc); fleet contracted from 11→7 active forks week-over-week.

---

## Most adopted (top 15)

| # | Skill | Category | Enabled by | Adoption | WoW |
|---|-------|----------|------------|----------|-----|
| 1 | heartbeat | core | 7/7 | 100% | — |
| 2 | auto-workflow | core | 1/7 | 14% | -4 |
| 3 | autoresearch | evolution | 1/7 | 14% | +5 |
| 4 | create-skill | evolution | 1/7 | 14% | +5 |
| 5 | defi-overview | crypto | 1/7 | 14% | +5 |
| 6 | deploy-prototype | dev | 1/7 | 14% | +5 |
| 7 | distribute-tokens | crypto | 1/7 | 14% | +5 |
| 8 | fetch-tweets | basics | 1/7 | 14% | +5 |
| 9 | last30 | basics | 1/7 | 14% | +5 |
| 10 | monitor-polymarket | crypto | 1/7 | 14% | +5 |
| 11 | narrative-tracker | crypto | 1/7 | 14% | +5 |
| 12 | reply-maker | productivity | 1/7 | 14% | +5 |
| 13 | skill-health | evolution | 1/7 | 14% | -4 |
| 14 | skill-repair | evolution | 1/7 | 14% | +5 |
| 15 | spawn-instance | core | 1/7 | 14% | +5 |

*Note: WoW deltas reflect the denominator shift (11→7 readable forks). Apparent gains (+5pts) are largely driven by fleet contraction, not new adoptions. The one diversified operator (tomscaria/aeon) runs all 18 non-heartbeat skills listed above plus token-movers, token-pick, vuln-scanner, and write-tweet.*

## Least adopted (bottom 15, established skills only)

| Skill | Category | Enabled by | Adoption | Shipped |
|-------|----------|------------|----------|---------|
| action-converter | basics | 0/7 | 0% | 2026-08-04 |
| anatomy | dev | 0/7 | 0% | 2026-10-12 |
| arc-studio | dev | 0/7 | 0% | 2026-09-21 |
| article | basics | 0/7 | 0% | 2026-08-04 |
| auto-merge | core | 0/7 | 0% | 2026-10-01 |
| base-mcp | crypto | 0/7 | 0% | 2026-10-02 |
| bd-radar | basics | 0/7 | 0% | 2026-10-01 |
| changelog | dev | 0/7 | 0% | 2026-09-14 |
| competitor-monitor | productivity | 0/7 | 0% | 2026-10-01 |
| compute-resell | crypto | 0/7 | 0% | 2026-10-02 |
| cortx-reliability | crypto | 0/7 | 0% | 2026-08-28 |
| create-prove | dev | 0/7 | 0% | 2026-09-18 |
| deploy-uni-hook | crypto | 0/7 | 0% | 2026-09-09 |
| digest | basics | 0/7 | 0% | 2026-10-01 |
| executor-mcp | basics | 0/7 | 0% | 2026-10-01 |

*Caution: dispatch-only skills (workflow_dispatch schedule, by design never auto-run) could not be filtered this run — upstream skills.json schedule field unavailable. Some bottom-15 entries may be intentionally operator-triggered tools.*

## Shipped into silence (zero fleet adoption, established)

65 established skills at 0% fleet adoption. The single active diversified operator (tomscaria/aeon) accounts for all non-heartbeat adoption in the fleet. Selected zero-adoption established skills of note:

- auto-merge, operator-scorecard, soul-builder, strategy-builder, fleet-control, fork-fleet (core/infra)
- article, digest, skill-article, video-script, write-tweet... wait — write-tweet IS enabled (1/7)
- posthog-errors, seo-audit, sc-audit, vuln-tracker (dev tools)
- narrator: narrative-convergence, mention-radar, inbox-triage
- crypto suite: picks-tracker, miroshark-matchday, pm-manipulation, investigation-report, submit-hook

Zero-adoption core list (all 65): action-converter, anatomy, arc-studio, article, auto-merge, base-mcp, bd-radar, changelog, competitor-monitor, compute-resell, cortx-reliability, create-prove, deploy-uni-hook, digest, executor-mcp, feature, feedback-builder, finance-district-mcp, fleet-control, fork-fleet, github-filing-registry, github-monitor, github-trending, glim-mcp, higgsfield, hunter-22, idea-forge, idea-pipeline, inbox-triage, install-skill, investigation-report, memory-flush, mention-radar, miroshark-matchday, narrative-convergence, operator-scorecard, pack-submit, picks-tracker, pm-manipulation, posthog-errors, pr-review, pr-triage, price-alert, remotion, rightstack, robinhood-mcp, sc-audit, schedule-ads, search-skill, self-improve, send-email, seo-audit, shiplog, skill-article, soul-builder, spend-watch, strategy-builder, submit-hook, taskmarket-delegate, tx-explain, unlock-monitor, video-script, vuln-tracker, weekly-aeoncard, you-web-search

## Freshly shipped (≤14d — not yet ranked against the fleet)

| Skill | Shipped | Adoption so far |
|-------|---------|-----------------|
| vuln-scanner | 2026-10-28 | 14% (1/7) — fast start |
| onchain-monitor | 2026-10-25 | 0% (0/7) — was 9% last week (fork went stale) |
| aeon-update | 2026-10-21 | 0% (0/7) — was 18% last week (fork went stale) |
| aeon-doctor | 2026-10-20 | 0% (0/7) — was 9% last week (fork went stale) |

Also new to the upstream universe this week:
- github-filing-registry (dev, no updated date) — 0% (0/7)

## This week's movement

- **Adoption gainers (≥5pts):** autoresearch +5pts, create-skill +5pts, defi-overview +5pts, deploy-prototype +5pts, distribute-tokens +5pts, fetch-tweets +5pts, last30 +5pts, monitor-polymarket +5pts, narrative-tracker +5pts, reply-maker +5pts, skill-repair +5pts, spawn-instance +5pts, token-movers +5pts, token-pick +5pts, write-tweet +5pts *(denominator-driven: same fork, smaller cohort)*
- **Adoption decliners (≥5pts):** auto-merge −18pts, operator-scorecard −18pts, aeon-doctor −9pts (now freshly shipped), aeon-update −9pts (now freshly shipped), arc-studio −9pts, article −9pts, base-mcp −9pts, bd-radar −9pts, changelog −9pts, competitor-monitor −9pts, compute-resell −9pts, cortx-reliability −9pts, and 50+ more *(all driven by fleet contraction: 4 forks went stale)*
- **Entered top-10:** create-skill, defi-overview, deploy-prototype, distribute-tokens, fetch-tweets, last30, monitor-polymarket
- **Left top-10:** aeon-update, auto-merge, operator-scorecard, skill-health, aeon-doctor, arc-studio, article

## Fleet contraction note

The 11→7 active fork decline is the dominant signal this week. Four forks dropped below the 7-day activity threshold. This is a natural weekly fluctuation pattern — stale forks often re-activate on dispatch. The leaderboard percentages (14% vs prior 9–18%) reflect the smaller active denominator, not genuine adoption changes. Only one fork (tomscaria/aeon) runs a meaningful skill suite beyond heartbeat.

## Source status

`cohort_source=live · forks_audited=80 · readable=7/7 · unreadable=0 · truncated=true (cap=80) · cohort_state_age_days=N/A`
