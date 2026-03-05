The user wants me to create a comprehensive markdown summary of our entire conversation about setting up automated daily and weekly reports for their GitHub project. Let me extract the key information:

1. Project: "The Oracle That Wears Us" - MCCIA Master's Program Project II
2. Team: 3 members (Nadine, Andrey, Dmitri)
3. Main goal: Automated GitHub Actions for daily plans and weekly reports with PDF generation
4. Key challenges faced: Typst syntax issues, Python escaping, @ symbol conflicts
5. Solutions implemented: Clean Python script, template file, proper escaping
6. Current status: Both workflows working

Let me create a comprehensive summary.# Project Summary

## Overall Goal
Automate GitHub Actions to generate personalized daily plan PDFs and weekly progress reports for "The Oracle That Wears Us" MCCIA Master's project, matching the Project02-Plan.typ visual style.

## Key Knowledge

### Project Information
- **Project Name:** The Oracle That Wears Us
- **Program:** MCCIA Master's Program (Creative Computing and Artificial Intelligence)
- **Semester:** 2025-2026 / 2nd Semester
- **Team Members:**
  - Nadine Allan (@naydino) - System Architecture & Integration
  - Andrey Dyakov (@berlogabob) - Plotter & Materialization
  - Dmitri Kazantsev (@electricianv001) - Generative Concepts & Fabrication
- **Repository:** https://github.com/berlogabob/Project02
- **Project Board:** https://github.com/users/berlogabob/projects/7

### Technology Stack
- **Typst:** Document typesetting system for PDF generation (v0.14.2)
- **GitHub Actions:** Automation workflows
- **GitHub CLI (gh):** Issue fetching and management
- **Python 3.11+:** Report generation scripts
- **Unity, TouchDesigner, OSC:** Core project technologies (from brief)

### Critical Technical Decisions
1. **Standalone Typst files:** No imports in generated files to avoid path issues
2. **Template file approach:** `reports/daily-plan-template.typ` provides reusable components matching Project02-Plan.typ style
3. **Date-prefixed filenames:** `YYYYMMDD-daily-plan-username.pdf` prevents overwrites
4. **Text escaping required:**
   - `@` → `at ` (prevents Typst label interpretation)
   - `[` → `(` and `]` → `)` (prevents Typst bracket conflicts)
   - Remove markdown images, HTML tags, URLs from issue content
5. **Typst syntax:** Use `weight: "bold"` not `bold: true`

### Build & Test Commands
```bash
# Run daily plan workflow manually
gh workflow run daily-plans-v2.yml

# Run weekly report workflow manually
gh workflow run weekly-report.yml --field week_number=1

# Local Typst compilation
typst compile reports/daily-plan-template.typ
typst compile reports/20260305-daily-plan-berlogabob.typ

# View workflow runs
https://github.com/berlogabob/Project02/actions
```

### File Structure
```
Project02/
├── .github/workflows/
│   ├── daily-plans-v2.yml      # Daily PDF generation (00:00 UTC)
│   └── weekly-report.yml        # Weekly PDF generation (Sun 22:00 UTC)
├── reports/
│   ├── daily-plan-template.typ  # Reusable Typst components
│   └── daily-plans/             # Generated daily plans
├── scripts/
│   ├── generate_daily_plan.py   # Daily plan generator
│   └── generate_weekly_report.py # Weekly report generator
└── Project02-Plan.typ           # Original style reference
```

## Recent Actions

### Accomplishments
1. ✅ **Daily Plan Workflow Created** - Generates personalized PDFs for each team member at 00:00 UTC daily
2. ✅ **Weekly Report Workflow Restored** - Generates comprehensive weekly reports every Sunday at 22:00 UTC
3. ✅ **Project02-Plan.typ Styling Applied** - Both reports now use identical colors, fonts, and components
4. ✅ **Date Prefix Implementation** - Files named `20260305-daily-plan-username.pdf` prevent overwrites
5. ✅ **Issue Integration** - Fetches assigned GitHub issues with comments, priorities, milestones, labels
6. ✅ **Project Cleanup** - Removed 39 unnecessary files (13,251 lines) from development iterations

### Issues Resolved
1. **Typst Import Errors** - Solved by using standalone Typst generation with template import
2. **Python f-string Conflicts** - Solved by building Typst files line-by-line with proper escaping
3. **@username as Typst Labels** - Solved by replacing `@` with `at ` in `clean_text()` function
4. **Markdown Images in Comments** - Solved by regex removal: `re.sub(r'!\[.*?\]\(.*?\)', '', text)`
5. **Typst bold Syntax** - Solved by using `weight: "bold"` instead of `bold: true`
6. **Quote Escaping in Python** - Solved by alternating single/double quotes in f-strings

### Documentation Created
- `reports/DAILY_PLAN_ACTION_DOCUMENTATION.md` - Complete technical documentation with all issues and solutions

## Current Plan

### [DONE]
1. ✅ Daily plan GitHub Action workflow
2. ✅ Weekly report GitHub Action workflow
3. ✅ Project02-Plan.typ styling integration
4. ✅ Date-prefixed filename format
5. ✅ GitHub issue fetching with comments
6. ✅ Text escaping for Typst compatibility
7. ✅ Project cleanup and organization

### [IN PROGRESS]
1. ⏳ Testing daily plan PDF generation with actual issues
2. ⏳ Verifying styling matches Project02-Plan.typ exactly

### [TODO]
1. 📋 Test weekly report generation with actual milestone data
2. 📋 Add email notifications for daily plans (optional - requires SMTP setup)
3. 📋 Add Slack/Discord integration for team notifications (optional)
4. 📋 Create team onboarding documentation for using daily plans
5. 📋 Set up automatic milestone tracking in weekly reports
6. 📋 Add progress comparison (planned vs completed tasks)

### Known Issues to Monitor
- Typst font warnings for "Noto Sans" (non-critical, PDFs still generate)
- Issue comments with special characters may need additional escaping
- Large numbers of issues may exceed PDF page limits (currently capped at 10 per section)

### Workflow URLs
- **Daily Plans:** https://github.com/berlogabob/Project02/actions/workflows/daily-plans-v2.yml
- **Weekly Report:** https://github.com/berlogabob/Project02/actions/workflows/weekly-report.yml
- **Full Documentation:** https://github.com/berlogabob/Project02/blob/main/reports/DAILY_PLAN_ACTION_DOCUMENTATION.md

---

## Summary Metadata
**Update time**: 2026-03-05T10:23:52.099Z 
