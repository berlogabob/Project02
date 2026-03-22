#!/usr/bin/env python3
"""
Local test script for the weekly report generation pipeline.

Runs the full MD→JSON→Typst pipeline with fixed, deterministic test data
so it can be executed offline (no GitHub CLI, no Ollama required).

Usage:
    python3 scripts/test_report_generation.py
    python3 scripts/test_report_generation.py --week 3 --output /tmp/test-report.typ
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

# Ensure the scripts/ directory is importable when run from anywhere
sys.path.insert(0, str(Path(__file__).parent))

from validate_report_data import (
    build_report_json,
    sanitize_for_typst,
    save_report_json,
    validate_ai_summary,
    sanitize_summary,
)

# ---------------------------------------------------------------------------
# Fixed test data (Cyrillic strings intentionally included)
# ---------------------------------------------------------------------------

FIXED_COMPLETED = [
    {
        "number": 101,
        "title": "Design #Plotter firmware architecture",
        "body": "Designed the core firmware for CNC plotter. Refs **Parent:** #50. "
                "URL stripped: https://example.com",
        "labels": [{"name": "week-3"}, {"name": "high-priority"}, {"name": "show-in-report"}],
        "assignees": [{"login": "berlogabob"}],
    },
    {
        "number": 102,
        "title": "Генерация концептов [AI] & фабрикация",
        "body": "Использовали Stable Diffusion $formula$ для генерации визуальных [концептов].",
        "labels": [{"name": "week-3"}, {"name": "medium"}],
        "assignees": [{"login": "electricianv001"}],
    },
    {
        "number": 103,
        "title": "System integration – wiring & sensors",
        "body": "Integrated Arduino Mega with stepper drivers. #critical path item.",
        "labels": [{"name": "week-3"}, {"name": "show-in-report"}],
        "assignees": [{"login": "naydino"}],
    },
]

FIXED_INCOMPLETE = [
    {
        "number": 104,
        "title": "Calibrate *plotter* axis [X, Y]",
        "body": "Axis calibration not finished. Next step: tuning PID parameters.",
        "labels": [{"name": "week-3"}],
        "assignees": [{"login": "berlogabob"}],
    },
]

FIXED_FUTURE = [
    {
        "number": 201,
        "title": "Week 4: Build enclosure #2",
        "body": "Enclosure design pending final dimensions.",
        "labels": [{"name": "week-4"}],
        "assignees": [{"login": "naydino"}],
    },
]

# An AI summary intentionally containing problematic characters
FIXED_AI_SUMMARY_RAW = """\
- Implemented #plotter firmware with multi-axis control [completed]
- Created AI-generated visual *concepts* using Stable Diffusion $model$
- Integrated sensor suite and Arduino firmware for system [wiring]
- Calibration of X/Y axes is 60% done; PID tuning in progress
"""

# ---------------------------------------------------------------------------
# Minimal Typst generation (mirrors logic in generate_weekly_report.py)
# ---------------------------------------------------------------------------


def build_typst_from_json(report_data: dict) -> str:
    """Convert the intermediate JSON into a Typst source string."""
    week = report_data["week"]
    meta = report_data["metadata"]
    bullets = report_data["summary"]["bullets"]
    issues = report_data["issues"]

    completed = [i for i in issues if i["status"] == "completed"]
    incomplete = [i for i in issues if i["status"] == "in_progress"]
    future = [i for i in issues if i["status"] == "future"]

    def issue_block(issue: dict) -> str:
        num = issue["number"]
        title = issue["title"]
        body = issue["body"][:150]
        priority = issue["priority"].upper()
        assignee = issue["assignee"] or "—"
        return (
            f'#box(width: 100%, inset: 10pt, radius: 4pt, fill: rgb("\\#f4f4f4"), [\n'
            f"  *\\#{num}* — {title} \\\n"
            f"  #text(size: 8pt, fill: gray)[{priority} | {assignee}] \\\n"
            f"  #text(size: 8pt)[{body}]\n"
            f"])\n#v(4pt)\n"
        )

    completed_section = "\n".join(issue_block(i) for i in completed) or (
        '#text(fill: gray)[No completed issues.]\n'
    )
    incomplete_section = "\n".join(issue_block(i) for i in incomplete) or (
        '#text(fill: green)[All tasks completed! 🎉]\n'
    )
    future_section = "\n".join(issue_block(i) for i in future) or (
        '#text(fill: gray)[No future tasks started early.]\n'
    )

    summary_lines = "\n".join(f"- {b}" for b in bullets) if bullets else "- No summary available."

    generated_at = meta.get("generated_at", "unknown")
    github_sha = (meta.get("github_sha") or "local")[:7]
    qwen_model = meta.get("qwen_model") or "n/a"

    return f"""\
