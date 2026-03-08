#!/bin/bash
# Weekly Report Generator - Local Usage
# Generates weekly report with AI summary

set -e

echo "📊 Weekly Report Generator"
echo "=========================="
echo ""

# Auto-detect current week number
WEEK_NUM=$(python3 -c "from datetime import datetime; start=datetime(2026,3,2); today=datetime.now(); print(((today-start).days//7)+1)")

echo "📅 Current week: ${WEEK_NUM}"
echo ""

# Generate AI summary first
echo "🤖 Generating AI summary..."
python3 scripts/generate_ai_summary.py --week ${WEEK_NUM} --api qwen || echo "⚠️  AI summary skipped (API not available)"
echo ""

# Generate weekly report
echo "📝 Generating weekly report..."
python3 scripts/generate_weekly_report.py --week ${WEEK_NUM} --output reports/week-${WEEK_NUM}-report.typ

# Compile to PDF
echo "📄 Compiling to PDF..."
typst compile --root . reports/week-${WEEK_NUM}-report.typ reports/week-${WEEK_NUM}-report.pdf

echo ""
echo "✅ Done!"
echo "📁 Report: reports/week-${WEEK_NUM}-report.pdf"
echo ""

# Open PDF (macOS)
if [[ "$OSTYPE" == "darwin"* ]]; then
    open reports/week-${WEEK_NUM}-report.pdf
fi
