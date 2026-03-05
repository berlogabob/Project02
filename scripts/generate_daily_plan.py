#!/usr/bin/env python3
"""Daily Plan Generator - Uses Project02-Plan.typ Style"""

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
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"https?://\S+", "", text)
    text = text.replace("@", "at ")
    return text.replace("[", "(").replace("]", ")").replace("\n", " ")


def add_issue(lines, issue):
    num = issue["number"]
    title = clean_text(issue["title"])
    priority = ""
    for lbl in issue.get("labels", []):
        if "critical" in lbl.get("name", ""):
            priority = "critical"
            break
        elif "high" in lbl.get("name", ""):
            priority = "high"
    ms = issue.get("milestone", {})
    milestone = clean_text(ms["title"]) if ms and ms.get("title") else ""
    labels = ", ".join([l["name"] for l in issue.get("labels", [])])
    body = clean_text(issue.get("body", ""))[:200]
    lines.append(
        f'#issue_card(#{num}, [{title}], "{priority}", [{body}], [{milestone}], [{labels}])'
    )
    lines.append("")


def main():
    output_dir = Path("reports/daily-plans")
    output_dir.mkdir(parents=True, exist_ok=True)

    date_prefix = datetime.now().strftime("%Y%m%d")
    date_str = datetime.now().strftime("%d/%m")

    for username, name in TEAM_MEMBERS.items():
        print(f"\n📋 {name} (@{username})")
        issues = get_issues(username)
        print(f"   Found {len(issues)} issues")

        lines = [
            "// Daily Plan - Matches Project02-Plan.typ Style",
            '#import "daily-plan-template.typ"',
            "",
            f"// Generated: {date_prefix}",
            "",
            '#report_header("1")',
            "",
            f'#section_title("1", "{date_str}", "Daily Plan")',
            "",
            "#table(",
            "  columns: (1fr),",
            "  inset: 12pt,",
            "  stroke: none,",
            "  fill: muted_bg,",
            "  [",
            "    #grid(",
            "      columns: (1fr, 1fr),",
            "      gutter: 15pt,",
            "      [",
            f"        *Team Member:* \\ {name} \\ #text(size: 8pt)[@{username}] \\ \\",
            f"        *Date:* \\ {datetime.now().strftime('%B %d, %Y')}",
            "      ],",
            "      [",
            "        *Project:* \\ The Oracle That Wears Us \\ \\",
            "        *Milestone:* \\ 1st milestone: Documentation",
            "      ]",
            "    )",
            "  ]",
            ")",
            "",
            "#v(2em)",
            "",
            "== Your Tasks for Today",
            "",
        ]

        if not issues:
            lines.extend(
                [
                    "#box(",
                    "  width: 100%,",
                    "  inset: 20pt,",
                    '  fill: chapter_themes.at("3").accent.lighten(90%),',
                    "  radius: 4pt,",
                    "  align(center, [",
                    "    #text(size: 12pt)[🎉 No tasks assigned for today!]",
                    "    #v(8pt)",
                    "    #text(size: 9pt, fill: gray)[Use this time to explore, experiment, or help teammates]",
                    "  ])",
                    ")",
                ]
            )
        else:
            high_priority = sum(
                1
                for i in issues
                if any(
                    "critical" in l.get("name", "") or "high" in l.get("name", "")
                    for l in i.get("labels", [])
                )
            )
            lines.extend(
                [
                    "#grid(",
                    "  columns: (1fr, 1fr, 1fr),",
                    "  gutter: 15pt,",
                    "  #box(",
                    '    fill: chapter_themes.at("1").accent.lighten(90%),',
                    "    inset: 12pt,",
                    "    radius: 4pt,",
                    "    align(center, [",
                    f'      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[{len(issues)}]',
                    "      #text(size: 8pt)[Total Tasks]",
                    "    ])",
                    "  ),",
                    "  #box(",
                    '    fill: chapter_themes.at("2").accent.lighten(90%),',
                    "    inset: 12pt,",
                    "    radius: 4pt,",
                    "    align(center, [",
                    f'      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[{high_priority}]',
                    "      #text(size: 8pt)[High Priority]",
                    "    ])",
                    "  ),",
                    "  #box(",
                    '    fill: chapter_themes.at("3").accent.lighten(90%),',
                    "    inset: 12pt,",
                    "    radius: 4pt,",
                    "    align(center, [",
                    f'      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[{date_str}]',
                    "      #text(size: 8pt)[Date]",
                    "    ])",
                    "  )",
                    ")",
                    "",
                    "#v(2em)",
                    "",
                    "== Priority Tasks",
                    '#line(length: 100%, stroke: 1pt + chapter_themes.at("2").accent)',
                    "#v(10pt)",
                    "",
                ]
            )

            for issue in issues:
                labels = issue.get("labels", [])
                is_priority = any(
                    "critical" in l.get("name", "") or "high" in l.get("name", "")
                    for l in labels
                )
                if is_priority:
                    add_issue(lines, issue)

            lines.extend(
                [
                    "",
                    "#v(2em)",
                    "",
                    "== All Tasks",
                    '#line(length: 100%, stroke: 1pt + chapter_themes.at("1").accent)',
                    "#v(10pt)",
                    "",
                ]
            )

            for issue in issues:
                labels = issue.get("labels", [])
                is_priority = any(
                    "critical" in l.get("name", "") or "high" in l.get("name", "")
                    for l in labels
                )
                if not is_priority:
                    add_issue(lines, issue)

        lines.extend(
            [
                "",
                "#v(2em)",
                "",
                "#box(",
                "  width: 100%,",
                "  inset: 15pt,",
                "  fill: muted_bg,",
                "  radius: 4pt,",
                "  [",
                "    #text(size: 9pt)[",
                "      1. *Review* each task and its comments \\",
                "      2. *Check* recent updates \\",
                "      3. *Estimate* time needed \\",
                "      4. *Plan* your approach \\",
                "      5. *Comment* your progress",
                "    ]",
                "  ]",
                ")",
                "",
                '#page_footer("1", "1")',
                "#pagebreak()",
                "",
                "// PAGE 2: PLANNING",
                '#report_header("2")',
                '#section_title("2", "2.0", "Planning Notes")',
                "",
                "== Today's Goals",
                "#box(",
                "  width: 100%,",
                "  height: 150pt,",
                "  inset: 15pt,",
                "  fill: muted_bg.lighten(50%),",
                "  radius: 4pt,",
                "  stroke: 1pt + gray.lighten(60%),",
                "  [",
                '    #text(size: 9pt, fill: gray, style: "italic")[Write your main goals for today here...]',
                "  ]",
                ")",
                "",
                "== Time Blocks",
                "#table(",
                "  columns: (auto, 1fr),",
                "  inset: 8pt,",
                "  stroke: 0.5pt + gray.lighten(50%),",
                "  fill: (x, y) => if calc.even(y) { muted_bg.lighten(50%) },",
                "  [*Time*], [*Plan*],",
                "  [09:00-10:00], [],",
                "  [10:00-11:00], [],",
                "  [11:00-12:00], [],",
                "  [12:00-13:00], [Lunch Break],",
                "  [13:00-14:00], [],",
                "  [14:00-15:00], [],",
                "  [15:00-16:00], [],",
                "  [16:00-17:00], [],",
                ")",
                "",
                "== Blockers & Questions",
                "#box(",
                "  width: 100%,",
                "  height: 100pt,",
                "  inset: 15pt,",
                '  fill: chapter_themes.at("2").accent.lighten(95%),',
                "  radius: 4pt,",
                '  stroke: 1pt + chapter_themes.at("2").accent.lighten(70%),',
                "  [",
                '    #text(size: 9pt, fill: gray, style: "italic")[List any blockers or questions for the team...]',
                "  ]",
                ")",
                "",
                "== End of Day Checklist",
                "#box(",
                "  width: 100%,",
                "  inset: 15pt,",
                "  fill: muted_bg,",
                "  radius: 4pt,",
                "  [",
                "    #text(size: 9pt)[",
                "      □ *Update* issue status (In Progress → Review/Done) \\",
                "      □ *Add* progress comments to issues \\",
                "      □ *Push* code changes to GitHub \\",
                "      □ *Create* PR if work is ready for review \\",
                "      □ *Prepare* demo/screenshots for tomorrow \\",
                "      □ *Plan* tomorrow's tasks",
                "    ]",
                "  ]",
                ")",
                "",
                '#page_footer("2", "2")',
            ]
        )

        typ_file = output_dir / f"{date_prefix}-daily-plan-{username}.typ"
        typ_file.write_text("\n".join(lines))
        print(f"   ✅ {typ_file.name}")

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
