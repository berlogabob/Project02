# Daily Plan GitHub Action - Complete Documentation

## 🎯 Goal

Automatically generate personalized daily plan PDFs for each team member with:
- Date-prefixed filenames (e.g., `20260305-daily-plan-naydino.pdf`)
- Assigned GitHub issues
- Comments on issues
- Planning notes section
- Files committed to repository

---

## 📁 File Structure

```
Project02/
├── .github/
│   └── workflows/
│       └── daily-plans-v2.yml          # GitHub Action workflow
├── reports/
│   └── daily-plans/
│       ├── 20260305-daily-plan-naydino.typ
│       ├── 20260305-daily-plan-naydino.pdf
│       ├── 20260305-daily-plan-berlogabob.typ
│       ├── 20260305-daily-plan-berlogabob.pdf
│       ├── 20260305-daily-plan-electricianv001.typ
│       └── 20260305-daily-plan-electricianv001.pdf
└── scripts/
    └── generate_daily_plan.py          # Python generator script
```

---

## 🔧 Configuration

### Team Members
```python
TEAM_MEMBERS = {
    "naydino": "Nadine Allan",
    "berlogabob": "Andrey Dyakov",
    "electricianv001": "Dmitri Kazantsev"
}
```

### Schedule
- **When:** Every day at 00:00 UTC (02:00 Lisbon time)
- **Manual trigger:** Available via GitHub Actions UI

---

## 🚀 How to Run

### Automatic
Workflow runs automatically every day at 00:00 UTC.

### Manual
1. Go to: https://github.com/berlogabob/Project02/actions/workflows/daily-plans-v2.yml
2. Click **"Run workflow"**
3. Select branch: `main`
4. Click **"Run workflow"**
5. Wait 2-3 minutes
6. Check results in `reports/daily-plans/`

---

## 📊 Workflow Steps

```yaml
1. Checkout repository
2. Install Typst
3. Install GitHub CLI
4. Authenticate GitHub CLI
5. Set up Python
6. Install dependencies
7. Generate date stamp
8. Run Python script (generate daily plans)
9. Compile PDFs
10. Commit and push plans
11. Upload PDFs as artifacts
12. Upload TYP sources as artifacts
```

---

## 🐛 Issues Encountered & Solutions

### Issue 1: Typst Template Import Errors
**Problem:** `#import "template.typ"` caused file not found errors
**Solution:** Generate standalone Typst files without imports

### Issue 2: Python f-strings Breaking Typst Code
**Problem:** `{variable}` in Python f-strings conflicted with Typst syntax
**Solution:** Build Typst files line-by-line with proper escaping

### Issue 3: @username Interpreted as Typst Labels
**Problem:** `@naydino` created `<naydino>` labels in Typst
**Solution:** Replace `@` with `at ` in `escape_typst()` function

### Issue 4: Markdown Images in Comments
**Problem:** `![alt](url)` broke Typst compilation
**Solution:** Remove images with regex: `re.sub(r'!\[.*?\]\(.*?\)', '', text)`

### Issue 5: HTML Tags in Comments
**Problem:** `<img width="...">` caused errors
**Solution:** Remove HTML tags: `re.sub(r'<[^>]+>', '', text)`

### Issue 6: URLs in Comments
**Problem:** `https://...` broke compilation
**Solution:** Remove URLs: `re.sub(r'https?://\S+', '', text)`

### Issue 7: Typst `bold: true` Syntax
**Problem:** `bold: true` is invalid in Typst
**Solution:** Use `weight: "bold"` instead

### Issue 8: Filename Collisions
**Problem:** `daily-plan-naydino.pdf` overwritten daily
**Solution:** Add date prefix: `20260305-daily-plan-naydino.pdf`

---

## ✅ Working Code

### Python Script: `scripts/generate_daily_plan.py`

