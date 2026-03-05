#!/usr/bin/env python3
"""
Daily Plan Generator - Styled Version
Uses Project02-Plan.typ styling
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


def run_gh_command(args: list) -> list:
    """Run a GitHub CLI command and return JSON result"""
    cmd = (
        ["gh"]
        + args
        + [
            "--json",
            "number,title,state,labels,assignees,milestone,body,comments,createdAt",
        ]
    )
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return []
    return json.loads(result.stdout)


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
        elif "medium" in name:
            return "medium"
        elif "low" in name:
            return "low"
    return "medium"


def escape_typst(text: str) -> str:
    """Escape special Typst characters"""
    if not text:
        return ""
    return text.replace("[", "(").replace("]", ")").replace("\n", " ")


def generate_styled_typst(
    member_name: str, member_username: str, issues: list, output_path: str
) -> str:
    """Generate styled Typst file matching Project02-Plan.typ"""

    today = datetime.now()
    date_str = f"{today.day:02d}/{today.month:02d}"
    year_month_day = today.strftime("%Y%m%d")

    # Prepare issues
    prepared_issues = []
    for issue in issues:
        prepared_issues.append(
            {
                "number": issue["number"],
                "title": escape_typst(issue["title"]),
                "priority": format_priority(issue),
                "body": escape_typst(issue.get("body", ""))[:200],
                "milestone": issue.get("milestone"),
                "labels": issue.get("labels", []),
                "comments": issue.get("comments", [])[:3],  # Last 3 comments
            }
        )

    # Sort by priority
    priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    prepared_issues.sort(key=lambda x: priority_order.get(x["priority"], 2))

    # Count stats
    total = len(prepared_issues)
    high_priority = len(
        [i for i in prepared_issues if i["priority"] in ["critical", "high"]]
    )

    # Generate issues content
    issues_content = ""
    for i, issue in enumerate(prepared_issues):
        priority_badge = (
            f"[#{issue['priority'].upper()}]"
            if issue["priority"] in ["critical", "high"]
            else ""
        )
        issues_content += f"""
