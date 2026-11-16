#!/usr/bin/env python3
"""Fetch and classify aeon.yml from active forks."""

import subprocess
import json
import base64
import sys
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

FORKS = [
    "bgiesing/pepper-bgiesing", "dajiaohuang/aeonfun-aeon", "inginjadipro/aeonfun-aeon",
    "icepy/aeon-token", "moosebizlab/aeon", "xiaozz8/aeon", "00288/aeon",
    "repoken/aeon", "AragAgg/aeon", "mervwtf/aeon-mervwtf", "sentinelhood/aeon",
    "FggDarkOnee420/Fgg-aeon", "0xAnvesaka/aeon", "nhutminh159/aeon-nhutminh159",
    "gelo11/aeon", "rauhaton/aeon-rauhaton", "unifirer/aeon",
    "stevenclaus00/aeon-AIGUY", "rikomuslimnur1001/aeon-rikomuslimnur1001",
    "divyesh54/aeon", "djh4ck3r/aeon", "CHEYCKIT/aeon", "Svector-anu/aeon",
    "normancomics/aeon", "Domimueller85/aeon", "Blockchains/aeon", "nkipa/aeon",
    "mardemsean/aeon-autonomous-agent-platform", "super-ai-8453/aeon",
    "brainsparker/aeon", "Ditto190/aeon-automaton-modme", "rohitctrl/aeon",
    "hansj73/aeon", "thanhdat3007-create/aeon", "czijian729-oss/aeon",
    "amritmirch/aeon", "AwesomeAgentTools/aeon", "alexverify/aeon",
    "stefrogovskyi/aeon", "NurstarK/aeon-upstream", "beijiangqukuailian/aeon",
    "gdalabs/aeon", "swarm-ai-research/aeon-atlas", "AIRYDER/aeon",
    "TakamiyaZee/aeon", "richard7463/aeon", "sparkleware/aeon", "UIZorrot/aeon",
    "lawbworld-tech/aeon", "gitlawbounty/aeon", "taekwonv89/aeon",
    "danbuildss/aeon", "0xMal0u/aeon", "youpsla/aeon", "antfleet-ops/aeon",
    "damo-nu11/aeon-minebean", "abhirajprasad/aeon", "enzoonchain/aeon",
    "takanafur/aeon", "madebyshun/blueagent-aeon", "Boodszw/Boodszw_Bread",
    "ether-btc/aeon", "pezetel/aeon", "naolnegassa/aeon",
]

UPSTREAM_ENABLED_TRUE = {
    "heartbeat", "skill-health", "api-health-probe", "ai-framework-watch",
    "ecosystem-pulse", "fleet-state", "fork-cohort", "fork-release-tracker",
    "contributor-spotlight", "fork-first-run-alert", "skill-evals",
    "skill-update-check", "fleet-scorecard", "skill-leaderboard",
    "fork-contributor-leaderboard", "operator-scorecard", "follow-up-patrol",
    "fork-skill-digest", "fork-skill-gap", "fleet-skill-adoption",
    "fork-health-score", "workflow-security-audit", "atlas", "atlas-layers",
    "atlas-improve", "skill-freshness",
}

UPSTREAM_MODEL_SONNET = {
    "telegram-digest", "huggingface-trending", "pr-skill-triage",
    "monitor-polymarket", "monitor-kalshi", "token-report", "price-threshold-alert",
    "market-context-refresh", "star-momentum-alert", "repo-scanner",
    "syndicate-article", "skill-analytics", "evening-recap", "vercel-projects",
    "cost-report", "spend-monitor", "ai-framework-watch", "competitor-launch-radar",
    "ecosystem-pulse", "fleet-state", "fork-cohort", "fork-release-tracker",
    "contributor-spotlight", "fork-first-run-alert", "skill-evals",
    "skill-update-check", "fleet-scorecard", "skill-leaderboard",
    "fork-contributor-leaderboard", "contributor-reward", "operator-scorecard",
    "follow-up-patrol", "fork-skill-digest", "fork-skill-gap", "fleet-skill-adoption",
    "fork-health-score", "self-review", "signal-verdict", "idea-pipeline",
    "idea-validator", "narrative-convergence", "launch-radar", "topic-momentum",
    "builder-map", "rwa-pulse", "compute-pulse", "x402-monitor", "mcp-pulse",
    "agent-displacement", "pm-pulse", "pm-intel", "pm-manipulation", "polymarket",
    "nixbt-pulse", "sparkleware-catalog",
}

