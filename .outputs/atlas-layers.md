Done.

## Summary

Executed the **atlas-layers** skill for 2026-07-26.

**What I did:**
1. Ran `node scripts/atlas-layers.mjs` → `7 layers · 12 hand entries · 31 forks · 16 packs · 6 ecosystem`, regenerating `quartz/content/atlas-layers.md`.
2. Diffed against `HEAD`. The page changed, so I computed the four signal buckets:
   - **new_hand_entries = 0** — curated layers (1, 4–7) unchanged; `data/atlas-layers.json` untouched → no hand promotions.
   - **new_packs = 0** — Layer 3 unchanged.
   - **new_unclassified_ecosystem = 0** — the ecosystem section vanished (upstream `atlas.json` ecosystem feed shrank 43→6, all now claimed).
   - **new_fleet = 9**, all ★0 (also 9 dropped; total fork pool contracted 97→58 upstream).
3. Verdict fell to the bland `atlas-layers refreshed` form (new fleet exists but max stars = 0, so the `stars ≥ 1` gate isn't met).
4. Opened **PR #17** capturing the refresh, with an operator note flagging the sharp upstream `atlas.json` contraction (forks 97→58, ecosystem 43→6).
5. **Skipped the notify** — no operator-relevant signal; the only change is ★0 long-tail fork churn, which the skill explicitly treats as "not news."
6. Logged the run to `memory/logs/2026-07-26.md`.

**Exit mode:** `LAYERS_OK` (regenerated + PR opened, notify intentionally withheld).

**Files created/modified:** `quartz/content/atlas-layers.md`, `memory/logs/2026-07-26.md` (both on branch `atlas-layers/2026-07-26`, PR #17).

**Follow-up for the operator:** The underlying `atlas.json` feed contracted sharply this cycle (forks 97→58, ecosystem 43→6) with the header re-dated 06-05→06-28. That's an upstream `atlas` skill data change, outside this skill's notify scope — worth a glance if the contraction was unexpected.
