import json
import re
from datetime import datetime
import os

with open('db.json', 'r') as f:
    data = json.load(f)

posts = data['models']['Post']
post_dates = {}
for post in posts:
    slug = post['slug']
    date_str = post['date']
    dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    formatted_date = dt.strftime('%Y-%m-%d %H:%M:%S')
    post_dates[slug] = formatted_date

for slug, date in post_dates.items():
    file_path = f"source/_posts/{slug}.md"
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'date:' in content:
            content = re.sub(r'date:\s*[^\n]*', f'date: {date}', content)
        else:
            content = re.sub(r'---\n', f'---\ndate: {date}\n', content, count=1)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {slug}: {date}")

print("Done!")