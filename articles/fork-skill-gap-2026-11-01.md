# Fork Skill Gap — 2026-11-01

**Verdict:** WIDE_GAP — 7 readable forks each missing 20+ upstream skills (median gap: 47)

**Parent:** aeonfun/aeon · **Baseline skills.json:** swarm-ai-research/aeon-atlas · **Upstream skills:** 171
**Active forks audited:** 30 (POWER + ACTIVE, live check) · **Readable manifests:** 12/30
**Median gap:** 47 · **Max gap:** 101 · **Min gap:** 0

---

## Forks by gap size

| Fork | Owner | Source | Total upstream | Missing | Top missing categories |
|------|-------|--------|----------------|---------|------------------------|
| nigelon11/aeon | @nigelon11 | live | 171 | 101 | other (38), dev (19), productivity (14) |
| Boodszw/Boodszw_Bread | @Boodszw | live | 171 | 58 | other (37), dev (8), crypto (7) |
| madebyshun/blueagent-aeon | @madebyshun | live | 171 | 53 | other (34), dev (8), crypto (6) |
| damo-nu11/aeon-minebean | @damo-nu11 | live | 171 | 51 | other (34), dev (6), research (3) |
| lawbworld-tech/aeon | @lawbworld-tech | live | 171 | 50 | other (34), dev (6), crypto (6) |
| youpsla/aeon | @youpsla | live | 171 | 50 | other (34), dev (6), crypto (6) |
| gitlumen-team/aeon | @gitlumen-team | live | 171 | 45 | other (15), dev (9), productivity (8) |
| richard7463/aeon | @richard7463 | live | 171 | 14 | crypto (6), dev (5), productivity (2) |
| NurstarK/aeon-upstream | @NurstarK | live | 171 | 0 | — (extra skills: approval-audit, capabilities-map, ecosystem-entrants, fund-flow, honeypot-check, investigation-report, linked-wallets, liquidpad-launch, lp-lock-check, pr-merge-queue) |
| beijiangqukuailian/aeon | @beijiangqukuailian | live | 171 | 0 | — (extra skills: approval-audit, capabilities-map, fund-flow, honeypot-check, investigation-report, linked-wallets, liquidpad-launch, lp-lock-check, pr-merge-queue) |
| ashneil12/aeon-upstream | @ashneil12 | live | 171 | 0 | — (202 skills; all upstream + 31 fork-only) |
| aeoncity-hub/aeon | @aeoncity-hub | live | 171 | 0 | — (202 skills; all upstream + 31 fork-only) |

---

## Top 10 unadopted upstream skills

Slugs missing on the most readable forks — the inverse view.

| Slug | Category | Shipped | Forks missing it |
|------|----------|---------|------------------|
| fork-health-score | dev | 2026-05-29 | 8 / 12 |
| follow-up-patrol | productivity | 2026-05-29 | 8 / 12 |
| spend-monitor | productivity | 2026-05-29 | 7 / 12 |
| fleet-scorecard | dev | 2026-05-29 | 7 / 12 |
| mcp-pulse | dev | 2026-05-29 | 7 / 12 |
| pvr-triage-monitor | other | 2026-05-23 | 7 / 12 |
| self-review | other | 2026-05-23 | 6 / 12 |
| skill-enabler | other | 2026-05-23 | 6 / 12 |
| config-validator | other | 2026-05-23 | 6 / 12 |
| wallet-profile | crypto | — | 6 / 12 |

**Note on nigelon11 and gitlumen-team:** Both forks use renamed aliases for several upstream skills (e.g. `followup-patrol` vs `follow-up-patrol`, `fork-health` vs `fork-health-score`, `skill-gap` vs `fork-skill-gap`). These are counted as missing per slug-exact matching. The forks are functionally closer than the raw gap numbers suggest, but have diverged from upstream's canonical slug namespace — which complicates future sync.

---

## Unreadable forks

Forks where `skills.json` returned 404 (no manifest at default branch). Not counted in gap totals.

| Fork | Owner | Reason |
|------|-------|--------|
| enuno/noesis-aeon | @enuno | 404 |
| icepy/aeon-token | @icepy | 404 |
| Svector-anu/aeon | @Svector-anu | 404 |
| alexverify/aeon | @alexverify | 404 |
| ether-btc/aeon | @ether-btc | 404 |
| moosebizlab/aeon | @moosebizlab | 404 |
| 00288/aeon | @00288 | 404 |
| njfyanf9-a11y/aeon-njfyanf9-a11y | @njfyanf9-a11y | 404 |
| FggDarkOnee420/Fgg-aeon | @FggDarkOnee420 | 404 |
| mervwtf/aeon-mervwtf | @mervwtf | 404 |
| rauhaton/aeon-rauhaton | @rauhaton | 404 |
| stevenclaus00/aeon-AIGUY | @stevenclaus00 | 404 |
| xiaozz8/aeon | @xiaozz8 | 404 |
| gelo11/aeon | @gelo11 | 404 |
| normancomics/aeon | @normancomics | 404 |
| airdropia/aeon | @airdropia | 404 |
| o8613844-cpu/aeon-o8613844-cpu | @o8613844-cpu | 404 |
| MagIcKEarl/aeon | @MagIcKEarl | 404 |

These forks are actively running workflows (verified via Actions API) but have stripped or never added `skills.json`. Their true skill inventory is unknown — gap reporting treats them as `unreadable`, not zero-skill.

---

## Source status

`active_list_source=live · forks_audited=30 · skills_json_lookup=12/30 · unreadable=18 · truncated=false · cohort_state_age_days=N/A (no cohort state)`
