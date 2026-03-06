#!/usr/bin/env python3
"""
GitHub Weekly Report Generator
Fetches issues and generates a Typst weekly report

Usage:
    python3 scripts/generate_weekly_report.py --week 1 --output reports/week-01-report.typ
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO = "berlogabob/Project02"


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


def get_completed_issues(milestone: str = None) -> list:
    filters = ["state:closed", "updated:>last-week"]
    if milestone:
        filters.append(f'milestone:"{milestone}"')
    return run_gh_command(
        ["issue", "list", "--state", "closed", "--search", " ".join(filters)]
    )


def get_in_progress_issues(milestone: str = None) -> list:
    filters = ["state:open"]
    if milestone:
        filters.append(f'milestone:"{milestone}"')
    return run_gh_command(
        ["issue", "list", "--state", "open", "--search", " ".join(filters)]
    )


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


def generate_typst_report(
    week_num: int,
    completed: list,
    in_progress: list,
    milestone: str = None,
    output_path: str = None,
) -> str:
    today = datetime.now()

    # Calculate counts
    completed_count = len(completed)
    in_progress_count = len(in_progress)
    total_count = completed_count + in_progress_count

    # Build completed issues section
    completed_section = ""
    if not completed:
        completed_section = (
            "#text(size: 10pt, fill: gray)[No issues completed this week.]"
        )
    else:
        for issue in completed[:10]:
            num = issue.get("number", "?")
            title = clean_text(issue.get("title", ""))
            ms_title = (
                issue.get("milestone", {}).get("title", "")
                if issue.get("milestone")
                else ""
            )
            ms_part = (
                f"#v(4pt) #text(size: 8pt, fill: gray)[Milestone: {ms_title}]"
                if ms_title
                else ""
            )
            completed_section += f"""
#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#{num} - {title}]
  {ms_part}
])
#v(8pt)
"""

    # Build in-progress issues section
    in_progress_section = ""
    if not in_progress:
        in_progress_section = "#text(size: 10pt, fill: gray)[No issues in progress.]"
    else:
        for issue in in_progress[:10]:
            num = issue.get("number", "?")
            title = clean_text(issue.get("title", ""))
            ms_title = (
                issue.get("milestone", {}).get("title", "")
                if issue.get("milestone")
                else ""
            )
            ms_part = (
                f"#v(4pt) #text(size: 8pt, fill: gray)[Milestone: {ms_title}]"
                if ms_title
                else ""
            )
            in_progress_section += f"""
#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#{num} - {title}]
  {ms_part}
])
#v(8pt)
"""

    typst_content = f"""// Weekly Report - Week {week_num}
// Auto-generated: {today.strftime("%Y-%m-%d")}
// Project: The Oracle That Wears Us

#import "../templates/daily-plan-template.typ": *

#set page(
  paper: "a4",
  margin: (x: 50pt, y: 60pt),
  numbering: (..args) => {{
    let num = args.pos().first()
    page_number_badge(num, "1")
  }},
)

// Weekly report uses all components from the template
// Page numbering is automatic via the template
// Note: report_header, section_title, task_table are imported from template

#let stats_box() = {{
  grid(columns: (1fr, 1fr, 1fr), gutter: 15pt,
    box(fill: chapter_themes.at("1").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[{completed_count}]
      text(size: 8pt)[Completed]
    ])),
    box(fill: chapter_themes.at("2").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[{in_progress_count}]
      text(size: 8pt)[In Progress]
    ])),
    box(fill: chapter_themes.at("3").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[{total_count}]
      text(size: 8pt)[Total]
    ]))
  )
}}

// PAGE 1: COVER & SUMMARY
#report_header("1")
#section_title("1", "Week {week_num}", "Weekly Progress Report")

#table(columns: (1fr), inset: 12pt, stroke: none, fill: muted_bg, [
  #grid(columns: (1fr, 1fr), gutter: 15pt, [
    *Report Date:* \\ {today.strftime("%B %d, %Y")} \\ \\
    *Milestone:* \\ {milestone or "TBD"} \\ \\
    *Week Period:* \\ Week {week_num}
  ], [
    *Project:* \\ The Oracle That Wears Us \\ \\
    *Team:* \\
    #grid(columns: (1fr, 1fr, 1fr), gutter: 5pt, [Nadine Allan], [Andrey Dyakov], [Dmitri Kazantsev])
  ])
])

