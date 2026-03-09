#!/usr/bin/env python3
import subprocess, json
from difflib import SequenceMatcher

# Get all issues
result = subprocess.run(
    ['gh', 'issue', 'list', '--limit', '200', '--json', 
     'number,title,body,labels,state', '--state', 'all'],
    capture_output=True, text=True
)
issues = json.loads(result.stdout)

print("🔍 CHECKING FOR DUPLICATES\n")
print("=" * 60)

# Check for duplicate titles
title_map = {}
for issue in issues:
    title = issue['title'].lower().strip()
    num = issue['number']
    if title not in title_map:
        title_map[title] = []
    title_map[title].append(num)

# Exact duplicates
exact_dups = {k: v for k, v in title_map.items() if len(v) > 1}

if exact_dups:
    print("❌ EXACT DUPLICATE TITLES:")
    for title, nums in exact_dups.items():
        print(f"\n  Title: '{title}'")
        print(f"  Issues: {nums}")
else:
    print("✅ No exact duplicate titles found")

# Check for similar titles (partial duplicates)
print("\n" + "=" * 60)
print("🔍 CHECKING FOR SIMILAR TITLES (>85% match)...")

similar = []
issue_list = [(i['number'], i['title'].lower().strip()) for i in issues]

for i in range(len(issue_list)):
    for j in range(i + 1, len(issue_list)):
        num1, title1 = issue_list[i]
        num2, title2 = issue_list[j]
        
        similarity = SequenceMatcher(None, title1, title2).ratio()
        
        if similarity > 0.85 and num1 != num2:
            similar.append((num1, title1, num2, title2, similarity))

if similar:
    print(f"\n⚠️  Found {len(similar)} potentially similar issues:\n")
    for num1, t1, num2, t2, sim in sorted(similar, key=lambda x: -x[4])[:20]:
        print(f"  #{num1} vs #{num2} ({sim*100:.0f}% similar)")
        print(f"    '{t1[:50]}...'")
        print(f"    '{t2[:50]}...'")
        print()
else:
    print("✅ No similar titles found")

# Check for duplicate content in body
print("\n" + "=" * 60)
print("🔍 CHECKING FOR DUPLICATE CONTENT IN BODY...")

body_map = {}
for issue in issues:
    body = (issue.get('body') or '').strip()[:100].lower()
    if body and len(body) > 20:
        num = issue['number']
        if body not in body_map:
            body_map[body] = []
        body_map[body].append(num)

body_dups = {k: v for k, v in body_map.items() if len(v) > 1}

if body_dups:
    print(f"\n⚠️  Found {len(body_dups)} issues with similar content:")
    for body, nums in body_dups.items():
        print(f"  Issues {nums}: '{body[:50]}...'")
else:
    print("✅ No duplicate content in body found")

print("\n" + "=" * 60)
print("✅ DUPLICATE CHECK COMPLETE")
