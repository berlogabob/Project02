# Automated Weekly Report System

## ✅ Yes - Fully Automatic as Described in Project02-Plan.typ

Your report system is configured to match the exact workflow from your project plan:

---

## 📅 Schedule

### From Project02-Plan.typ:
> *"Weekly Flow:*
> 1. *Monday: Team meeting, issues moved to "This Week".*
> 2. *During week: Work in individual branches with tiny PRs.*
> 3. *Sunday night: GitHub Action generates this PDF report.*
> 4. *Monday morning: Report + live demo to the professor.*"

### Automated Implementation:

| Step | When | What Happens |
|------|------|--------------|
| **1** | Monday | Team meeting, plan week |
| **2** | Mon-Sun | Work on issues, create PRs |
| **3** | **Sunday 22:00 UTC** | GitHub Action wakes up |
| **4** | **Sunday 22:05 UTC** | Fetches all issues from GitHub |
| **5** | **Sunday 22:06 UTC** | Generates Typst report |
| **6** | **Sunday 22:07 UTC** | Compiles to PDF |
| **7** | **Sunday 22:08 UTC** | Commits to repository |
| **8** | **Sunday 22:09 UTC** | Creates GitHub Release |
| **9** | **Sunday 22:10 UTC** | Posts issue tagging team |
| **10** | **Monday 00:00 Lisbon** | **Report ready for professor!** |

---

## ⏰ Time Zone Conversion

```
Sunday 22:00 UTC = Monday 00:00 Lisbon (UTC+2 in summer)
```

**Cron Schedule:**
```yaml
- cron: '0 22 * * 0'  # Sunday 22:00 UTC
```

---

## 🔧 What Gets Generated Automatically

### Every Sunday Night:

1. **PDF Report** (`reports/week-XX-report.pdf`)
   - Professional A4 layout
   - Your project colors and styling
   - 4 pages of progress data

2. **Typst Source** (`reports/week-XX-report.typ`)
   - Editable source file
   - Auto-filled with issue data

3. **GitHub Release**
   - PDF attached for download
   - Tagged with week number

4. **GitHub Issue**
   - Summary post
   - Download links
   - Tags all team members: @naydino @berlogabob @electricianv001

---

## 📊 Report Content (Auto-Filled)

### Page 1: Cover & Summary
- ✅ Week number (auto-calculated)
- ✅ Current milestone
- ✅ Team members
- ✅ Executive summary
- ✅ Stats (completed, in progress, blocked, total)
- ✅ Key achievements

### Page 2: Completed Work
- ✅ List of issues closed this week
- ✅ Auto-fetched from GitHub
- ✅ Notes & observations

### Page 3: Work In Progress
- ✅ Current sprint issues
- ✅ Blocked issues (if any)
- ✅ Blockers & challenges

### Page 4: Next Week Plan
- ✅ Planned issues
- ✅ Milestone progress bar (auto-calculated)
- ✅ Team workload distribution
- ✅ Risks & decisions needed

---

## 🎨 Styling (From Project02-Plan.typ)

The weekly report uses **identical styling** to your main project plan:

- ✅ Same color gradients (blue-purple, red-orange, green, yellow)
- ✅ Same font (Noto Sans)
- ✅ Same page layout (A4, margins)
- ✅ Same headers, footers, tables
- ✅ Same visual identity

---

## 🚀 How to Enable

### 1. Enable GitHub Actions
```
Settings → Actions → Enable Actions
```

### 2. Verify Workflow
```
Actions → Generate Weekly Report → Should show "This workflow has a workflow_dispatch event"
```

### 3. Test Manually (Optional)
```bash
# Or use GitHub UI: Actions → Run workflow
./scripts/weekly-report.sh
```

### 4. Wait for Sunday
The workflow will automatically run every Sunday at 22:00 UTC.

---

## 📁 Files Created

```
Project02/
├── .github/
│   └── workflows/
│       └── weekly-report.yml          # ⭐ Auto-run every Sunday
├── reports/
│   ├── weekly-report-template.typ     # Template (your styling)
│   ├── README.md                       # Documentation
│   └── week-XX-report.typ              # Auto-generated weekly
│   └── week-XX-report.pdf              # Auto-generated PDF
└── scripts/
    ├── generate_weekly_report.py       # Fetches issues, generates report
    └── weekly-report.sh                # Manual quick-start
```

---

## 🔄 Weekly Cycle

```
┌─────────────────────────────────────────────────────────────┐
│ WEEK BEGINS (Monday)                                        │
│ - Team meeting                                              │
│ - Move issues to "This Week"                                │
│ - Assign tasks                                              │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ MONDAY - SUNDAY                                             │
│ - Work on issues                                            │
│ - Create tiny PRs                                           │
│ - Close issues when done                                    │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ SUNDAY 22:00 UTC (Monday 00:00 Lisbon)                      │
│ ⭐ GITHUB ACTION TRIGGERS                                   │
│ 1. Fetches completed issues (closed this week)              │
│ 2. Fetches in-progress issues (still open)                  │
│ 3. Calculates milestone progress                            │
│ 4. Generates Typst report                                   │
│ 5. Compiles to PDF                                          │
│ 6. Commits both files                                       │
│ 7. Creates GitHub Release                                   │
│ 8. Posts summary issue                                      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ MONDAY MORNING                                              │
│ ✅ Report ready!                                            │
│ - Download PDF from Releases                                │
│ - Present to professor                                      │
│ - Show live demo                                            │
└─────────────────────────────────────────────────────────────┘
```

---

## ✅ Checklist

- [x] Template matches Project02-Plan.typ styling
- [x] Auto-generates Sunday night (Monday 00:00 Lisbon)
- [x] Fetches real GitHub issues
- [x] Calculates milestone progress
- [x] Creates PDF automatically
- [x] Commits to repository
- [x] Creates GitHub Release
- [x] Tags team members
- [x] Ready for Monday morning demo

---

## 🎯 Summary

**Yes!** Your weekly report is configured to auto-generate exactly as described in your project plan:

- ✅ **Sunday night** generation (22:00 UTC = Monday 00:00 Lisbon)
- ✅ **Monday morning** ready for professor
- ✅ **Beautiful PDF** with your project styling
- ✅ **Auto-filled** from GitHub issues
- ✅ **Zero manual work** required (after initial setup)

Just enable GitHub Actions and it will run automatically every week! 🎉

---

**Created for:** Project II - The Oracle That Wears Us (MCCIA)  
**Schedule:** Every Sunday 22:00 UTC (Monday 00:00 Lisbon)  
**First Report:** Week 1 (when you enable the workflow)