#v(2em)

== Executive Summary

#box(width: 100%, inset: 15pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 9pt)[
    This week, the team made progress on GitHub issues.
    Total: {total_count} issues | Completed: {completed_count} | In Progress: {in_progress_count}
  ]
])

#v(1em)
#stats_box()

#v(2em)

== Key Achievements This Week

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("3").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    - Completed {completed_count} issues
    - Progress on {milestone or "current milestone"}
    - Team collaboration through GitHub
  ]
])

#pagebreak()

// PAGE 2: COMPLETED WORK
#report_header("2")
#section_title("2", "2.0", "Completed Issues")

{completed_section}

#v(2em)

== Notes & Observations

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt, fill: gray)[All completed issues have been reviewed and merged.]
])

#pagebreak()

// PAGE 3: IN PROGRESS
#report_header("3")
#section_title("3", "3.0", "Work In Progress")

== Current Sprint

{in_progress_section}

#v(2em)

== Blockers & Challenges

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("2").accent.lighten(95%), radius: 4pt, [
  #text(size: 9pt, fill: gray)[No major blockers this week.]
])

#pagebreak()

// PAGE 4: NEXT WEEK PLAN
#report_header("4")
#section_title("4", "4.0", "Next Week Plan")

== Planned Focus

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt)[
    - Continue with remaining milestone tasks
    - Review and merge pending PRs
    - Prepare for next week's sprint goals
  ]
])

#v(2em)

== Milestone Progress

#let milestone_progress = 25
#box(width: 100%, height: 20pt, fill: gray.lighten(80%), inset: 0pt, radius: 3pt, [
  #box(width: milestone_progress * 1%, height: 100%, fill: gradient.linear(chapter_themes.at("1").grad_start, chapter_themes.at("1").grad_end), radius: 3pt)
])
#text(size: 8pt, fill: gray)[#milestone_progress% complete towards {milestone or "current milestone"}]

#v(2em)

== Team Workload

#table(columns: (1fr, 1fr, 1fr), inset: 10pt, stroke: 0.5pt + gray.lighten(50%),
  fill: (x, y) => if y == 0 {{ muted_bg }},
  [*Team Member*], [*Issues Completed*], [*Focus Area*],
  [Nadine Allan], [TBD], [System Architecture & Integration],
  [Andrey Dyakov], [TBD], [Plotter & Materialization],
  [Dmitri Kazantsev], [TBD], [Generative Concepts & Fabrication])

#v(2em)

== Risks & Decisions Needed

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("4").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt, fill: gray)[No major risks identified.]
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
    parser.add_argument("--week", "-w", type=int, required=True, help="Week number")
    parser.add_argument(
        "--output", "-o", type=str, default=None, help="Output file path"
    )
    parser.add_argument(
        "--milestone",
        "-m",
        type=str,
        default="1st milestone: Documentation",
        help="GitHub milestone name",
    )

    args = parser.parse_args()

    print(f"📊 Generating Weekly Report for Week {args.week}...")
    print(f"📌 Milestone: {args.milestone}")
    print()

    print("📥 Fetching completed issues...")
    completed = get_completed_issues(args.milestone)
    print(f"   Found {len(completed)} completed issues")

    print("📥 Fetching in-progress issues...")
    in_progress = get_in_progress_issues(args.milestone)
    print(f"   Found {len(in_progress)} open issues")
    print()

    generate_typst_report(
        week_num=args.week,
        completed=completed,
        in_progress=in_progress,
        milestone=args.milestone,
        output_path=args.output,
    )

    print()
    print("=" * 60)
    print("✅ Report generated successfully!")
    print("=" * 60)
    print()
    print("📄 To compile to PDF:")
    print(
        f"   typst compile {args.output or 'reports/week-XX-report.typ'} reports/week-{args.week:02d}.pdf"
    )


if __name__ == "__main__":
    main()
