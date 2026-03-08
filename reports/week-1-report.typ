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
  grid(columns: (1fr, 1fr, 1fr), gutter: 15pt,
    box(fill: chapter_themes.at("3").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[12]
      text(size: 8pt)[Completed]
    ])),
    box(fill: chapter_themes.at("2").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[9]
      text(size: 8pt)[Incomplete]
    ])),
    box(fill: chapter_themes.at("1").accent.lighten(90%), inset: 12pt, radius: 4pt, align(center, [
      text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[16]
      text(size: 8pt)[Future Weeks]
    ]))
  )
}

// PAGE 1: COVER & SUMMARY
#report_header("1")
#section_title("1", "Week 1", "Weekly Progress Report")

#table(columns: (1fr), inset: 12pt, stroke: none, fill: muted_bg, [
  #grid(columns: (1fr, 1fr), gutter: 15pt, [
    [
      *Report Date:* \ March 08, 2026 \ \
      *Week Period:* \ Mar 02 - Mar 08, 2026 \ \
      *Project:* \ The Oracle That Wears Us
    ],
    [
      *Team:* \
      #grid(columns: (1fr, 1fr, 1fr), gutter: 5pt, [Nadine Allan], [Andrey Dyakov], [Dmitri Kazantsev]) \ \
      *Total Issues This Week:* \ 21
    ]
  ])
])

#v(2em)

== Executive Summary

#box(width: 100%, inset: 15pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 9pt)[
    Week 1 progress: 12 of 21 tasks completed (57%).
    16 tasks from future weeks already in progress.
  ]
])

#v(1em)
#stats_box()

#v(2em)

== Week Progress

#let week_progress = 57
#box(width: 100%, height: 24pt, fill: gray.lighten(80%), inset: 0pt, radius: 3pt, [
  #box(width: week_progress * 1%, height: 100%, fill: gradient.linear(chapter_themes.at("3").grad_start, chapter_themes.at("3").grad_end), radius: 3pt)
])
#text(size: 8pt, fill: gray)[57% complete]

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


#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#52 - STT->TTT->TTS Pure Python workflow]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#49 - Build STT - LLM - TTS logic inside of Touchdesigner]
  
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#13 - TTS - Text to Speech KittenTTS]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#12 - STT- Speech to Text LLM]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#11 - plan tasks for next week]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#10 - add milestone from Brf]
  
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#9 - Create blanc Project v2]
  
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#8 - Create blanc Repo]
  
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#7 - TD Test: "Can TD push that text out (on-screen now; Unity later if needed)?"]
  
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#6 - TD Test: "Can TD call a free speech-to-text system and return text back into TD as DAT/CHOP?"]
  
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#5 - TD Test: "Can TD reliably ingest mic audio and turn it into usable control/data?"]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#2 - Make gitHub Kanban]
  
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)


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


#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#29 - #8 - Milestone 1 Presentation Preparation] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#28 - #7 - Hardware & Framework Selection] #text(size: 9pt, fill: red, weight: "bold")[HIGH]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#27 - #6 - Related Projects Research]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#26 - #5 - Weekly Activity Plan Creation] #text(size: 9pt, fill: red, weight: "bold")[HIGH]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#25 - #4 - Topic Selection & Theoretical Framework] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#24 - #3 - User Flow Definition]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#23 - #2 - Visual & Audio Reference Board]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#22 - #1 - Research Emergent Technologies] #text(size: 9pt, fill: red, weight: "bold")[HIGH]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#20 - Unity: Microphone input test completed]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 1]
])
#v(8pt)


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


#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#45 - Unity vs TouchDesigner vs Hybrid: Real-Time Microphone Audio Visualization – Evaluation & Final Technology Choice]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 1st milestone: Documentation]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 2]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#44 - #23 - Milestone 2 Presentation Preparation] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 2nd milestone: Prototype]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 2]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#43 - #22 - Milestone 2 Documentation] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 2nd milestone: Prototype]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 2]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#42 - #21 - Core Functionality Prototype] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 2nd milestone: Prototype]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 2]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#41 - #20 - Audio Assets Integration]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 2nd milestone: Prototype]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 2]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#40 - #19 - Graphical Assets Integration]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 2nd milestone: Prototype]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 2]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#39 - #18 - VR/AR Interaction Design]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 2nd milestone: Prototype]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 2]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#38 - #17 - Sensor-Based Interaction Implementation]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 2nd milestone: Prototype]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 2]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#37 - #16 - Latent Space Experiments]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 2nd milestone: Prototype]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 2]
])
#v(8pt)

#box(width: 100%, inset: 10pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#36 - #15 - Model Training/Fine-tuning]
  #v(4pt) #text(size: 8pt, fill: gray)[Milestone: 2nd milestone: Prototype]
  #v(4pt) #text(size: 8pt, fill: gray)[Week 2]
])
#v(8pt)


#v(2em)

== Next Week Preview

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt)[
    *Week 2:* Mar 09 - Mar 15, 2026 \
    Focus on completing remaining Week 1 tasks and starting Week 2 planned work.
  ]
])

#v(2em)

== Team Workload Overview

#table(columns: (1fr, 1fr, 1fr), inset: 10pt, stroke: 0.5pt + gray.lighten(50%),
  fill: (x, y) => if y == 0 { muted_bg },
  [*Team Member*], [*Focus Area*], [*Status*],
  [Nadine Allan], [System Architecture & Integration], [Active],
  [Andrey Dyakov], [Plotter & Materialization], [Active],
  [Dmitri Kazantsev], [Generative Concepts & Fabrication], [Active])

#v(2em)

== Risks & Decisions Needed

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("4").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt, fill: gray)[Document any risks or decisions needed from the team.]
])
