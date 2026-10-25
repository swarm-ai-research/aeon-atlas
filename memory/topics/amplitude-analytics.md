# Amplitude Analytics Setup

Browser and Agent Analytics installation for aeon-atlas. Tracks user engagement and agent LLM cost metrics.

## Browser Analytics (2026-09-11)

### Installation
- **Package:** `@amplitude/unified@^1` installed in `dashboard/`
- **Init:** Single `initAll` call in client-only `components/Analytics.tsx` component
- **Mount:** `analytics.tsx` mounted in `app/layout.tsx`, guarded by module-level flag
- **Config:** `NEXT_PUBLIC_AMPLITUDE_API_KEY` in `dashboard/.env.local` (gitignored), documented empty in `.env.example`

### First Event
- **Event name:** `Viewed Home Page`
- **Trigger:** Load-time, fires at Dashboard mount (right after Amplitude init)
- **Verified:** booted `next dev` locally, confirmed home page renders 200 with Amplitude bundle loaded, no runtime errors

### Coverage
- Fires on every route (mounted in root layout.tsx)
- Session Replay enabled and bundled

## Agent Analytics (2026-09-11)

### Architecture
No in-process LLM SDK found in repo — `mcp-server/` and `a2a-server/` both spawn `claude` CLI as subprocess with `--output-format json`.
**Solution:** Manual instrumentation (provider wrappers don't apply to subprocess pattern).

### Implementation
- **Package:** `@amplitude/ai` configured for manual tracking
- **Per-skill-run:** One-turn agent session built from CLI's own `total_cost_usd` and `usage` fields
- **Token convention:** Anthropic cache-inclusive (input_tokens + cache_read_input_tokens + cache_creation_input_tokens)
- **Tracking methods:** `trackUserMessage()` + `trackAiMessage()`
- **Servers instrumented:** `mcp-server/` and `a2a-server/`
- **Config:** `AMPLITUDE_AI_API_KEY` read from `process.env` at runtime
- **Graceful fallback:** Disables with warning if env var unset
- **Env docs:** Added `.env.example` files in each package (mcp-server/ was missing one)

### Validation (2026-09-11)
- All three TypeScript builds pass: dashboard, mcp-server, a2a-server
- `next dev` local boot: home page renders 200, Amplitude bundle loaded, no errors
- **Note:** Could not verify live event landing in Amplitude dashboard from sandbox (requires operator's project + real browser/API-key round trip)

## Branch & PR Status
- **Branch:** `claude/amplitude-analytics-setup-h2tmpr`
- **PR:** #3 (draft, subscribed to activity)
- **Status:** Ready for operator review and Amplitude API key configuration

## Next Steps
- Operator provides real Amplitude project API keys for testing live event delivery
- Verify events landing in Amplitude dashboard
- Configure agent cost tracking (mcp-server, a2a-server test runs)
