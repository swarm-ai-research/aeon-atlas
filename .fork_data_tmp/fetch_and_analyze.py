#!/usr/bin/env python3 -I
"""Fetch aeon.yml from all forks and analyze divergence."""

import subprocess
import json
import os
import re
from collections import defaultdict, Counter
import math

FORKS = [
    "Skalda555/aeon", "ukiyo-p/aeon", "CamillaTeston/aeon", "Nickforall/aeon",
    "Bastiansure/aeon-bastiansure", "itsablabla/aeon", "aeonone/aeon-aeonone",
    "susilo77/aeon-susilo77", "opencolin/aeon", "domosta/aeon",
    "SuperFluouss/aeon-superfluouss", "chandras19349/aeon", "mohammadi0011/aeon",
    "Metroxe/aeon", "hypurr-inc/aeon", "wtfsayo/aeon", "yusasecurity/aeon",
    "SorenMoussavian/SorenOS-Aeon", "caigen18/aeon", "ardy03851-bit/aeon",
    "duan521127/aeon", "shubu258/aeon", "Tunn3l/aeon-tunn3l",
    "njfyanf9-a11y/aeon-njfyanf9-a11y", "vaubandev/aeon", "TReinaCOM/aeon",
    "airdropia/aeon", "o8613844-cpu/aeon-o8613844-cpu", "icepy/aeon-token",
    "moosebizlab/aeon", "xiaozz8/aeon", "00288/aeon", "AragAgg/aeon",
    "mervwtf/aeon-mervwtf", "sentinelhood/aeon", "FggDarkOnee420/Fgg-aeon",
    "0xAnvesaka/aeon", "nhutminh159/aeon-nhutminh159", "gelo11/aeon",
    "rauhaton/aeon-rauhaton", "unifirer/aeon", "stevenclaus00/aeon-AIGUY",
    "Svector-anu/aeon", "normancomics/aeon", "Domimueller85/aeon",
    "Kodawari10/aeon", "alexverify/aeon", "enuno/noesis-aeon",
    "anondevv69/bankr-space-aeon", "NurstarK/aeon-upstream", "beijiangqukuailian/aeon",
    "swarm-ai-research/aeon-atlas", "AIRYDER/aeon", "richard7463/aeon",
    "lawbworld-tech/aeon", "youpsla/aeon", "damo-nu11/aeon-minebean",
    "madebyshun/blueagent-aeon", "traewang/aeon-contrib", "Boodszw/Boodszw_Bread",
    "ether-btc/aeon",
]

def fetch_aeon_yml(fork):
    """Fetch and decode aeon.yml from a fork."""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{fork}/contents/aeon.yml", "--jq", ".content"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0 or not result.stdout.strip() or result.stdout.strip() == "null":
            return None, "no_aeon_yml"
        import base64
        try:
            content = base64.b64decode(result.stdout.strip()).decode("utf-8")
            return content, "ok"
        except Exception:
            return None, "decode_fail"
    except subprocess.TimeoutExpired:
        return None, "timeout"
    except Exception as e:
        return None, f"error:{e}"

def parse_skills_simple(yml_text):
    """Parse skills section from aeon.yml text. Returns dict of skill_name -> {enabled, model, var, schedule}."""
    skills = {}
    # Find the skills: section
    in_skills = False
    model_default = None

    # Try to extract default model
    m = re.search(r'^model:\s*([^\s#\n]+)', yml_text, re.MULTILINE)
    if m:
        model_default = m.group(1).strip()

    # Parse skill lines - they look like:
    # skill-name: { enabled: true/false, schedule: "...", model: "...", var: "..." }
    # or on multiple lines

    # Simple regex approach for inline skill definitions
    skill_pattern = re.compile(
        r'^\s{2,4}([\w-]+):\s*\{([^}]+)\}',
        re.MULTILINE
    )

    for m in skill_pattern.finditer(yml_text):
        skill_name = m.group(1)
        body = m.group(2)

        # Check if we're in the skills section (look for 'skills:' before this)
        pos = m.start()
        preceding = yml_text[:pos]
        if 'skills:' not in preceding:
            continue
        # Also skip if we're in chains: or reactive: section
        # Find the last section header before this skill
        section_matches = list(re.finditer(r'^(skills|reactive|chains|model|gateway|channels|telegram):', preceding, re.MULTILINE))
        if section_matches and section_matches[-1].group(1) != 'skills':
            continue

        entry = {}

        # enabled
        em = re.search(r'enabled:\s*(true|false)', body)
        if em:
            entry['enabled'] = em.group(1) == 'true'

        # model
        mm = re.search(r'model:\s*["\']?([^\s,"\'\}#]+)["\']?', body)
        if mm:
            entry['model'] = mm.group(1).strip().strip('"\'')

        # var
        vm = re.search(r'var:\s*["\']([^"\']*)["\']', body)
        if vm:
            entry['var'] = vm.group(1)
        else:
            vm2 = re.search(r'var:\s*(\S+)', body)
            if vm2:
                val = vm2.group(1).rstrip(',').strip('"\'')
                entry['var'] = val

        # schedule
        sm = re.search(r'schedule:\s*["\']([^"\']+)["\']', body)
        if sm:
            entry['schedule'] = sm.group(1)

        skills[skill_name] = entry

    return skills, model_default

