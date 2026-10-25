# Fork Contributor Leaderboard — 2026-10-25

*78 contributors moved aaronjmars/aeon this week across 65 active forks, ~220 upstream PRs, and 0 community review comments.*

## Movement This Week

The story this week is infrastructure density. Svector-anu has now landed **78 merged PRs** — fixes across the scheduler, MCP server, dashboard, CI gates, and the dev-loop harness. That's not sprint velocity; that's sustained ownership. The past week alone added Robinhood Chain Alchemy support, harness group-kill fixes, and schedule timezone handling. When a single contributor drives this much correctness, the whole fleet benefits.

ether-btc is one of the most interesting names not yet in the merged column. With **67 commits on their fork** and an open PR adding `github-filing-registry` — a persistent GitHub filing ledger — they're building at upstream quality. Their fork also carries `gh-filing-standards` and `github-upstream-tracker`, skills upstream doesn't have. The open PR (#1267) is the gap that could close into their first merge next week.

alexverify has been quietly shipping security audit tooling: six PRs, six merged, zero waste. The `eyebrow` skill-integrity gate, optional runtime hardening for the MCP server, and ecosystem docs round out a focused set of contributions that every operator running Aeon benefits from without knowing it.

NurstarK and sentinelhood are both active on two fronts — PRs upstream and forks that run well ahead. NurstarK's fork carries nine skills upstream hasn't seen yet (`approval-audit`, `fund-flow`, `honeypot-check`, `linked-wallets`, `liquidpad-launch` among others) alongside a freshly merged `lazybrief` and a matchday video skill. sentinelhood's merged work this week added reorg-safe evidence replay and offline receipt verification to `onchain-monitor` — unglamorous reliability work.

rohitctrl has 12 commits on their fork with no upstream PRs yet — and the fork has taken a distinct direction: `ab-testing`, `ads`, `analytics`, `ai-seo`, `aso`, `attribution`, `churn-prevention`, `cold-email`. That's a marketing operations layer built on top of Aeon. High outreach priority.

## Top Contributors

| Rank | Contributor | Score | Merged PRs | Open PRs | Reviews | Fork Commits | New Skills | First PR? | Change |
|------|-------------|-------|------------|----------|---------|--------------|------------|-----------|--------|
| 1 | @Svector-anu | 814 | 78 | 3 | 0 | 0 | 5 | — | — |
| 2 | @antfleet-ops | 149 | 14 | 3 | 0 | 0 | 0 | — | — |
| 3 | @houndflow | 98 | 8 | 6 | 0 | 0 | 0 | — | — |
| 4 | @alexverify | 85 | 6 | 0 | 0 | 0 | 5 | — | — |
| 5 | @NurstarK | 79 | 5 | 1 | 0 | 1 | 5 | — | — |
| 6 | @sentinelhood | 78 | 5 | 1 | 0 | 0 | 5 | — | — |
| 7 | @ether-btc | 58 | 0 | 1 | 0 | 30 | 5 | — | — |
| 8 | @icepy | 58 | 0 | 1 | 0 | 30 | 5 | — | — |
| 9 | @UIZorrot | 41 | 3 | 2 | 0 | 0 | 1 | — | — |
| 10 | @rohitctrl | 37 | 0 | 0 | 0 | 12 | 5 | — | — |
| 11 | @codexvritra | 32 | 2 | 4 | 0 | 0 | 0 | — | — |
| 12 | @bgiesing | 30 | 0 | 0 | 0 | 5 | 5 | — | — |
| 13 | @Atrium-Hermes | 30 | 3 | 0 | 0 | 0 | 0 | — | — |
| 14 | @BBridgeers | 30 | 3 | 0 | 0 | 0 | 0 | — | — |
| 15 | @keyurbodar | 30 | 3 | 0 | 0 | 0 | 0 | — | — |
| 16 | @LiamVisionary | 30 | 3 | 0 | 0 | 0 | 0 | — | — |
| 17 | @ryjin111 | 30 | 3 | 0 | 0 | 0 | 0 | — | — |
| 18 | @usephylax | 30 | 3 | 0 | 0 | 0 | 0 | — | — |
| 19 | @liquidpadbot | 23 | 2 | 1 | 0 | 0 | 0 | — | — |
| 20 | @sparkleware | 23 | 2 | 1 | 0 | 0 | 0 | — | — |

*(top 20; ✨ in First PR? column means at least one of their upstream PRs was their first-ever contribution to aaronjmars/aeon — none this period.)*

## Outreach Candidates

Active forks whose owner has never opened an upstream PR — the highest-conversion outreach pool, sorted by fork commit count:

- @rohitctrl — 12 fork commits, 0 stars, 5+ new skills (marketing ops variant: ab-testing, ads, analytics, ai-seo, aso)
- @bgiesing — 5 fork commits, 0 stars, 5+ new skills (pepper-bgiesing fork, active today)
- @nhutminh159 — 4 fork commits, 0 stars, upstream-close skill set
- @Domimueller85 — 1 fork commit, 0 stars, 1 open PR with no activity yet
- @00288 — 0 owner commits, ahead_by 55, 0 stars
- @gelo11 — 0 owner commits, ahead_by 30, 0 stars
- @mervwtf — 0 owner commits, ahead_by 10, 0 stars
- @FggDarkOnee420 — 0 owner commits, ahead_by 11, 1 star
- @0xAnvesaka — 0 owner commits, ahead_by 15, 0 stars
- @rauhaton — 0 owner commits, ahead_by 38, 0 stars

## Upstream Contribution Signal

- **Contributors with merged upstream PRs:** 35
- **First-time contributors this period:** 0 — no FIRST_TIME_CONTRIBUTOR associations detected
- **Top reviewer:** — (no community PR review comments in the last 30 days; only bot activity detected)
- **Most-merged contributor:** @Svector-anu with 78 merged PRs
- **Active forks whose owner has never opened an upstream PR:** 10+ identified

## Fork Fleet Summary

- **Active forks scanned (pushed last 30d):** 65
- **Total upstream PRs tracked (all time, filtered to community):** ~220
- **Total review comments tracked (last 30d):** 0 (after bot/core filter)
- **Unique contributors:** ~78
- **Contributors filtered as bots/core:** dependabot[bot], github-actions, aaronjmars, aeonframework

---
*Source: GitHub API — forks, pulls, pull review comments, and compare endpoints of aaronjmars/aeon. Scoring: merged PR +10, first-PR bonus +5, open PR +3, review comment +2 (cap 20), fork commit +1 (cap 30), new skill +5 (cap 5), fork star +1 (cap 20).*
