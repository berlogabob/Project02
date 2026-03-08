#!/usr/bin/env python3
"""
GitHub Weekly Report Generator
Fetches issues and generates a Typst weekly report based on calendar weeks

Project weeks start on Mondays. Week 1 = Mar 2-8, 2026

Usage:
    python3 scripts/generate_weekly_report.py --week 2 --output reports/week-2-report.typ
    python3 scripts/generate_weekly_report.py  # Auto-detect current week
"""

import argparse
import json
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

REPO = "berlogabob/Project02"
PROJECT_START_DATE = datetime(2026, 3, 2)  # Week 1 starts Monday, Mar 2, 2026


def get_current_week() -> int:
    """Calculate current week number from project start date."""
    today = datetime.now()
    delta = today - PROJECT_START_DATE
    week_num = (delta.days // 7) + 1
    return week_num


def get_week_date_range(week_num: int) -> tuple:
    """Get start and end dates for a given week number."""
    week_start = PROJECT_START_DATE + timedelta(weeks=(week_num - 1))
    week_end = week_start + timedelta(days=6)
    return week_start, week_end


def run_gh_command(args: list) -> list:
    cmd = (
        ["gh"]
        + args
        + [
            "--json",
            "number,title,state,labels,assignees,milestone,body,comments,createdAt,closedAt",
        ]
    )
    result = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return json.loads(result.stdout) if result.stdout else []
    except:
        return []


def get_issue_week(issue: dict) -> int:
    """Extract week number from issue labels."""
    labels = issue.get("labels", [])
    for label in labels:
        name = label.get("name", "")
        if name.startswith("week-"):
            try:
                return int(name.replace("week-", ""))
            except:
                pass
    return 0  # No week label


def get_issues_by_week(week_num: int, state: str = "open") -> tuple:
    """
    Get issues for a specific week, categorized by completion status.
    Returns: (completed_this_week, incomplete_this_week, future_week_issues)
    """
    # Get all issues with the week label
    all_issues = run_gh_command(
        ["issue", "list", "--state", "all", "--limit", "100"]
    )
    
    # Filter by week label
    week_issues = [i for i in all_issues if get_issue_week(i) == week_num]
    
    # Get closed issues from this week
    week_start, week_end = get_week_date_range(week_num)
    week_start_str = week_start.strftime("%Y-%m-%d")
    week_end_str = (week_end + timedelta(days=1)).strftime("%Y-%m-%d")
    
    # Closed issues that were updated during this week
    closed_issues = run_gh_command([
        "issue", "list", "--state", "closed",
        "--search", f"closed:>{week_start_str} closed:<{week_end_str}"
    ])
    closed_this_week = [i for i in closed_issues if get_issue_week(i) == week_num]
    
    # Open issues for this week (incomplete)
    open_issues = run_gh_command(["issue", "list", "--state", "open", "--limit", "100"])
    incomplete_this_week = [i for i in open_issues if get_issue_week(i) == week_num]
    
    # Future week issues (started early)
    future_issues = [i for i in open_issues if get_issue_week(i) > week_num]
    
    return closed_this_week, incomplete_this_week, future_issues


def get_all_open_issues() -> list:
    """Get all open issues."""
    return run_gh_command(["issue", "list", "--state", "open", "--limit", "100"])


def clean_text(text: str) -> str:
    if not text:
        return ""
    import re

    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"https?://\S+", "", text)
    return (
        text.replace("@", "at ").replace("[", "(").replace("]", ")").replace("\n", " ")
    )


def get_priority(issue: dict) -> str:
    """Extract priority from issue labels."""
    labels = issue.get("labels", [])
    for label in labels:
        name = label.get("name", "")
        if "critical" in name:
            return "critical"
        if "high" in name:
            return "high"
    return ""


def format_issue_box(issue: dict, show_week: bool = False) -> str:
    """Format a single issue as a Typst box."""
    num = issue.get("number", "?")
    title = clean_text(issue.get("title", ""))
    
    # Get milestone
    ms = issue.get("milestone", {})
    ms_title = ms.get("title", "") if ms else ""
    ms_part = f"#v(4pt) #text(size: 8pt, fill: gray)[Milestone: {ms_title}]" if ms_title else ""
    
    # Get week label
    week_num = get_issue_week(issue)
    week_part = f"#v(4pt) #text(size: 8pt, fill: gray)[Week {week_num}]" if week_num > 0 else ""
    
    # Get priority
    priority = get_priority(issue)
    priority_badge = f" #text(size: 9pt, fill: red, weight: \"bold\")[{priority.upper()}]" if priority else ""
    
    return f"""
#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#{num} - {title}]{priority_badge}
  {ms_part}
  {week_part}
])
#v(8pt)
"""


