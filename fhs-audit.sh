#!/usr/bin/env bash
# Fork Health Score Audit Script
set -euo pipefail

TODAY="2026-10-26"
TODAY_EPOCH=$(date -u -d "$TODAY" +%s)
SINCE_30D=$(date -u -d "30 days ago" +%Y-%m-%dT00:00:00Z)
OUTPUT="/tmp/fhs-results.json"

FORKS=(
  "Corykidios/aeon" "use-agent-os/aeon" "FggDarkOnee420/Fgg-aeon"
  "normancomics/aeon" "mardemsean/aeon-autonomous-agent-platform"
  "thesmithdao/aeon" "kairunedev/aeon" "hesreallyhim/aeon-fork"
  "bgiesing/pepper-bgiesing" "dajiaohuang/aeonfun-aeon"
  "inginjadipro/aeonfun-aeon" "icepy/aeon-token" "moosebizlab/aeon"
  "xiaozz8/aeon" "00288/aeon" "repoken/aeon" "AragAgg/aeon"
  "mervwtf/aeon-mervwtf" "sentinelhood/aeon" "0xAnvesaka/aeon"
  "nhutminh159/aeon-nhutminh159" "gelo11/aeon" "rauhaton/aeon-rauhaton"
  "unifirer/aeon" "stevenclaus00/aeon-AIGUY"
  "rikomuslimnur1001/aeon-rikomuslimnur1001" "divyesh54/aeon"
  "djh4ck3r/aeon" "CHEYCKIT/aeon" "Svector-anu/aeon"
  "Domimueller85/aeon" "Blockchains/aeon" "nkipa/aeon" "googio/aeon"
  "super-ai-8453/aeon" "Secure-Code-Pro-Zyloch/aeon" "Oscar-Williams/aeon"
  "brainsparker/aeon" "Ditto190/aeon-automaton-modme" "rohitctrl/aeon"
  "iamziek/aeon" "niu12503/aeon" "0xsnackbaker/aeon" "Pinont/aeon.fun"
  "corinth1ans/aeon" "krpx0341/aeon" "darkstaryuri/aeon"
  "cyborganeh/aeon" "Jason9720/aeon" "dipanshuhappy/aeon"
  "forumchen388-debug/aeon" "keyurbodar/aeon" "MADRIGAL007/aeon"
  "weezyf1995-boop/aeon" "elegarmco/aeon" "MagIcKEarl/aeon"
  "Calcutatator/aeon" "cultosagent/aeon" "jsfranklin221/aeon"
  "kevin-houston/aeon" "theia-ttista/aeon" "hansj73/aeon"
  "kyleobrien91/aeon" "Kodawari10/aeon" "kajr0s/aeon"
  "thanhdat3007-create/aeon" "JDMD21/aeon" "czijian729-oss/aeon"
  "pkhr/aeon" "pablorq/aeon" "Cristian35s/aeon" "robertluciu-wq/aeon"
  "yghffhgx/aeon" "Akshmit/aeon" "kdegeek/aeon" "evrimulgen/aeon"
  "carsam2021/aeon" "dacode-dev/aeon" "raul1stdigital/aeon"
  "sysvhurtstop/susfux"
)

