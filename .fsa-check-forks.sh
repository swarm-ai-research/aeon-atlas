#!/bin/bash
# Check each fork for POWER+ACTIVE status (workflow run in last 7 days)
# Reads fork list from stdin, outputs active forks to stdout

CUTOFF=$(date -u -d "7 days ago" +%s)
TODAY=$(date -u +%s)

while IFS= read -r FORK; do
  # Skip empty lines
  [ -z "$FORK" ] && continue

  # Get most recent workflow run timestamp
  RUN_AT=$(gh api "repos/${FORK}/actions/runs?per_page=1" --jq '.workflow_runs[0].updated_at // empty' 2>/dev/null)

  if [ -n "$RUN_AT" ]; then
    RUN_TS=$(date -u -d "$RUN_AT" +%s 2>/dev/null)
    if [ -n "$RUN_TS" ] && [ "$RUN_TS" -ge "$CUTOFF" ]; then
      echo "$FORK"
    fi
  fi
done
