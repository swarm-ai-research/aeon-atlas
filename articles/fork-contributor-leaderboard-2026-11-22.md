# Fork Contributor Leaderboard — 2026-11-22

*61 contributors moved aaronjmars/aeon this week across 61 active forks, 36 upstream PRs, and 2 review comments.*

## Movement This Week

vaubandev made the sharpest climb on this board in weeks — #19 to #6, thirteen ranks, driven by their fourth upstream PR landing in this period (the Vauban Pack v0.5.0 registry update) on top of three earlier infrastructure merges: recording the commit SHA when `gh` is logged out, finding a `--path` pack's LICENSE next to its manifest, and the initial Vauban Pack listing. None of it is glamorous. All of it makes the ecosystem more reliable. Four merges, an active fork, and a 35-point jump.

yusasecurity debuts at #4 this week with six upstream merges — all in the last 30 days, all security-focused. They started by listing the YUSA Pack, then escalated through three consecutive `skill-scan` hardening PRs: hidden Unicode detection (TAG smuggling, bidi, zero-width), case-insensitive injection-phrase matching that catches capitalizations and look-alike characters, and finally a full-folder scan on install rather than just SKILL.md. That's systematic hardening of a real attack surface. Coming in at #4 on first appearance is unusual; landing there via pure security infrastructure work is rarer still.

Svector-anu absorbed two more upstream merges — a dev-loop proof gate generalization (PR 1349) and a workflow model-recording fix (PR 1343) — to reach 85 lifetime merges. Their ICP integration workstream (SNS digest sweep, canister audit, IC Rust audit pack, ICP docs) landed earlier in the period. At 879 points they hold a 754-point gap over #2, and they remain the only contributor with upstream review comments this period (2 of them).

Thirteen of last week's top 20 fell off the board this period, including antfleet-ops (#2, 149 points) and houndflow (#5, 98 points). Both had no upstream PRs in the last 30 days and their forks weren't pushed in the same window. The leaderboard's rolling eligibility criteria are unforgiving: a fork that goes quiet for 31 days stops counting, regardless of historical score. The 11 new entries filling the lower half of this week's table are almost entirely operators who have never sent work upstream — the board is resetting toward its natural baseline.

duan521127 is the highest-commit operator on the board this week with no upstream PRs (16 fork commits, 5 unique skills added, score 41). They're ranked #9 and they're the clearest outreach target in the fleet right now.

## Top Contributors

| Rank | Contributor | Score | Merged PRs | Open PRs | Reviews | Fork Commits | New Skills | First PR? | Change |
|------|-------------|-------|------------|----------|---------|--------------|------------|-----------|--------|
| 1 | @Svector-anu | 879 | 85 | 0 | 2 | 0 | 5 | — | = |
| 2 | @sentinelhood | 125 | 10 | 0 | 0 | 0 | 5 | — | ↑1 |
| 3 | @NurstarK | 106 | 8 | 0 | 0 | 1 | 5 | — | ↑1 |
| 4 | @yusasecurity | 85 | 6 | 0 | 0 | 0 | 5 | — | new |
| 5 | @alexverify | 85 | 6 | 0 | 0 | 0 | 5 | — | ↑1 |
| 6 | @vaubandev | 65 | 4 | 0 | 0 | 0 | 5 | — | ↑13 |
| 7 | @ether-btc | 55 | 0 | 0 | 0 | 30 | 5 | — | = |
| 8 | @richard7463 | 54 | 2 | 0 | 0 | 9 | 5 | — | new |
| 9 | @duan521127 | 41 | 0 | 0 | 0 | 16 | 5 | — | new |
| 10 | @icepy | 40 | 0 | 0 | 0 | 15 | 5 | — | ↓1 |
| 11 | @normancomics | 36 | 1 | 0 | 0 | 0 | 5 | — | new |
| 12 | @anondevv69 | 36 | 0 | 0 | 0 | 10 | 5 | — | new |
| 13 | @Metroxe | 35 | 1 | 0 | 0 | 0 | 5 | — | new |
| 14 | @domosta | 33 | 0 | 0 | 0 | 8 | 5 | — | new |
| 15 | @nhutminh159 | 29 | 0 | 0 | 0 | 4 | 5 | — | new |
| 16 | @SorenMoussavian | 28 | 0 | 0 | 0 | 3 | 5 | — | new |
| 17 | @unifirer | 27 | 0 | 0 | 0 | 2 | 5 | — | new |
| 18 | @TReinaCOM | 27 | 0 | 0 | 0 | 2 | 5 | — | new |
| 19 | @Domimueller85 | 26 | 0 | 0 | 0 | 1 | 5 | — | new |
| 20 | @FggDarkOnee420 | 26 | 0 | 0 | 0 | 0 | 5 | — | new |

*(top 20; no ✨ entries this period — no FIRST_TIME_CONTRIBUTOR associations detected.)*

## Outreach Candidates

Active forks whose owner has never opened an upstream PR — the highest-conversion outreach pool, sorted by fork commit count:

- @duan521127 — 16 fork commits, 0 stars, 5 new skills
- @anondevv69 — 10 fork commits, 1 star, 5 new skills (approval-audit, atrium-watch, bankr-communities, bankr-space-worker, beat-tracker)
- @domosta — 8 fork commits, 0 stars, 5 new skills
- @nhutminh159 — 4 fork commits, 0 stars, 5 new skills
- @SorenMoussavian — 3 fork commits, 0 stars, 5 new skills (ai2human series: QA, handoff, local-verification)
- @unifirer — 2 fork commits, 0 stars, 5 new skills
- @TReinaCOM — 2 fork commits, 0 stars, 5 new skills
- @Domimueller85 — 1 fork commit, 0 stars, 5 new skills
- @swarm-ai-research — 0 fork commits, 2 stars, 0 new skills (ahead by 1,366 commits — high-divergence fork)
- @Boodszw — 0 fork commits, 0 stars, 4 new skills (alchemy, bankr, opensea, zerion)

## Upstream Contribution Signal

- **Contributors with merged upstream PRs:** 9
- **First-time contributors this period:** 0 (no FIRST_TIME_CONTRIBUTOR associations detected)
- **Top reviewer:** @Svector-anu with 2 review comments
- **Most-merged contributor:** @Svector-anu with 85 merged PRs (2 new merges this period)
- **Active forks whose owner has never opened an upstream PR:** ~52 of 61

## Fork Fleet Summary

- **Active forks scanned (pushed last 30d):** 61
- **Total upstream PRs tracked (last 30d):** 36
- **Total review comments tracked (last 30d):** 2
- **Unique contributors:** 61
- **Contributors filtered as bots/core:** aaronjmars, aeonframework, Copilot[bot], github-actions

---
*Source: GitHub API — forks, pulls, pull review comments, and compare endpoints of aaronjmars/aeon. Scoring: merged PR +10, first-PR bonus +5, open PR +3, review comment +2 (cap 20), fork commit +1 (cap 30), new skill +5 (cap 5), fork star +1 (cap 20).*
