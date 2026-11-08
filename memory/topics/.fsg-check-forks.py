#!/usr/bin/env python3
"""
Check which forks are POWER+ACTIVE (workflow run in last 7d)
and read their skills.json gaps vs upstream slugs.
Outputs JSON to stdout.
"""
import subprocess, json, sys
from datetime import datetime, timezone

UPSTREAM_SLUGS = set("""action-converter agent-buzz agent-displacement ai-framework-watch aixbt-pulse article auto-merge auto-workflow autoresearch batch-health builder-map changelog channel-recap code-health competitor-launch-radar compute-pulse config-validator contract-audit contributor-reward contributor-spotlight cost-report create-campaign create-skill daily-routine deal-flow deep-research defi-monitor defi-overview deploy-prototype deployer-trace digest disclosure-tracker distribute-tokens ecosystem-pulse engagement-act evening-recap external-feature farcaster-digest feature fetch-tweets fleet-control fleet-scorecard fleet-skill-adoption fleet-state follow-up-patrol fork-cohort fork-contributor-leaderboard fork-first-run-alert fork-fleet fork-health-score fork-release-tracker fork-skill-digest fork-skill-gap github-issues github-monitor github-releases github-trending goal-tracker hacker-news-digest heartbeat holder-concentration huggingface-trending idea-capture idea-pipeline idea-validator issue-triage janitor last30 launch-radar list-digest market-context-refresh mcp-pulse memory-flush memory-structural-dedupe milestone-tracker monitor-kalshi monitor-polymarket monitor-runners morning-brief narrative-convergence narrative-tracker note-taking on-chain-monitor onboard operator-scorecard paper-digest paper-pick pm-intel pm-manipulation pm-pulse polymarket polymarket-comments pr-review pr-skill-triage pr-tracker pr-triage price-threshold-alert product-hunt-launch project-lens push-recap pvr-triage-monitor pvr-watchlist reddit-digest reflect refresh-x reg-monitor remix-tweets reply-maker repo-actions repo-article repo-pulse repo-revive repo-scanner research-brief rss-digest rss-feed rug-scan run-frequency-guard rwa-pulse schedule-ads search-skill security-digest self-improve self-review show-hn-draft signal-verdict skill-analytics skill-enabler skill-evals skill-freshness skill-graph skill-health skill-leaderboard skill-repair skill-security-scan skill-update-check smithery-manifest sparkleware-catalog spawn-instance spend-monitor star-milestone star-momentum-alert startup-idea syndicate-article technical-explainer telegram-digest thread-formatter token-alert token-movers token-pick token-report tool-builder topic-momentum treasury-info tweet-digest tweet-roundup tx-explain unlock-monitor update-gallery v4-readiness vercel-projects vibecoding-digest vuln-scanner vuln-tracker wallet-digest wallet-profile weekly-review weekly-shiplog workflow-security-audit write-tweet x402-monitor""".split())

# Bot owners to skip
BOT_OWNERS = {'dependabot[bot]', 'github-actions[bot]', 'aeonframework[bot]'}

NOW = datetime.now(timezone.utc)
CUTOFF_7D = (NOW.timestamp() - 7 * 86400)