// Weekly Report - Week {week} (TEST BUILD)
// Generated: {generated_at}
// SHA: {github_sha}  Model: {qwen_model}

#import "../templates/daily-plan-template.typ": *

#set page(paper: "a4", margin: (x: 50pt, y: 60pt))
#set text(size: 10pt, fill: rgb("#333333"), lang: "en")

= Week {week} Weekly Progress Report (Test)

#box(width: 100%, inset: 12pt, fill: rgb("#f4f4f4"), radius: 4pt, [
  #text(size: 9pt)[*Generated:* {generated_at}] \\
  #text(size: 9pt)[*SHA:* {github_sha} | *Model:* {qwen_model}]
])

#v(1em)

== Executive Summary

#box(width: 100%, inset: 15pt, fill: rgb("#e8f5e9"), radius: 4pt, [
  #text(size: 9pt, weight: "bold")[Week Summary:]
  #v(4pt)
  #text(size: 9pt)[{summary_lines}]
])

#pagebreak()

== Completed This Week

{completed_section}

#pagebreak()

== Incomplete This Week

{incomplete_section}

#pagebreak()

== Future Weeks (Started Early)

{future_section}
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Test report generation with fixed data")
    parser.add_argument("--week", "-w", type=int, default=3, help="Week number for the test report")
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default=None,
        help="Path for the generated .typ file (default: /tmp/test-week-N-report.typ)",
    )
    parser.add_argument(
        "--json-output",
        type=str,
        default=None,
        help="Path to save intermediate JSON (default: /tmp/test-week-N-data.json)",
    )
    parser.add_argument(
        "--compile",
        action="store_true",
        help="Attempt to compile the generated .typ to PDF via `typst compile`",
    )
    args = parser.parse_args()

    week = args.week
    typ_path = args.output or f"/tmp/test-week-{week}-report.typ"
    json_path = args.json_output or f"/tmp/test-week-{week}-data.json"

    print("=" * 60)
    print(f"🧪 Test Report Generation — Week {week}")
    print("=" * 60)

    # Step 1: Sanitize AI summary
    print("\n📋 Step 1: Sanitize AI summary …")
    sanitized = sanitize_summary(FIXED_AI_SUMMARY_RAW)
    is_valid, errors = validate_ai_summary(sanitized)
    if is_valid:
        print("  ✅ Summary is valid after sanitization")
    else:
        print("  ⚠️  Summary still has issues after sanitization:")
        for err in errors:
            print(f"     • {err}")
    print(f"  Summary:\n{sanitized}")

    # Step 2: Build intermediate JSON
    print("\n📦 Step 2: Build intermediate JSON …")
    report_data = build_report_json(
        week_num=week,
        completed=FIXED_COMPLETED,
        incomplete=FIXED_INCOMPLETE,
        future=FIXED_FUTURE,
        ai_summary=sanitized,
        github_sha="test000",
        qwen_model="test-fixed-data",
    )
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
    print(f"  ✅ JSON saved to: {json_path}")
    print(f"  Issues: {report_data['metadata']['issues_count']}")

    # Step 3: Generate Typst source
    print("\n📝 Step 3: Generate Typst source …")
    typst_src = build_typst_from_json(report_data)
    with open(typ_path, "w", encoding="utf-8") as f:
        f.write(typst_src)
    print(f"  ✅ Typst source saved to: {typ_path}")

    # Step 4: Optionally compile to PDF
    if args.compile:
        print("\n📄 Step 4: Compile to PDF …")
        repo_root = str(Path(__file__).parent.parent)
        pdf_path = typ_path.replace(".typ", ".pdf")
        result = subprocess.run(
            ["typst", "compile", "--root", repo_root, typ_path, pdf_path],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0 and Path(pdf_path).exists():
            size = Path(pdf_path).stat().st_size
            print(f"  ✅ PDF compiled: {pdf_path}  ({size:,} bytes)")
        else:
            print("  ❌ PDF compilation failed:")
            print(result.stdout)
            print(result.stderr)
            sys.exit(1)

    print("\n✅ All steps completed successfully!")
    print(f"   Typst: {typ_path}")
    print(f"   JSON:  {json_path}")


if __name__ == "__main__":
    main()
