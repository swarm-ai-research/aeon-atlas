from datetime import datetime, timezone
import re, os, sys

today = datetime(2026, 11, 9, 8, 0, 0, tzinfo=timezone.utc)
now_ts = today.timestamp()
base = '/home/runner/work/aeon-atlas/aeon-atlas'

article_files = os.listdir(os.path.join(base, 'articles'))
outputs_files = os.listdir(os.path.join(base, '.outputs'))
topics_files = os.listdir(os.path.join(base, 'memory/topics'))

producer_latest = {}
for f in article_files:
    m = re.match(r'^([a-zA-Z0-9_-]+?)-(\d{4}-\d{2}-\d{2})\.md$', f)
    if m:
        producer, date_str = m.group(1), m.group(2)
        file_dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        age_hours = (now_ts - file_dt.timestamp()) / 3600
        if producer not in producer_latest or file_dt > producer_latest[producer][1]:
            producer_latest[producer] = (f, file_dt, age_hours)

print("=== Most recent article per producer ===")
for prod, (fname, dt, age) in sorted(producer_latest.items()):
    print("  %s: %s (%.0fh old)" % (prod, fname, age))

enabled_skills = {
    'skill-health': 'daily',
    'api-health-probe': 'daily',
    'ai-framework-watch': 'weekly',
    'ecosystem-pulse': 'weekly',
    'fleet-state': 'weekly',
    'fork-cohort': 'weekly',
    'fork-release-tracker': 'weekly',
    'contributor-spotlight': 'weekly',
    'fork-first-run-alert': 'daily',
    'skill-evals': 'weekly',
    'skill-update-check': 'weekly',
    'fleet-scorecard': 'daily',
    'skill-leaderboard': 'weekly',
    'fork-contributor-leaderboard': 'weekly',
    'operator-scorecard': 'weekly',
    'follow-up-patrol': 'weekly',
    'fork-skill-digest': 'weekly',
    'fork-skill-gap': 'weekly',
    'fleet-skill-adoption': 'weekly',
    'fork-health-score': 'weekly',
    'workflow-security-audit': 'weekly',
    'atlas': 'weekly',
    'atlas-layers': 'weekly',
    'atlas-improve': 'on_demand',
    'skill-freshness': 'daily',
    'heartbeat': 'daily',
}

print("\n=== Enabled skills with no articles ===")
for skill, cadence in sorted(enabled_skills.items()):
    if skill not in producer_latest and cadence != 'on_demand':
        print("  NO_ARTICLE: %s (cadence: %s)" % (skill, cadence))

print("\n=== .outputs files ===")
for f in sorted(outputs_files):
    if not f.startswith('.gitkeep') and not f.endswith('.py'):
        fp = os.path.join(base, '.outputs', f)
        mtime = os.path.getmtime(fp)
        age_h = (now_ts - mtime) / 3600
        print("  %s: %.1fh old (mtime)" % (f, age_h))

print("\n=== memory/topics files ===")
for f in sorted(topics_files):
    if not f.startswith('.gitkeep') and not f.startswith('.fsg') and f.endswith(('.md', '.json')):
        fp = os.path.join(base, 'memory/topics', f)
        mtime = os.path.getmtime(fp)
        age_h = (now_ts - mtime) / 3600
        print("  %s: %.1fh old (mtime)" % (f, age_h))
