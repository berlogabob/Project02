# Project02: Interactive Installation "The Oracle That Wears Us" - Comprehensive Documentation and Automation Setup

## Document Overview
This document provides a complete, self-contained summary of the Project02 setup, including the Typst-based project plan, Python script for generating daily plans from GitHub issues, GitHub Actions workflow for automation, and related configurations. It is designed for offline use, with all relevant code, explanations, and recommendations included inline. No external references or links are used.

The project involves an interactive art installation combining fashion and emerging tech, using AI, hardware like plotters, and software like Unity and TouchDesigner. The focus here is on the reporting and automation system: generating styled daily plans (PDFs) based on GitHub issues, ensuring consistency with the main project plan's theme.

Key features:
- Typst for document generation (modern typesetting).
- Python script to fetch and process GitHub issues.
- GitHub Actions for daily automation.
- Handling of issues with images: Images from GitHub issues are not embedded in daily reports. Instead, use a placeholder tag like `[IMAGE_PLACEHOLDER: Original issue contained an image - check manually for weekly report inclusion]`. This allows manual review to decide if images are needed in the larger weekly report (e.g., for visual documentation of prototypes or diagrams).

This document is maximally detailed for standalone reference, including full code snippets where applicable.

## Project Description
**Project Title:** The Oracle That Wears Us  
**Field:** Fashion & Emerging Tech  
**Team Members:**  
- Nadine Allan (@naydino, Student ID: 20250828) - System Architecture & Integration  
- Andrey Dyakov (@berlogabob, Student ID: 20251186) - Plotter & Materialization  
- Dmitri Kazantsev (@electricianv001, Student ID: 20220711) - Generative Concepts & Fabrication  

**Core Concept:** An arcade-style installation in a projection-mapped tent. User inputs are captured, processed via AI, and plotted onto fabric fragments using a robotic pen plotter. Hardware includes plotter, arcade console, projector, camera. Software stack: Unity, TouchDesigner, OSC, Python, Generative AI.

**Project Structure:**  
- Agile setup with big milestones (6 phases), weekly small milestones, and daily tiny sprints.  
- GitHub for tracking: Main branch (stable), weekly branches (week-XX), personal branches (name/).  
- Weekly flow: Monday meeting, work in branches, Sunday PDF generation, Monday demo.  

**Phases (High-Level Timeline):**  
1. **Research:** Core problems, similar installations, tech evaluation.  
2. **Experimentation:** Interaction tests, generative techniques, plotter tests.  
3. **System Architecture:** OSC schema, Unity prototype, data flow.  
4. **Fabrication & Spatial Setup:** Projection mapping, console build, safety plan.  
5. **Testing & Polish:** Rehearsals, bug fixing, final docs.  
6. **MVP & Extras:** Core version first, then optional features like UV layers.

**Terms/Abbreviations:**  
- Big M: Major GitHub Milestone (e.g., Research).  
- OSC: Open Sound Control.  
- Typst: Typesetting system for reports.  
- MVP: Minimum Viable Product.  
- PR: Pull Request.  
- Tiny Sprint: 1-4 issues per person daily/2-day.  
- Project Board: GitHub Kanban (Backlog → Done).

## Typst Configurations and Templates
Typst is used for generating styled reports (project plan and daily plans). The main project plan ("Project02-Plan.typ") defines themes, components, and layout. For modularity, extract reusable parts into a separate template file ("daily-plan-template.typ") in a "templates/" folder. This allows easy editing of styles (colors, fonts, insets) without modifying the generator script.