def get_upstream_defaults():
    """Read upstream aeon.yml and extract defaults."""
    with open('/home/runner/work/aeon-atlas/aeon-atlas/aeon.yml') as f:
        content = f.read()
    return parse_skills_simple(content)

def get_upstream_skills():
    """Get list of skill directory names."""
    skills_dir = '/home/runner/work/aeon-atlas/aeon-atlas/skills'
    return set(d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d)))

def get_skill_tags():
    """Read tags from SKILL.md frontmatter for each skill."""
    tags = {}
    skills_dir = '/home/runner/work/aeon-atlas/aeon-atlas/skills'
    for skill in os.listdir(skills_dir):
        skill_md = os.path.join(skills_dir, skill, 'SKILL.md')
        if os.path.exists(skill_md):
            try:
                with open(skill_md) as f:
                    content = f.read(500)
                # Parse frontmatter tags
                m = re.search(r'^tags:\s*\[([^\]]*)\]', content, re.MULTILINE)
                if m:
                    tag_list = [t.strip() for t in m.group(1).split(',')]
                    tags[skill] = tag_list
                else:
                    tags[skill] = []
            except Exception:
                tags[skill] = []
        else:
            tags[skill] = []
    return tags

def compute_fingerprint_category(fork_skills, upstream_skills, skill_tags):
    """Determine dominant category for a fork."""
    tag_counts = defaultdict(int)
    for skill, settings in fork_skills.items():
        if not settings.get('enabled', False):
            continue
        if skill in upstream_skills:
            for tag in skill_tags.get(skill, []):
                tag_counts[tag] += 1
        else:
            tag_counts['fork-only'] += 1

    if not tag_counts:
        return 'mixed', dict(tag_counts)

    total_enabled = sum(tag_counts.values())
    max_tag = max(tag_counts, key=lambda t: tag_counts[t])
    if tag_counts[max_tag] / total_enabled > 0.40:
        return max_tag, dict(tag_counts)
    return 'mixed', dict(tag_counts)

