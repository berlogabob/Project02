#!/usr/bin/env python3
"""
Daily Plan Generator
Creates personalized daily plan PDFs for each team member with their assigned issues.

Usage:
    python3 generate_daily_plan.py --member berlogabob --output reports/daily-plan-berlogabob.typ
    python3 generate_daily_plan.py --all-members --output-dir reports/daily-plans/
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List

# Team configuration
TEAM_MEMBERS = {
    "naydino": "Nadine Allan",
    "berlogabob": "Andrey Dyakov",
    "electricianv001": "Dmitri Kazantsev",
}

REPO = "berlogabob/Project02"


def run_gh_command(args: list) -> dict:
    """Run a GitHub CLI command and return JSON result"""
    fields = [
        "number",
        "title",
        "state",
        "labels",
        "assignees",
        "milestone",
        "body",
        "comments",
        "createdAt",
    ]

    cmd = ["gh"] + args + ["--json"] + fields
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def get_assigned_issues(username: str) -> list:
    """Get open issues assigned to a specific user"""
    # Use search instead of --assignee flag for better compatibility
    cmd = [
        "gh",
        "issue",
        "list",
        "--state",
        "open",
        "--search",
        f"assignee:{username} repo:{REPO}",
        "--limit",
        "20",
        "--json",
        "number,title,state,labels,assignees,milestone,body,comments,createdAt",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Warning: Could not fetch issues for {username}: {result.stderr}")
        return []

    return json.loads(result.stdout)


def get_sub_issues(parent_number: int) -> list:
    """Get sub-issues (issues that reference this issue)"""
    # Search for issues that mention the parent issue number
    cmd = [
        "gh",
        "issue",
        "list",
        "--state",
        "open",
        "--search",
        f"repo:{REPO} #{parent_number}",
        "--limit",
        "10",
        "--json",
        "number,title,state,labels,assignees,milestone,body,comments,createdAt",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return []

    issues = json.loads(result.stdout)
    # Filter out the parent issue itself
    return [i for i in issues if i["number"] != parent_number]


def get_priority(issue: dict) -> str:
    """Extract priority from labels"""
    labels = issue.get("labels", [])
    priority_map = {
        "priority: critical": "critical",
        "priority: high": "high",
        "priority: medium": "medium",
        "priority: low": "low",
    }

    for label in labels:
        name = label.get("name", "")
        if name in priority_map:
            return priority_map[name]

    return "medium"


def format_labels(issue: dict) -> list:
    """Format labels for Typst"""
    labels = issue.get("labels", [])
    formatted = []

    for label in labels:
        formatted.append(
            {"name": label.get("name", ""), "color": label.get("color", "808080")}
        )

    return formatted


def format_comments(comments: list) -> list:
    """Format comments for Typst"""
    if not comments:
        return []

    formatted = []
    # Get last 3 comments
    recent_comments = comments[-3:] if len(comments) > 3 else comments

    for comment in recent_comments:
        author = comment.get("author", {}).get("login", "Unknown")
        body = comment.get("body", "")
        created = comment.get("createdAt", "")[:10]

        # Clean body text
        body_clean = body.replace("[", "(").replace("]", ")").replace("\n", " ")
        if len(body_clean) > 100:
            body_clean = body_clean[:97] + "..."

        formatted.append({"author": author, "date": created, "body": body_clean})

    return formatted


def format_body(body: str) -> str:
    """Format issue body for Typst"""
    if not body:
        return ""

    # Clean and truncate
    body_clean = body.replace("[", "(").replace("]", ")").replace("\n", " ")
    if len(body_clean) > 200:
        body_clean = body_clean[:197] + "..."

    return body_clean


def prepare_issue_for_typst(issue: dict) -> dict:
    """Prepare issue data for Typst template"""
    sub_issues = get_sub_issues(issue["number"])

    return {
        "number": issue["number"],
        "title": issue["title"].replace("[", "(").replace("]", ")"),
        "body": format_body(issue.get("body", "")),
        "priority": get_priority(issue),
        "labels": format_labels(issue),
        "milestone": issue.get("milestone"),
        "comments": format_comments(issue.get("comments", [])),
        "sub_issues": [
            {
                "number": sub["number"],
                "title": sub["title"].replace("[", "(").replace("]", ")"),
            }
            for sub in sub_issues[:5]  # Limit to 5 sub-issues
        ],
    }


def generate_typst_plan(
    member_name: str, member_username: str, issues: list, output_path: str
) -> str:
    """Generate Typst daily plan"""

    today = datetime.now()
    prepared_issues = [prepare_issue_for_typst(i) for i in issues]

    # Sort by priority
    priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    prepared_issues.sort(key=lambda x: priority_order.get(x["priority"], 2))

    typst_content = f'''// Daily Plan for {member_name}
// Generated: {today.strftime("%Y-%m-%d %H:%M")}
// Project: The Oracle That Wears Us

#import "daily-plan-template.typ"

#show: report.with(
  member_name: "{member_name}",
  member_username: "@{member_username}",
  date: datetime.today(),
  issues: {prepared_issues}
)
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

    for username, name in TEAM_MEMBERS.items():
        print(f"\n📋 Generating plan for {name} (@{username})...")

        # Get assigned issues
        issues = get_assigned_issues(username)
        print(f"   Found {len(issues)} open issues")

        if not issues:
            print(f"   ⚠️  No issues assigned, generating empty plan")

        # Generate plan
        output_file = output_path / f"daily-plan-{username}.typ"
        generate_typst_plan(name, username, issues, str(output_file))

        # Compile to PDF
        pdf_file = output_path / f"daily-plan-{username}.pdf"
        print(f"   📄 Compiling to PDF...")
        subprocess.run(
            ["typst", "compile", str(output_file), str(pdf_file)],
            check=True,
            capture_output=True,
        )
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
    parser = argparse.ArgumentParser(
        description="Generate daily plan PDFs for team members"
    )
    parser.add_argument(
        "--member",
        "-m",
        type=str,
        choices=list(TEAM_MEMBERS.keys()),
        help="Generate plan for specific team member",
    )
    parser.add_argument(
        "--all-members", action="store_true", help="Generate plans for all team members"
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default=None,
        help="Output file path (for single member)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="reports/daily-plans",
        help="Output directory (for all members)",
    )
    parser.add_argument(
        "--no-compile",
        action="store_true",
        help="Don't compile to PDF (Typst file only)",
    )

    args = parser.parse_args()

    # Check if typst is installed
    try:
        subprocess.run(["typst", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Typst not found. Install with: brew install typst")
        sys.exit(1)

    print("=" * 60)
    print("📅 Daily Plan Generator")
    print("   The Oracle That Wears Us")
    print("=" * 60)
    print()

    if args.all_members:
        # Generate for all members
        generated = generate_all_plans(args.output_dir)

        print("\n" + "=" * 60)
        print("✅ All Daily Plans Generated!")
        print("=" * 60)

        for plan in generated:
            print(f"\n{plan['name']} (@{plan['username']}):")
            print(f"   📄 PDF: {plan['pdf_file']}")
            print(f"   📝 Issues: {plan['issue_count']}")

        print("\n💡 Tip: Plans are generated at midnight daily")
        print("   Check reports/daily-plans/ for all PDFs")

    elif args.member:
        # Generate for single member
        name = TEAM_MEMBERS[args.member]
        print(f"📋 Generating plan for {name} (@{args.member})...")

        issues = get_assigned_issues(args.member)
        print(f"   Found {len(issues)} open issues")

        output = args.output or f"reports/daily-plan-{args.member}.typ"
        generate_typst_plan(name, args.member, issues, output)

        if not args.no_compile:
            pdf_output = output.replace(".typ", ".pdf")
            print(f"📄 Compiling to PDF...")
            subprocess.run(["typst", "compile", output, pdf_output], check=True)
            print(f"✅ Compiled: {pdf_output}")

        print("\n" + "=" * 60)
        print("✅ Daily Plan Generated!")
        print("=" * 60)
    else:
        parser.print_help()
        print("\n💡 Examples:")
        print("   python3 generate_daily_plan.py --all-members")
        print("   python3 generate_daily_plan.py --member berlogabob")
        print(
            "   python3 generate_daily_plan.py --member naydino -o reports/nadine-plan.typ"
        )


if __name__ == "__main__":
    main()
