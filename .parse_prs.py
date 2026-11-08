import sys, json
from collections import defaultdict

with open('/home/runner/.claude/projects/-home-runner-work-aeon-atlas-aeon-atlas/ac0915a5-4e9d-4fcf-b1b1-d72ceaf44d5e/tool-results/b3afk5ghr.txt', 'r') as f:
    data = f.read()

prs = []
depth = 0
in_str = False
escape = False
start_pos = None

i = 0
while i < len(data):
    c = data[i]
    if escape:
        escape = False
    elif c == '\\' and in_str:
        escape = True
    elif c == '"' and not escape:
        in_str = not in_str
    elif not in_str:
        if c == '[':
            if depth == 0:
                start_pos = i
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0 and start_pos is not None:
                try:
                    chunk = json.loads(data[start_pos:i+1])
                    prs.extend(chunk)
                except Exception as e:
                    pass
                start_pos = None
    i += 1

BOT_FILTER = set(['aaronjmars', 'aeonframework', 'github-actions'])
filtered = []
for p in prs:
    u = p['user']
    if not u.endswith('[bot]') and u not in BOT_FILTER:
        filtered.append(p)

pr_map = defaultdict(lambda: {'opened': 0, 'merged': 0, 'first_time': False, 'pr_titles': []})
for p in filtered:
    u = p['user']
    pr_map[u]['opened'] += 1
    if p['merged_at']:
        pr_map[u]['merged'] += 1
    if p['author_association'] == 'FIRST_TIME_CONTRIBUTOR':
        pr_map[u]['first_time'] = True
    pr_map[u]['pr_titles'].append(p['title'])

result = {}
for k, v in pr_map.items():
    result[k] = dict(v)

with open('/home/runner/work/aeon-atlas/aeon-atlas/.pr_map.json', 'w') as f:
    json.dump(result, f)

# Print summary
sorted_items = sorted(result.items(), key=lambda x: (-x[1]['merged'], -x[1]['opened']))
for login, stats in sorted_items[:40]:
    ft = 'FT' if stats['first_time'] else ''
    print(f"{login}: merged={stats['merged']}, opened={stats['opened']} {ft}")
