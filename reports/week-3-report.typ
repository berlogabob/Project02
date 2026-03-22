// Weekly Report - Week 3
// Auto-generated: 2026-03-22
// Project: The Oracle That Wears Us
// Week Period: Mar 16 - Mar 22, 2026
// SHA: a3f5653

#import "../templates/daily-plan-template.typ": *

#set page(
  paper: "a4",
  margin: (x: 50pt, y: 60pt),
  footer: [
    #place(
      bottom + left,
      dx: 5pt,
      dy: -8pt,
      text(size: 7pt, fill: gray)[Generated 2026-03-22 · SHA: a3f5653 · model: qwen3.5:2b]
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
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[5] \
      #text(size: 7pt)[COMPLETED]
    ]),
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("2").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[49] \
      #text(size: 7pt)[INCOMPLETE]
    ]),
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("1").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[1] \
      #text(size: 7pt)[FUTURE WEEKS]
    ])
  )
}

// PAGE 1: COVER & SUMMARY
#report_header("1")
#section_title("1", "Week 3", "Weekly Progress Report")

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
    #text(size: 9pt)[*Report Date:* March 22, 2026]
    #h(1fr)
    #text(size: 9pt)[*Week Period:* Mar 16 - Mar 22, 2026]
  ])
])

#v(2em)

== Executive Summary

#box(width: 100%, inset: 15pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 9pt)[
    Week 3 progress: 5 of 54 tasks completed (9%).
    1 tasks from future weeks already in progress.
  ]
])

#v(1em)
#stats_box()

#v(2em)

== Week Progress

#let week_progress = 9
#box(width: 100%, height: 28pt, fill: gray.lighten(80%), inset: 0pt, radius: 3pt, [
  #box(width: week_progress * 1%, height: 100%, fill: gradient.linear(chapter_themes.at("3").grad_start, chapter_themes.at("3").grad_end), radius: 3pt)
  #place(
    center + horizon,
    text(size: 10pt, weight: "bold", fill: white)[9% complete]
  )
])

#pagebreak()

// PAGE 2: COMPLETED THIS WEEK
#report_header("2")
#section_title("2", "2.0", "Completed This Week")

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("3").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    These tasks were planned for Week 3 and successfully completed:
  ]
])

#v(1em)

#text(size: 10pt, weight: "bold", fill: chapter_themes.at("3").accent)[✨ HIGHLIGHTS]
#v(8pt)
#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#158 - add in "visitor possession" test] #text(size: 8pt, fill: gray)[by naydino]
  
])
#v(6pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#157 - Management- Create document system for figma group work] #text(size: 8pt, fill: gray)[by naydino]
  
])
#v(6pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#156 - Team Management- Create Team Figma board] #text(size: 8pt, fill: gray)[by naydino]
  
])
#v(6pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#155 - UX phase 1 research] #text(size: 8pt, fill: gray)[by naydino]
  
])
#v(6pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#48 - Test and compare speech to text models inside of TD] #text(size: 8pt, fill: gray)[by naydino]
  #v(4pt) #text(size: 9pt)[test  ]
])
#v(6pt)


#v(2em)

== Notes

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("3").accent.lighten(95%), radius: 4pt, [
  #text(size: 9pt, weight: "bold")[✨ Week Summary:]
  #v(4pt)
  #text(size: 9pt)[- \#158 add in "visitor possession" test
- \#157 Management- Create document system for figma group work
- \#156 Team Management- Create Team Figma board
- \#155 UX phase 1 research
- \#48 Test and compare speech to text models inside of TD]
])

#pagebreak()

// PAGE 3: INCOMPLETE THIS WEEK
#report_header("3")
#section_title("3", "3.0", "Not Completed This Week")

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("2").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    These tasks were planned for Week 3 but remain incomplete:
  ]
])

#v(1em)


#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#135 - Test - Draw circle]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 27 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#134 - Test - Draw square 100x100mm]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 27 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#133 - Hardware - Create temporary pencil holder]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 27 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#132 - Calibrate - Acceleration values]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 26 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#131 - Calibrate - Y max feed rate]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 26 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#130 - Calibrate - X max feed rate]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 26 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#129 - Calibrate - Y axis steps/mm]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 26 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#128 - Calibrate - X axis steps/mm]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 26 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#127 - Test - Full homing cycle]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 25 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#126 - Test - Manual Y movement G0 Y20]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 25 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#125 - Test - Manual X movement G0 X10]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 25 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#124 - Test - Homing command]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 25 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#123 - Verify - Board responds]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 24 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#122 - Upload - config.yaml to board]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 24 AM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#121 - Flash - FluidNC firmware]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 24 AM...]
])
#v(4pt)


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


#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#159 - Conversation design- map outline] #text(size: 8pt, fill: gray)[(Week 4)]
  
])
#v(4pt)


#v(2em)

== Next Week Preview

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt)[
    *Week 4:* Mar 23 - Mar 29, 2026
  ]
])

#v(1em)


#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#159 - Conversation design- map outline]
  
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#56 - Oracle output based on user interaction]
  
])
#v(4pt)


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