def gh_api(path, default=None):
    try:
        r = subprocess.run(['gh', 'api', path], capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            return default
        return json.loads(r.stdout)
    except Exception:
        return default

def check_fork_active(fork_name):
    """Returns last_run_ts or None"""
    data = gh_api(f'repos/{fork_name}/actions/runs?per_page=1')
    if not data or not data.get('workflow_runs'):
        return None
    run = data['workflow_runs'][0]
    updated = run.get('updated_at', '')
    if not updated:
        return None
    try:
        ts = datetime.fromisoformat(updated.replace('Z', '+00:00')).timestamp()
        return ts
    except Exception:
        return None

def get_fork_skills(fork_name):
    """Returns (slugs_set, unreadable, reason)"""
    data = gh_api(f'repos/{fork_name}/contents/skills.json')
    if not data or 'content' not in data:
        return set(), True, '404'
    try:
        import base64
        content = base64.b64decode(data['content']).decode()
        skills = json.loads(content).get('skills', [])
        slugs = set(s['slug'] for s in skills)
        return slugs, False, ''
    except Exception as e:
        return set(), True, f'parse-error:{e}'

def category_rollup(missing_slugs, cat_map):
    from collections import Counter
    cats = Counter()
    for slug in missing_slugs:
        cat = cat_map.get(slug, 'other')
        cats[cat] += 1
    return cats.most_common(3)

# Forks to check: previously active + new candidates
FORKS_TO_CHECK = [
    # Previously active (from last state)
    'nigelon11/aeon',
    'Boodszw/Boodszw_Bread',
    'madebyshun/blueagent-aeon',
    'damo-nu11/aeon-minebean',
    'lawbworld-tech/aeon',
    'youpsla/aeon',
    'gitlumen-team/aeon',
    'richard7463/aeon',
    'NurstarK/aeon-upstream',
    'beijiangqukuailian/aeon',
    'ashneil12/aeon-upstream',
    'aeoncity-hub/aeon',
    # New candidates from current fork list
    'wtfsayo/aeon',
    'yusasecurity/aeon',
    'SorenMoussavian/SorenOS-Aeon',
    'caigen18/aeon',
    'ardy03851-bit/aeon',
    'duan521127/aeon',
    'shubu258/aeon',
    'Tunn3l/aeon-tunn3l',
    'vaubandev/aeon',
    'TReinaCOM/aeon',
    'dajiaohuang/aeonfun-aeon',
    'inginjadipro/aeonfun-aeon',
    'repoken/aeon',
    'AragAgg/aeon',
    'sentinelhood/aeon',
    '0xAnvesaka/aeon',
    'nhutminh159/aeon-nhutminh159',
    'unifirer/aeon',
    'rikomuslimnur1001/aeon-rikomuslimnur1001',
    'divyesh54/aeon',
    'djh4ck3r/aeon',
    'CHEYCKIT/aeon',
    'Domimueller85/aeon',
    'Blockchains/aeon',
    'nkipa/aeon',
    'mardemsean/aeon-autonomous-agent-platform',
    'googio/aeon',
    'super-ai-8453/aeon',
    'Secure-Code-Pro-Zyloch/aeon',
    'Oscar-Williams/aeon',
    'brainsparker/aeon',
    'Ditto190/aeon-automaton-modme',
    'rohitctrl/aeon',
    'Corykidios/aeon',
    'iamziek/aeon',
    'niu12503/aeon',
    '0xsnackbaker/aeon',
    'Pinont/aeon.fun',
    'corinth1ans/aeon',
    'krpx0341/aeon',
    'darkstaryuri/aeon',
    'cyborganeh/aeon',
    'Jason9720/aeon',
    'dipanshuhappy/aeon',
    'forumchen388-debug/aeon',
    'keyurbodar/aeon',
    'MADRIGAL007/aeon',
    'elegarmco/aeon',
    'Calcutatator/aeon',
    'cultosagent/aeon',
    'jsfranklin221/aeon',
    'thesmithdao/aeon',
    'kevin-houston/aeon',
    'theia-ttista/aeon',
    'hansj73/aeon',
    'kyleobrien91/aeon',
    'Kodawari10/aeon',
    'use-agent-os/aeon',
    'kajr0s/aeon',
    'thanhdat3007-create/aeon',
    'JDMD21/aeon',
    'czijian729-oss/aeon',
    'pkhr/aeon',
    'pablorq/aeon',
    'Cristian35s/aeon',
    'robertluciu-wq/aeon',
    'yghffhgx/aeon',
    'Akshmit/aeon',
    'kdegeek/aeon',
    'evrimulgen/aeon',
    'carsam2021/aeon',
    'dacode-dev/aeon',
    'raul1stdigital/aeon',
    'sysvhurtstop/susfux',
    'amritmirch/aeon',
    'hatari07/aeon',
    'MEMIX-AI/aeon',
    'Autonomy-Labs-Tech/aeon',
    'AwesomeAgentTools/aeon',
    'kairunedev/aeon',
    'edsonmartins/aeon',
    'olanotolu/aeon',
    'nickmimic/aeon',
    'LUKES254/aeon--ai-agent',
    'JessieJanie/aeon',
]

active_forks = []
inactive_count = 0
errors = 0

print("Checking fork activity...", file=sys.stderr)
for fork in FORKS_TO_CHECK[:80]:  # cap at 80
    owner = fork.split('/')[0]
    if owner in BOT_OWNERS:
        continue
    ts = check_fork_active(fork)
    if ts and ts > CUTOFF_7D:
        active_forks.append(fork)
        print(f"  ACTIVE: {fork}", file=sys.stderr)
    else:
        inactive_count += 1

print(f"\nActive: {len(active_forks)}, Inactive: {inactive_count}", file=sys.stderr)
print("Fetching skills.json for active forks...", file=sys.stderr)

# Build category map from upstream
CAT_MAP = {}  # slug -> category — will be populated from the already-known upstream data

results = {}
for fork in active_forks:
    slugs, unreadable, reason = get_fork_skills(fork)
    if unreadable:
        results[fork] = {
            'missing_count': None,
            'missing_slugs': [],
            'top_missing_categories': [],
            'unreadable': True,
            'unreadable_reason': reason,
        }
    else:
        missing = sorted(UPSTREAM_SLUGS - slugs)
        results[fork] = {
            'missing_count': len(missing),
            'missing_slugs': missing[:50],
            'top_missing_categories': [],
            'unreadable': False,
        }

print(json.dumps({'active_forks': active_forks, 'results': results}))
