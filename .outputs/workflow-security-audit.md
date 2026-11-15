*Workflow audit — 2026-11-15*
WORKFLOW_AUDIT_NEW_CRITICAL — 1 new critical, 2 new high (all script injection). Fixes prepared (3) · manual review (3).
Top chain: messages.yml:577 echoes toJson(client_payload) into a single-quoted shell string — an inbound chat message with a quote breaks out → RCE with GH_GLOBAL and every job secret (the April audit missed it).
Note: workflow-file push blocked — the Actions token lacks 'workflows' permission; the ready-to-apply patch is in the report Appendix. Scan ran DEGRADED (zizmor/actionlint install blocked; hand-rolled + manual review).
PR: https://github.com/swarm-ai-research/aeon-atlas/pull/36