```python
#!/usr/bin/env python3
"""Daily Plan Generator - Clean Simple Version"""

import json
import subprocess
from datetime import datetime
from pathlib import Path
import re

TEAM_MEMBERS = {"naydino": "Nadine Allan", "berlogabob": "Andrey Dyakov", "electricianv001": "Dmitri Kazantsev"}
REPO = "berlogabob/Project02"

def get_issues(username):
    result = subprocess.run(
        ["gh", "issue", "list", "--state", "open", "--assignee", username, "--repo", REPO, "--limit", "50",
         "--json", "number,title,labels,milestone,body,comments"],
        capture_output=True, text=True
    )
    try:
        return json.loads(result.stdout)
    except:
        return []

def clean_text(text):
    if not text:
        return ""
    # Remove images, HTML, URLs
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'https?://\S+', '', text)
    # Replace @ with "at" to avoid Typst labels
    text = text.replace('@', 'at ')
    # Escape brackets
    return text.replace('[', '(').replace(']', ')').replace('\n', ' ')

def main():
    output_dir = Path("reports/daily-plans")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    date_prefix = datetime.now().strftime("%Y%m%d")
    date_str = datetime.now().strftime("%d/%m")
    
    for username, name in TEAM_MEMBERS.items():
        issues = get_issues(username)
        
        # Build Typst file
        lines = [
            f'// Daily Plan - {name} - {date_prefix}',
            '#set page(paper: "a4", margin: 50pt)',
            '#set text(size: 10pt)',
            '#let blue = rgb("#2F80ED")',
            '',
            '#align(center)[#text(size: 20pt, fill: blue, weight: "bold")[📅 Daily Plan]]',
            f'#align(center)[#text(size: 16pt)[{date_str}]]',
            f'#align(center)[#text(size: 14pt)[{name}]]',
            '',
            '#line(length: 100%)',
            '',
            f'#text(size: 12pt, weight: "bold")[Tasks: {len(issues)}]',
            '',
            '== Your Tasks',
            ''
        ]
        
        if not issues:
            lines.append('#text(size: 12pt, fill: green)[🎉 No tasks!]')
        else:
            for issue in issues:
                num = issue['number']
                title = clean_text(issue['title'])
                priority = ""
                for lbl in issue.get('labels', []):
                    if 'critical' in lbl.get('name', ''):
                        priority = " [CRITICAL]"
                    elif 'high' in lbl.get('name', ''):
                        priority = " [HIGH]"
                
                lines.append(f'=== #{num} - {title}{priority}')
                
                ms = issue.get('milestone', {})
                if ms and ms.get('title'):
                    lines.append(f'*Milestone:* {clean_text(ms["title"])}')
                
                labels = ', '.join([l['name'] for l in issue.get('labels', [])])
                if labels:
                    lines.append(f'*Labels:* {labels}')
                
                body = clean_text(issue.get('body', ''))
                if body:
                    lines.append(f'\n{body[:200]}')
                
                comments = issue.get('comments', [])[:2]
                if comments:
                    lines.append('\n*Comments:*')
                    for c in comments:
                        author = c.get('author', {}).get('login', 'Unknown')
                        cbody = clean_text(c.get('body', ''))[:100]
                        lines.append(f'- {author}: {cbody}')
                
                lines.append('')
        
        lines.extend([
            '',
            '#line(length: 100%)',
            '',
            '== Planning',
            '',
            '=== Goals',
            '- [ ] ',
            '',
            '=== Time Blocks',
            '| 09:00-10:00 | |',
            '| 10:00-11:00 | |',
            '| 11:00-12:00 | |',
            '| 12:00-13:00 | Lunch |',
            '| 13:00-14:00 | |',
            '| 14:00-15:00 | |',
            '| 15:00-16:00 | |',
            '| 16:00-17:00 | |',
            '',
            '=== Checklist',
            '- [ ] Update issues',
            '- [ ] Add comments',
            '- [ ] Push code',
            '- [ ] Plan tomorrow'
        ])
        
        # Write .typ file
        typ_file = output_dir / f"{date_prefix}-daily-plan-{username}.typ"
        typ_file.write_text('\n'.join(lines))
        
        # Compile to PDF
        pdf_file = output_dir / f"{date_prefix}-daily-plan-{username}.pdf"
        result = subprocess.run(["typst", "compile", str(typ_file), str(pdf_file)], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ PDF: {pdf_file.name}")
        else:
            print(f"❌ PDF failed: {result.stderr[:100]}")

if __name__ == "__main__":
    main()
```

