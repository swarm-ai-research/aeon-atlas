#!/usr/bin/env python3
"""fork-first-run-alert execution script — 2026-10-31"""
import json, subprocess, sys, os
from datetime import datetime, timezone, timedelta

TODAY = "2026-10-31"
PARENT = "aeonfun/aeon"
STATE_PATH = "memory/topics/fork-first-run-state.json"
STATE_TMP  = "memory/topics/.fork-first-run-state.tmp.json"
LOG_PATH   = "memory/logs/2026-10-31.md"
BOT_LIST   = {"dependabot[bot]", "github-actions[bot]", "aeonframework[bot]"}
ACTIVE_CUTOFF = datetime(2026, 10, 24, tzinfo=timezone.utc)  # now - 7 days

def gh(*args):
    r = subprocess.run(["gh"] + list(args), capture_output=True, text=True)
    return r.stdout.strip(), r.returncode

# ── 1. Load state ──────────────────────────────────────────────────────────────
with open(STATE_PATH) as f:
    state = json.load(f)
seen = {k.lower(): v for k, v in state.get("seen", {}).items()}
print(f"Loaded state: {len(seen)} seen forks, last_run={state.get('last_run')}")

# ── 2. Fetch forks (paginated) ─────────────────────────────────────────────────
result = subprocess.run(
    ["gh", "api", f"repos/{PARENT}/forks", "--paginate",
     "--jq", '[.[] | select(.archived != true and .disabled != true) | {full_name, owner: .owner.login, stargazers_count, pushed_at}]'],
    capture_output=True, text=True
)
pages = []
for line in result.stdout.splitlines():
    line = line.strip()
    if line:
        try:
            pages.extend(json.loads(line))
        except Exception:
            pass
pages.sort(key=lambda x: x.get("pushed_at", ""), reverse=True)
forks = pages[:80]
truncated = len(pages) > 80
print(f"Total forks fetched: {len(pages)}, capped to: {len(forks)}{', truncated_at=80' if truncated else ''}")

# ── 3. Diff against seen ───────────────────────────────────────────────────────
new_forks = [f for f in forks if f["full_name"].lower() not in seen]
print(f"New (unseen) forks to check: {len(new_forks)}")

# ── 4. Check workflow activity for each new fork ───────────────────────────────
active_new = []
for fork in new_forks:
    fn = fork["full_name"]
    out, rc = gh("api", f"repos/{fn}/actions/runs?per_page=1",
                 "--jq", '.workflow_runs[0] | {name, display_title, updated_at, html_url} // empty')
    if rc != 0 or not out or out == "null":
        print(f"  {fn}: no runs or 404 — skipping")
        continue
    try:
        run_meta = json.loads(out)
    except Exception:
        print(f"  {fn}: parse error — skipping")
        continue
    updated_at_str = run_meta.get("updated_at")
    if not updated_at_str:
        print(f"  {fn}: no updated_at — skipping")
        continue
    updated_at = datetime.fromisoformat(updated_at_str.replace("Z", "+00:00"))
    if updated_at >= ACTIVE_CUTOFF:
        active_new.append({**fork, "run_meta": run_meta})
        print(f"  {fn}: ACTIVE (ran {updated_at_str})")
    else:
        print(f"  {fn}: stale run ({updated_at_str}) — not active")

print(f"\nNew active forks: {len(active_new)}")

# ── 5. Bot filter ──────────────────────────────────────────────────────────────
eligible = [f for f in active_new if f["owner"] not in BOT_LIST]
print(f"Eligible (non-bot): {len(eligible)}")

