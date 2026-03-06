#!/bin/bash
# Daily Plan Generator Script
# Usage: generate-daily-plan.sh USERNAME FULL_NAME DATE_PREFIX DATE_READABLE DATE_FULL

set -e

USERNAME="$1"
FULL_NAME="$2"
DATE_PREFIX="$3"
DATE_READABLE="$4"
DATE_FULL="$5"

OUTPUT_FILE="reports/daily-plans/${DATE_PREFIX}-daily-plan-${USERNAME}.typ"
TEMPLATE_FILE="templates/daily-plan-template.typ"

echo "Generating daily plan for ${FULL_NAME} (@${USERNAME})"

# Fetch open issues as JSON array
ISSUES_JSON=$(gh issue list --state open --assignee "${USERNAME}" --limit 50 \
  --json number,title,labels,milestone,body 2>/dev/null || echo "[]")

# Ensure we have valid JSON
if [ -z "${ISSUES_JSON}" ] || [ "${ISSUES_JSON}" = "null" ]; then
  ISSUES_JSON="[]"
fi

# Count issues
ISSUE_COUNT=$(echo "${ISSUES_JSON}" | jq 'length')

# Count high priority
HIGH_PRIORITY=$(echo "${ISSUES_JSON}" | jq '[.[] | select(.labels[].name | test("critical|high"))] | length')

# Create Typst file header
cat > "${OUTPUT_FILE}" << EOF
// Daily Plan - Auto-generated
#import "../../templates/daily-plan-template.typ": *

#set page(
  paper: "a4",
  margin: (x: 50pt, y: 60pt),
  footer: [
    #place(
      bottom + right,
      dx: -45pt,
      dy: 15pt,
      square(
        size: 35pt,
        fill: chapter_themes.at("1").accent,
        align(center + horizon, text(white, weight: "bold", size: 14pt)[#context counter(page).display()])
      )
    )
  ],
)

// Generated: ${DATE_PREFIX}

#report_header("1")

#section_title("1", "${DATE_READABLE}", "Daily Plan")

#table(
  columns: (1fr),
  inset: 12pt,
  stroke: none,
  fill: muted_bg,
  [
    #grid(
      columns: (1fr, 1fr),
      gutter: 15pt,
      [
        *Team Member:* \\ ${FULL_NAME} \\ #text(size: 8pt)[\@${USERNAME}] \\ \\
        *Date:* \\ ${DATE_FULL}
      ],
      [
        *Project:* \\ The Oracle That Wears Us \\ \\
        *Milestone:* \\ Varies by issue (see tasks)
      ]
    )
  ]
)

#v(2em)

== Your Tasks for Today

EOF

# Handle no issues case
if [ "${ISSUE_COUNT}" -eq 0 ]; then
  cat >> "${OUTPUT_FILE}" << 'EOF'
#box(
  width: 100%,
  inset: 20pt,
  fill: chapter_themes.at("3").accent.lighten(90%),
  radius: 4pt,
  align(center, [
    #text(size: 12pt)[🎉 No tasks assigned for today!]
    #v(8pt)
    #text(size: 9pt, fill: gray)[Use this time to explore, experiment, or help teammates]
  ])
)
EOF
else
  # Write summary boxes - using table() for Typst 0.14+
  cat >> "${OUTPUT_FILE}" << EOF
