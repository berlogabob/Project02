// Weekly Report - Week 1
// Auto-generated: 2026-03-08
// Project: The Oracle That Wears Us
// Week Period: Mar 02 - Mar 08, 2026

#import "../templates/daily-plan-template.typ": *

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

#let stats_box() = {
  grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 10pt,
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("3").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[17] \
      #text(size: 7pt)[COMPLETED]
    ]),
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("2").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[0] \
      #text(size: 7pt)[INCOMPLETE]
    ]),
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("1").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[16] \
      #text(size: 7pt)[FUTURE WEEKS]
    ])
  )
}

// PAGE 1: COVER & SUMMARY
#report_header("1")
#section_title("1", "Week 1", "Weekly Progress Report")

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
    #text(size: 9pt)[*Report Date:* March 08, 2026]
    #h(1fr)
    #text(size: 9pt)[*Week Period:* Mar 02 - Mar 08, 2026]
  ])
])

#v(2em)

== Executive Summary

#box(width: 100%, inset: 15pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 9pt)[
    Week 1 progress: 17 of 17 tasks completed (100%).
    16 tasks from future weeks already in progress.
  ]
])

#v(1em)
#stats_box()

#v(2em)

== Week Progress

#let week_progress = 100
#box(width: 100%, height: 28pt, fill: gray.lighten(80%), inset: 0pt, radius: 3pt, [
  #box(width: week_progress * 1%, height: 100%, fill: gradient.linear(chapter_themes.at("3").grad_start, chapter_themes.at("3").grad_end), radius: 3pt)
  #place(
    center + horizon,
    text(size: 10pt, weight: "bold", fill: white)[100% complete]
  )
])

#pagebreak()

// PAGE 2: COMPLETED THIS WEEK
#report_header("2")
#section_title("2", "2.0", "Completed This Week")

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("3").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    These tasks were planned for Week 1 and successfully completed:
  ]
])

#v(1em)


#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#54 - Weekly - report generator]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#53 - Auto Daily-Planning report generator]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#52 - STT->TTT->TTS Pure Python workflow]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#49 - Build STT - LLM - TTS logic inside of Touchdesigner]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#26 - #5 - Weekly Activity Plan Creation] #text(size: 9pt, fill: red, weight: "bold")[HIGH]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#20 - Unity: Microphone input test completed]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#13 - TTS - Text to Speech KittenTTS]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#12 - STT- Speech to Text LLM]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#11 - plan tasks for next week]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#10 - add milestone from Brf]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#9 - Create blanc Project v2]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#8 - Create blanc Repo]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#7 - TD Test: "Can TD push that text out (on-screen now; Unity later if needed)?"]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#6 - TD Test: "Can TD call a free speech-to-text system and return text back into TD as DAT/CHOP?"]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#5 - TD Test: "Can TD reliably ingest mic audio and turn it into usable control/data?"]
])
#v(4pt)


#v(2em)

== Notes

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt, fill: gray)[Review completed work and ensure quality standards are met.]
])

#pagebreak()

// PAGE 3: INCOMPLETE THIS WEEK
#report_header("3")
#section_title("3", "3.0", "Not Completed This Week")

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("2").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    These tasks were planned for Week 1 but remain incomplete:
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


#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#45 - Unity vs TouchDesigner vs Hybrid: Real-Time Microphone Audio Visualization – Evaluation & Final Technology Choice] #text(size: 8pt, fill: gray)[(Week 2)]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#44 - #23 - Milestone 2 Presentation Preparation] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL] #text(size: 8pt, fill: gray)[(Week 2)]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#43 - #22 - Milestone 2 Documentation] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL] #text(size: 8pt, fill: gray)[(Week 2)]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#42 - #21 - Core Functionality Prototype] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL] #text(size: 8pt, fill: gray)[(Week 2)]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#41 - #20 - Audio Assets Integration] #text(size: 8pt, fill: gray)[(Week 2)]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#40 - #19 - Graphical Assets Integration] #text(size: 8pt, fill: gray)[(Week 2)]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#39 - #18 - VR/AR Interaction Design] #text(size: 8pt, fill: gray)[(Week 2)]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#38 - #17 - Sensor-Based Interaction Implementation] #text(size: 8pt, fill: gray)[(Week 2)]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#37 - #16 - Latent Space Experiments] #text(size: 8pt, fill: gray)[(Week 2)]
])
#v(4pt)

#box(width: 100%, inset: 8pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 10pt)[#36 - #15 - Model Training/Fine-tuning] #text(size: 8pt, fill: gray)[(Week 2)]
])
#v(4pt)


#v(2em)

== Next Week Preview

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt)[
    *Week 2:* Mar 09 - Mar 15, 2026 \
    Focus on completing remaining Week 1 tasks and starting Week 2 planned work.
  ]
])

#v(2em)

== Team

#grid(columns: (1fr, 1fr, 1fr), gutter: 10pt,
  box(inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, align(center, [
    text(size: 9pt, weight: "bold")[Nadine Allan]
    text(size: 8pt, fill: gray)[System Architecture]
  ])),
  box(inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, align(center, [
    text(size: 9pt, weight: "bold")[Andrey Dyakov]
    text(size: 8pt, fill: gray)[Plotter & Materialization]
  ])),
  box(inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, align(center, [
    text(size: 9pt, weight: "bold")[Dmitri Kazantsev]
    text(size: 8pt, fill: gray)[Generative Concepts]
  ]))
)

#v(2em)

== Risks & Decisions Needed

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("4").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt, fill: gray)[Document any risks or decisions needed from the team.]
])
