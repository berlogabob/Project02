#!/usr/bin/env python3
"""Daily Plan Generator - Clean Simple Version"""

import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

TEAM_MEMBERS = {
    "naydino": "Nadine Allan",
    "berlogabob": "Andrey Dyakov",
    "electricianv001": "Dmitri Kazantsev",
}
REPO = "berlogabob/Project02"


def get_issues(username):
    result = subprocess.run(
        [
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
            "number,title,labels,milestone,body,comments",
        ],
        capture_output=True,
        text=True,
    )
    try:
        return json.loads(result.stdout)
    except:
        return []


def clean_text(text):
    if not text:
        return ""
    # Remove images, HTML, URLs
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"https?://\S+", "", text)
    # Replace @ with "at" to avoid Typst labels
    text = text.replace("@", "at ")
    # Escape brackets
    return text.replace("[", "(").replace("]", ")").replace("\n", " ")


def main():
    output_dir = Path("reports/daily-plans")
    output_dir.mkdir(parents=True, exist_ok=True)

    date_prefix = datetime.now().strftime("%Y%m%d")
    date_str = datetime.now().strftime("%d/%m")

    for username, name in TEAM_MEMBERS.items():
        print(f"\n📋 {name} (@{username})")
        issues = get_issues(username)
        print(f"   Found {len(issues)} issues")

        # Build Typst file
        lines = [
            f"// Daily Plan - {name} - {date_prefix}",
            '#set page(paper: "a4", margin: 50pt)',
            "#set text(size: 10pt)",
            '#let blue = rgb("#2F80ED")',
            "",
            "#align(center)[#text(size: 20pt, fill: blue, weight: "bold")[📅 Daily Plan]]",
            f"#align(center)[#text(size: 16pt)[{date_str}]]",
            f"#align(center)[#text(size: 14pt)[{name}]]",
            "",
            "#line(length: 100%)",
            "",
            f"#text(size: 12pt, weight: "bold")[Tasks: {len(issues)}]",
            "",
            "== Your Tasks",
            "",
        ]

        if not issues:
            lines.append("#text(size: 12pt, fill: green)[🎉 No tasks!]")
        else:
            for issue in issues:
                num = issue["number"]
                title = clean_text(issue["title"])
                priority = ""
                for lbl in issue.get("labels", []):
                    if "critical" in lbl.get("name", ""):
                        priority = " [CRITICAL]"
                    elif "high" in lbl.get("name", ""):
                        priority = " [HIGH]"

                lines.append(f"=== #{num} - {title}{priority}")

                ms = issue.get("milestone", {})
                if ms and ms.get("title"):
                    lines.append(f"*Milestone:* {clean_text(ms['title'])}")

                labels = ", ".join([l["name"] for l in issue.get("labels", [])])
                if labels:
                    lines.append(f"*Labels:* {labels}")

                body = clean_text(issue.get("body", ""))
                if body:
                    lines.append(f"\n{body[:200]}")

                comments = issue.get("comments", [])[:2]
                if comments:
                    lines.append("\n*Comments:*")
                    for c in comments:
                        author = c.get("author", {}).get("login", "Unknown")
                        cbody = clean_text(c.get("body", ""))[:100]
                        lines.append(f"- {author}: {cbody}")

                lines.append("")

        lines.extend(
            [
                "",
                "#line(length: 100%)",
                "",
                "== Planning",
                "",
                "=== Goals",
                "- [ ] ",
                "",
                "=== Time Blocks",
                "| 09:00-10:00 | |",
                "| 10:00-11:00 | |",
                "| 11:00-12:00 | |",
                "| 12:00-13:00 | Lunch |",
                "| 13:00-14:00 | |",
                "| 14:00-15:00 | |",
                "| 15:00-16:00 | |",
                "| 16:00-17:00 | |",
                "",
                "=== Checklist",
                "- [ ] Update issues",
                "- [ ] Add comments",
                "- [ ] Push code",
                "- [ ] Plan tomorrow",
            ]
        )

        # Write .typ file
        typ_file = output_dir / f"{date_prefix}-daily-plan-{username}.typ"
        typ_file.write_text("\n".join(lines))
        print(f"   ✅ {typ_file.name}")

        # Compile to PDF
        pdf_file = output_dir / f"{date_prefix}-daily-plan-{username}.pdf"
        result = subprocess.run(
            ["typst", "compile", str(typ_file), str(pdf_file)],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"   ✅ PDF: {pdf_file.name}")
        else:
            print(f"   ❌ PDF failed: {result.stderr[:100]}")


if __name__ == "__main__":
    main()