#table(
  columns: (1fr, 1fr, 1fr),
  gutter: 15pt,
  inset: 12pt,
  stroke: none,
  fill: (
    chapter_themes.at("1").accent.lighten(90%),
    chapter_themes.at("2").accent.lighten(90%),
    chapter_themes.at("3").accent.lighten(90%)
  ),
  [#block(radius: 4pt, inset: 12pt)[#align(center, [#text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[${ISSUE_COUNT}] #text(size: 8pt)[Total Tasks]])]],
  [#block(radius: 4pt, inset: 12pt)[#align(center, [#text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[${HIGH_PRIORITY}] #text(size: 8pt)[High Priority]])]],
  [#block(radius: 4pt, inset: 12pt)[#align(center, [#text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[${DATE_READABLE}] #text(size: 8pt)[Date]])]]
)

#v(2em)

== Priority Tasks
#line(length: 100%, stroke: 1pt + chapter_themes.at("2").accent)
#v(10pt)

EOF

  # Process priority issues (critical/high)
  echo "${ISSUES_JSON}" | jq -c '.[] | select(.labels[].name | test("critical|high"))' 2>/dev/null | while IFS= read -r issue; do
    if [ -n "${issue}" ] && [ "${issue}" != "null" ]; then
      NUM=$(echo "${issue}" | jq -r '.number')
      TITLE=$(echo "${issue}" | jq -r '.title' | sed 's/\[/(/g; s/\]/)/g' | head -c 200)
      BODY=$(echo "${issue}" | jq -r '.body // ""' | sed 's/!\[[^]]*\]([^)]*)/[IMAGE_PLACEHOLDER]/g; s/\[/(/g; s/\]/)/g' | tr '\n' ' ' | sed 's/  */ /g' | head -c 300)
      PRIORITY="critical"
      MS=$(echo "${issue}" | jq -r '.milestone.title // "None"')
      LABELS=$(echo "${issue}" | jq -r '[.labels[].name] | join(", ")')

      cat >> "${OUTPUT_FILE}" << EOF
#issue_card(${NUM}, [${TITLE}], "${PRIORITY}", [${BODY}...], [${MS}], [${LABELS}])

EOF
    fi
  done

  cat >> "${OUTPUT_FILE}" << 'EOF'

#v(2em)

== All Tasks
#line(length: 100%, stroke: 1pt + chapter_themes.at("1").accent)
#v(10pt)

EOF

  # Process remaining issues
  echo "${ISSUES_JSON}" | jq -c '.[] | select(.labels[].name | test("critical|high") | not)' 2>/dev/null | while IFS= read -r issue; do
    if [ -n "${issue}" ] && [ "${issue}" != "null" ]; then
      NUM=$(echo "${issue}" | jq -r '.number')
      TITLE=$(echo "${issue}" | jq -r '.title' | sed 's/\[/(/g; s/\]/)/g' | head -c 200)
      BODY=$(echo "${issue}" | jq -r '.body // ""' | sed 's/!\[[^]]*\]([^)]*)/[IMAGE_PLACEHOLDER]/g; s/\[/(/g; s/\]/)/g' | tr '\n' ' ' | sed 's/  */ /g' | head -c 300)
      PRIORITY=$(echo "${issue}" | jq -r '.labels[].name' | grep -E "medium|low" | head -1 || echo "")
      MS=$(echo "${issue}" | jq -r '.milestone.title // "None"')
      LABELS=$(echo "${issue}" | jq -r '[.labels[].name] | join(", ")')

      cat >> "${OUTPUT_FILE}" << EOF
#issue_card(${NUM}, [${TITLE}], "${PRIORITY}", [${BODY}...], [${MS}], [${LABELS}])

EOF
    fi
  done
fi

# Add footer sections
cat >> "${OUTPUT_FILE}" << 'EOF'

#v(2em)

#box(
  width: 100%,
  inset: 15pt,
  fill: muted_bg,
  radius: 4pt,
  [
    #text(size: 9pt)[
      1. *Review* each task and its comments \
      2. *Check* recent updates \
      3. *Estimate* time needed \
      4. *Plan* your approach \
      5. *Comment* your progress
    ]
  ]
)

#pagebreak()

// PAGE 2: PLANNING
#report_header("2")
#section_title("2", "2.0", "Planning Notes")

== Today's Goals
#box(
  width: 100%,
  height: 150pt,
  inset: 15pt,
  fill: muted_bg.lighten(50%),
  radius: 4pt,
  stroke: 1pt + gray.lighten(60%),
  [
    #text(size: 9pt, fill: gray, style: "italic")[Write your main goals for today here...]
  ]
)

== Time Blocks
#table(
  columns: (auto, 1fr),
  inset: 8pt,
  stroke: 0.5pt + gray.lighten(50%),
  fill: (x, y) => if calc.even(y) { muted_bg.lighten(50%) },
  [*Time*], [*Plan*],
  [09:00-10:00], [],
  [10:00-11:00], [],
  [11:00-12:00], [],
  [12:00-13:00], [Lunch Break],
  [13:00-14:00], [],
  [14:00-15:00], [],
  [15:00-16:00], [],
  [16:00-17:00], [],
)

== Blockers & Questions
#box(
  width: 100%,
  height: 100pt,
  inset: 15pt,
  fill: chapter_themes.at("2").accent.lighten(95%),
  radius: 4pt,
  stroke: 1pt + chapter_themes.at("2").accent.lighten(70%),
  [
    #text(size: 9pt, fill: gray, style: "italic")[List any blockers or questions for the team...]
  ]
)

== End of Day Checklist
#box(
  width: 100%,
  inset: 15pt,
  fill: muted_bg,
  radius: 4pt,
  [
    #text(size: 9pt)[
      □ *Update* issue status (In Progress → Review/Done) \
      □ *Add* progress comments to issues \
      □ *Push* code changes to GitHub \
      □ *Create* PR if work is ready for review \
      □ *Prepare* demo/screenshots for tomorrow \
      □ *Plan* tomorrow's tasks
    ]
  ]
)

EOF

echo "✅ Generated ${OUTPUT_FILE}"
