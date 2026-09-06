Weekly ecosystem refresh — **267 repos**, 264 fork edges, 331 skill-overlap edges, **21 ★** across the fork network (3 upstream roots: `aaronjmars/aeon`, `aaronjmars/aeon-agent`, `aaronjmars/miroshark-aeon`).

A big week: the fork network grew net +68 (80 new, 12 gone since the last run), 210 forks now ship custom skills across 290 distinct novel slugs.

**New forks since last run (80):** cyborganeh/aeon, Jason9720/aeon, dipanshuhappy/aeon, forumchen388-debug/aeon, keyurbodar/aeon, MADRIGAL007/aeon, weezyf1995-boop/aeon, elegarmco/aeon, MagIcKEarl/aeon, Calcutatator/aeon, cultosagent/aeon, jsfranklin221/aeon, thesmithdao/aeon, kevin-houston/aeon, theia-ttista/aeon, hansj73/aeon, kyleobrien91/aeon, Kodawari10/aeon, use-agent-os/aeon, kajr0s/aeon … and 60 more (full list in `atlas.json`). Notable non-`aeon`-named forks: enuno/noesis-aeon, Svector-anu/svectors-lab, sysvhurtstop/susfux, Boodszw/Boodszw_Bread, AITOBIAS04/CHORUS.

**Resumed activity after dormancy (36):** sinfronterasai/aeon, stefrogovskyi/aeon, clawhunter/add-clawhunter-pack, gitlumen-team/aeon, chxoky/aeon, aeoncity-hub/aeon, sparkleware/aeon, UIZorrot/aeon, gitlawbounty/aeon, danbuildss/aeon … (36 forks pushed >7 days beyond their prior `pushedAt`).

**Newly archived:** AntFleet/aeon (flipped `archived: false → true`; a new `AntFleet/aeon-template` fork appeared alongside).

**New high-overlap skill pairs (294, weight ≥ 0.5):** a large cluster of the new forks share near-identical customization sets (many at weight 1.0 — e.g. s97472091-pixel/aeon ⇄ usepaxterapp/aeon ⇄ anajuliabit/aeon-fork ⇄ SamsShow/aeon), suggesting a wave of forks provisioned from a common skill pack.

**★ jumps:** none (no fork gained ≥ 3 stars this cycle).

**Universe build failed:** the Quartz universe view (`docs/universe/`) could not be rebuilt in this run. The build step (`scripts/build-universe.sh`) requires `rsync`/`cp` to bootstrap the gitignored Quartz upstream scaffold and script execution, all of which were blocked by this session's sandbox (git clone and npm are reachable, but the scaffold-copy and wrapper-script steps were denied). Per the skill's fallback, the atlas regen was not aborted and universe-related parts of the commit were skipped — `docs/universe/` is unchanged from the prior run and will refresh on the next environment with full build permissions. The atlas source markdown in `quartz/content/` **is** current (written by `scripts/atlas.mjs`).

Interactive map: `docs/atlas.html`. Digest: `docs/atlas.md`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