### Full Content of "daily-plan-template.typ"
```
// templates/daily-plan-template.typ
// Reusable template for daily plans - edit styles here

#set page(
  paper: "a4",
  margin: (x: 50pt, y: 60pt),
)

#set text(
  font: "Noto Sans",
  size: 10pt,
  fill: rgb("#333333"),
  lang: "en"
)

#let chapter_themes = (
  "1": (
    grad_start: rgb("#2F80ED"),
    grad_end: rgb("#9B51E0"),
    accent: rgb("#33A1C9"),
    page_bg: rgb("#A5C7F3")
  ),
  "2": (
    grad_start: rgb("#eb3349"),
    grad_end: rgb("#f45c43"),
    accent: rgb("#e74c3c"),
    page_bg: rgb("#ff9a9e")
  ),
  "3": (
    grad_start: rgb("#11998e"),
    grad_end: rgb("#38ef7d"),
    accent: rgb("#1b5e20"),
    page_bg: rgb("#c8e6c9")
  ),
  "4": (
    grad_start: rgb("#F2994A"),
    grad_end: rgb("#F2C94C"),
    accent: rgb("#d35400"),
    page_bg: rgb("#fdebd0")
  )
)

#let muted_bg = rgb("#f4f4f4")

#let report_header(ch_idx, category: "DAILY PLAN") = {
  let t = chapter_themes.at(ch_idx)
  move(dy: -20pt)[
    #box(
      width: 100%,
      height: 30pt,
      fill: gradient.linear(t.grad_start, t.grad_end),
      inset: (right: 15pt),
      align(right + horizon, text(white, weight: "bold", tracking: 1.5pt, size: 8pt)[#upper(category)])
    )
  ]
}

#let section_title(ch_idx, num, title) = {
  let t = chapter_themes.at(ch_idx)
  v(20pt)
  text(fill: t.accent, size: 22pt, weight: "extrabold")[#num]
  v(-12pt)
  text(fill: t.accent, size: 22pt, weight: "bold")[#upper(title)]
  v(20pt)
}

#let page_footer(ch_idx, num) = {
  let t = chapter_themes.at(ch_idx)
  place(
    bottom + right,
    dx: 30pt,
    dy: 30pt,
    square(
      size: 35pt,
      fill: t.page_bg,
      align(center + horizon, text(white, weight: "bold", size: 14pt)[#num])
    )
  )
}

#let task_table(rows) = {
  table(
    columns: (1fr, 1fr),
    inset: 10pt,
    stroke: 0.5pt + gray.lighten(50%),
    fill: (x, y) => if y == 0 { muted_bg } else { white },
    [*Task*], [*Deliverable*],
    ..rows
  )
}

#let issue_card(num, title, priority, body, milestone, labels) = {
  let bg = if priority == "critical" { rgb("#ffebee") }
           else if priority == "high"    { rgb("#fff3e0") }
           else if priority == "medium"  { rgb("#e8f5e9") }
           else                          { muted_bg }
  
  let border = if priority == "critical" { rgb("#c62828") }
               else if priority == "high"    { rgb("#f57c00") }
               else                          { gray.lighten(60%) }

  box(
    width: 100%,
    inset: 12pt,
    radius: 6pt,
    fill: bg,
    stroke: 1pt + border,
    [
      #text(weight: "bold", fill: chapter_themes.at("1").accent)[Issue ##num: #title] \
      #if priority != "" [#text(fill: red, weight: "semibold")[#upper(priority)]] \
      #h(1fr) #text(size: 9pt, fill: gray)[#milestone] \
      #v(0.4em)
      #text(size: 9.5pt)[#body]
      #v(0.3em)
      #text(size: 8.5pt, fill: gray)[Labels: #labels]
    ]
  )
}
```

### Usage in Generated Files
Generated daily plan .typ files start with:  
`#import "templates/daily-plan-template.typ": *`  
This imports all definitions, ensuring consistency.

## Python Script: generate_daily_plan.py
This script fetches open GitHub issues for each team member using `gh` CLI, cleans text (handling images with placeholders), generates Typst code matching the project theme, and compiles to PDF.