### GitHub Action: `.github/workflows/daily-plans-v2.yml`

```yaml
name: Generate Daily Plans v2

on:
  schedule:
    - cron: "0 0 * * *"  # Every day at 00:00 UTC
  
  workflow_dispatch:
    inputs:
      member:
        description: "Specific member (leave empty for all)"
        required: false
        default: ""
        type: choice
        options:
          - ""
          - naydino
          - berlogabob
          - electricianv001

permissions:
  contents: write
  actions: write

jobs:
  generate-daily-plans:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Install Typst
        uses: typst-community/setup-typst@v3
        with:
          typst-version: "latest"
      
      - name: Install GitHub CLI
        run: |
          gh --version || sudo apt-get install -y gh
      
      - name: Authenticate GitHub CLI
        run: gh auth setup-git
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
      
      - name: Generate date stamp
        id: date
        run: |
          echo "date=$(date +'%Y-%m-%d')" >> $GITHUB_OUTPUT
      
      - name: Generate plans for all members
        if: ${{ github.event.inputs.member == '' }}
        run: |
          python3 scripts/generate_daily_plan.py
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Compile PDFs
        run: |
          cd reports/daily-plans
          for typ_file in *-daily-plan-*.typ; do
            pdf_file="${typ_file%.typ}.pdf"
            echo "Compiling $typ_file -> $pdf_file"
            typst compile "$typ_file" "$pdf_file" && echo "✅ $pdf_file" || echo "⚠️  Failed: $typ_file"
          done
          ls -la *-daily-plan-*.pdf 2>/dev/null || echo "No PDFs found"
      
      - name: Commit and push plans
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add reports/daily-plans/
          git commit -m "📅 Auto-generate daily plans: ${{ steps.date.outputs.date }}" || echo "No changes to commit"
          git push
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Upload PDFs as artifacts
        uses: actions/upload-artifact@v4
        with:
          name: daily-plans-pdf-${{ steps.date.outputs.date }}
          path: reports/daily-plans/*.pdf
          retention-days: 7
      
      - name: Upload TYP sources as artifacts
        uses: actions/upload-artifact@v4
        with:
          name: daily-plans-source-${{ steps.date.outputs.date }}
          path: reports/daily-plans/*.typ
          retention-days: 7
```

---

## 📦 Dependencies

- **Typst** v0.14.2+ (for PDF compilation)
- **GitHub CLI** (gh) (for fetching issues)
- **Python** 3.11+ (for script execution)

---

## 🔍 Troubleshooting

### PDF Compilation Fails
Check Typst syntax in generated `.typ` files:
```bash
typst compile reports/daily-plans/20260305-daily-plan-naydino.typ
```

### No Issues Found
Verify GitHub CLI authentication:
```bash
gh auth status
gh issue list --repo berlogabob/Project02
```

### Workflow Fails
Check Actions logs: https://github.com/berlogabob/Project02/actions

---

## 📊 Output Example

### Filename Format
```
YYYYMMDD-daily-plan-username.pdf
20260305-daily-plan-naydino.pdf
20260305-daily-plan-berlogabob.pdf
20260305-daily-plan-electricianv001.pdf
```

### PDF Contents
- Header with date and name
- Task count
- List of assigned issues with:
  - Issue number and title
  - Priority badges (CRITICAL, HIGH)
  - Milestone
  - Labels
  - Description
  - Recent comments
- Planning section with goals, time blocks, checklist

---

## 🎯 Next Steps for Future Development

1. **Email Notifications** - Send PDFs via email (requires SMTP setup)
2. **Slack/Discord Integration** - Post notifications to team chat
3. **Custom Styling** - Match Project02-Plan.typ exactly
4. **Weekly Summary** - Aggregate daily plans into weekly report
5. **Progress Tracking** - Compare plans vs actual work completed

---

**Created:** March 5, 2026  
**Last Updated:** March 5, 2026  
**Status:** ✅ Working - PDFs generated with date-prefixed filenames
