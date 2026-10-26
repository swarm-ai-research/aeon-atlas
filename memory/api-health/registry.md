# API Health Registry

Operator-curated list of external hosts the fleet depends on. One row per distinct
host with a cheap, side-effect-free probe URL (documented health/ping endpoint, or
the lightest read-only endpoint available). Probed by `skills/api-health-probe`.

> **SEEDED 2026-10-26** by api-health-probe (first run). Operator: please review —
> drop hosts you don't care about, fix any probe URLs that return the wrong status,
> and add hosts the grep missed. Auth-gated hosts (api.x.ai, api.replicate.com,
> api.resend.com, api.vercel.com, api.bankr.bot, api.g.alchemy.com, api.aixbt.tech,
> api.neynar.com, pro-api.coingecko.com) were mostly omitted — a keyless probe of
> those returns noisy 401/403s, not a liveness signal. Add any you want tracked.

| host | probe_url | used_by |
|---|---|---|
| api.coingecko.com | https://api.coingecko.com/api/v3/ping | market-context-refresh, token-pick, token-movers, token-alert, on-chain-monitor, treasury-info, unlock-monitor |
| api.llama.fi | https://api.llama.fi/protocols | market-context-refresh, defi-overview |
| stablecoins.llama.fi | https://stablecoins.llama.fi/stablecoins?includePrices=false | market-context-refresh, defi-overview |
| yields.llama.fi | https://yields.llama.fi/pools | defi-overview |
| api.alternative.me | https://api.alternative.me/fng/?limit=1 | market-context-refresh |
| gamma-api.polymarket.com | https://gamma-api.polymarket.com/markets?limit=1 | polymarket, monitor-polymarket, market-context-refresh, last30, token-pick, pm-manipulation, polymarket-comments |
| clob.polymarket.com | https://clob.polymarket.com/ | polymarket, monitor-polymarket, pm-manipulation |
| api.dexscreener.com | https://api.dexscreener.com/token-profiles/latest/v1 | price-threshold-alert, token-pick, token-report |
| api.geckoterminal.com | https://api.geckoterminal.com/api/v2/networks?page=1 | token-report, monitor-runners |
| api.etherscan.io | https://api.etherscan.io/api?module=stats&action=ethprice | contract-audit, deployer-trace, holder-concentration, rug-scan, on-chain-monitor, wallet-profile |
| api.elections.kalshi.com | https://api.elections.kalshi.com/trade-api/v2/exchange/status | last30, monitor-kalshi |
| api.openalex.org | https://api.openalex.org/works?per_page=1 | research-brief |
| api.semanticscholar.org | https://api.semanticscholar.org/graph/v1/paper/search?query=ai&limit=1 | research-brief, technical-explainer, deep-research |
| export.arxiv.org | http://export.arxiv.org/api/query?max_results=1 | paper-digest, paper-pick, deep-research, write-tweet |
| huggingface.co | https://huggingface.co/api/models?limit=1 | huggingface-trending, paper-digest, paper-pick |
| hn.algolia.com | https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=1 | hacker-news-digest, last30, competitor-launch-radar |
| hacker-news.firebaseio.com | https://hacker-news.firebaseio.com/v0/maxitem.json | hacker-news-digest |
| api.github.com | https://api.github.com/zen | atlas, github-releases, security-digest, mcp-pulse, pvr-watchlist, skill-update-check, pvr-triage-monitor |
| api.npmjs.org | https://api.npmjs.org/downloads/point/last-week/react | mcp-pulse, x402-monitor |
| registry.npmjs.org | https://registry.npmjs.org/ | smithery-manifest |
| pypistats.org | https://pypistats.org/api/packages/pip/recent | mcp-pulse |
| api.first.org | https://api.first.org/data/v1/epss?limit=1 | security-digest |
| www.federalregister.gov | https://www.federalregister.gov/api/v1/documents.json?per_page=1 | reg-monitor |
| api.telegram.org | https://api.telegram.org | notify (Telegram channel) |
| discord.com | https://discord.com/api/v10/gateway | notify (Discord channel) |
| hooks.slack.com | https://hooks.slack.com/ | notify (Slack channel) |

## Excluded — needs a better probe (operator action)

These hosts are reachable but a plain read-only `GET` does **not** return a liveness
signal, so a probe would flag them DOWN even when the API is healthy. They were
pulled from the active table on the 2026-10-26 seed run. To re-enable, give each a
probe the skill's GET-based loop can score as 2xx/3xx:

| host | observed on seed | why GET fails | how to re-enable | used_by |
|---|---|---|---|---|
| eth.llamarpc.com | 403 | JSON-RPC endpoint; rejects GET | probe needs a cheap read-only POST (`eth_blockNumber`), or a different health URL | wallet-digest, defi-monitor, treasury-info |
| mainnet.base.org | 405 | JSON-RPC endpoint; GET = Method Not Allowed | same — read-only POST `eth_blockNumber` | contract-audit, rug-scan, wallet-profile, tx-explain |
| www.reddit.com | 403 | blocks default curl User-Agent | probe needs a custom UA header (skills already set one) | reddit-digest, vibecoding-digest, digest |
| api.semanticscholar.org | 429 | keyless requests are rate-limited | probe with `x-api-key` (skills use `SEMANTIC_SCHOLAR_API_KEY`) | research-brief, technical-explainer, deep-research |
