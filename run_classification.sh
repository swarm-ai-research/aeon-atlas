#!/bin/bash
# Classify each fork's aeon.yml against upstream defaults

UPSTREAM_ENABLED_TRUE="heartbeat skill-health api-health-probe ai-framework-watch ecosystem-pulse fleet-state fork-cohort fork-release-tracker contributor-spotlight fork-first-run-alert skill-evals skill-update-check fleet-scorecard skill-leaderboard fork-contributor-leaderboard operator-scorecard follow-up-patrol fork-skill-digest fork-skill-gap fleet-skill-adoption fork-health-score workflow-security-audit atlas atlas-layers atlas-improve skill-freshness"

FORKS=(
  "bgiesing/pepper-bgiesing"
  "dajiaohuang/aeonfun-aeon"
  "inginjadipro/aeonfun-aeon"
  "icepy/aeon-token"
  "moosebizlab/aeon"
  "xiaozz8/aeon"
  "00288/aeon"
  "repoken/aeon"
  "AragAgg/aeon"
  "mervwtf/aeon-mervwtf"
  "sentinelhood/aeon"
  "FggDarkOnee420/Fgg-aeon"
  "0xAnvesaka/aeon"
  "nhutminh159/aeon-nhutminh159"
  "gelo11/aeon"
  "rauhaton/aeon-rauhaton"
  "unifirer/aeon"
  "stevenclaus00/aeon-AIGUY"
  "rikomuslimnur1001/aeon-rikomuslimnur1001"
  "divyesh54/aeon"
  "djh4ck3r/aeon"
  "CHEYCKIT/aeon"
  "Svector-anu/aeon"
  "normancomics/aeon"
  "Domimueller85/aeon"
  "Blockchains/aeon"
  "nkipa/aeon"
  "mardemsean/aeon-autonomous-agent-platform"
  "super-ai-8453/aeon"
  "brainsparker/aeon"
  "Ditto190/aeon-automaton-modme"
  "rohitctrl/aeon"
  "hansj73/aeon"
  "thanhdat3007-create/aeon"
  "czijian729-oss/aeon"
  "amritmirch/aeon"
  "AwesomeAgentTools/aeon"
  "alexverify/aeon"
  "stefrogovskyi/aeon"
  "NurstarK/aeon-upstream"
  "beijiangqukuailian/aeon"
  "gdalabs/aeon"
  "swarm-ai-research/aeon-atlas"
  "AIRYDER/aeon"
  "TakamiyaZee/aeon"
  "richard7463/aeon"
  "sparkleware/aeon"
  "UIZorrot/aeon"
  "lawbworld-tech/aeon"
  "gitlawbounty/aeon"
  "taekwonv89/aeon"
  "danbuildss/aeon"
  "0xMal0u/aeon"
  "youpsla/aeon"
  "antfleet-ops/aeon"
  "damo-nu11/aeon-minebean"
  "abhirajprasad/aeon"
  "enzoonchain/aeon"
  "takanafur/aeon"
  "madebyshun/blueagent-aeon"
  "Boodszw/Boodszw_Bread"
  "ether-btc/aeon"
  "pezetel/aeon"
  "naolnegassa/aeon"
)

OUTPUT_FILE="/home/runner/work/aeon-atlas/aeon-atlas/fork_analysis.json"
exec 3>&1  # Save original stdout
exec 1>"$OUTPUT_FILE"  # Redirect stdout to file

is_upstream_enabled() {
  local skill="$1"
  for s in $UPSTREAM_ENABLED_TRUE; do
    if [ "$s" = "$skill" ]; then return 0; fi
  done
  return 1
}

