import subprocess
import json
import re
import sys
import base64

ACTIVE_FORKS = [
    "yusasecurity/aeon", "SorenMoussavian/SorenOS-Aeon", "caigen18/aeon",
    "ardy03851-bit/aeon", "duan521127/aeon", "shubu258/aeon", "Tunn3l/aeon-tunn3l",
    "njfyanf9-a11y/aeon-njfyanf9-a11y", "vaubandev/aeon", "TReinaCOM/aeon",
    "airdropia/aeon", "o8613844-cpu/aeon-o8613844-cpu", "dajiaohuang/aeonfun-aeon",
    "inginjadipro/aeonfun-aeon", "icepy/aeon-token", "moosebizlab/aeon",
    "xiaozz8/aeon", "00288/aeon", "repoken/aeon", "AragAgg/aeon",
    "mervwtf/aeon-mervwtf", "sentinelhood/aeon", "FggDarkOnee420/Fgg-aeon",
    "0xAnvesaka/aeon", "nhutminh159/aeon-nhutminh159", "gelo11/aeon",
    "rauhaton/aeon-rauhaton", "unifirer/aeon", "stevenclaus00/aeon-AIGUY",
    "divyesh54/aeon", "CHEYCKIT/aeon", "Svector-anu/aeon",
    "normancomics/aeon", "Domimueller85/aeon", "alexverify/aeon",
    "enuno/noesis-aeon", "NurstarK/aeon-upstream", "beijiangqukuailian/aeon",
    "anondevv69/bankr-space-aeon", "AIRYDER/aeon", "richard7463/aeon",
    "rohitctrl/aeon", "hansj73/aeon", "thanhdat3007-create/aeon",
    "czijian729-oss/aeon", "AwesomeAgentTools/aeon", "sparkleware/aeon",
    "antfleet-ops/aeon", "amritmirch/aeon", "gdalabs/aeon",
    "stefrogovskyi/aeon", "takanafur/aeon", "TakamiyaZee/aeon",
    "UIZorrot/aeon", "abhirajprasad/aeon", "danbuildss/aeon",
    "youpsla/aeon", "lawbworld-tech/aeon", "taekwonv89/aeon",
    "madebyshun/blueagent-aeon", "Boodszw/Boodszw_Bread", "ether-btc/aeon",
    "damo-nu11/aeon-minebean", "0xMal0u/aeon", "enzoonchain/aeon"
]

UPSTREAM_ENABLED = {
    "skill-health", "api-health-probe", "ai-framework-watch", "ecosystem-pulse",
    "fleet-state", "fork-cohort", "fork-release-tracker", "contributor-spotlight",
    "fork-first-run-alert", "skill-evals", "skill-update-check", "fleet-scorecard",
    "skill-leaderboard", "fork-contributor-leaderboard", "operator-scorecard",
    "follow-up-patrol", "fork-skill-digest", "fork-skill-gap", "fleet-skill-adoption",
    "fork-health-score", "workflow-security-audit", "atlas", "atlas-layers",
    "atlas-improve", "skill-freshness", "heartbeat"
}

UPSTREAM_SONNET_SKILLS = {
    "telegram-digest", "pr-skill-triage", "huggingface-trending", "monitor-polymarket",
    "monitor-kalshi", "price-threshold-alert", "market-context-refresh", "token-report",
    "ai-framework-watch", "competitor-launch-radar", "ecosystem-pulse", "sparkleware-catalog",
    "fleet-state", "fork-cohort", "fork-release-tracker", "contributor-spotlight",
    "fork-first-run-alert", "skill-evals", "skill-update-check", "fleet-scorecard",
    "skill-leaderboard", "fork-contributor-leaderboard", "contributor-reward",
    "operator-scorecard", "follow-up-patrol", "fork-skill-digest", "fork-skill-gap",
    "fleet-skill-adoption", "fork-health-score", "star-momentum-alert", "repo-scanner",
    "syndicate-article", "evening-recap", "cost-report", "spend-monitor",
    "self-review", "signal-verdict", "skill-freshness", "smithery-manifest",
    "v4-readiness", "schedule-ads", "aixbt-pulse", "vercel-projects",
    "builder-map", "agent-displacement", "launch-radar", "topic-momentum",
    "narrative-convergence", "pm-pulse", "pm-intel", "pm-manipulation",
    "rwa-pulse", "compute-pulse", "x402-monitor", "mcp-pulse",
    "idea-pipeline", "idea-validator"
}