def generate_typst_report(
    week_num: int,
    completed: list,
    incomplete: list,
    future: list,
    all_open: list,
    output_path: str = None,
) -> str:
    today = datetime.now()
    week_start, week_end = get_week_date_range(week_num)
    
    # Calculate counts
    completed_count = len(completed)
    incomplete_count = len(incomplete)
    future_count = len(future)
    total_this_week = completed_count + incomplete_count
    
    # Build completed issues section
    completed_section = ""
    if not completed:
        completed_section = "#text(size: 10pt, fill: gray)[No issues completed this week.]"
    else:
        for issue in completed[:15]:
            completed_section += format_issue_box(issue)

    # Build incomplete issues section
    incomplete_section = ""
    if not incomplete:
        incomplete_section = "#text(size: 10pt, fill: green)[All planned tasks completed! 🎉]"
    else:
        for issue in incomplete[:15]:
            incomplete_section += format_issue_box(issue)

    # Build future issues section
    future_section = ""
    if future:
        for issue in future[:10]:
            future_section += format_issue_box(issue, show_week=True)

    # Calculate completion percentage
    completion_pct = round((completed_count / total_this_week * 100)) if total_this_week > 0 else 0

    typst_content = f"""// Weekly Report - Week {week_num}
// Auto-generated: {today.strftime("%Y-%m-%d")}
// Project: The Oracle That Wears Us
// Week Period: {week_start.strftime("%b %d")} - {week_end.strftime("%b %d, %Y")}

#import "../templates/daily-plan-template.typ": *

#set page(
  paper: "a4",
  margin: (x: 50pt, y: 60pt),
  footer: [
    #place(
      bottom + right,
      dx: -45pt,
      dy: -5pt,
      square(
        size: 35pt,
        fill: chapter_themes.at("1").accent,
        align(center + horizon, text(white, weight: "bold", size: 14pt)[#context counter(page).display()])
      )
    )
  ],
)

#let stats_box() = {{
  grid(columns: (1fr, 1fr, 1fr), gutter: 15pt,
    box(fill: chapter_themes.at("3").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[{completed_count}]
      text(size: 8pt)[Completed]
    ])),
    box(fill: chapter_themes.at("2").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[{incomplete_count}]
      text(size: 8pt)[Incomplete]
    ])),
    box(fill: chapter_themes.at("1").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[{future_count}]
      text(size: 8pt)[Future Weeks]
    ]))
  )
}}

// PAGE 1: COVER & SUMMARY
#report_header("1")
#section_title("1", "Week {week_num}", "Weekly Progress Report")

#table(columns: (1fr), inset: 12pt, stroke: none, fill: muted_bg, [
  #grid(columns: (1fr, 1fr), gutter: 15pt, [
    [
      *Report Date:* \\ {today.strftime("%B %d, %Y")} \\ \\
      *Week Period:* \\ {week_start.strftime("%b %d")} - {week_end.strftime("%b %d, %Y")} \\ \\
      *Project:* \\ The Oracle That Wears Us
    ],
    [
      *Team:* \\
      #grid(columns: (1fr, 1fr, 1fr), gutter: 5pt, [Nadine Allan], [Andrey Dyakov], [Dmitri Kazantsev]) \\ \\
      *Total Issues This Week:* \\ {total_this_week}
    ]
  ])
])

#v(2em)

== Executive Summary

#box(width: 100%, inset: 15pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 9pt)[
    Week {week_num} progress: {completed_count} of {total_this_week} tasks completed ({completion_pct}%).
    {future_count} tasks from future weeks already in progress.
  ]
])

#v(1em)
#stats_box()

#v(2em)

== Week Progress

#let week_progress = {completion_pct}
#box(width: 100%, height: 24pt, fill: gray.lighten(80%), inset: 0pt, radius: 3pt, [
  #box(width: week_progress * 1%, height: 100%, fill: gradient.linear(chapter_themes.at("3").grad_start, chapter_themes.at("3").grad_end), radius: 3pt)
])
#text(size: 8pt, fill: gray)[{completion_pct}% complete]

#pagebreak()

// PAGE 2: COMPLETED THIS WEEK
#report_header("2")
#section_title("2", "2.0", "Completed This Week")

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("3").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    These tasks were planned for Week {week_num} and successfully completed:
  ]
])

#v(1em)

{completed_section}

#v(2em)

== Notes

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt, fill: gray)[Review completed work and ensure quality standards are met.]
])

#pagebreak()

// PAGE 3: INCOMPLETE THIS WEEK
#report_header("3")
#section_title("3", "3.0", "Not Completed This Week")

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("2").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    These tasks were planned for Week {week_num} but remain incomplete:
  ]
])

#v(1em)

{incomplete_section}

#v(2em)

== Blockers & Challenges

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("2").accent.lighten(95%), radius: 4pt, [
  #text(size: 9pt, fill: gray)[Document any blockers or challenges that prevented completion.]
])

#pagebreak()

// PAGE 4: FUTURE WEEK TASKS (STARTED EARLY)
#report_header("4")
#section_title("4", "4.0", "Future Week Tasks (Started Early)")

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("1").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    These tasks are scheduled for future weeks but work has already begun:
  ]
])

#v(1em)

{future_section if future_section else "#text(size: 10pt, fill: gray)[No future week tasks started early.]"}

#v(2em)

== Next Week Preview

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt)[
    *Week {week_num + 1}:* {get_week_date_range(week_num + 1)[0].strftime("%b %d")} - {get_week_date_range(week_num + 1)[1].strftime("%b %d, %Y")} \\
    Focus on completing remaining Week {week_num} tasks and starting Week {week_num + 1} planned work.
  ]
])

#v(2em)

== Team Workload Overview

#table(columns: (1fr, 1fr, 1fr), inset: 10pt, stroke: 0.5pt + gray.lighten(50%),
  fill: (x, y) => if y == 0 {{ muted_bg }},
  [*Team Member*], [*Focus Area*], [*Status*],
  [Nadine Allan], [System Architecture & Integration], [Active],
  [Andrey Dyakov], [Plotter & Materialization], [Active],
  [Dmitri Kazantsev], [Generative Concepts & Fabrication], [Active])

#v(2em)

== Risks & Decisions Needed

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("4").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt, fill: gray)[Document any risks or decisions needed from the team.]
])
"""

    if output_path:
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, "w") as f:
            f.write(typst_content)
        print(f"✅ Generated: {output}")

    return typst_content