process_fork() {
  local fork="$1"

  # Fetch aeon.yml content directly
  local content
  content=$(gh api "repos/$fork/contents/aeon.yml" --jq '.content' 2>/dev/null)
  local exit_code=$?

  if [ $exit_code -ne 0 ] || [ -z "$content" ]; then
    echo "{\"tier\":\"UNREADABLE\",\"status\":\"no_yml\",\"skills_enabled\":[],\"var_set\":{},\"model_override\":{},\"fork_only_skills\":[],\"enabled_diff\":0,\"var_set_count\":0,\"model_override_count\":0}"
    return
  fi

  # Decode base64
  local yml_text
  yml_text=$(echo "$content" | tr -d '"' | tr -d '\n' | base64 -d 2>/dev/null)
  if [ -z "$yml_text" ]; then
    echo "{\"tier\":\"UNREADABLE\",\"status\":\"yml_unreadable\",\"skills_enabled\":[],\"var_set\":{},\"model_override\":{},\"fork_only_skills\":[],\"enabled_diff\":0,\"var_set_count\":0,\"model_override_count\":0}"
    return
  fi

  # Find enabled:true skills
  local enabled_skills=()
  local enabled_diff=0
  local var_set_pairs=""
  local model_override_pairs=""

  # Parse inline YAML skill entries
  while IFS= read -r line; do
    # Match: "  skill-name: { ... }"
    if [[ "$line" =~ ^[[:space:]]{2}([a-z0-9_-]+):[[:space:]]*\{(.+)\} ]]; then
      local skill_name="${BASH_REMATCH[1]}"
      local props="${BASH_REMATCH[2]}"

      # Skip non-skill lines
      [[ "$skill_name" =~ ^(enabled|schedule|model|var|provider|jsonrender|telegram|channels|gateway)$ ]] && continue

      # Extract enabled
      local fork_enabled=""
      if [[ "$props" =~ enabled:[[:space:]]*(true|false) ]]; then
        fork_enabled="${BASH_REMATCH[1]}"
      fi

      # Check divergence
      if [ "$fork_enabled" = "true" ]; then
        enabled_skills+=("\"$skill_name\"")
        if ! is_upstream_enabled "$skill_name"; then
          ((enabled_diff++))
        fi
      elif [ "$fork_enabled" = "false" ]; then
        if is_upstream_enabled "$skill_name"; then
          ((enabled_diff++))
        fi
      fi

      # Check var
      if [[ "$props" =~ var:[[:space:]]*\"([^\"]+)\" ]]; then
        local var_val="${BASH_REMATCH[1]}"
        var_set_pairs="${var_set_pairs},\"$skill_name\":\"$var_val\""
      fi

      # Check model
      if [[ "$props" =~ model:[[:space:]]*\"([^\"]+)\" ]]; then
        local model_val="${BASH_REMATCH[1]}"
        model_override_pairs="${model_override_pairs},\"$skill_name\":\"$model_val\""
      fi
    fi
  done <<< "$yml_text"

  # Build JSON arrays/objects
  local skills_json=""
  for s in "${enabled_skills[@]}"; do
    skills_json="${skills_json},${s}"
  done
  skills_json="[${skills_json#,}]"

  [ -z "$var_set_pairs" ] && var_set_json="{}" || var_set_json="{${var_set_pairs#,}}"
  [ -z "$model_override_pairs" ] && model_json="{}" || model_json="{${model_override_pairs#,}}"

  local var_count=$(echo "$var_set_pairs" | grep -o '"' | wc -l)
  var_count=$((var_count / 4))
  local model_count=$(echo "$model_override_pairs" | grep -o '"' | wc -l)
  model_count=$((model_count / 4))

  # Determine tier
  local tier="TEMPLATE"
  [ $enabled_diff -gt 0 ] && tier="CONFIGURED"
  [ $var_count -gt 0 ] && tier="CONFIGURED"
  [ $model_count -gt 0 ] && tier="CONFIGURED"

  echo "{\"tier\":\"$tier\",\"status\":\"ok\",\"skills_enabled\":$skills_json,\"var_set\":$var_set_json,\"model_override\":$model_json,\"fork_only_skills\":[],\"enabled_diff\":$enabled_diff,\"var_set_count\":$var_count,\"model_override_count\":$model_count}"
}

# Build result JSON
echo "{"
first=1
for fork in "${FORKS[@]}"; do
  result=$(process_fork "$fork")
  tier=$(echo "$result" | grep -o '"tier":"[^"]*"' | head -1 | cut -d'"' -f4)
  echo "Processing $fork -> $tier" >&2
  if [ $first -eq 1 ]; then
    echo "\"$fork\": $result"
    first=0
  else
    echo ",\"$fork\": $result"
  fi
done
echo "}"