TOTAL=${#FORKS[@]}
TRUNCATED=false
[ "$TOTAL" -ge 80 ] && TRUNCATED=true

echo "Starting audit of $TOTAL forks..." >&2

# Build JSON incrementally
FORKS_JSON="{}"
READABLE=0
ACTIVE_COUNT=0
WARM_COUNT=0
STALE_COUNT=0
QUIET_COUNT=0
PR_SAT=""

for FORK in "${FORKS[@]}"; do
  echo "  Auditing $FORK..." >&2

  # Fetch repos/{fork}
  REPO_JSON=$(gh api "repos/$FORK" 2>/dev/null || echo "ERROR")
  if [ "$REPO_JSON" = "ERROR" ] || echo "$REPO_JSON" | grep -q '"message".*"Not Found"'; then
    FORKS_JSON=$(echo "$FORKS_JSON" | jq --arg f "$FORK" \
      '.[$f] = {"tier":"QUIET","pushed_days":999,"enabled_count":0,"prs_30d":0,"score":0,"stars":0,"unreadable":true,"partial_signals":false}')
    QUIET_COUNT=$((QUIET_COUNT+1))
    continue
  fi

  PUSHED_AT=$(echo "$REPO_JSON" | jq -r '.pushed_at // empty')
  DEFAULT_BRANCH=$(echo "$REPO_JSON" | jq -r '.default_branch // "main"')
  [ "$DEFAULT_BRANCH" = "null" ] || [ -z "$DEFAULT_BRANCH" ] && DEFAULT_BRANCH="main"
  STARS=$(echo "$REPO_JSON" | jq -r '.stargazers_count // 0')

  # pushed_days
  if [ -z "$PUSHED_AT" ]; then
    PUSHED_DAYS=999
  else
    PUSHED_EPOCH=$(date -u -d "$PUSHED_AT" +%s 2>/dev/null || echo "0")
    if [ "$PUSHED_EPOCH" = "0" ]; then
      PUSHED_DAYS=999
    else
      PUSHED_DAYS=$(( (TODAY_EPOCH - PUSHED_EPOCH) / 86400 ))
      [ "$PUSHED_DAYS" -lt 0 ] && PUSHED_DAYS=0
    fi
  fi

  # aeon.yml enabled count
  AEON_CONTENT=$(gh api "repos/${FORK}/contents/aeon.yml?ref=${DEFAULT_BRANCH}" --jq '.content' 2>/dev/null || echo "")
  ENABLED_COUNT=0
  PARTIAL=false
  if [ -n "$AEON_CONTENT" ]; then
    DECODED=$(echo "$AEON_CONTENT" | tr -d '\n' | base64 -d 2>/dev/null || echo "")
    if [ -n "$DECODED" ]; then
      # Inline-object grep
      ENABLED_COUNT=$(echo "$DECODED" | grep -oE '^[[:space:]]*[A-Za-z0-9_-]+:[[:space:]]*\{[^}]*enabled:[[:space:]]*true' | wc -l || echo 0)
      ENABLED_COUNT=$((ENABLED_COUNT+0))
      # Fallback: if 0 but bare "enabled: true" lines exist, count bare lines
      if [ "$ENABLED_COUNT" -eq 0 ] && echo "$DECODED" | grep -q 'enabled: true'; then
        ENABLED_COUNT=$(echo "$DECODED" | grep -c 'enabled: true' || echo 0)
        ENABLED_COUNT=$((ENABLED_COUNT+0))
      fi
    fi
  fi

  # PRs merged in 30d
  PRS_30D=0
  PR_OUTPUT=$(gh api "repos/${FORK}/pulls" \
    --method GET \
    -f state=closed \
    -f "base=${DEFAULT_BRANCH}" \
    -f per_page=100 \
    -f sort=updated \
    -f direction=desc \
    --jq "[.[] | select(.merged_at != null and .merged_at >= \"${SINCE_30D}\")] | length" 2>/dev/null || echo "ERROR")
  if [ "$PR_OUTPUT" != "ERROR" ] && [ -n "$PR_OUTPUT" ]; then
    PRS_30D=$((PR_OUTPUT+0))
    if [ "$PRS_30D" -ge 100 ]; then
      PR_SAT="${PR_SAT} ${FORK}"
    fi
  else
    PARTIAL=true
    PRS_30D=0
  fi

  # Score computation
  if [ "$PUSHED_DAYS" -ge 30 ]; then
    PUSH_SCORE=0
  else
    PUSH_SCORE=$(echo "$PUSHED_DAYS" | awk '{v=100-($1/30)*100; if(v<0)v=0; if(v>100)v=100; printf "%d", v+0.5}')
  fi
  SKILL_SCORE=$((ENABLED_COUNT * 10))
  [ "$SKILL_SCORE" -gt 100 ] && SKILL_SCORE=100
  PR_SCORE=$((PRS_30D * 20))
  [ "$PR_SCORE" -gt 100 ] && PR_SCORE=100

  SCORE=$(echo "$PUSH_SCORE $SKILL_SCORE $PR_SCORE" | awk '{s=0.5*$1+0.3*$2+0.2*$3; printf "%d", s+0.5}')

  # Tier
  TIER="QUIET"
  if [ "$PUSHED_DAYS" -le 7 ] && [ "$ENABLED_COUNT" -ge 2 ] && [ "$SCORE" -ge 70 ]; then
    TIER="ACTIVE"
  elif [ "$PUSHED_DAYS" -le 30 ] && ([ "$ENABLED_COUNT" -ge 1 ] || [ "$PRS_30D" -ge 1 ]); then
    TIER="WARM"
  elif [ "$PUSHED_DAYS" -gt 30 ] && [ "$PUSHED_DAYS" -le 180 ]; then
    TIER="STALE"
  fi

  READABLE=$((READABLE+1))
  case "$TIER" in
    ACTIVE) ACTIVE_COUNT=$((ACTIVE_COUNT+1)) ;;
    WARM)   WARM_COUNT=$((WARM_COUNT+1)) ;;
    STALE)  STALE_COUNT=$((STALE_COUNT+1)) ;;
    QUIET)  QUIET_COUNT=$((QUIET_COUNT+1)) ;;
  esac

  FORKS_JSON=$(echo "$FORKS_JSON" | jq \
    --arg f "$FORK" \
    --arg tier "$TIER" \
    --argjson pd "$PUSHED_DAYS" \
    --argjson ec "$ENABLED_COUNT" \
    --argjson pr "$PRS_30D" \
    --argjson sc "$SCORE" \
    --argjson st "$STARS" \
    --argjson partial "$PARTIAL" \
    '.[$f] = {"tier":$tier,"pushed_days":$pd,"enabled_count":$ec,"prs_30d":$pr,"score":$sc,"stars":$st,"unreadable":false,"partial_signals":$partial}')

  echo "    -> $TIER pushed=${PUSHED_DAYS}d skills=${ENABLED_COUNT} prs=${PRS_30D} score=${SCORE}" >&2
