# Weekly Report System

## Quick Start

### Local Usage (with AI Summary)

```bash
# Install Ollama and pull model (one-time)
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen3.5:latest

# Run weekly report
./scripts/run-weekly-report.sh
```

### GitHub Actions (Automatic)

Workflow: `.github/workflows/weekly-report-ollama.yml`

- Runs every Sunday at 22:00 UTC
- Auto-generates PDF with AI summary
- Commits to repository

## Files

```
Project02/
├── scripts/
│   ├── generate_weekly_report.py    # Main report generator
│   ├── generate_ai_summary.py       # AI summary with Ollama
│   └── run-weekly-report.sh         # Local runner script
├── .github/workflows/
│   ├── weekly-report-ollama.yml     # GitHub Actions workflow
│   └── README_WEEKLY_REPORT.md      # Workflow documentation
└── reports/
    ├── WEEKLY_REPORT_GUIDE.md       # Usage guide
    └── week-X-report.pdf            # Generated reports
```

## AI Summary

Uses **Ollama + qwen3.5:latest** for intelligent summaries:

- Analyzes completed issues
- Generates 3-5 bullet points
- Professional, concise format

**Fallback:** Shows issue list if AI unavailable.

## Configuration

Edit team info in `scripts/generate_weekly_report.py`:

```python
TEAM_ROLES = {
    "naydino": "System Architecture & Integration",
    "berlogabob": "Plotter & Materialization",
    "electricianv001": "Generative Concepts & Fabrication"
}
```

## Documentation

- **Local usage:** `reports/WEEKLY_REPORT_GUIDE.md`
- **GitHub Actions:** `.github/workflows/README_WEEKLY_REPORT.md`
