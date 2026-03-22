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
import sys

REPO = "berlogabob/Project02"
PROJECT_START_DATE = datetime(2026, 3, 2)  # Week 1 starts Monday, Mar 2, 2026

# Import the sanitisation / validation helpers
sys.path.insert(0, str(Path(__file__).parent))
from validate_report_data import (
    sanitize_for_typst,
    build_report_json,
    save_report_json,
    validate_ai_summary,
    sanitize_summary,
)

# Team member roles (username -> role mapping)
TEAM_ROLES = {
    "naydino": "System Architecture & Integration",
    "berlogabob": "Plotter & Materialization",
    "electricianv001": "Generative Concepts & Fabrication",
}

# Team member full names (username -> full name mapping)
TEAM_NAMES = {
    "naydino": "Nadine Allan",
    "berlogabob": "Andrey Dyakov",
    "electricianv001": "Dmitri Kazantsev",
}


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


def is_show_in_report(issue: dict) -> bool:
    """Check if issue has show-in-report label."""
    labels = issue.get("labels", [])
    for label in labels:
        name = label.get("name", "")
        if name == "show-in-report":
            return True
    return False


def get_assignees(issue: dict) -> str:
    """Get assignee names."""
    assignees = issue.get("assignees", [])
    if not assignees:
        return ""
    names = [a.get("login", "") for a in assignees]
    return ", ".join(names)


# Global cache for parent mappings from Projects API
_parent_cache = {}


def get_parent_issue(issue_num: int, all_issues: list) -> int:
    """Get parent issue using multiple strategies:
    1. Check cache first (from Projects API)
    2. Title pattern: '#41 - #20 - Title' means #20 is parent of #41
    3. Body text: '**Parent:** #XX' or 'Parent: #XX' or 'Sub-task of #XX'
    """
    # Check cache first (loaded from Projects API)
    if issue_num in _parent_cache:
        return _parent_cache[issue_num]

    result = subprocess.run(
        ["gh", "issue", "view", str(issue_num), "--json", "body,title,number"],
        capture_output=True,
        text=True,
    )
    try:
        data = json.loads(result.stdout) if result.stdout else {}
        title = data.get("title", "") or ""
        body = data.get("body", "") or ""
        issue_num = data.get("number", issue_num)

        import re

        # Strategy 1: Title pattern "#XX - #YY - Title" where YY is parent
        match = re.match(r"#\d+\s*-\s*#(\d+)", title)
        if match:
            parent = int(match.group(1))
            _parent_cache[issue_num] = parent
            return parent

        # Strategy 2: Body has "**Parent:** #XX" or "Parent: #XX" or "Sub-task of #XX"
        # Match patterns like:
        # **Parent:** #45
        # Parent: #45
        # Sub-task of #45
        # Child of #45
        match = re.search(
            r"(?:\*\*Parent:\*\*|Parent:|Sub-task of|Child of)\s*#(\d+)",
            body,
            re.IGNORECASE,
        )
        if match:
            parent = int(match.group(1))
            _parent_cache[issue_num] = parent
            return parent

    except Exception as e:
        pass

    _parent_cache[issue_num] = 0
    return 0  # No parent found


