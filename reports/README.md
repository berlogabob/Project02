# Weekly Report Generation

Automated weekly progress reports using GitHub Actions and Typst.

---

## 🎯 Overview

Every Sunday at 23:00 UTC, a GitHub Action automatically:
1. Fetches completed and in-progress issues from GitHub
2. Generates a beautiful Typst report (matching your project style)
3. Compiles to PDF
4. Commits both files to the `reports/` directory
5. Creates a GitHub Release with the PDF
6. Posts a summary issue tagging all team members

---

## 📁 Files

| File | Purpose |
|------|---------|
| `reports/weekly-report-template.typ` | Main Typst template with project styling |
| `scripts/generate_weekly_report.py` | Python script to fetch issues and generate report |
| `.github/workflows/weekly-report.yml` | GitHub Action for automation |

---

## 🚀 Manual Usage

### Generate Report Manually

```bash
# Week 1 report
python3 scripts/generate_weekly_report.py --week 1 --output reports/week-01-report.typ

# With custom milestone
python3 scripts/generate_weekly_report.py \
  --week 2 \
  --milestone "2nd milestone: Prototype" \
  --output reports/week-02-report.typ
```

### Compile to PDF

```bash
# Compile
typst compile reports/week-01-report.typ reports/week-01-report.pdf

# Preview (live reload)
typst preview reports/week-01-report.typ
```

### Quick Command (All-in-One)

```bash
# Generate + Compile
python3 scripts/generate_weekly_report.py --week 1 --output reports/week-01-report.typ
typst compile reports/week-01-report.typ reports/week-01-report.pdf
```

---

## 📊 Trigger Manually (GitHub UI)

1. Go to: **Actions** → **Generate Weekly Report**
2. Click **Run workflow**
3. Fill in:
   - **Week number:** `1`, `2`, `3`, etc.
   - **Milestone:** Select current milestone
4. Click **Run workflow**
5. Wait ~2 minutes for completion
6. Download from **Releases** or check the new issue

---

## 📋 Report Structure

### Page 1: Cover & Summary
- Project info and team
- Executive summary
- Stats (completed, in progress, blocked, total)
- Key achievements

### Page 2: Completed Work
- List of closed issues this week
- Notes and observations

### Page 3: Work In Progress
- Current sprint issues
- Blocked issues
- Blockers & challenges

### Page 4: Next Week Plan
- Planned issues
- Milestone progress bar
- Team workload distribution
- Risks & decisions needed

---

## 🎨 Styling

The report uses the same visual style as `Project02-Plan.typ`:

- **Colors:** 4 theme gradients (blue-purple, red-orange, green, yellow)
- **Fonts:** Noto Sans
- **Components:** Matching headers, footers, tables, and badges
- **Layout:** A4, professional margins

---

## ⚙️ Customization

### Change Report Day/Time

Edit `.github/workflows/weekly-report.yml`:

```yaml
on:
  schedule:
    # Change cron schedule (UTC)
    - cron: '0 23 * * 0'  # Sunday 23:00 UTC
```

### Add Team Members

Edit `reports/weekly-report-template.typ`:

```typst
#let nadine_issues = ...
#let andrey_issues = ...
#let dmitri_issues = ...
# Add:
#let newmember_issues = ...
```

### Modify Sections

Edit the template to add/remove sections as needed.

---

## 🔧 Troubleshooting

### "GitHub CLI not found"
```bash
brew install gh  # macOS
sudo apt-get install gh  # Linux
```

### "typst: command not found"
```bash
# Install Typst
# macOS
brew install typst

# Or download from: https://github.com/typst/typst/releases
```

### "No issues found"
- Make sure issues have the correct milestone assigned
- Check that issues were updated in the last week
- Verify GitHub CLI authentication: `gh auth status`

### "Compilation failed"
- Check Typst syntax in the generated `.typ` file
- Ensure `weekly-report-template.typ` is in the `reports/` folder
- Try compiling manually to see detailed errors

---

## 📦 Example Output

After running, you'll have:

```
reports/
├── weekly-report-template.typ    # Main template
├── week-01-report.typ            # Generated Typst source
└── week-01-report.pdf            # Compiled PDF
```

---

## 🎓 Workflow Summary

```
┌─────────────────────────────────────────────────────────┐
│  Sunday 23:00 UTC (or manual trigger)                   │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  GitHub Action Starts                                   │
│  1. Checkout repo                                       │
│  2. Install Typst + GitHub CLI                          │
│  3. Calculate week number                               │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  Fetch GitHub Issues                                    │
│  - Completed (closed last week)                         │
│  - In Progress (open)                                   │
│  - Milestone stats                                      │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  Generate Typst Report                                  │
│  - Fill template with issue data                        │
│  - Write week-XX-report.typ                             │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  Compile to PDF                                         │
│  - typst compile                                        │
│  - Output: week-XX-report.pdf                           │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  Commit & Push                                          │
│  - Add .typ and .pdf to git                             │
│  - Commit with message                                  │
│  - Push to main                                         │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  Create Release + Issue                                 │
│  - Upload PDF to GitHub Releases                        │
│  - Create/Update issue with download links              │
│  - Tag team members                                     │
└─────────────────────────────────────────────────────────┘
```

---

## 📚 Related

- [Typst Documentation](https://typst.app/docs/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Project Plan Template](../Project02-Plan.typ)

---

**Created for:** Project II - The Oracle That Wears Us (MCCIA)  
**Auto-generated reports:** Every Sunday 23:00 UTC
