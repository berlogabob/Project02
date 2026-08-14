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

// Generated: 20260814

#report_header("1")

#section_title("1", "Week 24: August 14", "Daily Plan")

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
        *Team Member:* \ Andrey Dyakov \ #text(size: 8pt)[\@berlogabob] \ \
        *Date:* \ August 14, 2026 \ \
        *Week:* \ Week 24 (August 14)
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
  [#block(radius: 4pt, inset: 12pt)[#align(center, [#text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[13] #text(size: 8pt)[Total Tasks]])]],
  [#block(radius: 4pt, inset: 12pt)[#align(center, [#text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[0] #text(size: 8pt)[High Priority]])]],
  [#block(radius: 4pt, inset: 12pt)[#align(center, [#text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[August 14] #text(size: 8pt)[Date]])]]
)

#v(2em)

== Priority Tasks
#line(length: 100%, stroke: 1pt + chapter_themes.at("2").accent)
#v(10pt)


#v(2em)

== All Tasks
#line(length: 100%, stroke: 1pt + chapter_themes.at("1").accent)
#v(10pt)

#issue_card(114, [Config - Configure homing section], "", [Parent: #66 | Time: 30 min | Date: March 19 AM ...], [None], [type: development])

#issue_card(104, [Document - Create measurement sketch], "", [Parent: #64 | Time: 30 min | Date: March 14 PM ...], [None], [type: documentation, week-3])

#issue_card(104, [Document - Create measurement sketch], "", [Parent: #64 | Time: 30 min | Date: March 14 PM ...], [None], [type: documentation, week-3])

#issue_card(103, [Measure - Motor and endstop positions], "", [Parent: #64 | Time: 30 min | Date: March 14 AM ...], [None], [type: documentation])

#issue_card(102, [Measure - X/Y travel distance], "", [Parent: #64 | Time: 30 min | Date: March 14 AM ...], [None], [type: documentation, week-3])

#issue_card(102, [Measure - X/Y travel distance], "", [Parent: #64 | Time: 30 min | Date: March 14 AM ...], [None], [type: documentation, week-3])

#issue_card(71, [📊 Stabilization Phase], "", [Parent: #57 | Week 4 ...], [None], [type: documentation])

#issue_card(70, [🎯 Fine Tuning Phase], "", [Parent: #57 | Week 4 ...], [None], [type: testing])

#issue_card(69, [📐 Calibration Phase], "", [Parent: #57 | Week 3 ...], [None], [type: testing])

#issue_card(68, [🧪 Initial Testing Phase], "", [Parent: #57 | Week 3 ...], [None], [type: testing, week-3])

#issue_card(68, [🧪 Initial Testing Phase], "", [Parent: #57 | Week 3 ...], [None], [type: testing, week-3])

#issue_card(67, [🔌 Board Installation Phase], "", [Parent: #57 | Week 3 ...], [None], [type: development, week-3])

#issue_card(67, [🔌 Board Installation Phase], "", [Parent: #57 | Week 3 ...], [None], [type: development, week-3])

#issue_card(66, [⚙️ FluidNC Configuration Phase], "", [Parent: #57 | Week 2 ...], [None], [type: development, week-3])

#issue_card(66, [⚙️ FluidNC Configuration Phase], "", [Parent: #57 | Week 2 ...], [None], [type: development, week-3])

#issue_card(65, [📚 FluidNC Research Phase], "", [Parent: #57 | Week 2 ...], [None], [type: research, week-3])

#issue_card(65, [📚 FluidNC Research Phase], "", [Parent: #57 | Week 2 ...], [None], [type: research, week-3])

#issue_card(64, [📏 Measurement Phase], "", [Parent: #57 | Week 2 ...], [None], [type: documentation, week-3, Next-Week-Preview])

#issue_card(64, [📏 Measurement Phase], "", [Parent: #57 | Week 2 ...], [None], [type: documentation, week-3, Next-Week-Preview])

#issue_card(64, [📏 Measurement Phase], "", [Parent: #57 | Week 2 ...], [None], [type: documentation, week-3, Next-Week-Preview])

#issue_card(63, [✅ System Verification Phase], "", [Parent: #57 | Week 2 ...], [None], [type: testing])


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

