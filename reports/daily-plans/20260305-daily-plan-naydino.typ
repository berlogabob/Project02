// Daily Plan - Auto-generated
#import "../templates/daily-plan-template.typ": *

// Generated: 20260305

#report_header("1")

#section_title("1", "March 05", "Daily Plan")

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
        *Team Member:* \ Nadine Allan \ #text(size: 8pt)[@naydino] \ \
        *Date:* \ March 05, 2026
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

#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 15pt,
  #box(
    fill: chapter_themes.at("1").accent.lighten(90%),
    inset: 12pt,
    radius: 4pt,
    align(center, [
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[4]
      #text(size: 8pt)[Total Tasks]
    ])
  ),
  #box(
    fill: chapter_themes.at("2").accent.lighten(90%),
    inset: 12pt,
    radius: 4pt,
    align(center, [
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[0]
      #text(size: 8pt)[High Priority]
    ])
  ),
  #box(
    fill: chapter_themes.at("3").accent.lighten(90%),
    inset: 12pt,
    radius: 4pt,
    align(center, [
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[March 05]
      #text(size: 8pt)[Date]
    ])
  )
)

#v(2em)

== Priority Tasks
#line(length: 100%, stroke: 1pt + chapter_themes.at("2").accent)
#v(10pt)


#v(2em)

== All Tasks
#line(length: 100%, stroke: 1pt + chapter_themes.at("1").accent)
#v(10pt)

#issue_card(45, [Unity vs TouchDesigner vs Hybrid: Real-Time Microphone Audio Visualization – Evaluation & Final Technology Choice], "", [We need to decide once and for all what we will use for the real-time microphone input + visualization pipeline in Project02:

- Unity only
- TouchDesigner only
- Hybrid (Unity + TouchDesigner connected)...], [1st milestone: Documentation], [type: research, type: testing])

#issue_card(45, [Unity vs TouchDesigner vs Hybrid: Real-Time Microphone Audio Visualization – Evaluation & Final Technology Choice], "", [We need to decide once and for all what we will use for the real-time microphone input + visualization pipeline in Project02:

- Unity only
- TouchDesigner only
- Hybrid (Unity + TouchDesigner connected)...], [1st milestone: Documentation], [type: research, type: testing])


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

#page_footer("1", "1")
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

#page_footer("2", "2")