### Full Script Code
```
#!/usr/bin/env python3
"""Daily Plan Generator - Uses Project02-Plan.typ Style"""

import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
import os

TEAM_MEMBERS = {
    "naydino": "Nadine Allan",
    "berlogabob": "Andrey Dyakov",
    "electricianv001": "Dmitri Kazantsev",
}
REPO = os.environ.get("GITHUB_REPOSITORY", "berlogabob/Project02")

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
    if result.returncode != 0:
        print(f"Error fetching issues for {username}: {result.stderr}")
        return []
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as e:
        print(f"JSON error: {e}")
        return []

def clean_text(text):
    if not text:
        return ""
    
    # Handle images: Replace with placeholder tag for manual review
    text = re.sub(
        r'!\[([^\]]*)\]\(([^)]+)\)',
        r'[IMAGE_PLACEHOLDER: Original issue contained an image - check manually for weekly report inclusion]',
        text
    )
    
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"https?://\S+", "", text)
    text = text.replace("@", "at ")
    return text.replace("[", "(").replace("]", ")").replace("\n", " ").strip()

def get_priority(labels):
    label_names = [l.get("name", "").lower() for l in labels]
    if any("critical" in n for n in label_names):
        return "critical"
    elif any("high" in n for n in label_names):
        return "high"
    elif any("medium" in n for n in label_names):
        return "medium"
    elif any("low" in n for n in label_names):
        return "low"
    return ""

def add_issue(lines, issue):
    num = issue["number"]
    title = clean_text(issue["title"])
    priority = get_priority(issue.get("labels", []))
    ms = issue.get("milestone", {}) or {}
    milestone = clean_text(ms.get("title", "None"))
    labels = ", ".join([l["name"] for l in issue.get("labels", [])])
    body = clean_text(issue.get("body", ""))[:300] + "..." if issue.get("body") else ""
    lines.append(
        f'#issue_card(#{num}, [{title}], "{priority}", [{body}], [{milestone}], [{labels}])'
    )
    lines.append("")

def main():
    output_dir = Path("reports/daily-plans")
    output_dir.mkdir(parents=True, exist_ok=True)

    date_prefix = datetime.now().strftime("%Y%m%d")
    date_str = datetime.now().strftime("%B %d")
    full_date = datetime.now().strftime("%B %d, %Y")

    for username, name in TEAM_MEMBERS.items():
        print(f"\n📋 {name} (@{username})")
        issues = get_issues(username)
        print(f"   Found {len(issues)} issues")

        lines = [
            "// Daily Plan - Matches Project02-Plan.typ Style",
            '#import "templates/daily-plan-template.typ": *',
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
            f"        *Date:* \\ {full_date}",
            "      ],",
            "      [",
            "        *Project:* \\ The Oracle That Wears Us \\ \\",
            "        *Milestone:* \\ Varies by issue (see tasks)",
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
            lines.extend([
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
            ])
        else:
            high_priority = sum(1 for i in issues if get_priority(i.get("labels", [])) in ["critical", "high"])
            lines.extend([
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
            ])

            for issue in issues:
                if get_priority(issue.get("labels", [])) in ["critical", "high"]:
                    add_issue(lines, issue)

            lines.extend([
                "",
                "#v(2em)",
                "",
                "== All Tasks",
                '#line(length: 100%, stroke: 1pt + chapter_themes.at("1").accent)',
                "#v(10pt)",
                "",
            ])

            for issue in issues:
                if get_priority(issue.get("labels", [])) not in ["critical", "high"]:
                    add_issue(lines, issue)

        lines.extend([
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
        ])

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
            print(f"   ❌ PDF failed: {result.stderr}")

if __name__ == "__main__":
    main()
```

### Key Features of the Script
- **Team Support:** Loops over all 3 team members, generating separate files for each. Works for all in scheduled runs, or specific in manual triggers (via --member flag, if added).
- **Issue Handling:** Fetches open issues, categorizes by priority (critical/high/medium/low based on labels), cleans text.
- **Image Handling:** Replaces Markdown images with `[IMAGE_PLACEHOLDER: Original issue contained an image - check manually for weekly report inclusion]`. This tags the presence without embedding, allowing manual check for inclusion in weekly reports (e.g., if the image is a diagram or photo relevant to progress).
- **Output:** .typ files imported from template, compiled to PDF. If no issues, shows "No tasks" box.
- **Error Handling:** Logs failures in fetching/compiling.

## GitHub Actions Workflow: daily-plans-v2.yml
Automates daily generation at 00:00 UTC. Supports manual triggers for specific members. Commits PDFs back to repo, uploads artifacts.

