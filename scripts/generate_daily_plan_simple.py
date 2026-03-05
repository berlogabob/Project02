#!/usr/bin/env python3
"""
Daily Plan Generator - Simple Version with Issues List
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
    """Get open issues assigned to a specific user"""
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
        print(f"Warning: {result.stderr[:100]}")
        return []
    try:
        data = json.loads(result.stdout)
        print(f"   Found {len(data)} open issues")
        return data
    except Exception as e:
        print(f"Warning: Could not parse JSON: {e}")
        return []


def format_priority(issue: dict) -> str:
    """Extract priority from labels"""
    for label in issue.get("labels", []):
        name = label.get("name", "")
        if "critical" in name:
            return "critical"
        elif "high" in name:
            return "high"
    return "medium"


def escape_typst(text: str) -> str:
    """Escape special Typst characters"""
    if not text:
        return ""
    return text.replace("[", "(").replace("]", ")").replace("\n", " ")


def generate_simple_typst(
    member_name: str, member_username: str, issues: list, output_path: str
) -> str:
    """Generate simple Typst file with issues list"""

    today = datetime.now()
    date_str = today.strftime("%d/%m")

    # Prepare issues
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

    # Count stats
    total = len(prepared_issues)
    high_priority = len(
        [i for i in prepared_issues if i["priority"] in ["critical", "high"]]
    )

    # Generate issues content as plain text (will be inserted into template)
    issues_text = ""
    for i, issue in enumerate(prepared_issues):
        priority_badge = (
            f" [{issue['priority'].upper()}]"
            if issue["priority"] in ["critical", "high"]
            else ""
        )
        issues_text += f"=== #{issue['number']} - {issue['title']}{priority_badge}\n"
        if issue["milestone"]:
            issues_text += f"*Milestone:* {issue['milestone']}\n"
        if issue["labels"]:
            issues_text += f"*Labels:* {issue['labels']}\n"
        if issue["body"]:
            issues_text += f"\n{issue['body']}\n"
        if issue["comments"]:
            issues_text += "\n*Comments:*\n"
            for comment in issue["comments"]:
                author = comment.get("author", {}).get("login", "Unknown")
                body = escape_typst(comment.get("body", ""))[:100]
                issues_text += f"- @{author}: {body}\n"
        issues_text += "\n---\n\n"

    # Simple Typst template
    typst_content = f'''// Daily Plan for {member_name}
// Generated: {today.strftime("%Y-%m-%d %H:%M")}

#set page(paper: "a4", margin: (x: 50pt, y: 60pt))
#set text(font: "Noto Sans", size: 10pt, fill: rgb("#333333"), lang: "en")

// Colors from Project02-Plan.typ
#let accent_blue = rgb("#2F80ED")
#let accent_red = rgb("#eb3349")
#let accent_green = rgb("#11998e")
#let accent_yellow = rgb("#F2994A")
#let muted_bg = rgb("#f4f4f4")

// Header
#align(center)[
  #text(size: 24pt, weight: "bold", fill: accent_blue, "📅 Daily Plan")
  #v(10pt)
  #text(size: 18pt, "{date_str}")
  #v(15pt)
  #text(size: 14pt, "{member_name}")
  #text(size: 10pt, fill: gray, " (@{member_username})")
]

#v(20pt)
#line(length: 100%, stroke: 1pt + accent_blue)
#v(20pt)

// Stats
#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 15pt,
  #box(
    fill: accent_blue.lighten(90%),
    inset: 12pt,
    radius: 4pt,
    align(center, [
      #text(size: 20pt, weight: "bold", fill: accent_blue, "{total}")
      #v(4pt)
      #text(size: 8pt, "Tasks")
    ])
  ),
  #box(
    fill: accent_red.lighten(90%),
    inset: 12pt,
    radius: 4pt,
    align(center, [
      #text(size: 20pt, weight: "bold", fill: accent_red, "{high_priority}")
      #v(4pt)
      #text(size: 8pt, "High Priority")
    ])
  ),
  #box(
    fill: accent_green.lighten(90%),
    inset: 12pt,
    radius: 4pt,
    align(center, [
      #text(size: 20pt, weight: "bold", fill: accent_green, "{today.strftime("%d/%m")}")
      #v(4pt)
      #text(size: 8pt, "Date")
    ])
  )
)

#v(30pt)
#line(length: 100%, stroke: 1pt + gray.lighten(70%))
#v(20pt)

== Your Tasks

#if {total} == 0 [
  #box(
    width: 100%,
    inset: 20pt,
    fill: accent_green.lighten(90%),
    radius: 4pt,
    align(center, [
      #text(size: 12pt, "🎉 No tasks for today!")
      #v(8pt)
      #text(size: 9pt, fill: gray, "Use this time to explore or help teammates")
    ])
  )
] else [
'''

    # Add issues as markdown (will be rendered by Typst)
    typst_content += issues_text

    typst_content += """
#v(30pt)
#line(length: 100%, stroke: 1pt + gray.lighten(70%))
#v(20pt)

== Planning Notes

=== Today's Goals
#box(
  width: 100%,
  height: 100pt,
  inset: 15pt,
  fill: muted_bg,
  radius: 4pt,
  [
    #text(size: 9pt, fill: gray, "Write your goals here...")
  ]
)

=== Time Blocks
#table(
  columns: (auto, 1fr),
  inset: 8pt,
  stroke: 0.5pt + gray.lighten(50%),
  fill: (x, y) => if calc.even(y) { muted_bg.lighten(50%) },
  [*Time*], [*Plan*],
  [09:00-10:00], [],
  [10:00-11:00], [],
  [11:00-12:00], [],
  [12:00-13:00], [Lunch],
  [13:00-14:00], [],
  [14:00-15:00], [],
  [15:00-16:00], [],
  [16:00-17:00], [],
)

=== End of Day Checklist
#box(
  width: 100%,
  inset: 15pt,
  fill: muted_bg,
  radius: 4pt,
  [
    #text(size: 9pt, [
      □ Update issue status
      □ Add progress comments
      □ Push code changes
      □ Create PR if ready
      □ Plan tomorrow
    ])
  ]
)
"""

    # Write to file
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w") as f:
        f.write(typst_content)

    print(f"✅ Generated: {output}")
    return typst_content


def generate_all_plans(output_dir: str) -> list:
    """Generate daily plans for all team members"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    generated = []
    today = datetime.now()
    date_prefix = today.strftime("%Y%m%d")

    for username, name in TEAM_MEMBERS.items():
        print(f"\n📋 Generating plan for {name} (@{username})...")

        issues = get_assigned_issues(username)

        # Use new filename format: YYYYMMDD-daily-plan-username.typ
        output_file = output_path / f"{date_prefix}-daily-plan-{username}.typ"
        generate_simple_typst(name, username, issues, str(output_file))

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

    # Check if typst is installed
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
