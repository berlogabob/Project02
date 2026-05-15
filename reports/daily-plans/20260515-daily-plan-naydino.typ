// Daily Plan - Auto-generated
#import "../../templates/daily-plan-template.typ": *

#set page(
  paper: "a4",
  margin: (x: 50pt, y: 60pt),
  footer: [
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

// Generated: 20260515

#report_header("1")

#section_title("1", "Week 11: May 15", "Daily Plan")

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
        *Team Member:* \ Nadine Allan \ #text(size: 8pt)[\@naydino] \ \
        *Date:* \ May 15, 2026 \ \
        *Week:* \ Week 11 (May 15)
      ],
      [
        *Project:* \ The Oracle That Wears Us \ \
        *Milestone:* \ Varies by issue (see tasks)
      ]
    )
  ]
)

#v(2em)

== Your Tasks for Today

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

