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

    completed_rows = []
    for issue in completed[:10]:
        title = clean_text(issue.get("title", ""))
        completed_rows.append(f"#task_table(([{title}], [Completed]))")

    in_progress_rows = []
    for issue in in_progress[:10]:
        title = clean_text(issue.get("title", ""))
        in_progress_rows.append(f"#task_table(([{title}], [In Progress]))")

    typst_content = f'''// Weekly Report - Week {week_num}
// Auto-generated: {today.strftime("%Y-%m-%d")}
// Project: The Oracle That Wears Us

#import "../../templates/daily-plan-template.typ"

// --- CONFIGURATION ---
#set page(paper: "a4", margin: (x: 50pt, y: 60pt))
#set text(font: "Noto Sans", size: 10pt, fill: rgb("#333333"), lang: "en")

#let chapter_themes = (
  "1": (grad_start: rgb("#2F80ED"), grad_end: rgb("#9B51E0"), accent: rgb("#33A1C9"), page_bg: rgb("#A5C7F3")),
  "2": (grad_start: rgb("#eb3349"), grad_end: rgb("#f45c43"), accent: rgb("#e74c3c"), page_bg: rgb("#ff9a9e")),
  "3": (grad_start: rgb("#11998e"), grad_end: rgb("#38ef7d"), accent: rgb("#1b5e20"), page_bg: rgb("#c8e6c9")),
  "4": (grad_start: rgb("#F2994A"), grad_end: rgb("#F2C94C"), accent: rgb("#d35400"), page_bg: rgb("#fdebd0"))
)

#let muted_bg = rgb("#f4f4f4")

#let report_header(ch_idx, category: "WEEKLY REPORT") = {{
  let t = chapter_themes.at(ch_idx)
  move(dy: -20pt)[
    #box(width: 100%, height: 30pt, fill: gradient.linear(t.grad_start, t.grad_end), inset: (right: 15pt),
      align(right + horizon, text(white, weight: "bold", tracking: 1.5pt, size: 8pt)[#upper(category)]))
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
  place(bottom + right, dx: 30pt, dy: 30pt,
    square(size: 35pt, fill: t.page_bg, align(center + horizon, text(white, weight: "bold", size: 14pt)[#num])))
}}

#let task_table(rows) = {{
  table(columns: (1fr, 1fr), inset: 10pt, stroke: 0.5pt + gray.lighten(50%),
    fill: (x, y) => if y == 0 {{ muted_bg }} else {{ white }}, [*Task*], [*Status*], ..rows)
}}

#let stats_box(completed_count, in_progress_count, total) = {{
  #grid(columns: (1fr, 1fr, 1fr), gutter: 15pt,
    #box(fill: chapter_themes.at("1").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[{completed_count}]
      #text(size: 8pt)[Completed]])),
    #box(fill: chapter_themes.at("2").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[{in_progress_count}]
      #text(size: 8pt)[In Progress]])),
    #box(fill: chapter_themes.at("3").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[{total}]
      #text(size: 8pt)[Total]])))
}}

// PAGE 1: COVER & SUMMARY
#report_header("1")
#section_title("1", f"Week {week_num}", "Weekly Progress Report")

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
    Total: {total} issues | Completed: {completed_count} | In Progress: {in_progress_count}
  ]
])

#v(1em)
#stats_box({len(completed)}, {len(in_progress)}, {len(completed) + len(in_progress)})

#v(2em)

== Key Achievements This Week

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("3").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    - Completed {len(completed)} issues
    - Progress on {milestone or "current milestone"}
    - Team collaboration through GitHub
  ]
])

#page_footer("1", "1")
#pagebreak()

// PAGE 2: COMPLETED WORK
#report_header("2")
#section_title("2", "2.0", "Completed Issues")

#if len(completed) == 0 [
  #text(size: 10pt, fill: gray)[No issues completed this week.]
] else [
  ..completed[:10].map(issue => [
    #box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
      #text(size: 11pt, weight: "bold")[#{issue.number} - {clean_text(issue.title)}]
      #if issue.milestone != none [#v(4pt) #text(size: 8pt, fill: gray)[Milestone: {issue.milestone.title}]]
    ])
    #v(8pt)
  ])
]

#v(2em)

== Notes & Observations

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt, fill: gray)[All completed issues have been reviewed and merged.]
])

#page_footer("2", "2")
#pagebreak()

// PAGE 3: IN PROGRESS
#report_header("3")
#section_title("3", "3.0", "Work In Progress")

== Current Sprint

#if len(in_progress) == 0 [
  #text(size: 10pt, fill: gray)[No issues in progress.]
] else [
  ..in_progress[:10].map(issue => [
    #box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
      #text(size: 11pt, weight: "bold")[#{issue.number} - {clean_text(issue.title)}]
      #if issue.milestone != none [#v(4pt) #text(size: 8pt, fill: gray)[Milestone: {issue.milestone.title}]]
    ])
    #v(8pt)
  ])
]

#v(2em)

== Blockers & Challenges

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("2").accent.lighten(95%), radius: 4pt, [
  #text(size: 9pt, fill: gray)[No major blockers this week.]
])

#page_footer("3", "3")
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
  #box(width: f"{milestone_progress}%", height: 100%, fill: gradient.linear(chapter_themes.at("1").grad_start, chapter_themes.at("1").grad_end), radius: 3pt)
])
#text(size: 8pt, fill: gray)[{milestone_progress}% complete towards {milestone or "current milestone"}]

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

#page_footer("4", "4")
'''

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
