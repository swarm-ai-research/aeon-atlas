#!/usr/bin/env python3
"""Collect enabled skill data from aeon forks via GitHub API."""
import subprocess
import json
import re

FORKS = [
    "Skalda555/aeon",
    "ukiyo-p/aeon",
    "CamillaTeston/aeon",
    "Nickforall/aeon",
    "Bastiansure/aeon-bastiansure",
    "itsablabla/aeon",
    "aeonone/aeon-aeonone",
    "susilo77/aeon-susilo77",
    "opencolin/aeon",
    "domosta/aeon",
    "SuperFluouss/aeon-superfluouss",
    "chandras19349/aeon",
    "mohammadi0011/aeon",
    "Metroxe/aeon",
    "hypurr-inc/aeon",
    "wtfsayo/aeon",
    "yusasecurity/aeon",
    "SorenMoussavian/SorenOS-Aeon",
    "caigen18/aeon",
    "ardy03851-bit/aeon",
    "duan521127/aeon",
    "shubu258/aeon",
    "Tunn3l/aeon-tunn3l",
    "njfyanf9-a11y/aeon-njfyanf9-a11y",
    "vaubandev/aeon",
    "TReinaCOM/aeon",
    "airdropia/aeon",
    "o8613844-cpu/aeon-o8613844-cpu",
    "icepy/aeon-token",
    "moosebizlab/aeon",
    "xiaozz8/aeon",
    "00288/aeon",
    "AragAgg/aeon",
    "mervwtf/aeon-mervwtf",
    "sentinelhood/aeon",
    "FggDarkOnee420/Fgg-aeon",
    "0xAnvesaka/aeon",
    "nhutminh159/aeon-nhutminh159",
    "gelo11/aeon",
    "rauhaton/aeon-rauhaton",
    "unifirer/aeon",
    "stevenclaus00/aeon-AIGUY",
    "Svector-anu/aeon",
    "normancomics/aeon",
    "Domimueller85/aeon",
    "Kodawari10/aeon",
    "alexverify/aeon",
    "enuno/noesis-aeon",
    "anondevv69/bankr-space-aeon",
    "NurstarK/aeon-upstream",
    "beijiangqukuailian/aeon",
    "swarm-ai-research/aeon-atlas",
    "AIRYDER/aeon",
    "richard7463/aeon",
    "lawbworld-tech/aeon",
    "youpsla/aeon",
    "damo-nu11/aeon-minebean",
    "madebyshun/blueagent-aeon",
    "traewang/aeon-contrib",
    "Boodszw/Boodszw_Bread",
    "ether-btc/aeon",
]

# Parse skill line: "  skill-name: { enabled: true/false, schedule: ..., model: ..., var: ... }"
SKILL_LINE_RE = re.compile(
    r'^\s+(\S+):\s*\{\s*enabled:\s*(true|false)'
    r'(?:,\s*schedule:\s*"([^"]*)")?'
    r'(?:,\s*(?:var|model):[^,}]*)*'
    r'(?:,\s*model:\s*"([^"]*)")?'
    r'(?:,\s*var:\s*"([^"]*)")?'
)

def parse_skill_line(line):
    """Extract skill name, enabled, model, var from an inline skill definition."""
    m = SKILL_LINE_RE.match(line)
    if not m:
        return None
    name = m.group(1)
    enabled = m.group(2) == "true"
    # More robust extraction
    model_m = re.search(r'model:\s*"([^"]*)"', line)
    var_m = re.search(r'var:\s*"([^"]*)"', line)
    schedule_m = re.search(r'schedule:\s*"([^"]*)"', line)
    return {
        "name": name,
        "enabled": enabled,
        "model": model_m.group(1) if model_m else None,
        "var": var_m.group(1) if var_m else "",
        "schedule": schedule_m.group(1) if schedule_m else None,
    }

def fetch_fork_skills(fork):
    """Fetch aeon.yml skill lines from a fork via gh api."""
    result = subprocess.run(
        ["gh", "api", f"repos/{fork}/contents/aeon.yml", "--jq", ".content"],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode != 0 or not result.stdout.strip():
        return None, "yml_unreadable"

    import base64
    try:
        content = base64.b64decode(
            result.stdout.strip().replace("\\n", "").replace("\n", "")
        ).decode("utf-8")
    except Exception:
        return None, "yml_unreadable"

    skills = {}
    for line in content.splitlines():
        parsed = parse_skill_line(line)
        if parsed:
            skills[parsed["name"]] = parsed

    if not skills:
        return None, "yml_unreadable"
    return skills, "ok"

results = []
for fork in FORKS:
    print(f"Processing {fork}...", flush=True)
    skills, status = fetch_fork_skills(fork)
    results.append({
        "full_name": fork,
        "status": status,
        "skills": skills,
    })
    print(f"  -> {status} ({len(skills) if skills else 0} skills)", flush=True)

with open("/home/runner/work/aeon-atlas/aeon-atlas/.outputs/fork-skills.json", "w") as f:
    json.dump(results, f, indent=2)

statuses = {}
for r in results:
    s = r["status"]
    statuses[s] = statuses.get(s, 0) + 1
print(f"\nSummary: {statuses}")
print("Written to .outputs/fork-skills.json")