def main():
    parser = argparse.ArgumentParser(
        description="Generate weekly Typst report from GitHub issues"
    )
    parser.add_argument(
        "--week", "-w",
        type=int,
        default=None,
        help="Week number (auto-calculated if not provided)"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Output file path"
    )

    args = parser.parse_args()
    
    # Auto-detect week if not specified
    week_num = args.week if args.week else get_current_week()
    
    # Set default output path if not provided
    if not args.output:
        args.output = f"reports/week-{week_num}-report.typ"

    print(f"📊 Generating Weekly Report for Week {week_num}...")
    week_start, week_end = get_week_date_range(week_num)
    print(f"📅 Week Period: {week_start.strftime('%b %d')} - {week_end.strftime('%b %d, %Y')}")
    print()

    print("📥 Fetching issues for Week {week_num}...")
    completed, incomplete, future = get_issues_by_week(week_num)
    all_open = get_all_open_issues()
    
    print(f"   ✅ Completed this week: {len(completed)}")
    print(f"   ⏳ Incomplete this week: {len(incomplete)}")
    print(f"   🔮 Future weeks (started early): {len(future)}")
    print()

    generate_typst_report(
        week_num=week_num,
        completed=completed,
        incomplete=incomplete,
        future=future,
        all_open=all_open,
        output_path=args.output,
    )

    print()
    print("=" * 60)
    print("✅ Report generated successfully!")
    print("=" * 60)
    print()
    print("📄 To compile to PDF:")
    print(f"   typst compile {args.output} reports/week-{week_num}-report.pdf")


if __name__ == "__main__":
    main()