# ── 6. Humanise time ──────────────────────────────────────────────────────────
def humanise(dt_str):
    try:
        dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
        now = datetime(2026, 10, 31, 20, 30, tzinfo=timezone.utc)
        delta = now - dt
        h = int(delta.total_seconds() // 3600)
        if h < 1:
            return "less than 1h ago"
        if h < 24:
            return f"{h}h ago"
        return f"{h//24}d ago"
    except Exception:
        return dt_str

# ── 7. Notifications ───────────────────────────────────────────────────────────
alerts_sent = 0
status = "FORK_FIRST_RUN_ALERT_QUIET"

if len(eligible) == 0:
    print("QUIET — no new activators")
elif 1 <= len(eligible) <= 3:
    for fork in eligible:
        rm = fork["run_meta"]
        first_run_line = rm.get("display_title") or rm.get("name") or ""
        when_line = humanise(rm.get("updated_at", ""))
        html_url = rm.get("html_url", "")
        msg_lines = [
            f"*New fork live — {TODAY} — {fork['full_name']}*",
            "",
            f"@{fork['owner']} just ran their first workflow on Aeon. Welcome to the running fleet.",
            "",
            f"Stars: {fork['stargazers_count']}",
        ]
        if first_run_line:
            msg_lines.append(f"First run: {first_run_line}")
        msg_lines.append(f"When: {when_line}")
        msg_lines.append("")
        msg_lines.append(f"Fork: https://github.com/{fork['full_name']}")
        if html_url:
            msg_lines.append(f"Run: {html_url}")
        msg = "\n".join(msg_lines)
        print(f"\n--- Notification ---\n{msg}\n")
        subprocess.run(["./notify", msg], capture_output=False)
        alerts_sent += 1
    status = "FORK_FIRST_RUN_ALERT_OK"
else:
    # 4+ batch
    rows = []
    for fork in eligible[:8]:
        rows.append(f"- @{fork['owner']} — {fork['full_name']} ({fork['stargazers_count']} stars)")
    footer = f"... and {len(eligible) - 8} more." if len(eligible) > 8 else ""
    batch_lines = [
        f"*{len(eligible)} new forks live — {TODAY}*",
        "",
        f"The fleet picked up {len(eligible)} first-time activators in the last day.",
        "",
    ] + rows
    if footer:
        batch_lines.append(footer)
    batch_lines += ["", f"Parent: {PARENT}", "Full list will land in Sunday's fork-cohort digest."]
    msg = "\n".join(batch_lines)
    print(f"\n--- Batch Notification ---\n{msg}\n")
    subprocess.run(["./notify", msg], capture_output=False)
    alerts_sent = 1
    status = "FORK_FIRST_RUN_ALERT_OK"

# ── 8. Update state ────────────────────────────────────────────────────────────
for fork in active_new:
    fn = fork["full_name"].lower()
    rm = fork.get("run_meta", {})
    seen[fn] = {
        "first_seen_active_at": TODAY,
        "first_seen_active_run_at": rm.get("updated_at"),
        "announced_at": TODAY if fork["owner"] not in BOT_LIST else None,
        "stargazers": fork["stargazers_count"],
    }

# LRU cap at 500
if len(seen) > 500:
    sorted_seen = sorted(seen.items(), key=lambda x: x[1].get("announced_at") or "0000-00-00")
    seen = dict(sorted_seen[-500:])
    print(f"Applied LRU cap, retained 500 entries")

new_state = {
    "parent_repo": PARENT,
    "last_run": TODAY,
    "last_status": status,
    "seen": {k: v for k, v in seen.items()},
}
with open(STATE_TMP, "w") as f:
    json.dump(new_state, f, indent=2)
os.replace(STATE_TMP, STATE_PATH)
print(f"State updated: {len(seen)} total seen, status={status}")

# ── 9. Log ─────────────────────────────────────────────────────────────────────
os.makedirs("memory/logs", exist_ok=True)
log_entry = f"""
## fork-first-run-alert
- **Skill**: fork-first-run-alert
- **Parent**: {PARENT}
- **Source**: live-fallback
- **Active forks scanned**: {len(forks)}
- **Previously seen**: {len({k: v for k, v in json.load(open(STATE_PATH))['seen'].items() if v.get('announced_at') and v['announced_at'] < TODAY})}
- **New activators**: {len(active_new)} (eligible after bot filter: {len(eligible)})
- **Alerts sent**: {alerts_sent}{' (BATCH)' if len(eligible) >= 4 and alerts_sent == 1 else ''}
- **Mode**: execute
- **Status**: {status}
"""
with open(LOG_PATH, "a") as f:
    f.write(log_entry)
print(f"Log written to {LOG_PATH}")
print(f"\nDone. Status: {status}")
