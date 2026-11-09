# AI Framework Watch — 2026-11-09

**Verdict:** RELEASE WEEK: 4 frameworks shipped — langgraph, crewai, mastra, pydantic-ai

**Tracked:** 9 of 9 frameworks  ·  **Unreachable:** 0  ·  **Anchor:** aaronjmars/aeon

> _First run — COLD START. All 7d/30d deltas are baselines only; momentum signals begin next week._

---

## Ranked table

(Anchor pinned to top. All deltas `—` on cold start. Ordered by stars after anchor.)

| Framework | Stars | 7d Δ | 30d Δ | Releases (7d) | Breaking? | Headline |
|-----------|------:|------|-------|:-------------:|:---------:|----------|
| aaronjmars/aeon | 789 | — | — | 0 | — | No release this week |
| microsoft/autogen | 61,755 | — | — | 0 | — | — |
| crewAIInc/crewAI | 60,676 | — | — | 5 | — | 1.15.35 → 1.15.39: rapid patch cadence |
| run-llama/llama_index | 52,853 | — | — | 0 | — | — |
| langchain-ai/langgraph | 44,679 | — | — | 5 | — | 1.2.20 + sdk/cli bumps |
| stanfordnlp/dspy | 38,980 | — | — | 0 | — | — |
| huggingface/smolagents | 30,271 | — | — | 0 | — | — |
| mastra-ai/mastra | 29,425 | — | — | 2 | — | @mastra/core@1.82.0 — Highlights |
| pydantic/pydantic-ai | 21,099 | — | — | 3 | — | v2.66.0 + v1.107.10 (dual-track) |

---

## Releases (7-day window)

### langchain-ai/langgraph

- **langgraph-cli==0.4.42** (2026-11-06) — Changes since cli==0.4.41
- **langgraph-sdk==0.4.14** (2026-11-06) — Changes since sdk==0.4.13
- **langgraph==1.2.20** (2026-11-05) — Changes since 1.2.19
- **langgraph-sdk==0.4.13** (2026-11-05) — Changes since sdk==0.4.12
- **langgraph-cli==0.4.41** (2026-11-05) — Changes since cli==0.4.40

### crewAIInc/crewAI

- **1.15.39** (2026-11-09) — What's Changed
- **1.15.38** (2026-11-08) — What's Changed
- **1.15.37** (2026-11-07) — What's Changed
- **1.15.36** (2026-11-06) — What's Changed
- **1.15.35** (2026-11-03) — What's Changed

### mastra-ai/mastra

- **@mastra/core@1.82.0** (2026-11-04) — Highlights (see release for details)
- **@mastra/core@1.81.0** (2026-11-02) — Highlights (see release for details)

### pydantic/pydantic-ai

- **v2.66.0** (2026-11-04) — Release notes generated from changelog
- **v1.107.10** (2026-11-04) — What's Changed _(v1 maintenance track)_
- **v2.65.0** (2026-11-03) — Release notes generated from changelog

_Note: pydantic-ai maintains parallel v1 and v2 release tracks. v1.107.10 and v2.66.0 were published simultaneously on 2026-11-04, indicating active dual-track support._

---

## Anchor position

aeon sits at 789 stars — the smallest by absolute count in this cohort, which is expected for a framework launched in July 2026 vs. peers with 2–3 year head starts. The two nearest comparables by age and niche (GitHub-native agent runtime) don't appear in this watchlist. aeon shipped no releases in the 7-day window; v0.1.0 remains the sole tagged release (2026-07-09). Autogen at 61,755 stars and crewai at 60,676 lead the cohort by star count, though both show quieter release cadences this week than their younger peers (mastra: weekly minor releases; langgraph: 5 releases across 3 packages in 2 days). Cold start — aeon's delta trajectory begins next week.

---

## Source status

`gh_api: ok · reachable: 9/9 · releases_lookup: 9/9 · breaking_signals_fired: 0`
