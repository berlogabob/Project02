#!/usr/bin/env python3
"""
Daily Plan Generator - Standalone Version
Creates self-contained Typst files (no imports needed)
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
        "--search",
        f"assignee:{username} repo:{REPO}",
        "--limit",
        "20",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return []
    return json.loads(result.stdout)


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


def generate_standalone_typst(
    member_name: str, member_username: str, issues: list, output_path: str
) -> str:
    """Generate standalone Typst file (no imports)"""

    today = datetime.now()
    date_str = f"{today.day:02d}/{today.month:02d}"

    # Prepare issues
    prepared_issues = []
    for issue in issues:
        prepared_issues.append(
            {
                "number": issue["number"],
                "title": issue["title"].replace("[", "(").replace("]", ")"),
                "priority": format_priority(issue),
                "body": issue.get("body", "")[:200]
                .replace("[", "(")
                .replace("]", ")")
                .replace("\n", " "),
                "milestone": issue.get("milestone"),
                "labels": issue.get("labels", []),
            }
        )

    # Sort by priority
    priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    prepared_issues.sort(key=lambda x: priority_order.get(x["priority"], 2))

    # Generate simple Typst content
    issues_content = ""
    for issue in prepared_issues:
        issues_content += f"""
== #{issue["number"]} - {issue["title"]}
*Priority:* {issue["priority"].upper()}
"""
        if issue["milestone"]:
            issues_content += f"*Milestone:* {issue['milestone']['title']}\n"
        if issue["body"]:
            issues_content += f"\n{issue['body']}\n"
        issues_content += "\n---\n"

    typst_content = f'''// Daily Plan for {member_name}
// Generated: {today.strftime("%Y-%m-%d %H:%M")}
// Project: The Oracle That Wears Us

#set page(paper: "a4", margin: (x: 50pt, y: 60pt))
#set text(font: "Noto Sans", size: 10pt, fill: rgb("#333333"), lang: "en")

// Header
#align(center)[
  #text(size: 24pt, weight: "bold", "📅 Daily Plan")
  #v(10pt)
  #text(size: 18pt, "{date_str}")
  #v(10pt)
  #text(size: 14pt, "{member_name} ({member_username})")
]

#v(20pt)
#line(length: 100%)
#v(20pt)

== Summary
*Total Tasks:* {len(prepared_issues)}
*High Priority:* {len([i for i in prepared_issues if i["priority"] in ["critical", "high"]])}
*Milestone:* {prepared_issues[0]["milestone"]["title"] if prepared_issues and prepared_issues[0]["milestone"] else "-"}

#v(20pt)
#line(length: 100%)
#v(20pt)

== Your Tasks

{issues_content}

#v(20pt)
#line(length: 100%)
#v(20pt)

== Planning Notes

=== Today's Goals
- [ ] 

=== Time Blocks
| Time | Plan |
|------|------|
| 09:00-10:00 | |
| 10:00-11:00 | |
| 11:00-12:00 | |
| 12:00-13:00 | Lunch |
| 13:00-14:00 | |
| 14:00-15:00 | |
| 15:00-16:00 | |
| 16:00-17:00 | |

=== Blockers
- 

=== End of Day Checklist
- [ ] Update issue status
- [ ] Add progress comments
- [ ] Push code changes
- [ ] Create PR if ready
- [ ] Plan tomorrow
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

        issues = get_assigned_issues(username)
        print(f"   Found {len(issues)} open issues")

        output_file = output_path / f"daily-plan-{username}.typ"
        generate_standalone_typst(name, username, issues, str(output_file))

        # Compile to PDF
        pdf_file = output_path / f"daily-plan-{username}.pdf"
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
