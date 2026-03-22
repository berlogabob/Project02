// Weekly Report - Week 2
// Auto-generated: 2026-03-16
// Project: The Oracle That Wears Us
// Week Period: Mar 09 - Mar 15, 2026

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
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[26] \
      #text(size: 7pt)[COMPLETED]
    ]),
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("2").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[0] \
      #text(size: 7pt)[INCOMPLETE]
    ]),
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("1").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[10] \
      #text(size: 7pt)[FUTURE WEEKS]
    ])
  )
}

// PAGE 1: COVER & SUMMARY
#report_header("1")
#section_title("1", "Week 2", "Weekly Progress Report")

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
    #text(size: 9pt)[*Report Date:* March 16, 2026]
    #h(1fr)
    #text(size: 9pt)[*Week Period:* Mar 09 - Mar 15, 2026]
  ])
])

#v(2em)

== Executive Summary

#box(width: 100%, inset: 15pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 9pt)[
    Week 2 progress: 26 of 26 tasks completed (100%).
    10 tasks from future weeks already in progress.
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
    These tasks were planned for Week 2 and successfully completed:
  ]
])

#v(1em)

#text(size: 10pt, weight: "bold", fill: chapter_themes.at("3").accent)[✨ HIGHLIGHTS]
#v(8pt)
#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#154 - add visual feed-back effects] #text(size: 8pt, fill: gray)[by naydino]
  
])
#v(6pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#153 - add subtitle text] #text(size: 8pt, fill: gray)[by naydino]
  
])
#v(6pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#151 - test animation] #text(size: 8pt, fill: gray)[by naydino]
  #v(4pt) #text(size: 9pt)[implement Filipe's suggestions on create the talking animation frames based on amplitude of voice]
])
#v(6pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#61 - 📸 Machine Documentation Phase] #text(size: 8pt, fill: gray)[by berlogabob]
  #v(4pt) #text(size: 9pt)[ | Week 2]
])
#v(6pt)

#h(30pt) #box(width: 100%, fill: chapter_themes.at("1").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("1").accent), [
  #text(size: 11pt, weight: "bold")[#72 - Photo - Machine front view] #text(size: 8pt, fill: gray)[by berlogabob]
  #v(4pt) #text(size: 9pt)[ Time: 30 min (1 Pomodoro) Date: March 10 AM  **Task:** Photograph machine from front angle with good lighting  **Checklist:** - ( ) Take photo from front - ( ) Upload to documentation folder]
])
#v(6pt)

#h(30pt) #box(width: 100%, fill: chapter_themes.at("1").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("1").accent), [
  #text(size: 11pt, weight: "bold")[#73 - Photo - Machine back view] #text(size: 8pt, fill: gray)[by berlogabob]
  #v(4pt) #text(size: 9pt)[ Time: 30 min Date: March 10 AM  **Task:** Photograph machine from back angle showing cable connections  **Checklist:** - ( ) Take photo from back - ( ) Upload to documentation folder]
])
#v(6pt)

#h(30pt) #box(width: 100%, fill: chapter_themes.at("1").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("1").accent), [
  #text(size: 11pt, weight: "bold")[#74 - Photo - Machine side views] #text(size: 8pt, fill: gray)[by berlogabob]
  #v(4pt) #text(size: 9pt)[ Time: 30 min Date: March 10 AM  **Task:** Photograph both side angles (left and right)  **Checklist:** - ( ) Take left side photo - ( ) Take right side photo - ( ) Upload to documentation folder]
])
#v(6pt)

#h(30pt) #box(width: 100%, fill: chapter_themes.at("1").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("1").accent), [
  #text(size: 11pt, weight: "bold")[#75 - Photo - Machine top/bottom views] #text(size: 8pt, fill: gray)[by berlogabob]
  #v(4pt) #text(size: 9pt)[ Time: 30 min Date: March 10 AM  **Task:** Photograph from top and bottom angles  **Checklist:** - ( ) Take top photo - ( ) Take bottom photo - ( ) Upload to documentation folder]
])
#v(6pt)