UPSTREAM_SKILLS_LIST = [
    "action-converter","agent-buzz","agent-displacement","ai-framework-watch","aixbt-pulse",
    "api-health-probe","article","atlas","atlas-improve","atlas-layers","auto-merge","auto-workflow",
    "autoresearch","batch-health","builder-map","changelog","channel-recap","code-health",
    "competitor-launch-radar","compute-pulse","config-validator","contract-audit","contributor-reward",
    "contributor-spotlight","cost-report","create-campaign","create-skill","daily-routine","deal-flow",
    "deep-research","defi-monitor","defi-overview","deploy-prototype","deployer-trace","digest",
    "disclosure-tracker","distribute-tokens","ecosystem-pulse","engagement-act","evening-recap",
    "external-feature","farcaster-digest","feature","fetch-tweets","fleet-control","fleet-scorecard",
    "fleet-skill-adoption","fleet-state","follow-up-patrol","fork-cohort","fork-contributor-leaderboard",
    "fork-first-run-alert","fork-fleet","fork-health-score","fork-release-tracker","fork-skill-digest",
    "fork-skill-gap","github-issues","github-monitor","github-releases","github-trending","goal-tracker",
    "hacker-news-digest","heartbeat","holder-concentration","huggingface-trending","idea-capture",
    "idea-pipeline","idea-validator","issue-triage","janitor","last30","launch-radar","list-digest",
    "market-context-refresh","mcp-pulse","memory-flush","memory-structural-dedupe","milestone-tracker",
    "monitor-kalshi","monitor-polymarket","monitor-runners","morning-brief","narrative-convergence",
    "narrative-tracker","note-taking","on-chain-monitor","onboard","operator-scorecard","paper-digest",
    "paper-pick","pm-intel","pm-manipulation","pm-pulse","polymarket","polymarket-comments",
    "pr-merge-queue","pr-review","pr-skill-triage","pr-tracker","pr-triage","price-threshold-alert",
    "product-hunt-launch","project-lens","push-recap","pvr-triage-monitor","pvr-watchlist",
    "reddit-digest","reflect","refresh-x","reg-monitor","remix-tweets","reply-maker","repo-actions",
    "repo-article","repo-pulse","repo-revive","repo-scanner","research-brief","rss-digest","rss-feed",
    "rug-scan","run-frequency-guard","rwa-pulse","schedule-ads","search-skill","security",
    "security-digest","self-improve","self-review","show-hn-draft","signal-verdict","skill-analytics",
    "skill-enabler","skill-evals","skill-freshness","skill-graph","skill-health","skill-leaderboard",
    "skill-repair","skill-security-scan","skill-update-check","smithery-manifest","sparkleware-catalog",
    "spawn-instance","spend-monitor","star-milestone","star-momentum-alert","startup-idea",
    "syndicate-article","technical-explainer","telegram-digest","thread-formatter","token-alert",
    "token-movers","token-pick","token-report","tool-builder","topic-momentum","treasury-info",
    "tweet-digest","tweet-roundup","tx-explain","unlock-monitor","update-gallery","v4-readiness",
    "vercel-projects","vibecoding-digest","vuln-scanner","vuln-tracker","wallet-digest","wallet-profile",
    "weekly-review","weekly-shiplog","workflow-security-audit","write-tweet","x402-monitor"
]
UPSTREAM_SKILLS = set(UPSTREAM_SKILLS_LIST)


def fetch_aeon_yml(fork):
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{fork}/contents/aeon.yml", "--jq", ".content"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            return None, "yml_404"
        content_b64 = result.stdout.strip()
        if not content_b64:
            return None, "yml_empty"
        content = base64.b64decode(content_b64).decode("utf-8", errors="replace")
        return content, "ok"
    except Exception as e:
        return None, f"error:{str(e)[:40]}"