=== #{issue["number"]} - {issue["title"]} {priority_badge}
"""
        if issue["milestone"]:
            issues_content += f"*Milestone:* {issue['milestone']['title']}\n"

        # Labels
        if issue["labels"]:
            label_names = [l["name"] for l in issue["labels"]]
            issues_content += f"*Labels:* {', '.join(label_names)}\n"

        if issue["body"]:
            issues_content += f"\n{issue['body']}\n"

        # Comments
        if issue["comments"]:
            issues_content += "\n*Recent Comments:*\n"
            for comment in issue["comments"]:
                author = comment.get("author", {}).get("login", "Unknown")
                body = escape_typst(comment.get("body", ""))[:100]
                date = comment.get("createdAt", "")[:10]
                issues_content += f"- @{author} ({date}): {body}\n"

        issues_content += "\n---\n"

    # Full Typst content with Project02-Plan.typ styling
    typst_content = f'''// Daily Plan for {member_name}
// Generated: {today.strftime("%Y-%m-%d %H:%M")}
// Project: The Oracle That Wears Us

// --- CONFIGURATION (from Project02-Plan.typ) ---
#set page(
  paper: "a4",
  margin: (x: 50pt, y: 60pt),
)

#set text(
  font: "Noto Sans",
  size: 10pt,
  fill: rgb("#333333"),
  lang: "en"
)

// --- THEME DEFINITION ---
#let chapter_themes = (
  "1": (
    grad_start: rgb("#2F80ED"),
    grad_end: rgb("#9B51E0"),
    accent: rgb("#33A1C9"),
    page_bg: rgb("#A5C7F3")
  ),
  "2": (
    grad_start: rgb("#eb3349"),
    grad_end: rgb("#f45c43"),
    accent: rgb("#e74c3c"),
    page_bg: rgb("#ff9a9e")
  ),
  "3": (
    grad_start: rgb("#11998e"),
    grad_end: rgb("#38ef7d"),
    accent: rgb("#1b5e20"),
    page_bg: rgb("#c8e6c9")
  ),
  "4": (
    grad_start: rgb("#F2994A"),
    grad_end: rgb("#F2C94C"),
    accent: rgb("#d35400"),
    page_bg: rgb("#fdebd0")
  )
)

#let muted_bg = rgb("#f4f4f4")

// --- REUSABLE COMPONENTS ---
#let report_header(ch_idx, category: "DAILY PLAN") = {{
  let t = chapter_themes.at(ch_idx)
  move(dy: -20pt)[
    #box(
      width: 100%,
      height: 30pt,
      fill: gradient.linear(t.grad_start, t.grad_end),
      inset: (right: 15pt),
      align(right + horizon, text(white, weight: "bold", tracking: 1.5pt, size: 8pt)[#upper(category)])
    )
  ]
}}

#let section_title(ch_idx, num, title) = {{
  let t = chapter_themes.at(ch_idx)
  v(20pt)
  text(fill: t.accent, size: 22pt, weight: "extrabold")[#num]
  v(-12pt)
  text(fill: t.accent, size: 22pt, weight: "bold")[#upper(title)]
  v(20pt)
}}

#let page_footer(ch_idx, num) = {{
  let t = chapter_themes.at(ch_idx)
  place(
    bottom + right,
    dx: 30pt,
    dy: 30pt,
    square(
      size: 35pt,
      fill: t.page_bg,
      align(center + horizon, text(white, weight: "bold", size: 14pt)[#num])
    )
  )
}}

#let priority_badge(priority) = {{
  let colors = (
    "critical": (bg: rgb("#B60205"), fg: white),
    "high": (bg: rgb("#D93F0B"), fg: white),
    "medium": (bg: rgb("#F9D0C4"), fg: rgb("#D93F0B")),
    "low": (bg: rgb("#0E8A16"), fg: white)
  )
  let c = colors.at(priority, (bg: gray, fg: white))
  box(
    fill: c.bg,
    inset: (x: 8pt, y: 3pt),
    radius: 3pt,
    text(size: 7pt, fill: c.fg, weight: "bold")[#upper(priority)]
  )
}}

#let issue_card(issue_num, title, priority, body, milestone, labels) = {{
  #box(
    width: 100%,
    inset: 12pt,
    fill: muted_bg.lighten(50%),
    radius: 4pt,
    stroke: 1pt + gray.lighten(60%),
    [
      #grid(
        columns: (1fr, auto),
        gutter: 10pt,
        [
          #text(size: 12pt, weight: "bold", [#{{issue_num}} - {{title}}])
          #if milestone != "" [
            #v(4pt)
            #text(size: 8pt, fill: gray, [Milestone: {{milestone}}])
          ]
          #if labels != "" [
            #v(4pt)
            #text(size: 8pt, fill: gray, [{{labels}}])
          ]
        ],
        align(top + right, [
          #if priority != "" [
            #priority_badge(priority)
          ]
        ])
      )
      #if body != "" [
        #v(8pt)
        #text(size: 9pt, fill: gray, {{body}})
      ]
    ]
  )
}}

#let stats_row(total_tasks, high_priority_count) = {{
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 15pt,
    box(
      fill: chapter_themes.at("1").accent.lighten(90%),
      inset: 12pt,
      radius: 4pt,
      align(center, [
        #text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent, [{total_tasks}])
        #text(size: 8pt, [Total Tasks])
      ])
    ),
    box(
      fill: chapter_themes.at("2").accent.lighten(90%),
      inset: 12pt,
      radius: 4pt,
      align(center, [
        #text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent, [{high_priority_count}])
        #text(size: 8pt, [High Priority])
      ])
    ),
    box(
      fill: chapter_themes.at("3").accent.lighten(90%),
      inset: 12pt,
      radius: 4pt,
      align(center, [
        #text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent, [{today.strftime("%d/%m")}])
        #text(size: 8pt, [Date])
      ])
    )
  )
}}

// --- PAGE 1: DAILY PLAN ---
#report_header("1")

#section_title("1", "{date_str}", "Daily Plan")

#table(
  columns: (1fr),
  inset: 12pt,
  stroke: none,
  fill: muted_bg,
  [
    #grid(
      columns: (1fr, 1fr),
      gutter: 15pt,
      [
        *Team Member:* \ {member_name} \\ #text(size: 8pt)[@{member_username}] \\ \\
        *Date:* \\ {today.strftime("%d %B %Y")}
      ],
      [
        *Project:* \ The Oracle That Wears Us \ \
        *Milestone:* \ 1st milestone: Documentation
      ]
    )
  ]
)

#v(2em)

== Your Tasks for Today

#if {total} == 0 [
  #box(
    width: 100%,
    inset: 20pt,
    fill: chapter_themes.at("3").accent.lighten(90%),
    radius: 4pt,
    align(center, [
      #text(size: 12pt)[🎉 No tasks assigned for today!]
      #v(8pt)
      #text(size: 9pt, fill: gray)[Use this time to explore, experiment, or help teammates]
    ])
  )
] else [
  #stats_row({total}, {high_priority})
  
  #v(2em)
  
  == Priority Tasks
  #line(length: 100%, stroke: 1pt + chapter_themes.at("2").accent)
  #v(10pt)
  
  {issues_content}
  
  #v(2em)
  
  == Planning Notes
  
  #box(
    width: 100%,
    inset: 15pt,
    fill: muted_bg,
    radius: 4pt,
    [
      #text(size: 9pt)[
        1. *Review* each task and its comments \
        2. *Check* recent updates \
        3. *Estimate* time needed \
        4. *Plan* your approach \
        5. *Comment* your progress
      ]
    ]
  )
]

#page_footer("1", "1")
#pagebreak()

// --- PAGE 2: PLANNING ---
#report_header("2")

#section_title("2", "2.0", "Planning Notes")

== Today's Goals

#box(
  width: 100%,
  height: 150pt,
  inset: 15pt,
  fill: muted_bg.lighten(50%),
  radius: 4pt,
  stroke: 1pt + gray.lighten(60%),
  [
    #text(size: 9pt, fill: gray, style: "italic")[
      Write your main goals for today here...
    ]
  ]
)

#v(2em)

== Time Blocks

#table(
  columns: (auto, 1fr),
  inset: 8pt,
  stroke: 0.5pt + gray.lighten(50%),
  fill: (x, y) => if calc.even(y) {{ muted_bg.lighten(50%) }},
  [*Time*], [*Plan*],
  [09:00 - 10:00], [],
  [10:00 - 11:00], [],
  [11:00 - 12:00], [],
  [12:00 - 13:00], [Lunch Break],
  [13:00 - 14:00], [],
  [14:00 - 15:00], [],
  [15:00 - 16:00], [],
  [16:00 - 17:00], [],
)

#v(2em)

== Blockers & Questions

#box(
  width: 100%,
  height: 100pt,
  inset: 15pt,
  fill: chapter_themes.at("2").accent.lighten(95%),
  radius: 4pt,
  stroke: 1pt + chapter_themes.at("2").accent.lighten(70%),
  [
    #text(size: 9pt, fill: gray, style: "italic")[
      List any blockers or questions for the team...
    ]
  ]
)

#v(2em)

== End of Day Checklist

#box(
  width: 100%,
  inset: 15pt,
  fill: muted_bg,
  radius: 4pt,
  [
    #text(size: 9pt)[
      □ *Update* issue status (In Progress → Review/Done) \
      □ *Add* progress comments to issues \
      □ *Push* code changes to GitHub \
      □ *Create* PR if work is ready for review \
      □ *Prepare* demo/screenshots for tomorrow \
      □ *Plan* tomorrow's tasks
    ]
  ]
)

#page_footer("2", "2")
'''

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
        generate_styled_typst(name, username, issues, str(output_file))

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