#h(30pt) #box(width: 100%, fill: chapter_themes.at("1").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("1").accent), [
  #text(size: 11pt, weight: "bold")[#76 - Photo - Old board overview] #text(size: 8pt, fill: gray)[by berlogabob]
  #v(4pt) #text(size: 9pt)[ Time: 30 min Date: March 10 PM  **Task:** Close-up photo of entire old board  **Checklist:** - ( ) Take overview photo - ( ) Ensure all components visible]
])
#v(6pt)

#h(30pt) #box(width: 100%, fill: chapter_themes.at("1").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("1").accent), [
  #text(size: 11pt, weight: "bold")[#77 - Photo - Board connectors detail] #text(size: 8pt, fill: gray)[by berlogabob]
  #v(4pt) #text(size: 9pt)[ Time: 30 min Date: March 10 PM  **Task:** Close-up photos of all connector ports  **Checklist:** - ( ) Photo each connector - ( ) Label connectors in photo]
])
#v(6pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#3 - Define characteristics of AI Oracle] #text(size: 8pt, fill: gray)[by naydino]
  
])
#v(6pt)


#v(2em)

== Notes

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("3").accent.lighten(95%), radius: 4pt, [
  #text(size: 9pt, weight: "bold")[✨ Week Summary:]
  #v(4pt)
  #text(size: 9pt)[**26 issues completed:**\n- #154 add visual feed-back effects\n- #153 add subtitle text\n- #151 test animation\n- #149 Future Hardware / IoT Integration Strategy\n- #148 System Architecture & Data Flow Definition\n- #96 Test - Launch original firmware\n- #86 Disconnect - Y stepper\n- #85 Label - Y stepper wires\n- #84 Photo - Y stepper connections\n- #83 Disconnect - X stepper]
])

#pagebreak()

// PAGE 3: INCOMPLETE THIS WEEK
#report_header("3")
#section_title("3", "3.0", "Not Completed This Week")

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("2").accent.lighten(90%), radius: 4pt, [
  #text(size: 9pt)[
    These tasks were planned for Week 2 but remain incomplete:
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


#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#155 - UX phase 1 research] #text(size: 8pt, fill: gray)[(Week 3)]
  
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#68 - 🧪 Initial Testing Phase] #text(size: 8pt, fill: gray)[(Week 3)]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Week 3...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#67 - 🔌 Board Installation Phase] #text(size: 8pt, fill: gray)[(Week 3)]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Week 3...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#66 - ⚙️ FluidNC Configuration Phase] #text(size: 8pt, fill: gray)[(Week 3)]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Week 2...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#65 - 📚 FluidNC Research Phase] #text(size: 8pt, fill: gray)[(Week 3)]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Week 2...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#64 - 📏 Measurement Phase] #text(size: 8pt, fill: gray)[(Week 3)]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Week 2...]
])
#v(4pt)

#h(30pt) #box(width: 100%, fill: chapter_themes.at("1").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("1").accent), [
  #text(size: 10pt, weight: "bold")[#102 - Measure - X/Y travel distance] #text(size: 8pt, fill: gray)[(Week 3)]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 14 AM...]
])
#v(4pt)

#h(30pt) #box(width: 100%, fill: chapter_themes.at("1").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("1").accent), [
  #text(size: 10pt, weight: "bold")[#104 - Document - Create measurement sketch] #text(size: 8pt, fill: gray)[(Week 3)]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Time: 30 min | Date: March 14 PM...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#56 - Oracle output based on user interaction] #text(size: 8pt, fill: gray)[(Week 3)]
  
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#48 - Test and compare speech to text models inside of TD] #text(size: 8pt, fill: gray)[(Week 3)]
  #v(2pt) #text(size: 8pt, fill: gray)[test  ...]
])
#v(4pt)


#v(2em)

== Next Week Preview

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt)[
    *Week 3:* Mar 16 - Mar 22, 2026
  ]
])

#v(1em)


#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#155 - UX phase 1 research]
  
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#64 - 📏 Measurement Phase]
  #v(2pt) #text(size: 8pt, fill: gray)[ | Week 2...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#56 - Oracle output based on user interaction]
  
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#48 - Test and compare speech to text models inside of TD]
  #v(2pt) #text(size: 8pt, fill: gray)[test  ...]
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