def load_projects_parent_map(project_owner: str, project_number: int):
    """Load parent-child mappings from GitHub Projects v2 API."""
    global _parent_cache

    try:
        # Query Projects v2 for items with their field values
        query = f'''query {{
            user(login: "{project_owner}") {{
                projectV2(number: {project_number}) {{
                    items(first: 100) {{
                        nodes {{
                            content {{
                                ... on Issue {{
                                    number
                                    title
                                }}
                            }}
                            fieldValues(first: 20) {{
                                nodes {{
                                    __typename
                                    ... on ProjectV2ItemFieldSingleSelectValue {{ name }}
                                    ... on ProjectV2ItemFieldTextValue {{ text }}
                                    ... on ProjectV2ItemFieldIssueValue {{
                                        number
                                        title
                                    }}
                                }}
                            }}
                        }}
                    }}
                }}
            }}
        }}'''

        result = subprocess.run(
            ["gh", "api", "graphql", "-f", f"query={query}"],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0 and result.stdout:
            data = json.loads(result.stdout)
            items = (
                data.get("data", {})
                .get("user", {})
                .get("projectV2", {})
                .get("items", {})
                .get("nodes", [])
            )

            for item in items:
                content = item.get("content", {})
                issue_num = content.get("number")
                if not issue_num:
                    continue

                # Look for parent field in fieldValues
                field_values = item.get("fieldValues", {}).get("nodes", [])
                for fv in field_values:
                    typename = fv.get("__typename", "")
                    # ProjectV2ItemFieldIssueValue is used for "Parent issue" field
                    if typename == "ProjectV2ItemFieldIssueValue":
                        parent_num = fv.get("number")
                        if parent_num:
                            _parent_cache[issue_num] = int(parent_num)

    except Exception as e:
        # Projects API not available, will fall back to title/body patterns
        pass


def get_sub_issues(parent_number: int, all_issues: list) -> list:
    """Get direct sub-issues of a parent issue."""
    sub_issues = []
    for issue in all_issues:
        # Skip duplicates
        if any(lbl.get("name") == "duplicate" for lbl in issue.get("labels", [])):
            continue

        # Check if this issue's parent is the given parent_number
        parent = get_parent_issue(issue.get("number"))
        if parent == parent_number:
            sub_issues.append(issue)

    return sub_issues


def get_issues_by_week(week_num: int, state: str = "open") -> tuple:
    """
    Get issues for a specific week, categorized by completion status.
    Returns: (completed_this_week, incomplete_this_week, future_week_issues)
    """
    # Get ALL closed issues with the week label (not limited to 100)
    closed_issues = run_gh_command(
        [
            "issue",
            "list",
            "--state",
            "closed",
            "--limit",
            "1000",
            "--search",
            f"label:week-{week_num}",
        ]
    )
    # Filter out duplicates
    closed_this_week = [
        i
        for i in closed_issues
        if not any(lbl.get("name") == "duplicate" for lbl in i.get("labels", []))
    ]

    # Get ALL open issues with the week label
    open_issues = run_gh_command(
        [
            "issue",
            "list",
            "--state",
            "open",
            "--limit",
            "1000",
            "--search",
            f"label:week-{week_num}",
        ]
    )
    incomplete_this_week = [
        i
        for i in open_issues
        if not any(lbl.get("name") == "duplicate" for lbl in i.get("labels", []))
    ]

    # Future week issues (started early) - search for issues with future week labels
    future_issues = run_gh_command(
        [
            "issue",
            "list",
            "--state",
            "open",
            "--limit",
            "1000",
        ]
    )
    # Filter: has future week label AND is assigned (in progress)
    future_filtered = []
    for i in future_issues:
        issue_week = get_issue_week(i)
        if issue_week > week_num and i.get("assignees", []):
            if not any(lbl.get("name") == "duplicate" for lbl in i.get("labels", [])):
                future_filtered.append(i)

    return closed_this_week, incomplete_this_week, future_filtered


def get_next_week_preview_tasks(week_num: int) -> list:
    """Get tasks for next week preview (week-N + Next-Week-Preview labels)."""
    next_week = week_num + 1

    # Get all open issues
    all_issues = run_gh_command(["issue", "list", "--state", "open", "--limit", "100"])

    # Filter by: has week-{next_week} label AND has Next-Week-Preview label
    preview_tasks = []
    for issue in all_issues:
        labels = [l.get("name", "") for l in issue.get("labels", [])]
        has_week_label = f"week-{next_week}" in labels
        has_preview_label = "Next-Week-Preview" in labels

        if has_week_label and has_preview_label:
            preview_tasks.append(issue)

    return preview_tasks


def get_all_open_issues() -> list:
    """Get all open issues."""
    return run_gh_command(["issue", "list", "--state", "open", "--limit", "100"])


def clean_text(text: str) -> str:
    """Clean raw issue text and sanitize for safe use in Typst."""
    if not text:
        return ""
    import re

    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"https?://\S+", "", text)
    # Remove Parent: #XX pattern (service information)
    text = re.sub(r"\*\*Parent:\*\*\s*#\d+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"Parent:\s*#\d+", "", text, flags=re.IGNORECASE)
    text = text.replace("\n", " ")
    return sanitize_for_typst(text)


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


def format_issue_box(
    issue: dict, show_week: bool = False, show_full: bool = False, indent: int = 0
) -> str:
    """Format a single issue as a Typst box with hierarchy indicators."""
    num = issue.get("number", "?")
    title = clean_text(issue.get("title", ""))
    body = clean_text(issue.get("body", ""))
    assignees = get_assignees(issue)

    # Escape # in body text for Typst
    body = body.replace("#", "\\#")

    # Get priority
    priority = get_priority(issue)
    priority_badge = (
        f' #text(size: 9pt, fill: red, weight: "bold")[{priority.upper()}]'
        if priority
        else ""
    )

    # Get week label for future tasks
    week_num = get_issue_week(issue)
    week_part = (
        f" #text(size: 8pt, fill: gray)[(Week {week_num})]"
        if (show_week and week_num > 0)
        else ""
    )

    # Hierarchy visual indicators with nested list style indents
    if indent == 0:
        # Root level - no indent, standard box
        indent_code = ""
        box_style = f"fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt"
    elif indent == 1:
        # First level child - indent with left border
        indent_code = "#h(30pt) "
        box_style = f'fill: chapter_themes.at("1").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("1").accent)'
    elif indent == 2:
        # Second level - more indent
        indent_code = "#h(60pt) "
        box_style = f'fill: chapter_themes.at("2").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("2").accent)'
    else:
        # Deeper levels - even more indent
        indent_code = f"#h({60 + (indent - 2) * 25}pt) "
        box_style = f"fill: muted_bg.lighten(70%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + gray)"

    if show_full:
        # Full format with complete description and assignee
        assignee_part = (
            f" #text(size: 8pt, fill: gray)[by {assignees}]" if assignees else ""
        )
        body_part = f"#v(4pt) #text(size: 9pt)[{body}]" if body else ""
        return f"""
{indent_code}#box(width: 100%, {box_style}, [
  #text(size: 11pt, weight: "bold")[#{num} - {title}]{priority_badge}{week_part}{assignee_part}
  {body_part}
])
#v(6pt)
"""
    else:
        # Compact format with short description
        desc_part = (
            f"#v(2pt) #text(size: 8pt, fill: gray)[{body[:150]}...]" if body else ""
        )
        return f"""
{indent_code}#box(width: 100%, {box_style}, [
  #text(size: 10pt, weight: "bold")[#{num} - {title}]{priority_badge}{week_part}
  {desc_part}
])
#v(4pt)
"""


def generate_ai_summary_for_week(issues: list, week_num: int) -> str:
    """Generate AI summary for completed issues using Ollama with fallback chain.

    Tries Ollama → falls back to a simple sanitized issue list if unavailable.
    All output is sanitized for safe embedding in Typst.
    """
    if not issues:
        return "- No issues completed this week."

    print(f"🤖 Generating AI summary for {len(issues)} issues...")
    issue_list = "\n".join(
        [f"- #{i.get('number')} {i.get('title', '')[:60]}" for i in issues[:15]]
    )
    prompt = (
        "Summarize these completed tasks in exactly 3-5 bullet points.\n"
        "Use action verbs. Group related work. Max 100 words total.\n"
        "Do NOT use hashtags, asterisks, brackets, or dollar signs in the text.\n"
        "Format each bullet with a leading hyphen (-).\n\n"
        f"{issue_list}\n\nSummary:"
    )

    raw_summary = None

    try:
        print("   Calling Ollama API...")
        result = subprocess.run(
            [
                "curl",
                "-s",
                "-m",
                "180",
                "http://localhost:11434/api/generate",
                "-d",
                json.dumps({"model": "qwen3.5:2b", "prompt": prompt, "stream": False}),
            ],
            capture_output=True,
            text=True,
            timeout=200,
        )
        print(f"   Return code: {result.returncode}")
        if result.returncode == 0 and result.stdout:
            response = json.loads(result.stdout).get("response", "").strip()
            print(f"   Response length: {len(response)}")
            if response and len(response) > 20:
                raw_summary = response
                print("   ✅ Ollama response received")
        if not raw_summary:
            print("   ⚠️  No valid response from Ollama, using fallback")
    except Exception as e:
        print(f"   ⚠️  Ollama error: {e}, using fallback")

    if not raw_summary:
        # Fallback: plain sanitized issue list
        raw_summary = "\n".join(
            [f"- #{i['number']} {i['title'][:60]}" for i in issues[:5]]
        )

    # Sanitize and validate
    sanitized = sanitize_summary(raw_summary)
    is_valid, errors = validate_ai_summary(sanitized)
    if not is_valid:
        print(f"   ⚠️  Summary validation warnings: {errors}")

    return sanitized


def generate_typst_report(
    week_num: int,
    completed: list,
    incomplete: list,
    future: list,
    all_open: list,
    output_path: str = None,
) -> str:
    # Get next week preview tasks
    next_week_tasks = get_next_week_preview_tasks(week_num)
    today = datetime.now()
    week_start, week_end = get_week_date_range(week_num)

    # Load parent-child mappings from GitHub Projects
    load_projects_parent_map("berlogabob", 7)

    # Calculate counts
    completed_count = len(completed)
    incomplete_count = len(incomplete)
    future_count = len(future)
    total_this_week = completed_count + incomplete_count

    # Separate highlighted tasks (show-in-report AND week label) from regular
    highlighted_completed = []
    regular_completed = []

    for issue in completed:
        issue_week = get_issue_week(issue)
        has_show_tag = is_show_in_report(issue)

        # Highlight only if has BOTH week label (>0) AND show-in-report label
        # Issue must have explicit week-N label
        if issue_week > 0 and has_show_tag:
            highlighted_completed.append(issue)
        else:
            regular_completed.append(issue)

    # Also filter regular_completed to only include issues from this week
    regular_completed = [
        i
        for i in regular_completed
        if get_issue_week(i) == week_num or not is_show_in_report(i)
    ]

    # Build completed issues section with highlights
    completed_section = ""
    if highlighted_completed:
        # Show highlighted tasks with full details and sub-issues
        completed_section += '#text(size: 10pt, weight: "bold", fill: chapter_themes.at("3").accent)[✨ HIGHLIGHTS]\n#v(8pt)'

        # Get all highlighted issue numbers for quick lookup
        highlighted_nums = set(i.get("number") for i in highlighted_completed)

        # Find root issues (those without a parent in highlighted set)
        root_issues = []

        for issue in highlighted_completed:
            parent = get_parent_issue(issue.get("number"), highlighted_completed)
            if parent not in highlighted_nums:
                root_issues.append(issue)

        # Sort root issues by number for consistent ordering
        root_issues.sort(key=lambda x: x.get("number", 0), reverse=True)

        # Track which issues we've already shown
        shown_issues = set()

        for issue in root_issues[:10]:
            issue_num = issue.get("number")
            if issue_num in shown_issues:
                continue
            shown_issues.add(issue_num)

            # Show parent issue
            completed_section += format_issue_box(issue, show_full=True)

            # Find direct sub-issues (children)
            children = []
            for child in highlighted_completed:
                child_parent = get_parent_issue(
                    child.get("number"), highlighted_completed
                )
                if child_parent == issue_num:
                    children.append(child)
            children.sort(key=lambda x: x.get("number", 0))

            for child in children:
                child_num = child.get("number")
                if child_num in shown_issues:
                    continue
                shown_issues.add(child_num)
                completed_section += format_issue_box(child, show_full=True, indent=1)

                # Find grandchildren
                grandchildren = []
                for gc in highlighted_completed:
                    gc_parent = get_parent_issue(
                        gc.get("number"), highlighted_completed
                    )
                    if gc_parent == child_num:
                        grandchildren.append(gc)

                for grandchild in grandchildren:
                    gc_num = grandchild.get("number")
                    if gc_num in shown_issues:
                        continue
                    shown_issues.add(gc_num)
                    completed_section += format_issue_box(
                        grandchild, show_full=True, indent=2
                    )

    if not completed_section:
        completed_section = (
            "#text(size: 10pt, fill: gray)[No highlighted issues completed this week.]"
        )

    # Build incomplete issues section
    incomplete_section = ""
    if not incomplete:
        incomplete_section = (
            "#text(size: 10pt, fill: green)[All planned tasks completed! 🎉]"
        )
    else:
        for issue in incomplete[:15]:
            incomplete_section += format_issue_box(issue, show_full=False)

    # Build future issues section with hierarchy (same as HIGHLIGHTS)
    future_section = ""
    if future:
        # Find parent-child relationships among future tasks
        future_nums = set(i.get("number") for i in future)
        parent_map = {}

        for issue in future:
            issue_num = issue.get("number")
            body = issue.get("body", "") or ""
            title = issue.get("title", "") or ""
            text = body + " " + title

            # Check if this issue references another future issue
            for other in future:
                other_num = other.get("number")
                if other_num != issue_num:
                    if f"#{other_num}" in text:
                        # other is parent of this issue
                        parent_map[issue_num] = other_num

        # Find root issues (no parent)
        root_future = [i for i in future if i.get("number") not in parent_map]
        root_future.sort(key=lambda x: x.get("number", 0), reverse=True)

        shown = set()
        for issue in root_future[:10]:
            issue_num = issue.get("number")
            if issue_num in shown:
                continue
            shown.add(issue_num)

            # Show parent
            future_section += format_issue_box(issue, show_week=True, show_full=False)

            # Find and show children
            children = [
                i for i in future if parent_map.get(i.get("number")) == issue_num
            ]
            children.sort(key=lambda x: x.get("number", 0))

            for child in children:
                child_num = child.get("number")
                if child_num in shown:
                    continue
                shown.add(child_num)
                future_section += format_issue_box(
                    child, show_week=True, show_full=False, indent=1
                )

    # Generate AI summary for completed work
    ai_summary = generate_ai_summary_for_week(completed, week_num)

    # Build and persist the intermediate JSON for debugging / traceability
    report_json = build_report_json(
        week_num=week_num,
        completed=completed,
        incomplete=incomplete,
        future=future,
        ai_summary=ai_summary,
        qwen_model="qwen3.5:2b",
    )
    json_path = save_report_json(report_json, output_dir="reports")
    print(f"📦 Intermediate JSON saved: {json_path}")

    # Build next week preview section
    if next_week_tasks:
        next_week_preview_section = ""
        for task in next_week_tasks[:10]:
            next_week_preview_section += format_issue_box(task, show_full=False)
    else:
        next_week_preview_section = (
            "#text(size: 10pt, fill: gray)[No tasks marked for next week preview.]\n"
        )

    # Calculate completion percentage
    completion_pct = (
        round((completed_count / total_this_week * 100)) if total_this_week > 0 else 0
    )

    github_sha = (report_json["metadata"].get("github_sha") or "local")[:7]

    typst_content = f"""// Weekly Report - Week {week_num}
// Auto-generated: {today.strftime("%Y-%m-%d")}
// Project: The Oracle That Wears Us
// Week Period: {week_start.strftime("%b %d")} - {week_end.strftime("%b %d, %Y")}
// SHA: {github_sha}

#import "../templates/daily-plan-template.typ": *

#set page(
  paper: "a4",
  margin: (x: 50pt, y: 60pt),
  footer: [
    #place(
      bottom + left,
      dx: 5pt,
      dy: -8pt,
      text(size: 7pt, fill: gray)[Generated {today.strftime("%Y-%m-%d")} · SHA: {github_sha} · model: qwen3.5:2b]
    )
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
  grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 10pt,
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("3").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[{completed_count}] \\
      #text(size: 7pt)[COMPLETED]
    ]),
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("2").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[{incomplete_count}] \\
      #text(size: 7pt)[INCOMPLETE]
    ]),
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("1").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[{future_count}] \\
      #text(size: 7pt)[FUTURE WEEKS]
    ])
  )
}}

// PAGE 1: COVER & SUMMARY
#report_header("1")
#section_title("1", "Week {week_num}", "Weekly Progress Report")

#box(width: 100%, inset: 12pt, fill: muted_bg, radius: 4pt, [
  #grid(columns: (1fr,), [
    #text(size: 9pt)[*Project:* The Oracle That Wears Us]
  ])
  #v(6pt)
  #grid(columns: (1fr,), [
    #text(size: 9pt)[*Team:* Nadine Allan | Andrey Dyakov | Dmitri Kazantsev]
  ])
  #v(8pt)
  #line(length: 100%, stroke: 0.5pt + gray.lighten(60%))
  #v(8pt)
  #grid(columns: (auto, 1fr, auto), gutter: 10pt, [
    #text(size: 9pt)[*Report Date:* {today.strftime("%B %d, %Y")}]
    #h(1fr)
    #text(size: 9pt)[*Week Period:* {week_start.strftime("%b %d")} - {week_end.strftime("%b %d, %Y")}]
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
#box(width: 100%, height: 28pt, fill: gray.lighten(80%), inset: 0pt, radius: 3pt, [
  #box(width: week_progress * 1%, height: 100%, fill: gradient.linear(chapter_themes.at("3").grad_start, chapter_themes.at("3").grad_end), radius: 3pt)
  #place(
    center + horizon,
    text(size: 10pt, weight: "bold", fill: white)[{completion_pct}% complete]
  )
])

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

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("3").accent.lighten(95%), radius: 4pt, [
  #text(size: 9pt, weight: "bold")[✨ Week Summary:]
  #v(4pt)
  #text(size: 9pt)[{ai_summary}]
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
    *Week {week_num + 1}:* {get_week_date_range(week_num + 1)[0].strftime("%b %d")} - {get_week_date_range(week_num + 1)[1].strftime("%b %d, %Y")}
  ]
])

#v(1em)

{next_week_preview_section}

#v(2em)

== Team

#table(
  columns: (1fr, 1fr, 1fr),
  gutter: 10pt,
  inset: 10pt,
  stroke: none,
  fill: muted_bg.lighten(50%),
  [
    #align(center, [
      #text(size: 9pt, weight: "bold")[{TEAM_NAMES.get("naydino", "Nadine Allan")}]
      #text(size: 8pt, fill: gray)[{TEAM_ROLES.get("naydino", "System Architecture")}]
    ])
  ],
  [
    #align(center, [
      #text(size: 9pt, weight: "bold")[{TEAM_NAMES.get("berlogabob", "Andrey Dyakov")}]
      #text(size: 8pt, fill: gray)[{TEAM_ROLES.get("berlogabob", "Plotter & Materialization")}]
    ])
  ],
  [
    #align(center, [
      #text(size: 9pt, weight: "bold")[{TEAM_NAMES.get("electricianv001", "Dmitri Kazantsev")}]
      #text(size: 8pt, fill: gray)[{TEAM_ROLES.get("electricianv001", "Generative Concepts")}]
    ])
  ]
)

#v(2em)

== Risks & Decisions Needed

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("4").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt, fill: gray)[Document any risks or decisions needed from the team.]
])
"""

    if output_path:
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, "w", encoding="utf-8") as f:
            f.write(typst_content)
        print(f"✅ Generated: {output}")

    return typst_content


