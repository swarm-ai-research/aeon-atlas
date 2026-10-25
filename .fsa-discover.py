#!/usr/bin/env python3
"""Discover POWER+ACTIVE forks of aeonfun/aeon with recent workflow activity."""
import subprocess
import json
from datetime import datetime, timezone, timedelta

PARENT = "aeonfun/aeon"
CUTOFF = datetime.now(timezone.utc) - timedelta(days=7)
BOT_OWNERS = {"dependabot[bot]", "github-actions[bot]", "aeonframework[bot]"}

def gh_api(path, jq=None):
    cmd = ["gh", "api", path]
    if jq:
        cmd += ["--jq", jq]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        return None
    return r.stdout.strip()

def gh_api_json(path):
    cmd = ["gh", "api", path]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except Exception:
        return None

# Get top 100 forks by stargazers
forks_data = gh_api_json(f"repos/{PARENT}/forks?per_page=100&sort=stargazers")
if not forks_data:
    print("ERROR: Could not list forks", flush=True)
    exit(1)

print(f"Total forks fetched: {len(forks_data)}", flush=True)

active_forks = []
audited = 0

for fork in forks_data:
    owner = fork.get("owner", {}).get("login", "")
    if owner in BOT_OWNERS:
        continue

    full_name = fork.get("full_name", "")
    audited += 1

    # Check most recent workflow run
    runs_data = gh_api_json(f"repos/{full_name}/actions/runs?per_page=1")

    if runs_data and runs_data.get("workflow_runs"):
        run = runs_data["workflow_runs"][0]
        updated_at = run.get("updated_at", "")
        if updated_at:
            try:
                run_dt = datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
                if run_dt >= CUTOFF:
                    default_br = fork.get("default_branch", "main") or "main"
                    active_forks.append((full_name, default_br))
                    print(f"ACTIVE: {full_name}\t{default_br}", flush=True)
                    if len(active_forks) >= 80:
                        print("TRUNCATED_AT_80", flush=True)
                        break
            except Exception:
                pass

    if audited % 10 == 0:
        print(f"PROGRESS: audited={audited} active={len(active_forks)}", flush=True)

print(f"FINAL: audited={audited} active={len(active_forks)}", flush=True)

# Write results
with open(".fsa-active-list.txt", "w") as f:
    for repo, branch in active_forks:
        f.write(f"{repo}\t{branch}\n")

print(f"Written {len(active_forks)} active forks to .fsa-active-list.txt", flush=True)