def main():
    print("Loading upstream defaults...")
    upstream_skills_data, upstream_model = get_upstream_defaults()
    upstream_skills = get_upstream_skills()
    skill_tags = get_skill_tags()

    print(f"Upstream: {len(upstream_skills_data)} skills, default model: {upstream_model}")

    # Fetch all forks
    print(f"Fetching {len(FORKS)} forks...")
    fork_results = {}
    for i, fork in enumerate(FORKS):
        print(f"  [{i+1}/{len(FORKS)}] {fork}")
        content, status = fetch_aeon_yml(fork)
        fork_results[fork] = {'content': content, 'status': status}

    # Parse each fork
    print("\nParsing fork configs...")
    fork_data = {}
    n_ok = 0
    n_no_yml = 0
    n_invalid = 0

    for fork, result in fork_results.items():
        if result['status'] != 'ok' or not result['content']:
            fork_data[fork] = {'tier': 'UNREADABLE', 'status': result['status'], 'skills': {}}
            n_no_yml += 1
            continue

        try:
            skills, fork_model = parse_skills_simple(result['content'])
            fork_data[fork] = {
                'tier': None,  # determined later
                'status': 'ok',
                'skills': skills,
                'default_model': fork_model,
            }
            n_ok += 1
        except Exception as e:
            fork_data[fork] = {'tier': 'UNREADABLE', 'status': f'yml_invalid:{e}', 'skills': {}}
            n_invalid += 1

    print(f"Parsed: {n_ok} ok, {n_no_yml} no_yml, {n_invalid} invalid")

    # Tier each fork: compare vs upstream defaults
    print("\nTiering forks...")
    for fork, data in fork_data.items():
        if data['tier'] == 'UNREADABLE':
            continue

        fork_skills = data['skills']
        fork_model = data.get('default_model')
        has_divergence = False

        enabled_diff = 0
        var_overrides = 0
        model_overrides = 0
        schedule_overrides = 0
        fork_only_count = 0

        for skill_name, fork_settings in fork_skills.items():
            if skill_name not in upstream_skills_data:
                # Fork-only skill
                if skill_name in upstream_skills:
                    pass  # upstream skill not in aeon.yml defaults - shouldn't happen
                else:
                    fork_only_count += 1
                    has_divergence = True
                continue

            upstream = upstream_skills_data[skill_name]

            # enabled diff
            if 'enabled' in fork_settings:
                upstream_enabled = upstream.get('enabled', False)
                if fork_settings['enabled'] != upstream_enabled:
                    enabled_diff += 1
                    has_divergence = True

            # var override
            if 'var' in fork_settings:
                upstream_var = upstream.get('var', '')
                if fork_settings['var'] != upstream_var and fork_settings['var']:
                    var_overrides += 1
                    has_divergence = True

            # model override
            if 'model' in fork_settings:
                upstream_model_for_skill = upstream.get('model', upstream_model)
                if fork_settings['model'] != upstream_model_for_skill:
                    model_overrides += 1
                    has_divergence = True

            # schedule override
            if 'schedule' in fork_settings:
                upstream_schedule = upstream.get('schedule', '')
                if fork_settings['schedule'] != upstream_schedule:
                    schedule_overrides += 1
                    has_divergence = True

        # Also check default model divergence
        if fork_model and fork_model != upstream_model:
            has_divergence = True

        data['enabled_diff'] = enabled_diff
        data['var_overrides'] = var_overrides
        data['model_overrides'] = model_overrides
        data['schedule_overrides'] = schedule_overrides
        data['fork_only_count'] = fork_only_count
        data['total_overrides'] = enabled_diff + var_overrides + model_overrides + schedule_overrides + fork_only_count

        if has_divergence or data['total_overrides'] > 0:
            data['tier'] = 'CONFIGURED'
        else:
            data['tier'] = 'TEMPLATE'

    configured_forks = {f: d for f, d in fork_data.items() if d['tier'] == 'CONFIGURED'}
    template_forks = {f: d for f, d in fork_data.items() if d['tier'] == 'TEMPLATE'}
    unreadable_forks = {f: d for f, d in fork_data.items() if d['tier'] == 'UNREADABLE'}

    N_CONFIGURED = len(configured_forks)
    N_TEMPLATE = len(template_forks)
    N_UNREADABLE = len(unreadable_forks)
    N_ACTIVE = len(FORKS)

    print(f"\nFleet: {N_CONFIGURED} configured, {N_TEMPLATE} template, {N_UNREADABLE} unreadable")

    if N_CONFIGURED < 2:
        print("N_CONFIGURED < 2 — FORK_SKILL_DIGEST_TEMPLATE_FLEET")
        result = {
            'status': 'FORK_SKILL_DIGEST_TEMPLATE_FLEET',
            'n_active': N_ACTIVE, 'n_configured': N_CONFIGURED,
            'n_template': N_TEMPLATE, 'n_unreadable': N_UNREADABLE,
        }
        with open('/home/runner/work/aeon-atlas/aeon-atlas/.fork_data_tmp/digest_result.json', 'w') as f:
            json.dump(result, f, indent=2)
        return

    # Aggregate divergence
    print("\nAggregating divergence signals...")

    # For each upstream skill, count how many CONFIGURED forks enable/disable it
    skill_enable_counts = defaultdict(int)   # forks that set enabled:true (when upstream is false)
    skill_disable_counts = defaultdict(int)  # forks that set enabled:false (when upstream is true)
    skill_var_values = defaultdict(list)
    skill_model_values = defaultdict(list)
    skill_schedule_values = defaultdict(list)

    for fork, data in configured_forks.items():
        fork_skills = data['skills']
        for skill_name in upstream_skills_data:
            if skill_name not in fork_skills:
                continue
            fork_settings = fork_skills[skill_name]
            upstream = upstream_skills_data[skill_name]

            # enabled
            if 'enabled' in fork_settings:
                upstream_enabled = upstream.get('enabled', False)
                fork_enabled = fork_settings['enabled']
                if not upstream_enabled and fork_enabled:
                    skill_enable_counts[skill_name] += 1
                elif upstream_enabled and not fork_enabled:
                    skill_disable_counts[skill_name] += 1

            # var
            if 'var' in fork_settings and fork_settings['var']:
                upstream_var = upstream.get('var', '')
                if fork_settings['var'] != upstream_var:
                    skill_var_values[skill_name].append(fork_settings['var'])

            # model
            if 'model' in fork_settings:
                upstream_model_for_skill = upstream.get('model', upstream_model)
                if fork_settings['model'] != upstream_model_for_skill:
                    skill_model_values[skill_name].append(fork_settings['model'])

            # schedule
            if 'schedule' in fork_settings:
                upstream_schedule = upstream.get('schedule', '')
                if fork_settings['schedule'] != upstream_schedule:
                    skill_schedule_values[skill_name].append(fork_settings['schedule'])

    # Also collect fork-only skills
    fork_only_skills = []
    for fork, data in fork_data.items():
        for skill_name in data['skills']:
            if skill_name not in upstream_skills_data and skill_name not in upstream_skills:
                fork_only_skills.append({'fork': fork, 'skill': skill_name})

    # Meta/dev tagged skills to exclude from DEFAULT_FLIP_ENABLE
    meta_skills = set()
    dev_skills = set()
    for skill, tags_list in skill_tags.items():
        if 'meta' in tags_list:
            meta_skills.add(skill)
        if 'dev' in tags_list:
            dev_skills.add(skill)

    # Workflow dispatch skills
    dispatch_skills = {s for s, v in upstream_skills_data.items() if v.get('schedule') == 'workflow_dispatch'}

    print(f"Meta skills: {len(meta_skills)}, dispatch skills: {len(dispatch_skills)}")

    # Categorize skills
    buckets = {
        'DEFAULT_FLIP_ENABLE': [],
        'DEFAULT_FLIP_DISABLE': [],
        'MODEL_CONSENSUS': [],
        'VAR_HOTSPOT': [],
        'EMERGING': [],
    }

    model_threshold = max(2, math.ceil(N_CONFIGURED * 0.40))
    var_threshold = max(2, math.ceil(N_CONFIGURED * 0.30))

    # Build skill divergence data
    skill_divergence = {}
    all_upstream_skill_names = set(upstream_skills_data.keys())

    for skill_name in all_upstream_skill_names:
        upstream = upstream_skills_data[skill_name]
        upstream_enabled = upstream.get('enabled', False)

        en_count = skill_enable_counts.get(skill_name, 0)
        dis_count = skill_disable_counts.get(skill_name, 0)
        var_count = len(skill_var_values.get(skill_name, []))
        model_count = len(skill_model_values.get(skill_name, []))
        schedule_count = len(skill_schedule_values.get(skill_name, []))

        if en_count == 0 and dis_count == 0 and var_count == 0 and model_count == 0 and schedule_count == 0:
            continue

        if upstream_enabled:
            divergence_pct = dis_count / N_CONFIGURED
            direction = 'DISABLE_DOWNWARD'
        else:
            divergence_pct = en_count / N_CONFIGURED
            direction = 'ENABLE_UPWARD'

        skill_divergence[skill_name] = {
            'upstream_enabled': upstream_enabled,
            'en_count': en_count,
            'dis_count': dis_count,
            'var_count': var_count,
            'model_count': model_count,
            'schedule_count': schedule_count,
            'divergence_pct': divergence_pct,
            'direction': direction,
        }

    # Classify into buckets (priority order)
    categorized = set()

    # DEFAULT_FLIP_ENABLE
    for skill_name, sd in skill_divergence.items():
        if skill_name in categorized:
            continue
        if (sd['direction'] == 'ENABLE_UPWARD'
                and sd['divergence_pct'] >= 0.50
                and skill_name not in dispatch_skills
                and skill_name not in meta_skills
                and skill_name not in dev_skills):
            buckets['DEFAULT_FLIP_ENABLE'].append({
                'skill': skill_name, 'forks': sd['en_count'], 'pct': sd['divergence_pct']
            })
            categorized.add(skill_name)

    # DEFAULT_FLIP_DISABLE
    for skill_name, sd in skill_divergence.items():
        if skill_name in categorized:
            continue
        if (sd['direction'] == 'DISABLE_DOWNWARD'
                and sd['divergence_pct'] >= 0.50
                and skill_name != 'heartbeat'
                and skill_name not in dispatch_skills):
            buckets['DEFAULT_FLIP_DISABLE'].append({
                'skill': skill_name, 'forks': sd['dis_count'], 'pct': sd['divergence_pct']
            })
            categorized.add(skill_name)

    # MODEL_CONSENSUS
    for skill_name, sd in skill_divergence.items():
        if skill_name in categorized:
            continue
        model_vals = skill_model_values.get(skill_name, [])
        if len(model_vals) >= model_threshold:
            counter = Counter(model_vals)
            top_model, top_count = counter.most_common(1)[0]
            if top_count >= model_threshold:
                buckets['MODEL_CONSENSUS'].append({
                    'skill': skill_name, 'model': top_model, 'forks': top_count
                })
                categorized.add(skill_name)

    # VAR_HOTSPOT
    for skill_name, sd in skill_divergence.items():
        if skill_name in categorized:
            continue
        var_vals = skill_var_values.get(skill_name, [])
        if len(var_vals) >= var_threshold:
            counter = Counter(var_vals)
            top_var, top_count = counter.most_common(1)[0]
            if top_count >= 2:
                buckets['VAR_HOTSPOT'].append({
                    'skill': skill_name, 'var': top_var, 'forks': top_count
                })
                categorized.add(skill_name)

    # EMERGING
    for skill_name, sd in skill_divergence.items():
        if skill_name in categorized:
            continue
        if (sd['direction'] == 'ENABLE_UPWARD'
                and 0.25 <= sd['divergence_pct'] < 0.50):
            buckets['EMERGING'].append({
                'skill': skill_name, 'pct': sd['divergence_pct'], 'forks': sd['en_count']
            })
            categorized.add(skill_name)

    # Sort buckets by pct/forks desc
    for bucket in buckets.values():
        bucket.sort(key=lambda x: x.get('forks', 0), reverse=True)

    print(f"\nBuckets:")
    for name, items in buckets.items():
        print(f"  {name}: {len(items)} items")
        for item in items[:3]:
            print(f"    {item}")

    # Per-fork fingerprints
    fingerprints = []
    for fork, data in configured_forks.items():
        dominant_cat, cat_counts = compute_fingerprint_category(
            data['skills'], upstream_skills, skill_tags
        )
        fingerprints.append({
            'fork': fork,
            'total_overrides': data.get('total_overrides', 0),
            'dominant_category': dominant_cat,
            'enabled_diff': data.get('enabled_diff', 0),
            'var_overrides': data.get('var_overrides', 0),
            'model_overrides': data.get('model_overrides', 0),
            'schedule_overrides': data.get('schedule_overrides', 0),
            'fork_only_count': data.get('fork_only_count', 0),
        })
    fingerprints.sort(key=lambda x: x['total_overrides'], reverse=True)
    top5 = fingerprints[:5]

    print(f"\nTop 5 customizers:")
    for fp in top5:
        print(f"  {fp['fork']}: {fp['total_overrides']} overrides, {fp['dominant_category']}")

    # Build appendix table (skills with any non-zero signal, sorted by total override count)
    appendix = []
    for skill_name, sd in skill_divergence.items():
        total_signal = sd['en_count'] + sd['dis_count'] + sd['var_count'] + sd['model_count'] + sd['schedule_count']
        appendix.append({
            'skill': skill_name,
            'enable_diff': sd['en_count'] + sd['dis_count'],
            'var_overrides': sd['var_count'],
            'model_overrides': sd['model_count'],
            'schedule_overrides': sd['schedule_count'],
            'total': total_signal,
        })
    appendix.sort(key=lambda x: x['total'], reverse=True)

    # Save result
    result = {
        'status': 'ok',
        'n_active': N_ACTIVE,
        'n_configured': N_CONFIGURED,
        'n_template': N_TEMPLATE,
        'n_unreadable': N_UNREADABLE,
        'buckets': buckets,
        'fork_only_skills': fork_only_skills[:80],
        'fingerprints': fingerprints,
        'top5': top5,
        'appendix': appendix[:40],
        'skill_divergence': {k: v for k, v in list(skill_divergence.items())[:100]},
    }

    with open('/home/runner/work/aeon-atlas/aeon-atlas/.fork_data_tmp/digest_result.json', 'w') as f:
        json.dump(result, f, indent=2)

    print(f"\nResult saved to .fork_data_tmp/digest_result.json")
    print(f"Fork-only skills: {len(fork_only_skills)}")
    print(f"Appendix skills: {len(appendix)}")


def compute_fingerprint_category(fork_skills, upstream_skills, skill_tags):
    """Determine dominant category for a fork."""
    tag_counts = defaultdict(int)
    for skill, settings in fork_skills.items():
        if not settings.get('enabled', False):
            continue
        if skill in upstream_skills:
            for tag in skill_tags.get(skill, []):
                tag_counts[tag] += 1
        else:
            tag_counts['fork-only'] += 1

    if not tag_counts:
        return 'mixed', dict(tag_counts)

    total_enabled = sum(tag_counts.values())
    max_tag = max(tag_counts, key=lambda t: tag_counts[t])
    if total_enabled > 0 and tag_counts[max_tag] / total_enabled > 0.40:
        return max_tag, dict(tag_counts)
    return 'mixed', dict(tag_counts)


if __name__ == '__main__':
    main()
