#!/usr/bin/env python3
"""
Daily Plan Generator - Truly Working Version
Writes Typst code directly without f-string conflicts
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

TEAM_MEMBERS = {
    "naydino": "Nadine Allan",
    "berlogabob": "Andrey Dyakov",
    "electricianv001": "Dmitri Kazantsev",
}

REPO = "berlogabob/Project02"


def get_assigned_issues(username: str) -> list:
    cmd = [
        "gh",
        "issue",
        "list",
        "--state",
        "open",
        "--assignee",
        username,
        "--repo",
        REPO,
        "--limit",
        "50",
        "--json",
        "number,title,state,labels,assignees,milestone,body,comments,createdAt",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return []
    try:
        data = json.loads(result.stdout)
        print(f"   Found {len(data)} open issues")
        return data
    except:
        return []


def format_priority(issue: dict) -> str:
    for label in issue.get("labels", []):
        name = label.get("name", "")
        if "critical" in name:
            return "critical"
        elif "high" in name:
            return "high"
    return "medium"


def escape_typst(text: str) -> str:
    if not text:
        return ""
    return text.replace("[", "(").replace("]", ")").replace("\n", " ")


def generate_all_plans(output_dir: str) -> list:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    generated = []
    today = datetime.now()
    date_prefix = today.strftime("%Y%m%d")
    date_str = today.strftime("%d/%m")

    for username, name in TEAM_MEMBERS.items():
        print(f"\n📋 Generating plan for {name} (@{username})...")

        issues = get_assigned_issues(username)

        # Prepare issues data
        prepared_issues = []
        for issue in issues:
            prepared_issues.append(
                {
                    "number": issue["number"],
                    "title": escape_typst(issue["title"]),
                    "priority": format_priority(issue),
                    "body": escape_typst(issue.get("body", ""))[:150],
                    "milestone": issue.get("milestone", {}).get("title", "")
                    if issue.get("milestone")
                    else "",
                    "labels": ", ".join([l["name"] for l in issue.get("labels", [])]),
                    "comments": issue.get("comments", [])[:2],
                }
            )

        # Sort by priority
        priority_order = {"critical": 0, "high": 1, "medium": 2}
        prepared_issues.sort(key=lambda x: priority_order.get(x["priority"], 2))

        total = len(prepared_issues)
        high_priority = len(
            [i for i in prepared_issues if i["priority"] in ["critical", "high"]]
        )

        # Build Typst file line by line
        lines = []
        lines.append(f"// Daily Plan for {name}")
        lines.append(f"// Generated: {today.strftime('%Y-%m-%d %H:%M')}")
        lines.append("")
        lines.append('#set page(paper: "a4", margin: (x: 50pt, y: 60pt))')
        lines.append(
            '#set text(font: "Noto Sans", size: 10pt, fill: rgb("#333333"), lang: "en")'
        )
        lines.append("")
        lines.append('#let accent_blue = rgb("#2F80ED")')
        lines.append('#let accent_red = rgb("#eb3349")')
        lines.append('#let accent_green = rgb("#11998e")')
        lines.append('#let muted_bg = rgb("#f4f4f4")')
        lines.append("")

        # Header
        lines.append("#align(center)[")
        lines.append(
            '  #text(size: 24pt, weight: "bold", fill: accent_blue, "📅 Daily Plan")'
        )
        lines.append("  #v(10pt)")
        lines.append(f'  #text(size: 18pt, "{date_str}")')
        lines.append("  #v(15pt)")
        lines.append(f'  #text(size: 14pt, "{name}")')
        lines.append(f'  #text(size: 10pt, fill: gray, " (@{username})")')
        lines.append("]")
        lines.append("")
        lines.append("#v(20pt)")
        lines.append("#line(length: 100%, stroke: 1pt + accent_blue)")
        lines.append("#v(20pt)")
        lines.append("")

        # Stats
        lines.append("#grid(")
        lines.append("  columns: (1fr, 1fr, 1fr),")
        lines.append("  gutter: 15pt,")
        lines.append("  #box(")
        lines.append("    fill: accent_blue.lighten(90%),")
        lines.append("    inset: 12pt,")
        lines.append("    radius: 4pt,")
        lines.append("    align(center, [")
        lines.append(
            f'      #text(size: 20pt, weight: "bold", fill: accent_blue, "{total}")'
        )
        lines.append("      #v(4pt)")
        lines.append('      #text(size: 8pt, "Tasks")')
        lines.append("    ])")
        lines.append("  ),")
        lines.append("  #box(")
        lines.append("    fill: accent_red.lighten(90%),")
        lines.append("    inset: 12pt,")
        lines.append("    radius: 4pt,")
        lines.append("    align(center, [")
        lines.append(
            f'      #text(size: 20pt, weight: "bold", fill: accent_red, "{high_priority}")'
        )
        lines.append("      #v(4pt)")
        lines.append('      #text(size: 8pt, "High Priority")')
        lines.append("    ])")
        lines.append("  ),")
        lines.append("  #box(")
        lines.append("    fill: accent_green.lighten(90%),")
        lines.append("    inset: 12pt,")
        lines.append("    radius: 4pt,")
        lines.append("    align(center, [")
        lines.append(
            f'      #text(size: 20pt, weight: "bold", fill: accent_green, "{date_str}")'
        )
        lines.append("      #v(4pt)")
        lines.append('      #text(size: 8pt, "Date")')
        lines.append("    ])")
        lines.append("  )")
        lines.append(")")
        lines.append("")
        lines.append("#v(30pt)")
        lines.append("#line(length: 100%, stroke: 1pt + gray.lighten(70%))")
        lines.append("#v(20pt)")
        lines.append("")
        lines.append("== Your Tasks")
        lines.append("")

        # Issues
        if total == 0:
            lines.append("#box(")
            lines.append("  width: 100%,")
            lines.append("  inset: 20pt,")
            lines.append("  fill: accent_green.lighten(90%),")
            lines.append("  radius: 4pt,")
            lines.append("  align(center, [")
            lines.append('    #text(size: 12pt, "🎉 No tasks for today!")')
            lines.append("    #v(8pt)")
            lines.append(
                '    #text(size: 9pt, fill: gray, "Use this time to explore or help teammates")'
            )
            lines.append("  ])")
            lines.append(")")
        else:
            for issue in prepared_issues:
                priority_badge = (
                    f" [{issue['priority'].upper()}]"
                    if issue["priority"] in ["critical", "high"]
                    else ""
                )
                lines.append(
                    f"=== #{issue['number']} - {issue['title']}{priority_badge}"
                )
                if issue["milestone"]:
                    lines.append(f"*Milestone:* {issue['milestone']}")
                if issue["labels"]:
                    lines.append(f"*Labels:* {issue['labels']}")
                if issue["body"]:
                    lines.append("")
                    lines.append(issue["body"])
                if issue["comments"]:
                    lines.append("")
                    lines.append("*Comments:*")
                    for comment in issue["comments"]:
                        author = comment.get("author", {}).get("login", "Unknown")
                        body = escape_typst(comment.get("body", ""))[:100]
                        lines.append(f"- @{author}: {body}")
                lines.append("")
                lines.append("---")
                lines.append("")

        lines.append("#v(30pt)")
        lines.append("#line(length: 100%, stroke: 1pt + gray.lighten(70%))")
        lines.append("#v(20pt)")
        lines.append("")
        lines.append("== Planning Notes")
        lines.append("")
        lines.append("=== Today's Goals")
        lines.append("#box(")
        lines.append("  width: 100%,")
        lines.append("  height: 100pt,")
        lines.append("  inset: 15pt,")
        lines.append("  fill: muted_bg,")
        lines.append("  radius: 4pt,")
        lines.append("  [")
        lines.append('    #text(size: 9pt, fill: gray, "Write your goals here...")')
        lines.append("  ]")
        lines.append(")")
        lines.append("")
        lines.append("=== Time Blocks")
        lines.append("#table(")
        lines.append("  columns: (auto, 1fr),")
        lines.append("  inset: 8pt,")
        lines.append("  stroke: 0.5pt + gray.lighten(50%),")
        lines.append("  fill: (x, y) => if calc.even(y) { muted_bg.lighten(50%) },")
        lines.append("  [*Time*], [*Plan*],")
        lines.append("  [09:00-10:00], [],")
        lines.append("  [10:00-11:00], [],")
        lines.append("  [11:00-12:00], [],")
        lines.append("  [12:00-13:00], [Lunch],")
        lines.append("  [13:00-14:00], [],")
        lines.append("  [14:00-15:00], [],")
        lines.append("  [15:00-16:00], [],")
        lines.append("  [16:00-17:00], [],")
        lines.append(")")
        lines.append("")
        lines.append("=== End of Day Checklist")
        lines.append("#box(")
        lines.append("  width: 100%,")
        lines.append("  inset: 15pt,")
        lines.append("  fill: muted_bg,")
        lines.append("  radius: 4pt,")
        lines.append("  [")
        lines.append("    #text(size: 9pt, [")
        lines.append("      □ Update issue status")
        lines.append("      □ Add progress comments")
        lines.append("      □ Push code changes")
        lines.append("      □ Create PR if ready")
        lines.append("      □ Plan tomorrow")
        lines.append("    ])")
        lines.append("  ]")
        lines.append(")")

        # Write file
        output_file = output_path / f"{date_prefix}-daily-plan-{username}.typ"
        with open(output_file, "w") as f:
            f.write("\n".join(lines))

        print(f"✅ Generated: {output_file}")

        # Compile to PDF
        pdf_file = output_path / f"{date_prefix}-daily-plan-{username}.pdf"
        print(f"   📄 Compiling to PDF...")
        result = subprocess.run(
            ["typst", "compile", str(output_file), str(pdf_file)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"   ⚠️  Typst compilation failed:")
            print(f"   {result.stderr[:200]}")
        else:
            print(f"   ✅ Compiled: {pdf_file}")

        generated.append(
            {
                "username": username,
                "name": name,
                "typ_file": str(output_file),
                "pdf_file": str(pdf_file),
                "issue_count": len(issues),
            }
        )

    return generated


def main():
    parser = argparse.ArgumentParser(description="Generate daily plan PDFs")
    parser.add_argument("--all-members", action="store_true", help="Generate for all")
    parser.add_argument(
        "--output-dir", default="reports/daily-plans", help="Output directory"
    )

    args = parser.parse_args()

    try:
        subprocess.run(["typst", "--version"], capture_output=True, check=True)
    except:
        print("❌ Typst not found. Install with: brew install typst")
        sys.exit(1)

    print("=" * 60)
    print("📅 Daily Plan Generator")
    print("   The Oracle That Wears Us")
    print("=" * 60)
    print()

    if args.all_members:
        generated = generate_all_plans(args.output_dir)

        print("\n" + "=" * 60)
        print("✅ All Daily Plans Generated!")
        print("=" * 60)

        for plan in generated:
            print(f"\n{plan['name']} (@{plan['username']}):")
            print(f"   📄 PDF: {plan['pdf_file']}")
            print(f"   📝 Issues: {plan['issue_count']}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