done

# Write final JSON
jq -n \
  --argjson audited "$TOTAL" \
  --argjson readable "$READABLE" \
  --argjson truncated "$TRUNCATED" \
  --argjson forks "$FORKS_JSON" \
  --arg fork_source "live" \
  '{
    "audited": $audited,
    "readable": $readable,
    "truncated": $truncated,
    "truncated_at": (if $truncated then 80 else null end),
    "fork_source": $fork_source,
    "forks": $forks
  }' > "$OUTPUT"

echo "" >&2
echo "=== RESULTS ===" >&2
echo "Audited: $TOTAL | Readable: $READABLE" >&2
echo "ACTIVE: $ACTIVE_COUNT | WARM: $WARM_COUNT | STALE: $STALE_COUNT | QUIET: $QUIET_COUNT" >&2
echo "Written to: $OUTPUT" >&2

# Print tier summary to stdout
echo "=== TIER SUMMARY ==="
echo "ACTIVE: $ACTIVE_COUNT"
echo "WARM:   $WARM_COUNT"
echo "STALE:  $STALE_COUNT"
echo "QUIET:  $QUIET_COUNT"
echo ""
echo "=== TOP ACTIVE FORKS ==="
jq -r '
  .forks | to_entries
  | map(select(.value.tier == "ACTIVE" and .value.unreadable == false))
  | sort_by(-.value.score, -.value.enabled_count, -.value.prs_30d, .value.pushed_days)
  | .[0:10]
  | to_entries
  | .[]
  | "\(.key+1). \(.value.key) score=\(.value.value.score) pushed=\(.value.value.pushed_days)d skills=\(.value.value.enabled_count) prs=\(.value.value.prs_30d)"
' "$OUTPUT"
