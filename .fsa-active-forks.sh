#!/bin/bash
# Check top forks for POWER+ACTIVE status (workflow run in last 7 days)
# Outputs tab-delimited: fork_name\tdefault_branch

PARENT_REPO="aeonfun/aeon"
CUTOFF=$(date -u -d "7 days ago" +%s)
ACTIVE_COUNT=0
AUDITED=0

# Get top 120 forks by stargazers
FORKS=$(gh api "repos/${PARENT_REPO}/forks?per_page=100&sort=stargazers" --jq \
  '.[] | select(.owner.login | test("dependabot\\[bot\\]|github-actions\\[bot\\]|aeonframework\\[bot\\]") | not) | .full_name' 2>/dev/null)

for FORK in $FORKS; do
  AUDITED=$((AUDITED + 1))

  # Check most recent workflow run
  RUN_AT=$(gh api "repos/${FORK}/actions/runs?per_page=1" \
    --jq '.workflow_runs[0].updated_at // empty' 2>/dev/null)

  if [ -n "$RUN_AT" ]; then
    RUN_TS=$(date -u -d "$RUN_AT" +%s 2>/dev/null || echo 0)
    if [ "$RUN_TS" -ge "$CUTOFF" ] 2>/dev/null; then
      # Get default branch
      DEFAULT_BR=$(gh api "repos/${FORK}" --jq '.default_branch // "main"' 2>/dev/null || echo "main")
      echo "${FORK}	${DEFAULT_BR}"
      ACTIVE_COUNT=$((ACTIVE_COUNT + 1))
      # Cap at 80
      if [ "$ACTIVE_COUNT" -ge 80 ]; then
        echo "TRUNCATED_AT_80" >&2
        break
      fi
    fi
  fi

  # Status update every 10
  if [ $((AUDITED % 10)) -eq 0 ]; then
    echo "PROGRESS: audited=${AUDITED} active=${ACTIVE_COUNT}" >&2
  fi
done

echo "FINAL: audited=${AUDITED} active=${ACTIVE_COUNT}" >&2