UPSTREAM_SKILLS = {
    "action-converter", "agent-buzz", "agent-displacement", "ai-framework-watch",
    "aixbt-pulse", "api-health-probe", "article", "atlas", "atlas-improve",
    "atlas-layers", "auto-merge", "auto-workflow", "autoresearch", "batch-health",
    "builder-map", "changelog", "channel-recap", "code-health",
    "competitor-launch-radar", "compute-pulse", "config-validator", "contract-audit",
    "contributor-reward", "contributor-spotlight", "cost-report", "create-campaign",
    "create-skill", "daily-routine", "deal-flow", "deep-research", "defi-monitor",
    "defi-overview", "deploy-prototype", "deployer-trace", "digest",
    "disclosure-tracker", "distribute-tokens", "ecosystem-pulse", "engagement-act",
    "evening-recap", "external-feature", "farcaster-digest", "feature",
    "fetch-tweets", "fleet-control", "fleet-scorecard", "fleet-skill-adoption",
    "fleet-state", "follow-up-patrol", "fork-cohort", "fork-contributor-leaderboard",
    "fork-first-run-alert", "fork-fleet", "fork-health-score", "fork-release-tracker",
    "fork-skill-digest", "fork-skill-gap", "github-issues", "github-monitor",
    "github-releases", "github-trending", "goal-tracker", "hacker-news-digest",
    "heartbeat", "holder-concentration", "huggingface-trending", "idea-capture",
    "idea-pipeline", "idea-validator", "issue-triage", "janitor", "last30",
    "launch-radar", "list-digest", "market-context-refresh", "mcp-pulse",
    "memory-flush", "memory-structural-dedupe", "milestone-tracker", "monitor-kalshi",
    "monitor-polymarket", "monitor-runners", "morning-brief", "narrative-convergence",
    "narrative-tracker", "note-taking", "on-chain-monitor", "onboard",
    "operator-scorecard", "paper-digest", "paper-pick", "pm-intel", "pm-manipulation",
    "pm-pulse", "polymarket", "polymarket-comments", "pr-merge-queue", "pr-review",
    "pr-skill-triage", "pr-tracker", "pr-triage", "price-threshold-alert",
    "product-hunt-launch", "project-lens", "push-recap", "pvr-triage-monitor",
    "pvr-watchlist", "reddit-digest", "reflect", "refresh-x", "reg-monitor",
    "remix-tweets", "reply-maker", "repo-actions", "repo-article", "repo-pulse",
    "repo-revive", "repo-scanner", "research-brief", "rss-digest", "rss-feed",
    "rug-scan", "run-frequency-guard", "rwa-pulse", "schedule-ads", "search-skill",
    "security", "security-digest", "self-improve", "self-review", "show-hn-draft",
    "signal-verdict", "skill-analytics", "skill-enabler", "skill-evals",
    "skill-freshness", "skill-graph", "skill-health", "skill-leaderboard",
    "skill-repair", "skill-security-scan", "skill-update-check", "smithery-manifest",
    "sparkleware-catalog", "spawn-instance", "spend-monitor", "star-milestone",
    "star-momentum-alert", "startup-idea", "syndicate-article", "technical-explainer",
    "telegram-digest", "thread-formatter", "token-alert", "token-movers",
    "token-pick", "token-report", "tool-builder", "topic-momentum", "treasury-info",
    "tweet-digest", "tweet-roundup", "tx-explain", "unlock-monitor", "update-gallery",
    "v4-readiness", "vercel-projects", "vibecoding-digest", "vuln-scanner",
    "vuln-tracker", "wallet-digest", "wallet-profile", "weekly-review",
    "weekly-shiplog", "workflow-security-audit", "write-tweet", "x402-monitor",
}


