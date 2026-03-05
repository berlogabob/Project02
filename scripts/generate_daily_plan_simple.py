#!/usr/bin/env python3
"""
Daily Plan Generator - Minimal Working Version
"""

import argparse
import json
import re
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
    # Remove markdown images
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Remove URLs
    text = re.sub(r"https?://\S+", "", text)
    # Replace @ with space to avoid Typst label issues
    text = text.replace("@", " ")
    # Escape other Typst special chars
    return text.replace("[", "(").replace("]", ")").replace("\n", " ").replace("#", "")


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

        # Sort
        priority_order = {"critical": 0, "high": 1, "medium": 2}
        prepared_issues.sort(key=lambda x: priority_order.get(x["priority"], 2))

        total = len(prepared_issues)
        high_priority = len(
            [i for i in prepared_issues if i["priority"] in ["critical", "high"]]
        )

        # Generate Typst - SIMPLE VERSION
        lines = []
        lines.append(f"// Daily Plan for {name}")
        lines.append(f"// Generated: {today.strftime('%Y-%m-%d %H:%M')}")
        lines.append("")
        lines.append('#set page(paper: "a4", margin: (x: 50pt, y: 60pt))')
        lines.append(
            '#set text(font: "Noto Sans", size: 10pt, fill: rgb("#333333"), lang: "en")'
        )
        lines.append("")
        lines.append('#let blue = rgb("#2F80ED")')
        lines.append('#let red = rgb("#eb3349")')
        lines.append('#let green = rgb("#11998e")')
        lines.append("")

        # Title
        lines.append("#align(center)[")
        lines.append(
            f'  #text(size: 24pt, weight: "bold", fill: blue, "📅 Daily Plan")'
        )
        lines.append(f"  #v(10pt)")
        lines.append(f'  #text(size: 18pt, "{date_str}")')
        lines.append(f"  #v(10pt)")
        lines.append(f'  #text(size: 14pt, "{name} (@{username})")')
        lines.append("]")
        lines.append("")
        lines.append("#v(20pt)")
        lines.append("#line(length: 100%)")
        lines.append("#v(20pt)")
        lines.append("")

        # Stats
        lines.append(
            f'#text(size: 12pt, weight: "bold", "Tasks: {total} | High Priority: {high_priority} | Date: {date_str}")'
        )
        lines.append("")
        lines.append("#v(20pt)")
        lines.append("#line(length: 100%)")
        lines.append("#v(20pt)")
        lines.append("")

        # Issues
        lines.append("== Your Tasks")
        lines.append("")

        if total == 0:
            lines.append('#text(size: 12pt, fill: green, "🎉 No tasks for today!")')
        else:
            for issue in prepared_issues:
                badge = (
                    f" [{issue['priority'].upper()}]"
                    if issue["priority"] in ["critical", "high"]
                    else ""
                )
                lines.append(f"=== #{issue['number']} - {issue['title']}{badge}")
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

        lines.append("")
        lines.append("#v(30pt)")
        lines.append("#line(length: 100%)")
        lines.append("#v(20pt)")
        lines.append("")
        lines.append("== Planning Notes")
        lines.append("")
        lines.append("=== Goals")
        lines.append("- [ ] ")
        lines.append("")
        lines.append("=== Time Blocks")
        lines.append("")
        lines.append("| Time | Plan |")
        lines.append("|------|------|")
        lines.append("| 09:00-10:00 | |")
        lines.append("| 10:00-11:00 | |")
        lines.append("| 11:00-12:00 | |")
        lines.append("| 12:00-13:00 | Lunch |")
        lines.append("| 13:00-14:00 | |")
        lines.append("| 14:00-15:00 | |")
        lines.append("| 15:00-16:00 | |")
        lines.append("| 16:00-17:00 | |")
        lines.append("")
        lines.append("=== Checklist")
        lines.append("- [ ] Update issues")
        lines.append("- [ ] Add comments")
        lines.append("- [ ] Push code")
        lines.append("- [ ] Plan tomorrow")

        # Write file
        output_file = output_path / f"{date_prefix}-daily-plan-{username}.typ"
        with open(output_file, "w") as f:
            f.write("\n".join(lines))

        print(f"✅ Generated: {output_file}")

        # Compile
        pdf_file = output_path / f"{date_prefix}-daily-plan-{username}.pdf"
        print(f"   📄 Compiling to PDF...")
        result = subprocess.run(
            ["typst", "compile", str(output_file), str(pdf_file)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"   ⚠️  Failed: {result.stderr[:200]}")
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--all-members", action="store_true")
    parser.add_argument("--output-dir", default="reports/daily-plans")
    args = parser.parse_args()

    try:
        subprocess.run(["typst", "--version"], capture_output=True, check=True)
    except:
        print("❌ Typst not found")
        sys.exit(1)

    print("=" * 60)
    print("📅 Daily Plan Generator")
    print("=" * 60)
    print()

    if args.all_members:
        generated = generate_all_plans(args.output_dir)
        print("\n" + "=" * 60)
        print("✅ Done!")
        print("=" * 60)
        for plan in generated:
            print(f"{plan['name']}: {plan['issue_count']} issues -> {plan['pdf_file']}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
