# Weekly Report - Local Usage Guide

## Quick Start

```bash
# Run with auto-detected week number
./scripts/run-weekly-report.sh

# Or run manually
python3 scripts/generate_weekly_report.py --week 2
```

## Requirements

1. **GitHub CLI** (`gh`) - authenticated with token
2. **Python 3.11+**
3. **Typst** v0.14.2+
4. **Ollama** (optional, for AI summary) - `ollama pull qwen3.5:latest`

## AI Summary Setup

The report can generate AI-powered summaries of completed work.

### Option 1: Ollama Local (Recommended for GitHub Actions)

```bash
# Install Ollama: https://ollama.ai/
curl -fsSL https://ollama.com/install.sh | sh

# Pull qwen3.5:latest model
ollama pull qwen3.5:latest

# Start Ollama server (if not running)
ollama serve

# Run report - AI summary will be generated automatically
./scripts/run-weekly-report.sh
```

### Option 2: Qwen API (DashScope)

```bash
# Get API key from https://dashscope.aliyun.com/
export DASHSCOPE_API_KEY="your-key-here"

# Run report
./scripts/run-weekly-report.sh
```

### Option 3: OpenAI API

```bash
# Get API key from https://platform.openai.com/
export OPENAI_API_KEY="your-key-here"

# Run with OpenAI
python3 scripts/generate_ai_summary.py --week 2 --api openai
```

### Without AI Summary

If no API is configured, the report will show a simple list of completed issues.

## Manual Commands

```bash
# Generate report for specific week
python3 scripts/generate_weekly_report.py --week 2 --output reports/week-2-report.typ

# Compile to PDF
typst compile --root . reports/week-2-report.typ reports/week-2-report.pdf

# Generate AI summary only
python3 scripts/generate_ai_summary.py --week 2 --api qwen --output summary.txt
```

## GitHub Actions Setup

### Automatic Weekly Reports

The workflow `.github/workflows/weekly-report-ollama.yml` runs automatically every Sunday.

**Features:**
- ✅ Auto-detects current week number
- ✅ Uses Ollama with qwen3.5:latest for AI summary
- ✅ Commits PDF to repository
- ✅ Uploads as artifact for download

**Manual trigger:**
1. Go to Actions → "Generate Weekly Report (Ollama)"
2. Click "Run workflow"
3. Optionally specify week number
4. Click "Run workflow"

**To enable:**
1. Make sure `GITHUB_TOKEN` has write permissions
2. Workflow runs automatically on schedule
3. First run will take ~5 minutes (Ollama model download)

## Configuration

Edit team information in `scripts/generate_weekly_report.py`:

```python
TEAM_ROLES = {
    "naydino": "System Architecture & Integration",
    "berlogabob": "Plotter & Materialization",
    "electricianv001": "Generative Concepts & Fabrication"
}

TEAM_NAMES = {
    "naydino": "Nadine Allan",
    "berlogabob": "Andrey Dyakov",
    "electricianv001": "Dmitri Kazantsev"
}
```

## Issue Labels

The report uses these labels:

- **`week-N`** - Assign issue to week N (e.g., `week-1`, `week-2`)
- **`show-in-report`** - Include in HIGHLIGHTS section
- **`Parent: #XX`** - Add parent-child relationship (in issue body)

## Output Structure

```
reports/
├── week-1-report.typ    # Typst source
├── week-1-report.pdf    # Generated PDF
└── WEEKLY_REPORT_GUIDE.md
```

## Troubleshooting

### "gh: command not found"
Install GitHub CLI: https://cli.github.com/

### "typst: command not found"
Install Typst: https://typst.app/

### AI summary not working
- Check API key is set: `echo $DASHSCOPE_API_KEY`
- Test API connection: `python3 scripts/generate_ai_summary.py --week 1 --api qwen`
- Fallback: Report will show simple issue list if AI unavailable
