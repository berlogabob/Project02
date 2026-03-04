#!/usr/bin/env python3
"""
GitHub Issues to Typst Weekly Report Generator

Fetches completed/in-progress issues from GitHub and generates
a Typst report file ready for PDF compilation.

Usage:
    python3 generate_weekly_report.py --week 1 --output reports/week-01-report.typ
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def run_gh_command(args: list) -> dict:
    """Run a GitHub CLI command and return JSON result"""
    cmd = ["gh"] + args + ["--json"] + [
        "number", "title", "state", "labels", "assignees", 
        "closedAt", "createdAt", "milestone"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def get_completed_issues(milestone: str = None, limit: int = 50) -> list:
    """Get issues closed in the last 7 days"""
    filters = ["state:closed", "updated:>last-week"]
    if milestone:
        filters.append(f'milestone:"{milestone}"')
    
    issues = run_gh_command([
        "issue", "list",
        "--state", "closed",
        "--limit", str(limit),
        "--search", " ".join(filters)
    ])
    return issues


def get_in_progress_issues(milestone: str = None, limit: int = 50) -> list:
    """Get open issues"""
    filters = ["state:open"]
    if milestone:
        filters.append(f'milestone:"{milestone}"')
    
    issues = run_gh_command([
        "issue", "list",
        "--state", "open",
        "--limit", str(limit),
        "--search", " ".join(filters)
    ])
    return issues


def get_milestone_progress(milestone: str) -> dict:
    """Get milestone completion percentage"""
    result = subprocess.run(
        ["gh", "api", "repos/berlogabob/Project02/milestones", "--jq", 
         f'.[] | select(.title == "{milestone}") | .{{"closed_issues": .closed_issues, "open_issues": .open_issues, "total": (.closed_issues + .open_issues)}'],
        capture_output=True, text=True
    )
    if result.stdout.strip():
        data = json.loads(result.stdout.strip())
        total = data.get("total", 1)
        closed = data.get("closed_issues", 0)
        return {
            "percentage": int((closed / total) * 100) if total > 0 else 0,
            "closed": closed,
            "open": data.get("open_issues", 0),
            "total": total
        }
    return {"percentage": 0, "closed": 0, "open": 0, "total": 0}


def format_issue_title(issue: dict) -> str:
    """Format issue title for Typst"""
    title = issue.get("title", "Untitled")
    number = issue.get("number", 0)
    # Escape special Typst characters
    title = title.replace("[", "(").replace("]", ")")
    return f"[#{number} - {title}]"


def generate_typst_report(
    week_num: int,
    completed: list,
    in_progress: list,
    milestone: str = None,
    output_path: str = None
) -> str:
    """Generate Typst report content"""
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Calculate stats
    completed_count = len(completed)
    in_progress_count = len(in_progress)
    blocked_count = sum(1 for i in in_progress if any(l["name"] == "priority: critical" for l in i.get("labels", [])))
    total_count = completed_count + in_progress_count
    
    # Get milestone progress
    milestone_data = get_milestone_progress(milestone) if milestone else {"percentage": 0}
    
    # Format completed issues
    completed_rows = []
    for issue in completed[:10]:  # Limit to 10
        title = format_issue_title(issue)
        completed_rows.append(title)
    
    # Format in-progress issues
    in_progress_rows = []
    for issue in in_progress[:10]:  # Limit to 10
        title = format_issue_title(issue)
        labels = [l["name"] for l in issue.get("labels", [])]
        status = "blocked" if "priority: critical" in labels else "in-progress"
        in_progress_rows.append(f"({title}, [{status}])")
    
    # Assignee summary
    assignee_counts = {}
    for issue in completed:
        for assignee in issue.get("assignees", []):
            name = assignee.get("login", "Unknown")
            assignee_counts[name] = assignee_counts.get(name, 0) + 1
    
    # Generate Typst content
    typst_content = f'''// Weekly Report - Week {week_num}
// Auto-generated: {today}
// Project: The Oracle That Wears Us

#import "weekly-report-template.typ": report

#show: report.with(
  week: {week_num},
  date: datetime.today(),
  milestone: "{milestone or "1st milestone: Documentation"}"
)

// --- AUTO-GENERATED CONTENT ---

#let summary = [
This week, the team completed **{completed_count} issues** and has **{in_progress_count} issues** in progress.
Focus areas include development, research, and integration tasks.
]

#let achievements = [
- Completed {completed_count} GitHub issues
- Advanced progress on {milestone or "current milestone"}
- Team collaboration through daily standups and PR reviews
]

#let stats = (
  completed: {completed_count},
  in_progress: {in_progress_count},
  blocked: {blocked_count},
  total: {total_count}
)

#let completed_issues = completed_table((
  {",\n  ".join(completed_rows) if completed_rows else "[No issues completed this week]"}
))

#let completed_notes = [
All completed issues have been reviewed and merged. Documentation updated accordingly.
]

#let in_progress_issues = in_progress_table((
  {",\n  ".join(in_progress_rows) if in_progress_rows else "([No issues in progress], [in-progress])"}
))

#let blocked_issues = in_progress_table((
  []
))

#let blockers = [
_No critical blockers this week. Team is progressing smoothly._
]

#let planned_issues = [
- [ ] Continue with remaining milestone tasks
- [ ] Review and merge pending PRs
- [ ] Prepare for next week's sprint goals
]

#let milestone_progress = {milestone_data.get("percentage", 0)}

#let nadine_issues = {assignee_counts.get("nadine-allan", assignee_counts.get("Nadine Allan", 0))}
#let nadine_focus = [System Architecture & Integration]

#let andrey_issues = {assignee_counts.get("andrey-dyakov", assignee_counts.get("Andrey Dyakov", 0))}
#let andrey_focus = [Plotter & Materialization]

#let dmitri_issues = {assignee_counts.get("dmitri-kazantsev", assignee_counts.get("Dmitri Kazantsev", 0))}
#let dmitri_focus = [Generative Concepts & Fabrication]

#let risks = [
_No major risks identified. Timeline is on track._
]
'''
    
    # Write to file
    if output_path:
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, "w") as f:
            f.write(typst_content)
        print(f"✅ Generated: {output}")
    else:
        print(typst_content)
    
    return typst_content


def main():
    parser = argparse.ArgumentParser(
        description="Generate weekly Typst report from GitHub issues"
    )
    parser.add_argument(
        "--week", "-w",
        type=int,
        required=True,
        help="Week number (e.g., 1, 2, 3)"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Output file path (e.g., reports/week-01-report.typ)"
    )
    parser.add_argument(
        "--milestone", "-m",
        type=str,
        default="1st milestone: Documentation",
        help="GitHub milestone name"
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Preview to stdout instead of file"
    )
    
    args = parser.parse_args()
    
    # Check if gh is installed
    try:
        subprocess.run(["gh", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ GitHub CLI (gh) not found. Install with: brew install gh")
        sys.exit(1)
    
    print(f"📊 Generating Weekly Report for Week {args.week}...")
    print(f"📌 Milestone: {args.milestone}")
    print()
    
    # Fetch issues
    print("📥 Fetching completed issues...")
    completed = get_completed_issues(args.milestone)
    print(f"   Found {len(completed)} completed issues")
    
    print("📥 Fetching in-progress issues...")
    in_progress = get_in_progress_issues(args.milestone)
    print(f"   Found {len(in_progress)} open issues")
    print()
    
    # Generate report
    output_path = args.output if not args.preview else None
    generate_typst_report(
        week_num=args.week,
        completed=completed,
        in_progress=in_progress,
        milestone=args.milestone,
        output_path=output_path
    )
    
    if not args.preview:
        print()
        print("✅ Report generated successfully!")
        print()
        print("📄 To compile to PDF:")
        print(f"   typst compile {args.output or 'reports/week-XX-report.typ'} reports/week-{args.week:02d}.pdf")
        print()
        print("👁️  To preview:")
        print(f"   typst preview {args.output or 'reports/week-XX-report.typ'}")


if __name__ == "__main__":
    main()