def gh_api(path, jq=None, timeout=30):
    cmd = ["gh", "api", path]
    if jq:
        cmd += ["--jq", jq]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    return r


def parse_aeon_yml_skills(yml_text):
    """
    Parse skills section from aeon.yml text.
    Returns dict: skill_name -> {enabled, var, model, schedule}
    Uses regex since we don't want to depend on pyyaml.
    """
    skills = {}
    in_skills = False
    current_skill = None

    for line in yml_text.splitlines():
        # Detect start of skills block
        if re.match(r'^skills\s*:', line):
            in_skills = True
            continue
        # Detect end of skills block (new top-level key)
        if in_skills and re.match(r'^\S', line) and not line.strip().startswith('#'):
            key = line.split(':')[0].strip()
            if key not in ('', 'skills'):
                in_skills = False
                continue

        if not in_skills:
            continue

        # Skip comments
        stripped = line.strip()
        if stripped.startswith('#') or not stripped:
            continue

        # Match skill entry: "  skill-name: { ... }"
        # Could be multi-line but usually inline
        m = re.match(r'^\s{2}([\w-]+)\s*:\s*\{(.+)\}', line)
        if m:
            skill_name = m.group(1)
            props_str = m.group(2)

            enabled = None
            var = None
            model = None
            schedule = None

            # enabled
            em = re.search(r'enabled\s*:\s*(true|false)', props_str)
            if em:
                enabled = em.group(1) == 'true'

            # var
            vm = re.search(r'var\s*:\s*"([^"]*)"', props_str)
            if vm:
                var = vm.group(1)
            else:
                vm2 = re.search(r"var\s*:\s*'([^']*)'", props_str)
                if vm2:
                    var = vm2.group(1)

            # model
            mm = re.search(r'model\s*:\s*"([^"]+)"', props_str)
            if mm:
                model = mm.group(1)
            else:
                mm2 = re.search(r"model\s*:\s*'([^']+)'", props_str)
                if mm2:
                    model = mm2.group(1)
                else:
                    mm3 = re.search(r'model\s*:\s*([\w.-]+)', props_str)
                    if mm3 and mm3.group(1) not in ('true', 'false', 'null'):
                        model = mm3.group(1)

            # schedule
            sm = re.search(r'schedule\s*:\s*"([^"]+)"', props_str)
            if sm:
                schedule = sm.group(1)

            skills[skill_name] = {
                'enabled': enabled,
                'var': var,
                'model': model,
                'schedule': schedule,
            }

    return skills


