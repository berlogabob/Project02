# Automated Daily Planning System

## 🎯 Overview

Every day at **00:00 UTC (02:00 Lisbon time)**, each team member automatically receives a **personalized PDF** with their assigned tasks for the day.

---

## ⏰ Schedule

**First Run:** Tonight at 00:00 UTC (in 28 minutes from now - it's 23:32!)

**Daily:** 00:00 UTC = 02:00 Lisbon time

---

## 📊 What Gets Generated

### For Each Team Member:

1. **Personalized PDF** (`daily-plan-{username}.pdf`)
   - Their name and GitHub handle
   - All their assigned open issues
   - Priority badges (critical, high, medium, low)
   - Recent comments on each issue
   - Sub-issues listed
   - Milestone information
   - Time blocking template
   - Planning notes section

2. **Typst Source** (`daily-plan-{username}.typ`)
   - Editable source file
   - Auto-filled with issue data

3. **Summary Issue** on GitHub
   - Tags all team members
   - Links to all PDFs
   - Shows issue count per member

4. **Personal Comment** on each member's first issue
   - Direct notification
   - Link to their plan

---

## 📁 File Structure

```
reports/daily-plans/
├── daily-plan-naydino.typ           # Nadine's plan source
├── daily-plan-naydino.pdf           # Nadine's plan PDF
├── daily-plan-berlogabob.typ        # Andrey's plan source
├── daily-plan-berlogabob.pdf        # Andrey's plan PDF
├── daily-plan-electricianv001.typ   # Dmitri's plan source
└── daily-plan-electricianv001.pdf   # Dmitri's plan PDF
```

---

## 🎨 PDF Contents

### Page 1: Daily Plan

**Header:**
- Team member name
- GitHub username
- Today's date
- Current milestone

**Stats:**
- Total tasks
- High priority tasks
- Tasks with milestones

**Priority Tasks Section:**
- Critical and high priority issues first
- Each issue shows:
  - Issue number and title
  - Priority badge
  - Labels
  - Milestone
  - Description (truncated)
  - Recent comments (last 3)
  - Sub-issues

**All Tasks Section:**
- Medium and low priority issues
- Same detailed format

**Quick Planning Tips:**
1. Review each task and sub-issues
2. Check recent comments for updates
3. Estimate time needed
4. Plan your approach
5. Comment your progress

### Page 2: Planning Notes

**Today's Goals:**
- Blank space to write main objectives

**Time Blocks:**
- 09:00 - 17:00 schedule
- Pre-filled lunch break
- Empty slots for planning

**Blockers & Questions:**
- Space to note challenges
- Questions for the team

**End of Day Checklist:**
- [ ] Update issue status
- [ ] Add progress comments
- [ ] Push code changes
- [ ] Create PR if ready
- [ ] Prepare demo/screenshots
- [ ] Plan tomorrow's tasks

---

## 🚀 How to Use

### Automatic (GitHub Actions)

**Runs every day at 00:00 UTC**

1. Workflow triggers
2. Fetches all open issues
3. Groups by assignee
4. Generates personalized PDFs
5. Commits to repository
6. Creates summary issue
7. Comments on team members' issues

### Manual (Test Now!)

```bash
# Generate for all team members
./scripts/daily-plan.sh

# Or specific member
python3 scripts/generate_daily_plan.py --member berlogabob

# Or all at once
python3 scripts/generate_daily_plan.py --all-members --output-dir reports/daily-plans
```

---

## 📋 Example Output

### Nadine's Daily Plan

```
═══════════════════════════════════════════════════
05/03                          DAILY PLAN
═══════════════════════════════════════════════════

Team Member: Nadine Allan @naydino
Date: March 5, 2026
Project: The Oracle That Wears Us
Milestone: 1st milestone: Documentation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your Tasks for Today

┌─────────────────────────────────────────────┐
│ Total: 3  │  High Priority: 2  │  Milestones: 3 │
└─────────────────────────────────────────────┘

PRIORITY TASKS:

┌─────────────────────────────────────────────┐
│ #4 - Topic Selection & Theoretical Framework│
│                              ##4  [CRITICAL] │
│ Milestone: 1st milestone: Documentation     │
│ Labels: [type: research] [milestone-1]      │
│                                             │
│ Define project topic with critical and      │
│ theoretical support...                      │
│                                             │
│ Recent Comments:                            │
│ @berlogabob (2026-03-04): I think we       │
│ should focus on Identity theme...           │
│                                             │
│ Sub-issues:                                 │
│ □ #24 - Research identity theories          │
│ □ #25 - Collect visual references           │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ #7 - Hardware & Framework Selection         │
│                              ##7    [HIGH]  │
│ Milestone: 1st milestone: Documentation     │
│ Labels: [unit:emerging-tech] [priority:high]│
│                                             │
│ Select appropriate hardware and define      │
│ integration strategy...                     │
│                                             │
│ Recent Comments:                            │
│ @naydino (2026-03-04): Looking into        │
│ Leap Motion vs Kinect...                    │
└─────────────────────────────────────────────┘

ALL TASKS:

┌─────────────────────────────────────────────┐
│ #2 - Visual & Audio Reference Board         │
│                              ##2   [MEDIUM] │
│ Milestone: 1st milestone: Documentation     │
│ Labels: [type:design] [milestone-1]         │
└─────────────────────────────────────────────┘

═══════════════════════════════════════════════
PLANNING NOTES
═══════════════════════════════════════════════

Today's Goals:
- Complete topic selection research
- Decide on hardware platform
- Update team on progress

Time Blocks:
09:00-10:00: _________________________________
10:00-11:00: _________________________________
11:00-12:00: _________________________________
12:00-13:00: Lunch Break
13:00-14:00: _________________________________
14:00-15:00: _________________________________
15:00-16:00: _________________________________
16:00-17:00: _________________________________

Blockers & Questions:
- Need to discuss UV fabric availability

End of Day Checklist:
□ Update issue status
□ Add progress comments
□ Push code changes
□ Create PR if ready
□ Prepare demo
□ Plan tomorrow
```

---

## 🔧 Features

### ✅ Automatic Features

| Feature | Description |
|---------|-------------|
| **Daily Generation** | Runs at 00:00 UTC automatically |
| **Personalization** | Each member gets their own PDF |
| **Issue Fetching** | Pulls from GitHub in real-time |
| **Priority Sorting** | Critical/high priority first |
| **Comments Included** | Last 3 comments per issue |
| **Sub-issues** | Lists related sub-tasks |
| **Milestone Tracking** | Shows which milestone each issue belongs to |
| **Labels** | Displays all issue labels |
| **GitHub Notifications** | Comments on issues, creates summary issue |
| **Auto-commit** | Pushes PDFs to repository |

### ✅ Manual Features

| Feature | Command |
|---------|---------|
| **Generate all** | `./scripts/daily-plan.sh` |
| **Generate one** | `python3 scripts/generate_daily_plan.py --member USERNAME` |
| **No compile** | Add `--no-compile` flag |
| **Custom output** | Use `-o` or `--output-dir` |

---

## 📅 Workflow Timeline

```
┌─────────────────────────────────────────────────────┐
│ 00:00 UTC (02:00 Lisbon)                            │
│ GitHub Action Wakes Up                              │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│ Step 1: Fetch Issues                                │
│ - Get all open issues                               │
│ - Group by assignee                                 │
│ - Fetch comments and sub-issues                     │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│ Step 2: Generate PDFs                               │
│ - Create personalized plan for each member          │
│ - Sort by priority                                  │
│ - Format with project styling                       │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│ Step 3: Commit & Push                               │
│ - Add PDFs to reports/daily-plans/                  │
│ - Commit with date message                          │
│ - Push to main branch                               │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│ Step 4: Notify Team                                 │
│ - Create summary issue                              │
│ - Tag all members                                   │
│ - Comment on individual issues                      │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│ 02:00 Lisbon Time                                   │
│ Team members wake up to:                            │
│ - Email notification from GitHub                    │
│ - Summary issue with all PDFs                       │
│ - Personal comment on their issue                   │
│ - Ready-to-use daily plan!                          │
└─────────────────────────────────────────────────────┘
```

---

## 🎯 Benefits

### For Team Members:
- ✅ Wake up to clear tasks
- ✅ No morning confusion
- ✅ See priorities immediately
- ✅ Track comments and updates
- ✅ Plan your day effectively
- ✅ Never miss a sub-issue

### For Professor:
- ✅ See what everyone's working on
- ✅ Clear progress tracking
- ✅ Morning demos with context
- ✅ Identify blockers early

### For Project:
- ✅ Consistent daily planning
- ✅ Automatic documentation
- ✅ Better task completion
- ✅ Improved communication

---

## 🧪 Test Tonight!

It's 23:32 now. The workflow will run in **28 minutes** at midnight.

**To test manually right now:**

```bash
# Quick test for all members
./scripts/daily-plan.sh

# Or just for yourself
python3 scripts/generate_daily_plan.py --member berlogabob --output reports/daily-plan-berlogabob.typ

# Open the PDF
open reports/daily-plan-berlogabob.pdf
```

---

## 📊 Files Created

| File | Purpose |
|------|---------|
| `reports/daily-plan-template.typ` | Template with project styling |
| `scripts/generate_daily_plan.py` | Python generator script |
| `scripts/daily-plan.sh` | Quick-start shell script |
| `.github/workflows/daily-plans.yml` | GitHub Action (auto-runs daily) |
| `reports/daily-plans/` | Output directory for PDFs |
| `reports/DAILY_PLAN_GUIDE.md` | This documentation |

---

## ✅ Checklist for First Run

- [x] Template created
- [x] Python script ready
- [x] GitHub Action configured
- [x] Team usernames correct
- [x] Output directory exists
- [ ] **Tonight 00:00: First automatic run!**
- [ ] Check emails for notifications
- [ ] Download your PDF
- [ ] Use it for planning tomorrow

---

## 🎉 Summary

**Starting tonight**, every team member will receive:
- 📄 Personalized PDF at 02:00 Lisbon time
- 📋 List of their assigned tasks
- 💬 Recent comments and updates
- 🔗 Links to sub-issues
- 📊 Priority indicators
- 📝 Planning template
- ✅ Daily checklist

**All automatic!** No manual work needed! 🚀

---

**Created for:** Project II - The Oracle That Wears Us  
**First Run:** March 5, 2026 at 00:00 UTC (in 28 minutes!)  
**Schedule:** Daily at 00:00 UTC (02:00 Lisbon)
