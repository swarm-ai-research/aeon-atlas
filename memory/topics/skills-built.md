# Skills Built & Deployed

Inventory of skills scaffolded, deployed, or upstreamed. Tracks adoption across forks.

## Recent Builds (2026-09 session)

### api-health-probe (2026-09-11)
- **Status:** Deployed, registered in aeon.yml
- **Purpose:** Proactively probes third-party API hosts fleet depends on before outages cause skill failures
- **Adoption:** Shipped by 7 forks
- **Notes:** Disabled by default, `var` = optional single host. Registered in docs/skills.md under Productivity & Meta. Differs from `skill-health` which audits *run* outcomes post-failure.
- **Files:** `skills/api-health-probe/SKILL.md`, aeon.yml entry, docs/skills.md catalog

### pr-merge-queue (2026-09-11)
- **Status:** Deployed, registered in aeon.yml
- **Purpose:** Safe queue-based PR merging (FIFO, one-at-a-time) to prevent unsafe multi-PR merges touching shared files (lockfiles, aeon.yml, generated catalogs)
- **Adoption:** 19 forks have this skill (highest adoption of remaining un-upstreamed candidates)
- **Features:** 
  - Opt-in via `merge-queue` label
  - Reuses auto-merge's safety gates (author allowlist, size cap, no opt-out labels)
  - Immediate `gh pr update-branch` on head PR post-merge to revalidate
  - Retry-capped (3 attempts) evictions get `merge-queue-blocked` label
- **Schedule:** 20:14 UTC (right after auto-merge's 14:00 slot)
- **Files:** `skills/pr-merge-queue/SKILL.md`, aeon.yml entry, docs/skills.md Dev & Code table
- **Notes:** Validated aeon.yml YAML parse + SKILL.md frontmatter. skills.json left untouched (no CI auto-regen).

### CrystalCore.OS Dashboard Route (2026-09-11)
- **Status:** Deployed, merged into PR #1
- **Purpose:** Themed React "CrystalCore.OS" UI (boot sequence, terminal, module dock) wired to live aeon-atlas data
- **Tech:** `/crystalcore` route in `dashboard/app/crystalcore/page.tsx`, reuses read-only `/api/` routes (skills, runs, memory topics/issues)
- **Data sources:** Live skill counts, last run timestamps, open issues, memory topics
- **Features:** Cosmetic only, no fetch/eval/cookie/localStorage/network calls in compiled bundle
- **Files:** `dashboard/app/crystalcore/page.tsx`, one-line link in TopBar.tsx

## Upstream Candidates (fork catalog)
- `skill-health`: Audits skill *run* outcomes after failures (paired with api-health-probe for full coverage)
- `auto-merge`: Merges every independently-qualifying PR (basis for pr-merge-queue safety gates)
- Additional candidates in `quartz/content/novel-skills/`
