import subprocess, json, base64, re, sys

ALL_FORKS = [
  "duan521127/aeon", "shubu258/aeon", "Tunn3l/aeon-tunn3l",
  "njfyanf9-a11y/aeon-njfyanf9-a11y", "vaubandev/aeon", "TReinaCOM/aeon",
  "airdropia/aeon", "o8613844-cpu/aeon-o8613844-cpu",
  "dajiaohuang/aeonfun-aeon", "inginjadipro/aeonfun-aeon",
  "icepy/aeon-token", "moosebizlab/aeon", "xiaozz8/aeon", "00288/aeon",
  "repoken/aeon", "AragAgg/aeon", "mervwtf/aeon-mervwtf",
  "sentinelhood/aeon", "FggDarkOnee420/Fgg-aeon", "0xAnvesaka/aeon",
  "nhutminh159/aeon-nhutminh159", "gelo11/aeon", "rauhaton/aeon-rauhaton",
  "unifirer/aeon", "stevenclaus00/aeon-AIGUY",
  "rikomuslimnur1001/aeon-rikomuslimnur1001", "divyesh54/aeon",
  "djh4ck3r/aeon", "CHEYCKIT/aeon", "Svector-anu/aeon",
  "normancomics/aeon", "Domimueller85/aeon", "Blockchains/aeon",
  "nkipa/aeon", "rohitctrl/aeon", "hansj73/aeon",
  "thanhdat3007-create/aeon", "czijian729-oss/aeon", "amritmirch/aeon",
  "AwesomeAgentTools/aeon", "alexverify/aeon",
  "enuno/noesis-aeon", "stefrogovskyi/aeon", "anondevv69/bankr-space-aeon",
  "NurstarK/aeon-upstream", "beijiangqukuailian/aeon", "gdalabs/aeon",
  "swarm-ai-research/aeon-atlas", "AIRYDER/aeon", "TakamiyaZee/aeon",
  "richard7463/aeon", "sparkleware/aeon", "UIZorrot/aeon",
  "lawbworld-tech/aeon", "gitlawbounty/aeon", "taekwonv89/aeon",
  "danbuildss/aeon", "0xMal0u/aeon", "youpsla/aeon",
  "antfleet-ops/aeon", "damo-nu11/aeon-minebean", "abhirajprasad/aeon",
  "enzoonchain/aeon", "takanafur/aeon", "madebyshun/blueagent-aeon",
  "Boodszw/Boodszw_Bread", "ether-btc/aeon", "pezetel/aeon",
]

UPSTREAM_SKILLS = set([
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
  "paper-pick","pm-intel","pm-manipulation","pm-pulse","polymarket","polymarket-comments","pr-merge-queue",
  "pr-review","pr-skill-triage","pr-tracker","pr-triage","price-threshold-alert","product-hunt-launch",
  "project-lens","push-recap","pvr-triage-monitor","pvr-watchlist","reddit-digest","reflect","refresh-x",
  "reg-monitor","remix-tweets","reply-maker","repo-actions","repo-article","repo-pulse","repo-revive",
  "repo-scanner","research-brief","rss-digest","rss-feed","rug-scan","run-frequency-guard","rwa-pulse",
  "schedule-ads","search-skill","security","security-digest","self-improve","self-review","show-hn-draft",
  "signal-verdict","skill-analytics","skill-enabler","skill-evals","skill-freshness","skill-graph",
  "skill-health","skill-leaderboard","skill-repair","skill-security-scan","skill-update-check",
  "smithery-manifest","sparkleware-catalog","spawn-instance","spend-monitor","star-milestone",
  "star-momentum-alert","startup-idea","syndicate-article","technical-explainer","telegram-digest",
  "thread-formatter","token-alert","token-movers","token-pick","token-report","tool-builder","topic-momentum",
  "treasury-info","tweet-digest","tweet-roundup","tx-explain","unlock-monitor","update-gallery","v4-readiness",
  "vercel-projects","vibecoding-digest","vuln-scanner","vuln-tracker","wallet-digest","wallet-profile",
  "weekly-review","weekly-shiplog","workflow-security-audit","write-tweet","x402-monitor"
])

# Only heartbeat is enabled:true in upstream defaults
UPSTREAM_DEFAULTS_ENABLED = {"heartbeat"}