def main():
    parser = argparse.ArgumentParser(
        description="Generate weekly Typst report from GitHub issues"
    )
    parser.add_argument(
        "--week",
        "-w",
        type=int,
        default=None,
        help="Week number (auto-calculated if not provided)",
    )
    parser.add_argument(
        "--output", "-o", type=str, default=None, help="Output file path"
    )

    args = parser.parse_args()

    # Auto-detect week if not specified
    week_num = args.week if args.week else get_current_week()

    # Set default output path if not provided
    if not args.output:
        args.output = f"reports/week-{week_num}-report.typ"

    print(f"📊 Generating Weekly Report for Week {week_num}...")
    week_start, week_end = get_week_date_range(week_num)
    print(
        f"📅 Week Period: {week_start.strftime('%b %d')} - {week_end.strftime('%b %d, %Y')}"
    )
    print()

    print(f"📥 Fetching issues for Week {week_num}...")
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
    print("✅ Typst file generated successfully!")
    print("=" * 60)
    print()

    # Try to compile to PDF
    print("📄 Compiling to PDF...")
    import subprocess

    pdf_path = args.output.replace(".typ", ".pdf")
    result = subprocess.run(
        ["typst", "compile", "--root", ".", args.output, pdf_path],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        # Check if PDF was actually created
        import os

        if os.path.exists(pdf_path):
            pdf_size = os.path.getsize(pdf_path)
            print(f"✅ PDF compiled successfully! ({pdf_size:,} bytes)")
            print(f"📁 File: {pdf_path}")
        else:
            print("❌ PDF file not found after compilation")
            exit(1)
    else:
        print("❌ PDF compilation failed!")
        print()
        print("Errors:")
        print(result.stdout)
        print(result.stderr)
        exit(1)


if __name__ == "__main__":
    main()
