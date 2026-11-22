import sys
from collections import defaultdict

pr_map = defaultdict(lambda: {'merged':0,'open':0,'unmerged_closed':0,'first_time':False})
for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) < 4:
        continue
    login, state, merge_status, assoc = parts
    if merge_status == 'merged':
        pr_map[login]['merged'] += 1
    elif state == 'open':
        pr_map[login]['open'] += 1
    else:
        pr_map[login]['unmerged_closed'] += 1
    if assoc == 'FIRST_TIME_CONTRIBUTOR':
        pr_map[login]['first_time'] = True

print('login\tmerged\topen\tunmerged_closed\tfirst_time')
for login, d in sorted(pr_map.items(), key=lambda x: -x[1]['merged']):
    print(f"{login}\t{d['merged']}\t{d['open']}\t{d['unmerged_closed']}\t{d['first_time']}")
print(f'---Total community logins: {len(pr_map)}')
