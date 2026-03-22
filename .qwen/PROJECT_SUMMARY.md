The user wants me to create a comprehensive project summary based on the entire conversation history. Let me analyze what we've accomplished:

1. **Weekly Report System** - Created automated weekly report generation with:
   - GitHub Issues integration
   - AI-powered summaries using Ollama qwen3.5:2b
   - Typst PDF generation
   - GitHub Actions automation

2. **Issue Hierarchy** - Set up proper parent-child relationships using gh sub-issue extension:
   - #57 Plotter project (72 sub-issues across 11 phases)
   - #58 Environmental Projection Unity/TD project (19 sub-issues)

3. **Fixed various issues**:
   - PDF compilation errors (escaping asterisks in AI summary)
   - Duplicate issues closed (#3, #59, #60)
   - Week system (weeks start Monday Mar 2, 2026)

4. **Documentation created**:
   - ISSUE_HIERARCHY.md
   - Various workflow documentation

Let me create a comprehensive summary following the specified format.# Project02 - Automated Weekly Reporting & Issue Management System

## Overall Goal
Create an automated weekly report system with AI-powered summaries using GitHub Issues, Typst PDF generation, and Ollama qwen3.5:2b for local and GitHub Actions usage, with proper issue hierarchy management.

## Key Knowledge

### Week System
- **Project weeks start Monday Mar 2, 2026**
- **Week N formula:** `(today - Mar 2, 2026) // 7 + 1`
- **Labels:** `week-N` for week assignment, `show-in-report` for HIGHLIGHTS, `duplicate` to exclude
- **Parent-Child:** Add `**Parent:** #XX` in issue body for hierarchy (legacy) or use `gh sub-issue`

### Technology Stack
- **AI Summary:** Ollama qwen3.5:2b (local) or GitHub Actions with auto-install
- **PDF Generation:** Typst v0.14.2+
- **Issue Management:** GitHub CLI (`gh`) + `gh sub-issue` extension (agbiotech/gh-sub-issue)
- **Python:** 3.11+

### Team Configuration
- TEAM_ROLES and TEAM_NAMES dictionaries in generate_weekly_report.py
- Assignee tracking via GitHub issue assignees

### Build Commands
```bash
# Local (with AI summary)
./scripts/run-weekly-report.sh

# Manual week generation
python3 scripts/generate_weekly_report.py --week 2

# AI summary only
python3 scripts/generate_ai_summary.py --week 2 --api ollama

# GitHub Actions
# Runs Sundays 22:00 UTC automatically
# Or trigger manually: Actions → "Generate Weekly Report (Ollama)"
```

### Issue Hierarchy Structure
```
#57 Plotter (ROOT)
├── 11 Phase tasks (Level 2)
│   └── 72 individual tasks (Level 3, 30 min each)

#58 Environmental Projection (Unity/TD)
└── 19 sub-issues (Milestone 2)
```

### Important Conventions
- **Task granularity:** Each task = 30 minutes (1 Pomodoro)
- **Weekends:** Free (not included in planning)
- **Future Week Preview:** Shows tasks with BOTH `week-N` + `Next-Week-Preview` labels
- **AI Summary escaping:** `*` → space, `#` → `\#`, `[` → `(`, `]` → `)`

## Recent Actions

### ✅ Weekly Report System (COMPLETED)
- Created `scripts/generate_weekly_report.py` with AI integration
- Created `scripts/generate_ai_summary.py` with Ollama/Qwen/OpenAI support
- Created `scripts/run-weekly-report.sh` local runner
- Created `.github/workflows/weekly-report-ollama.yml` GitHub Actions workflow
- Fixed PDF compilation errors (escaping asterisks in AI summary)
- Added PDF compilation verification with error handling
- Increased AI summary to 300 words (5-7 bullet points)

### ✅ Issue Hierarchy Setup (COMPLETED)
- Installed `gh sub-issue` extension (agbiotech/gh-sub-issue)
- Linked 72 Plotter tasks under #57 (11 Phase → 72 individual)
- Linked 19 Unity/TD tasks under #58 (Environmental Projection)
- Created ISSUE_HIERARCHY.md documentation

### ✅ Duplicate Cleanup (COMPLETED)
- Found and closed 3 duplicate issues: #3, #59, #60
- Verified no other duplicates exist
- Removed duplicates from sub-issue hierarchy

### ✅ Documentation Created
- `ISSUE_HIERARCHY.md` - Complete issue structure
- `.github/workflows/README_WEEKLY_REPORT.md` - Workflow documentation
- `reports/WEEKLY_REPORT_GUIDE.md` - Local usage guide
- `scripts/README.md` - Quick start guide

### Key Fixes Applied
1. **AI Summary Typst Compatibility:** Escape `*`, `#`, `[`, `]` characters
2. **GitHub Actions Git Push:** Added `git pull --rebase` before push
3. **Local Script Paths:** Fixed SCRIPT_DIR/PROJECT_DIR handling
4. **Ollama Timeout:** Increased to 180s for GitHub Actions
5. **Future Week Tasks:** Filter by assigned users only (in-progress)
6. **Future Week Hierarchy:** Added parent-child grouping (consistent with HIGHLIGHTS)

## Current Plan

1. [DONE] Create weekly report generator with GitHub Issues integration
2. [DONE] Implement week-based filtering and show-in-report highlights
3. [DONE] Add parent-child hierarchy support via gh sub-issue
4. [DONE] Integrate AI summary with Ollama qwen3.5:2b
5. [DONE] Create GitHub Actions workflow with auto Ollama installation
6. [DONE] Make team roles configurable
7. [DONE] Create comprehensive documentation (4 markdown files)
8. [DONE] Fix PDF compilation errors (Typst escaping)
9. [DONE] Link all active issues to proper hierarchy (#57, #58)
10. [DONE] Close duplicate issues (#3, #59, #60)
11. [TODO] Test GitHub Actions workflow in production (next Sunday 22:00 UTC)
12. [TODO] Add email/Slack notifications (optional)
13. [TODO] Create Project Board view for hierarchy visualization

## Project Statistics

| Metric | Value |
|--------|-------|
| **Total Issues** | 148 |
| **Active Open Issues** | 119 |
| **Closed Issues** | 29 |
| **Plotter Project (#57)** | 83 issues (11 Phase + 72 tasks) |
| **Unity/TD Project (#58)** | 19 issues |
| **Week 1 Completed** | 19 issues |
| **Week 2 Planned** | 75 issues |
| **Week 3 Planned** | 22 issues |
| **Week 4 Planned** | 14 issues |

## File Structure

```
Project02/
├── scripts/
│   ├── generate_weekly_report.py    # Main report generator
│   ├── generate_ai_summary.py       # AI summary via Ollama
│   └── run-weekly-report.sh         # Local runner
├── .github/workflows/
│   └── weekly-report-ollama.yml     # GitHub Actions workflow
├── reports/
│   ├── WEEKLY_REPORT_GUIDE.md       # Usage documentation
│   └── week-N-report.{typ,pdf}      # Generated reports
├── templates/
│   └── daily-plan-template.typ      # Reusable Typst components
├── ISSUE_HIERARCHY.md               # Issue structure documentation
└── TEAM.md                          # Team configuration
```

## Next Scheduled Run
- **GitHub Actions:** Sunday 22:00 UTC (automatic)
- **Week Detection:** Auto-calculated based on current date

---

## Summary Metadata
**Update time**: 2026-03-09T22:53:22.385Z 