def classify_fork(fork):
    result = {
        "tier": "UNREADABLE",
        "status": "unknown",
        "skills_enabled": [],
        "var_set": {},
        "model_override": {},
        "fork_only_skills": [],
        "enabled_diff": 0,
        "var_set_count": 0,
        "model_override_count": 0,
        "schedule_override_count": 0,
    }

    # Step 1: Get git tree
    jq_filter = '[.tree[] | select(.type == "blob") | .path]'
    try:
        r = gh_api(f"repos/{fork}/git/trees/HEAD?recursive=1", jq=jq_filter)
        if r.returncode != 0:
            stderr = r.stderr
            if "404" in stderr or "409" in stderr or "Git Repository is empty" in stderr:
                result["status"] = "no_tree"
                result["tier"] = "UNREADABLE"
                return result
            elif "rate limit" in stderr.lower() or ("403" in stderr):
                time.sleep(60)
                r2 = gh_api(f"repos/{fork}/git/trees/HEAD?recursive=1", jq=jq_filter)
                if r2.returncode != 0:
                    result["status"] = "rate_limited"
                    result["tier"] = "UNREADABLE"
                    return result
                r = r2
            else:
                result["status"] = "no_tree"
                result["tier"] = "UNREADABLE"
                return result

        files = json.loads(r.stdout)
    except Exception as e:
        result["status"] = "no_tree"
        result["tier"] = "UNREADABLE"
        return result

    # Check for aeon.yml
    if "aeon.yml" not in files:
        result["status"] = "no_yml"
        result["tier"] = "UNREADABLE"
        return result

    # Collect fork skill dirs
    fork_skill_dirs = set()
    for f in files:
        parts = f.split("/")
        if len(parts) >= 2 and parts[0] == "skills" and parts[1]:
            fork_skill_dirs.add(parts[1])

    fork_only = [d for d in fork_skill_dirs if d not in UPSTREAM_SKILLS]
    result["fork_only_skills"] = sorted(fork_only)

    # Step 2: Fetch aeon.yml
    try:
        r2 = gh_api(f"repos/{fork}/contents/aeon.yml", jq=".content")
        if r2.returncode != 0:
            result["status"] = "yml_unreadable"
            result["tier"] = "UNREADABLE"
            return result

        b64 = r2.stdout.strip().replace('\n', '')
        if b64.startswith('"') and b64.endswith('"'):
            b64 = b64[1:-1]
        b64 = b64.replace('\\n', '')
        yml_text = base64.b64decode(b64).decode("utf-8", errors="replace")
    except Exception:
        result["status"] = "yml_unreadable"
        result["tier"] = "UNREADABLE"
        return result

    result["status"] = "ok"

    # Step 3: Parse skills
    skills = parse_aeon_yml_skills(yml_text)

    # Step 4: Classify
    enabled_diff = 0
    var_set = {}
    model_override = {}
    schedule_override_count = 0
    skills_enabled = []

    all_skill_names = set(skills.keys()) | UPSTREAM_ENABLED_TRUE

    for skill_name, props in skills.items():
        fork_enabled = props.get('enabled')
        upstream_enabled = skill_name in UPSTREAM_ENABLED_TRUE

        if fork_enabled is not None and fork_enabled != upstream_enabled:
            enabled_diff += 1

        if fork_enabled:
            skills_enabled.append(skill_name)

        fork_var = props.get('var')
        if fork_var:  # non-empty var
            var_set[skill_name] = fork_var

        fork_model = props.get('model')
        if fork_model:
            upstream_model = "claude-sonnet-4-6" if skill_name in UPSTREAM_MODEL_SONNET else None
            if fork_model != upstream_model:
                model_override[skill_name] = fork_model

    result["skills_enabled"] = sorted(skills_enabled)
    result["var_set"] = var_set
    result["model_override"] = model_override
    result["enabled_diff"] = enabled_diff
    result["var_set_count"] = len(var_set)
    result["model_override_count"] = len(model_override)
    result["fork_only_skills"] = sorted(fork_only)

    # Classify tier
    is_configured = (
        enabled_diff > 0 or
        len(var_set) > 0 or
        len(model_override) > 0 or
        len(fork_only) > 0
    )
    result["tier"] = "CONFIGURED" if is_configured else "TEMPLATE"

    return result


print("Starting fork classification...", file=sys.stderr)

analysis = {}
with ThreadPoolExecutor(max_workers=6) as executor:
    futures = {executor.submit(classify_fork, fork): fork for fork in FORKS}
    for future in as_completed(futures):
        fork = futures[future]
        try:
            data = future.result()
            analysis[fork] = data
            print(f"  [{data['tier']:12s}] {fork}: {data['status']}", file=sys.stderr)
        except Exception as e:
            analysis[fork] = {
                "tier": "UNREADABLE", "status": "error",
                "skills_enabled": [], "var_set": {}, "model_override": {},
                "fork_only_skills": [], "enabled_diff": 0,
                "var_set_count": 0, "model_override_count": 0,
                "schedule_override_count": 0,
            }
            print(f"  [ERROR      ] {fork}: {e}", file=sys.stderr)

with open("/home/runner/work/aeon-atlas/aeon-atlas/fork_analysis.json", "w") as f:
    json.dump(analysis, f, indent=2)

configured = sum(1 for v in analysis.values() if v["tier"] == "CONFIGURED")
template = sum(1 for v in analysis.values() if v["tier"] == "TEMPLATE")
unreadable = sum(1 for v in analysis.values() if v["tier"] == "UNREADABLE")
print(f"\nDone. CONFIGURED={configured}, TEMPLATE={template}, UNREADABLE={unreadable}", file=sys.stderr)
print(f"Total: {len(analysis)}", file=sys.stderr)
