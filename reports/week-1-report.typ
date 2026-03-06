// Weekly Report - Week 1
// Auto-generated: 2026-03-06
// Project: The Oracle That Wears Us

#import "../templates/daily-plan-template.typ": *

// Weekly report uses all components from the template
// Page numbering is automatic via the template
// Note: report_header, section_title, task_table are imported from template

#let stats_box() = {
  grid(columns: (1fr, 1fr, 1fr), gutter: 15pt,
    box(fill: chapter_themes.at("1").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[0]
      text(size: 8pt)[Completed]
    ])),
    box(fill: chapter_themes.at("2").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[14]
      text(size: 8pt)[In Progress]
    ])),
    box(fill: chapter_themes.at("3").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[14]
      text(size: 8pt)[Total]
    ]))
  )
}

// PAGE 1: COVER & SUMMARY
#report_header("1")
#section_title("1", "Week 1", "Weekly Progress Report")

#table(columns: (1fr), inset: 12pt, stroke: none, fill: muted_bg, [
  #grid(columns: (1fr, 1fr), gutter: 15pt, [
    *Report Date:* \ March 06, 2026 \ \
    *Milestone:* \ 1st milestone: Documentation \ \
    *Week Period:* \ Week 1
  ], [
    *Project:* \ The Oracle That Wears Us \ \
    *Team:* \
    #grid(columns: (1fr, 1fr, 1fr), gutter: 5pt, [Nadine Allan], [Andrey Dyakov], [Dmitri Kazantsev])
  ])
])

#v(2em)

== Executive Summary

#box(width: 100%, inset: 15pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 9pt)[
    This week, the team made progress on GitHub issues.
    Total: 14 issues | Completed: 0 | In Progress: 14
  ]
])

#v(1em)
#stats_box()

#v(2em)

== Key Achievements This Week

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("3").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    - Completed 0 issues
    - Progress on 1st milestone: Documentation
    - Team collaboration through GitHub
  ]
])

#pagebreak()

// PAGE 2: COMPLETED WORK
#report_header("2")
#section_title("2", "2.0", "Completed Issues")

#text(size: 10pt, fill: gray)[No issues completed this week.]

#v(2em)

== Notes & Observations

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt, fill: gray)[All completed issues have been reviewed and merged.]
])

#pagebreak()

// PAGE 3: IN PROGRESS
#report_header("3")
#section_title("3", "3.0", "Work In Progress")

== Current Sprint


#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#45 - Unity vs TouchDesigner vs Hybrid: Real-Time Microphone Audio Visualization – Evaluation & Final Technology Choice]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#29 - #8 - Milestone 1 Presentation Preparation]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#28 - #7 - Hardware & Framework Selection]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#27 - #6 - Related Projects Research]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#26 - #5 - Weekly Activity Plan Creation]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#25 - #4 - Topic Selection & Theoretical Framework]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#24 - #3 - User Flow Definition]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#23 - #2 - Visual & Audio Reference Board]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#22 - #1 - Research Emergent Technologies]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#20 - Unity: Microphone input test completed]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
])
#v(8pt)


#v(2em)

== Blockers & Challenges

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("2").accent.lighten(95%), radius: 4pt, [
  #text(size: 9pt, fill: gray)[No major blockers this week.]
])

#pagebreak()

// PAGE 4: NEXT WEEK PLAN
#report_header("4")
#section_title("4", "4.0", "Next Week Plan")

== Planned Focus

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt)[
    - Continue with remaining milestone tasks
    - Review and merge pending PRs
    - Prepare for next week's sprint goals
  ]
])

#v(2em)

== Milestone Progress

#let milestone_progress = 25
#box(width: 100%, height: 20pt, fill: gray.lighten(80%), inset: 0pt, radius: 3pt, [
  #box(width: milestone_progress * 1%, height: 100%, fill: gradient.linear(chapter_themes.at("1").grad_start, chapter_themes.at("1").grad_end), radius: 3pt)
])
#text(size: 8pt, fill: gray)[#milestone_progress% complete towards 1st milestone: Documentation]

#v(2em)

== Team Workload

#table(columns: (1fr, 1fr, 1fr), inset: 10pt, stroke: 0.5pt + gray.lighten(50%),
  fill: (x, y) => if y == 0 { muted_bg },
  [*Team Member*], [*Issues Completed*], [*Focus Area*],
  [Nadine Allan], [TBD], [System Architecture & Integration],
  [Andrey Dyakov], [TBD], [Plotter & Materialization],
  [Dmitri Kazantsev], [TBD], [Generative Concepts & Fabrication])

#v(2em)

== Risks & Decisions Needed

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("4").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt, fill: gray)[No major risks identified.]
])
