#!/usr/bin/env bash
# Probe each registry host; print: host|http_code|time_total (or ERR on connect failure)
FMT='%{http_code} %{time_total}'
probe() {
  local host="$1"; local url="$2"
  local out rc
  out=$(curl -sS -o /dev/null -w "$FMT" --max-time 8 "$url" 2>/dev/null)
  rc=$?
  if [ $rc -ne 0 ]; then
    echo "$host|ERR|curl_rc=$rc"
  else
    echo "$host|$out"
  fi
}
probe "api.coingecko.com" "https://api.coingecko.com/api/v3/ping"
probe "api.llama.fi" "https://api.llama.fi/protocols"
probe "stablecoins.llama.fi" "https://stablecoins.llama.fi/stablecoins?includePrices=false"
probe "yields.llama.fi" "https://yields.llama.fi/pools"
probe "api.alternative.me" "https://api.alternative.me/fng/?limit=1"
probe "gamma-api.polymarket.com" "https://gamma-api.polymarket.com/markets?limit=1"
probe "clob.polymarket.com" "https://clob.polymarket.com/"
probe "api.dexscreener.com" "https://api.dexscreener.com/token-profiles/latest/v1"
probe "api.geckoterminal.com" "https://api.geckoterminal.com/api/v2/networks?page=1"
probe "api.etherscan.io" "https://api.etherscan.io/api?module=stats&action=ethprice"
probe "api.elections.kalshi.com" "https://api.elections.kalshi.com/trade-api/v2/exchange/status"
probe "api.openalex.org" "https://api.openalex.org/works?per_page=1"
probe "export.arxiv.org" "http://export.arxiv.org/api/query?max_results=1"
probe "huggingface.co" "https://huggingface.co/api/models?limit=1"
probe "hn.algolia.com" "https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=1"
probe "hacker-news.firebaseio.com" "https://hacker-news.firebaseio.com/v0/maxitem.json"
probe "api.github.com" "https://api.github.com/zen"
probe "api.npmjs.org" "https://api.npmjs.org/downloads/point/last-week/react"
probe "registry.npmjs.org" "https://registry.npmjs.org/"
probe "pypistats.org" "https://pypistats.org/api/packages/pip/recent"
probe "api.first.org" "https://api.first.org/data/v1/epss?limit=1"
probe "www.federalregister.gov" "https://www.federalregister.gov/api/v1/documents.json?per_page=1"
probe "api.telegram.org" "https://api.telegram.org"
probe "discord.com" "https://discord.com/api/v10/gateway"
probe "hooks.slack.com" "https://hooks.slack.com/"