def fetch_fork(fork):
    r = {"fork": fork, "status": "unknown", "enabled_skills": [], "fork_only_skills": [], "is_configured": False}

    try:
        out = subprocess.run(
            ["gh", "api", f"repos/{fork}/git/trees/HEAD?recursive=1",
             "--jq", '[.tree[] | select(.type == "blob") | .path]'],
            capture_output=True, text=True, timeout=30
        )
        stdout = out.stdout.strip()

        if out.returncode != 0 or not stdout or stdout.startswith("{"):
            # Check for error
            if "Not Found" in out.stderr or "Not Found" in stdout or "empty" in stdout.lower():
                r["status"] = "no_tree"
                return r
            # Try parsing as error JSON
            try:
                err = json.loads(stdout)
                if err.get("message") in ("Not Found", "Git Repository is empty"):
                    r["status"] = "no_tree"
                    return r
            except:
                pass
            r["status"] = "no_tree"
            return r

        try:
            paths = json.loads(stdout)
        except:
            r["status"] = "no_tree"
            return r

        if not isinstance(paths, list):
            r["status"] = "no_tree"
            return r

        skill_dirs = set()
        for p in paths:
            if p.startswith("skills/"):
                parts = p.split("/")
                if len(parts) >= 2:
                    skill_dirs.add(parts[1])

        fork_only = skill_dirs - UPSTREAM_SKILLS
        r["fork_only_skills"] = sorted(fork_only)
        r["all_skill_dirs"] = sorted(skill_dirs)

        if "aeon.yml" not in paths:
            r["status"] = "no_aeon_yml"
            r["is_configured"] = bool(fork_only)
            return r

        # Fetch aeon.yml
        yml_out = subprocess.run(
            ["gh", "api", f"repos/{fork}/contents/aeon.yml", "--jq", ".content"],
            capture_output=True, text=True, timeout=30
        )
        if yml_out.returncode != 0:
            r["status"] = "yml_unreadable"
            return r

        content_b64 = yml_out.stdout.strip().replace("\\n", "").replace("\n", "")
        try:
            content = base64.b64decode(content_b64).decode("utf-8")
        except:
            r["status"] = "yml_unreadable"
            return r

        # Extract enabled skills from aeon.yml
        enabled = []
        for line in content.split("\n"):
            m = re.match(r'^\s{2}([a-zA-Z0-9_-]+):\s*\{.*enabled:\s*true', line)
            if m:
                enabled.append(m.group(1))

        r["status"] = "ok"
        r["enabled_skills"] = enabled
        r["content"] = content

        # Divergence from upstream
        enabled_set = set(enabled)
        enabled_diff = len(enabled_set.symmetric_difference(UPSTREAM_DEFAULTS_ENABLED))

        # Check model/var/schedule overrides (simplified)
        has_model_override = bool(re.search(r'model:\s*"', content))
        has_var_set = bool(re.search(r'var:\s*"[^"]+', content))
        has_schedule_override = False  # complex to check inline

        r["is_configured"] = (enabled_diff > 0 or has_model_override or has_var_set or bool(fork_only))
        r["enabled_diff"] = enabled_diff

        return r

    except subprocess.TimeoutExpired:
        r["status"] = "timeout"
        return r
    except Exception as e:
        r["status"] = f"error: {e}"
        return r

results = []
for i, fork in enumerate(ALL_FORKS):
    print(f"[{i+1}/{len(ALL_FORKS)}] {fork}...", file=sys.stderr)
    r = fetch_fork(fork)
    results.append(r)
    status_str = r["status"]
    enabled = r.get("enabled_skills", [])
    configured = r.get("is_configured", False)
    fork_only = r.get("fork_only_skills", [])
    print(f"  status={status_str}, enabled={enabled[:5]}, configured={configured}, fork_only={fork_only[:3]}")

print("\n=== SUMMARY ===")
configured = [r for r in results if r.get("is_configured")]
template = [r for r in results if r["status"] == "ok" and not r.get("is_configured")]
unreadable = [r for r in results if r["status"] in ("no_tree", "yml_unreadable", "timeout", "no_aeon_yml") and not r.get("is_configured")]
print(f"Total active: {len(results)}")
print(f"Configured: {len(configured)}")
print(f"Template: {len(template)}")
print(f"Unreadable/no_tree: {len(unreadable)}")

# Save results to a temp file
with open("/tmp/skill-lb-results.json", "w") as f:
    json.dump(results, f, indent=2)
print("\nResults saved to /tmp/skill-lb-results.json")