def parse_skills(yml_content):
    skills_enabled = []
    skills_disabled = []
    model_overrides = {}
    var_set = []
    schedule_overrides = {}

    in_skills = False
    for line in yml_content.split('\n'):
        stripped = line.strip()
        if stripped == 'skills:':
            in_skills = True
            continue
        elif in_skills and line and not line[0].isspace() and stripped and not stripped.startswith('#'):
            in_skills = False
            continue
        if not in_skills:
            continue
        if stripped.startswith('#'):
            continue
        m = re.match(r'^\s+([\w-]+):\s*\{(.+)\}', line)
        if not m:
            continue
        skill_name = m.group(1)
        attrs = m.group(2)
        enabled_m = re.search(r'enabled:\s*(true|false)', attrs)
        if not enabled_m:
            continue
        enabled = enabled_m.group(1) == 'true'
        if enabled:
            skills_enabled.append(skill_name)
        else:
            skills_disabled.append(skill_name)
        model_m = re.search(r'model:\s*["\']?([\w.-]+)["\']?', attrs)
        if model_m:
            model = model_m.group(1)
            upstream_model = 'claude-sonnet-4-6' if skill_name in UPSTREAM_SONNET_SKILLS else 'claude-opus-4-8'
            if model != upstream_model:
                model_overrides[skill_name] = model
        var_m = re.search(r'var:\s*"([^"]*)"', attrs)
        if not var_m:
            var_m = re.search(r"var:\s*'([^']*)'", attrs)
        if var_m and var_m.group(1):
            var_set.append(skill_name)
        schedule_m = re.search(r'schedule:\s*"([^"]+)"', attrs)
        if not schedule_m:
            schedule_m = re.search(r"schedule:\s*'([^']+)'", attrs)
        if schedule_m:
            schedule_overrides[skill_name] = schedule_m.group(1)

    return {
        'skills_enabled': skills_enabled,
        'skills_disabled': skills_disabled,
        'model_overrides': model_overrides,
        'var_set': var_set,
        'schedule_overrides': schedule_overrides
    }


results = []

print(f"Processing {len(ACTIVE_FORKS)} forks...", file=sys.stderr)

for i, fork in enumerate(ACTIVE_FORKS):
    print(f"[{i+1}/{len(ACTIVE_FORKS)}] {fork}", file=sys.stderr, flush=True)
    yml_content, status = fetch_aeon_yml(fork)
    if yml_content is None:
        results.append({
            "full_name": fork,
            "status": "unreadable",
            "error": status,
            "skills_enabled": [],
            "skills_disabled_vs_upstream": [],
            "model_overrides": {},
            "var_set": [],
            "schedule_overrides": [],
            "fork_only_skills": [],
            "enabled_diff": 0,
            "var_set_count": 0,
            "model_override_count": 0,
            "schedule_override_count": 0
        })
        continue
    parsed = parse_skills(yml_content)
    enabled_set = set(parsed['skills_enabled'])
    disabled_set = set(parsed['skills_disabled'])
    enabled_diff = 0
    skills_disabled_vs_upstream = []
    for skill in UPSTREAM_ENABLED:
        if skill in disabled_set:
            enabled_diff += 1
            skills_disabled_vs_upstream.append(skill)
    for skill in enabled_set:
        if skill not in UPSTREAM_ENABLED and skill in UPSTREAM_SKILLS:
            enabled_diff += 1
    var_set_count = len(parsed['var_set'])
    model_override_count = len(parsed['model_overrides'])
    fork_status = 'configured' if (enabled_diff > 0 or var_set_count > 0 or model_override_count > 0) else 'template'
    results.append({
        "full_name": fork,
        "status": fork_status,
        "skills_enabled": parsed['skills_enabled'],
        "skills_disabled_vs_upstream": skills_disabled_vs_upstream,
        "model_overrides": parsed['model_overrides'],
        "var_set": parsed['var_set'],
        "schedule_overrides": list(parsed['schedule_overrides'].keys()),
        "fork_only_skills": [],
        "enabled_diff": enabled_diff,
        "var_set_count": var_set_count,
        "model_override_count": model_override_count,
        "schedule_override_count": 0
    })

output = {
    "target_repo": "aaronjmars/aeon",
    "n_active": len(ACTIVE_FORKS),
    "forks": results
}

print(json.dumps(output))
