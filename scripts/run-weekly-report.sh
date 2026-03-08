#!/bin/bash
# Weekly Report Generator - Local Usage
# Generates weekly report (AI summary optional - slow locally)

set -e

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$( cd "$SCRIPT_DIR/.." && pwd )"

cd "$PROJECT_DIR"

echo "📊 Weekly Report Generator"
echo "=========================="
echo ""

# Auto-detect current week number
WEEK_NUM=$(python3 -c "from datetime import datetime; start=datetime(2026,3,2); today=datetime.now(); print(((today-start).days//7)+1)")

echo "📅 Current week: ${WEEK_NUM}"
echo ""

# AI Summary (optional - can be slow locally)
echo "🤖 AI Summary: (y/n to skip, default: n)"
read -t 5 -n 1 answer || answer="n"
echo ""

if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
    echo "⏳ Generating AI summary... (may take 30-60s)"
    python3 "$SCRIPT_DIR/generate_ai_summary.py" --week ${WEEK_NUM} --api ollama || echo "⚠️  Skipped"
    echo ""
else
    echo "⚠️  AI summary skipped (faster)"
    echo "   For AI summary, run: python3 scripts/generate_ai_summary.py --week ${WEEK_NUM} --api ollama"
    echo ""
fi

# Generate weekly report
echo "📝 Generating weekly report..."
python3 "$SCRIPT_DIR/generate_weekly_report.py" --week ${WEEK_NUM} --output reports/week-${WEEK_NUM}-report.typ

# Compile to PDF
echo "📄 Compiling to PDF..."
typst compile --root . reports/week-${WEEK_NUM}-report.typ reports/week-${WEEK_NUM}-report.pdf

echo ""
echo "✅ Done!"
echo "📁 Report: reports/week-${WEEK_NUM}-report.pdf"
echo ""
echo "💡 Note: AI summary works best in GitHub Actions (automatic)."
echo "   Local Ollama can be slow. For faster local reports, skip AI."
echo ""

# Open PDF (macOS)
if [[ "$OSTYPE" == "darwin"* ]]; then
    open reports/week-${WEEK_NUM}-report.pdf
fi
