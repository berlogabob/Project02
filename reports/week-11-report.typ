// Weekly Report - Week 11
// Auto-generated: 2026-05-17
// Project: The Oracle That Wears Us
// Week Period: May 11 - May 17, 2026
// SHA: fc214f9

#import "../templates/daily-plan-template.typ": *

#set page(
  paper: "a4",
  margin: (x: 50pt, y: 60pt),
  footer: [
    #place(
      bottom + left,
      dx: 5pt,
      dy: -8pt,
      text(size: 7pt, fill: gray)[Generated 2026-05-17 · SHA: fc214f9 · model: qwen3.5:2b]
    )
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

#let stats_box() = {
  grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 10pt,
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("3").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[0] \
      #text(size: 7pt)[COMPLETED]
    ]),
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("2").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[0] \
      #text(size: 7pt)[INCOMPLETE]
    ]),
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("1").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[0] \
      #text(size: 7pt)[FUTURE WEEKS]
    ])
  )
}

// PAGE 1: COVER & SUMMARY
#report_header("1")
#section_title("1", "Week 11", "Weekly Progress Report")

#box(width: 100%, inset: 12pt, fill: muted_bg, radius: 4pt, [
  #grid(columns: (1fr,), [
    #text(size: 9pt)[*Project:* The Oracle That Wears Us]
  ])
  #v(6pt)
  #grid(columns: (1fr,), [
    #text(size: 9pt)[*Team:* Nadine Allan | Andrey Dyakov | Dmitri Kazantsev]
  ])
  #v(8pt)
  #line(length: 100%, stroke: 0.5pt + gray.lighten(60%))
  #v(8pt)
  #grid(columns: (auto, 1fr, auto), gutter: 10pt, [
    #text(size: 9pt)[*Report Date:* May 17, 2026]
    #h(1fr)
    #text(size: 9pt)[*Week Period:* May 11 - May 17, 2026]
  ])
])

#v(2em)

== Executive Summary

#box(width: 100%, inset: 15pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 9pt)[
    Week 11 progress: 0 of 0 tasks completed (0%).
    0 tasks from future weeks already in progress.
  ]
])

#v(1em)
#stats_box()

#v(2em)

== Week Progress

#let week_progress = 0
#box(width: 100%, height: 28pt, fill: gray.lighten(80%), inset: 0pt, radius: 3pt, [
  #box(width: week_progress * 1%, height: 100%, fill: gradient.linear(chapter_themes.at("3").grad_start, chapter_themes.at("3").grad_end), radius: 3pt)
  #place(
    center + horizon,
    text(size: 10pt, weight: "bold", fill: white)[0% complete]
  )
])

#pagebreak()

// PAGE 2: COMPLETED THIS WEEK
#report_header("2")
#section_title("2", "2.0", "Completed This Week")

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("3").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    These tasks were planned for Week 11 and successfully completed:
  ]
])

#v(1em)

#text(size: 10pt, fill: gray)[No highlighted issues completed this week.]

#v(2em)

== Notes

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("3").accent.lighten(95%), radius: 4pt, [
  #text(size: 9pt, weight: "bold")[✨ Week Summary:]
  #v(4pt)
  #text(size: 9pt)[- No issues completed this week.]
])

#pagebreak()

// PAGE 3: INCOMPLETE THIS WEEK
#report_header("3")
#section_title("3", "3.0", "Not Completed This Week")

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("2").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    These tasks were planned for Week 11 but remain incomplete:
  ]
])

#v(1em)

#text(size: 10pt, fill: green)[All planned tasks completed! 🎉]

#v(2em)

== Blockers & Challenges

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("2").accent.lighten(95%), radius: 4pt, [
  #text(size: 9pt, fill: gray)[Document any blockers or challenges that prevented completion.]
])

#pagebreak()

// PAGE 4: FUTURE WEEK TASKS (STARTED EARLY)
#report_header("4")
#section_title("4", "4.0", "Future Week Tasks (Started Early)")

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("1").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    These tasks are scheduled for future weeks but work has already begun:
  ]
])

#v(1em)

#text(size: 10pt, fill: gray)[No future week tasks started early.]

#v(2em)

== Next Week Preview

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt)[
    *Week 12:* May 18 - May 24, 2026
  ]
])

#v(1em)

#text(size: 10pt, fill: gray)[No tasks marked for next week preview.]


#v(2em)

== Team

#table(
  columns: (1fr, 1fr, 1fr),
  gutter: 10pt,
  inset: 10pt,
  stroke: none,
  fill: muted_bg.lighten(50%),
  [
    #align(center, [
      #text(size: 9pt, weight: "bold")[Nadine Allan]
      #text(size: 8pt, fill: gray)[System Architecture & Integration]
    ])
  ],
  [
    #align(center, [
      #text(size: 9pt, weight: "bold")[Andrey Dyakov]
      #text(size: 8pt, fill: gray)[Plotter & Materialization]
    ])
  ],
  [
    #align(center, [
      #text(size: 9pt, weight: "bold")[Dmitri Kazantsev]
      #text(size: 8pt, fill: gray)[Generative Concepts & Fabrication]
    ])
  ]
)

#v(2em)

== Risks & Decisions Needed

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("4").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt, fill: gray)[Document any risks or decisions needed from the team.]
])