### Full Workflow Code
```
name: Generate Daily Plans v2

on:
  schedule:
    - cron: "0 0 * * *"

  workflow_dispatch:
    inputs:
      member:
        description: "Specific member (leave empty for all)"
        required: false
        default: ""
        type: choice
        options:
          - ""
          - naydino
          - berlogabob
          - electricianv001

permissions:
  contents: write
  actions: read

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Install Typst
        uses: typst-community/setup-typst@v3
        with:
          typst-version: "latest"

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip

      - name: Authenticate GitHub CLI
        run: |
          echo "${{ secrets.GITHUB_TOKEN }}" | gh auth login --with-token --hostname github.com

      - name: Generate date stamp
        id: date
        run: |
          echo "date=$(date +'%Y-%m-%d')" >> "$GITHUB_OUTPUT"
          echo "datetime=$(date --iso-8601=minutes)" >> "$GITHUB_OUTPUT"

      - name: Generate daily plan(s)
        run: |
          if [ -z "${{ github.event.inputs.member }}" ]; then
            python3 scripts/generate_daily_plan.py
          else
            python3 scripts/generate_daily_plan.py \
              --member "${{ github.event.inputs.member }}"
          fi
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Compile Typst files to PDF
        run: |
          mkdir -p reports/daily-plans
          for file in reports/daily-plans/*.typ; do
            pdf="${file%.typ}.pdf"
            echo "Compiling $file → $pdf"
            typst compile "$file" "$pdf" || echo "Failed: $file"
          done

      - name: Commit generated daily plans
        run: |
          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A reports/daily-plans/
          if git diff --staged --quiet; then
            echo "No changes to commit"
          else
            git commit -m "📅 Auto-generated daily plans (${{ steps.date.outputs.date }})"
            git push
          fi

      - name: Upload PDFs (artifacts)
        uses: actions/upload-artifact@v4
        with:
          name: daily-plans-pdf-${{ steps.date.outputs.date }}
          path: reports/daily-plans/*.pdf
          if-no-files-found: warn
          retention-days: 14

      - name: Upload sources (artifacts)
        uses: actions/upload-artifact@v4
        with:
          name: daily-plans-typ-${{ steps.date.outputs.date }}
          path: reports/daily-plans/*.typ
          if-no-files-found: warn
          retention-days: 14
```

### Workflow Details
- **Triggers:** Daily schedule or manual (with member selection).
- **Steps:** Checkout, install Typst/Python/gh, auth, generate, compile, commit if changed, upload artifacts.
- **Team Integration:** Generates for all 3 members by default; supports specific via input.
- **Error Resilience:** Continues on failures, warns on no files.

## Issues and Resolutions
### Common Problems and Fixes
- **Missing Definitions (e.g., #issue_card):** Resolved by defining in template.
- **Image Errors in Issues:** Caused by Markdown/HTML in issue bodies. Fixed by replacing with placeholders in clean_text(). No embedding in daily PDFs; tag for manual weekly review (e.g., if image is a prototype sketch, add to weekly report manually).
- **Hardcoded Values:** Made dynamic (e.g., milestones from issues).
- **Workflow Auth/Commits:** Proper gh login, check for changes before commit.
- **Compilation Pathing:** Run from root; import paths relative.

### Recommendations for Offline/Manual Use
- Run script locally: `python scripts/generate_daily_plan.py` (needs gh/typst installed).
- Manual Image Check: Search daily PDFs for [IMAGE_PLACEHOLDER] tags. Review original GitHub issue; if useful (e.g., visual progress), include in weekly report PDF manually via Typst #image() or attachment.
- Customization: Edit template.typ for styles; add --member flag to script for single-user runs.
- Testing: Create test issues with images/labels; generate and verify PDFs.

This document is complete for standalone use. Date generated: March 05, 2026.



run [@github_workflow_action_day.md](file:///Users/berloga/Documents/GitHub/Project02/github_workflow_action_day.md) update uour daily workflow with this document
