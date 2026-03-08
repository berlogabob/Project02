# Weekly Planning System Documentation

## Overview

The project uses a **calendar-based weekly planning system** where each week is assigned a number starting from Week 1 (March 2, 2026).

## Week Calendar

| Week | Dates | Status |
|------|-------|--------|
| Week 1 | Mar 2-8, 2026 | ✅ Completed |
| Week 2 | Mar 9-15, 2026 | 🔄 Current |
| Week 3 | Mar 16-22, 2026 | ⏳ Upcoming |
| Week 4 | Mar 23-29, 2026 | ⏳ Upcoming |
| Week 5 | Mar 30 - Apr 5, 2026 | ⏳ Upcoming |
| Week 6 | Apr 6-12, 2026 | ⏳ Upcoming |
| Week 7 | Apr 13-19, 2026 | ⏳ Upcoming |
| Week 8 | Apr 20-26, 2026 | ⏳ Upcoming |
| Week 9 | Apr 27 - May 3, 2026 | ⏳ Upcoming |
| Week 10 | May 4-10, 2026 | ⏳ Upcoming |
| Week 11 | May 11-17, 2026 | ⏳ Upcoming |
| Week 12 | May 18-24, 2026 | ⏳ Upcoming |
| Week 13 | May 25-31, 2026 | ⏳ Upcoming |
| Week 14 | Jun 1-7, 2026 | ⏳ Upcoming |

## GitHub Labels

Each issue should have a **week label** to indicate which week it's planned for:

- `week-1`, `week-2`, `week-3`, ..., `week-14`
- Color: Blue (#207DE5)
- Description shows the date range

## Weekly Report Structure

The weekly report (`reports/week-X-report.typ`) contains:

### Page 1: Cover & Summary
- Week number and date range
- Team members
- Statistics: Completed, Incomplete, Future Week tasks
- Progress bar showing completion percentage

### Page 2: Completed This Week
- Tasks that were planned for this week and successfully completed
- Shows issue number, title, milestone, and priority

### Page 3: Not Completed This Week
- Tasks that were planned for this week but remain incomplete
- Helps identify blockers and carry-over work

### Page 4: Future Week Tasks (Started Early)
- Tasks scheduled for future weeks that have already been started
- Shows proactive work and early progress

## Daily Plan Structure

Daily plans (`reports/daily-plans/YYYYMMDD-daily-plan-username.typ`) now include:
- Week number in the header
- Week date range
- Assigned issues for the team member

## How to Use

### Adding Week Labels to Issues

```bash
# Add week label to an issue
gh issue edit <ISSUE_NUMBER> --add-label week-2

# Add multiple issues to a week
for issue in 30 31 32 33 34; do
    gh issue edit $issue --add-label week-2
done
```

### Generate Weekly Report Manually

```bash
# Auto-detect current week
python3 scripts/generate_weekly_report.py

# Specify week number
python3 scripts/generate_weekly_report.py --week 2 --output reports/week-2-report.typ

# Compile to PDF
typst compile --root . reports/week-2-report.typ reports/week-2-report.pdf
```

### Generate Daily Plan

```bash
bash scripts/generate-daily-plan.sh "username" "Full Name" "20260309" "March 09" "March 09, 2026"
```

## Automated Workflows

### Weekly Report
- **When:** Every Sunday at 22:00 UTC
- **Output:** `reports/week-X-report.pdf`
- **Workflow:** `.github/workflows/weekly-report.yml`

### Daily Plans
- **When:** Every day at 00:00 UTC
- **Output:** `reports/daily-plans/YYYYMMDD-daily-plan-username.pdf`
- **Workflow:** `.github/workflows/daily-plans.yml`

## Week Calculation

Week number is calculated from the project start date (March 2, 2026):

```python
from datetime import date

project_start = date(2026, 3, 2)  # Week 1 starts on Monday
current = date.today()
diff = (current - project_start).days
week_num = (diff // 7) + 1
```

## Best Practices

1. **Plan on Monday:** Add `week-X` labels to all tasks planned for the current week
2. **Update Daily:** Comment on issues with progress updates
3. **Close on Time:** Complete or move incomplete tasks by Sunday
4. **Start Early:** If starting future week tasks, add the appropriate week label
5. **Review Reports:** Use weekly reports to track progress and identify blockers

## Migration from Milestones

The week system complements (not replaces) milestones:
- **Milestones:** Long-term goals (Documentation, Prototype, Final Product)
- **Weeks:** Short-term planning and tracking

Issues can have both milestone and week labels:
- `milestone-1` + `week-2` = Documentation milestone, Week 2 task
- `milestone-2` + `week-5` = Prototype milestone, Week 5 task

---

**Created:** March 9, 2026
**Last Updated:** March 9, 2026
