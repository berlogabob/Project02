The user wants me to create a comprehensive project summary based on our entire conversation. Let me analyze what we accomplished:

1. **Main Goal**: Set up automated weekly/daily reports with AI summaries for their GitHub project "The Oracle That Wears Us"

2. **Key accomplishments**:
   - Created GitHub Actions workflow for weekly reports
   - Integrated Ollama with qwen3.5:2b for AI summaries
   - Fixed multiple Typst compilation issues
   - Set up week-based issue tracking with labels
   - Created parent-child issue hierarchy support

3. **Technical decisions**:
   - Uses Typst for PDF generation
   - Ollama qwen3.5:2b for AI (80 words, 3-4 bullets)
   - Week labels (week-1, week-2, etc.)
   - show-in-report label for highlights
   - Parent-child via issue body "**Parent:** #XX"

4. **Files created/modified**:
   - `.github/workflows/weekly-report-ollama.yml`
   - `scripts/generate_weekly_report.py`
   - `scripts/generate_ai_summary.py`
   - `scripts/run-weekly-report.sh`
   - `templates/daily-plan-template.typ`

5. **Issues resolved**:
   - PDF compilation with special characters
   - Git push conflicts in Actions
   - AI timeout issues
   - Typst escaping (#, *, [, ])

Let me create a comprehensive summary.# Project Summary

## Overall Goal
Automate GitHub Actions to generate weekly progress reports with AI-powered summaries using Ollama (qwen3.5:2b) and Typst for PDF generation, matching the Project02-Plan.typ visual style.

## Key Knowledge

### Project Information
- **Project:** "The Oracle That Wears Us" - MCCIA Master's Program Project II
- **Team:** Nadine Allan (System Architecture), Andrey Dyakov (Plotter & Materialization), Dmitri Kazantsev (Generative Concepts)
- **Repository:** https://github.com/berlogabob/Project02
- **Week System:** Week 1 started Mar 2, 2026; weeks run Monday-Sunday

### Technology Stack
- **Typst v0.14.2** - PDF generation (must use `--root .` for compilation)
- **Ollama** - Local AI with qwen3.5:2b model (2.7GB, GPU-accelerated)
- **GitHub Actions** - Automated weekly reports (Sundays 22:00 UTC)
- **GitHub CLI (gh)** - Issue fetching and management
- **Python 3.11+** - Report generation scripts

### Critical Technical Decisions
1. **AI Summary:** 80 words, 3-4 bullet points (increased from default for better detail)
2. **Issue Labels:**
   - `week-N` - Assign issue to week N (e.g., `week-1`, `week-2`)
   - `show-in-report` - Include in HIGHLIGHTS section
   - `**Parent:** #XX` in issue body - Creates parent-child hierarchy
3. **Typst Escaping:** Must escape `#` → `\#`, `*` → space, `[` → `(`, `]` → `)`
4. **PDF Compilation:** Always use `typst compile --root . file.typ file.pdf`
5. **Workflow Git:** Must `git pull --rebase` before `git push` in Actions

### Build & Test Commands
```bash
# Local weekly report generation
./scripts/run-weekly-report.sh          # Interactive (asks about AI)
python3 scripts/generate_weekly_report.py --week 1  # Direct

# Compile Typst to PDF
typst compile --root . reports/week-1-report.typ reports/week-1-report.pdf

# Test AI summary only
python3 scripts/generate_ai_summary.py --week 1 --api ollama

# GitHub Actions (manual trigger)
# Go to: https://github.com/berlogabob/Project02/actions
# Select "Generate Weekly Report (Ollama)" → Run workflow
```

### File Structure
```
Project02/
├── .github/workflows/
│   └── weekly-report-ollama.yml      # Weekly PDF generation (Ollama AI)
├── templates/
│   └── daily-plan-template.typ       # Reusable Typst components
├── reports/
│   ├── week-1-report.typ            # Generated Typst source
│   ├── week-1-report.pdf            # Generated PDF
│   └── WEEKLY_REPORT_GUIDE.md       # Usage documentation
├── scripts/
│   ├── generate_weekly_report.py    # Main report generator
│   ├── generate_ai_summary.py       # AI summary with Ollama
│   └── run-weekly-report.sh         # Local runner script
└── Project02-Plan.typ               # Original style reference
```

## Recent Actions

### Accomplishments
1. ✅ **Weekly Report Workflow** - Automated PDF generation with AI summaries every Sunday
2. ✅ **Ollama Integration** - Local qwen3.5:2b model for AI summaries (80 words, 3-4 bullets)
3. ✅ **Issue Hierarchy** - Parent-child relationships via `**Parent:** #XX` in issue body
4. ✅ **Week Labels** - `week-1`, `week-2`, etc. for calendar-based tracking
5. ✅ **HIGHLIGHTS Section** - Shows only issues with both `week-N` + `show-in-report` labels
6. ✅ **Typst Compilation** - Fixed escaping for `#`, `*`, `[`, `]` characters
7. ✅ **Git Actions Fix** - Added `git pull --rebase` before push to prevent conflicts
8. ✅ **Documentation** - Created WEEKLY_REPORT_GUIDE.md with full usage instructions

### Issues Resolved
1. **PDF Compilation Errors** - Asterisks `*` in AI output broke Typst; fixed with escaping
2. **Git Push Rejected** - Actions workflow now pulls before pushing
3. **AI Timeout** - Increased timeout to 180s for Ollama model loading
4. **Duplicate Workflows** - Removed old `weekly-report.yml`, kept `weekly-report-ollama.yml`
5. **Multi-line AI Text** - AI summaries with newlines broke Typst; kept as `#text()` not `#raw()`
6. **Label Filtering** - HIGHLIGHTS now shows only issues with BOTH week-N AND show-in-report labels

### Documentation Created
- `reports/WEEKLY_REPORT_GUIDE.md` - Complete usage guide
- `.github/workflows/README_WEEKLY_REPORT.md` - Actions workflow documentation
- `scripts/README.md` - Quick start guide

## Current Plan

### [DONE]
1. ✅ Weekly report GitHub Action workflow with Ollama AI
2. ✅ Local script for manual report generation
3. ✅ AI summary integration (80 words, 3-4 bullets)
4. ✅ Week-based issue tracking with labels
5. ✅ Parent-child issue hierarchy support
6. ✅ Typst PDF compilation (all escaping fixed)
7. ✅ Git workflow fixes for Actions
8. ✅ Documentation created

### [IN PROGRESS]
1. ⏳ Monitoring GitHub Actions runs for AI timeout issues
2. ⏳ Testing parent-child hierarchy visualization in PDF

### [TODO]
1. 📋 Add email/Slack notifications when reports are generated
2. 📋 Create team onboarding guide for using week labels
3. 📋 Add progress comparison (planned vs completed tasks)
4. 📋 Consider caching Ollama models in Actions for faster startup
5. 📋 Add milestone progress tracking in weekly reports

### Known Issues to Monitor
- **Ollama in Actions:** First run takes ~5 minutes (model download), subsequent runs ~2 minutes with cache
- **AI Summary Timeout:** 180s timeout set; may need adjustment for larger issue counts
- **Typst Warnings:** `**` markdown stars show warnings but don't break compilation (cosmetic only)
- **Local Ollama:** Can be slow without GPU; script offers 5s timeout to skip AI for faster generation

### Workflow URLs
- **Weekly Report:** https://github.com/berlogabob/Project02/actions/workflows/weekly-report-ollama.yml
- **Full Documentation:** https://github.com/berlogabob/Project02/blob/main/reports/WEEKLY_REPORT_GUIDE.md

---

## Summary Metadata
**Update time:** 2026-03-09T01:15:00.000Z  
**Last Commit:** `3b557b8` - "Add generated week-1-report.pdf (AI summary works!)"

---

## Summary Metadata
**Update time**: 2026-03-09T09:30:46.416Z 
