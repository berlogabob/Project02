#!/bin/bash
# Weekly Report Generator - Local Usage
# Generates weekly report with optional AI summary

set -e

# Get script directory (handles being called from any location)
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

# Generate AI summary (optional, with 30s timeout using Python)
echo "🤖 Generating AI summary... (timeout: 30s)"
python3 -c "
import subprocess, sys, signal, os
try:
    proc = subprocess.Popen(
        ['python3', '$SCRIPT_DIR/generate_ai_summary.py', '--week', '${WEEK_NUM}', '--api', 'ollama'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    try:
        out, err = proc.communicate(timeout=30)
        print(out.decode())
        print(err.decode(), file=sys.stderr)
    except subprocess.TimeoutExpired:
        proc.kill()
        print('⚠️  AI summary timeout (30s)', file=sys.stderr)
except Exception as e:
    print(f'⚠️  AI summary error: {e}', file=sys.stderr)
" 2>&1
echo ""

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

# Open PDF (macOS)
if [[ "$OSTYPE" == "darwin"* ]]; then
    open reports/week-${WEEK_NUM}-report.pdf
fi
