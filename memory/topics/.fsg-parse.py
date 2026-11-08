import sys, base64, json

data = base64.b64decode(sys.stdin.read().strip()).decode()
skills = json.loads(data)['skills']
print(f'TOTAL:{len(skills)}')
for s in skills:
    slug = s['slug']
    cat = s.get('category', 'other')
    updated = s.get('updated', '')
    print(f'{slug}\t{cat}\t{updated}')
