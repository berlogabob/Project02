// Weekly Report - Week 2
// Auto-generated: 2026-03-09
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
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[0] \
      #text(size: 7pt)[COMPLETED]
    ]),
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("2").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[15] \
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
    #text(size: 9pt)[*Report Date:* March 09, 2026]
    #h(1fr)
    #text(size: 9pt)[*Week Period:* Mar 09 - Mar 15, 2026]
  ])
])

#v(2em)

== Executive Summary

#box(width: 100%, inset: 15pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 9pt)[
    Week 2 progress: 0 of 15 tasks completed (0%).
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
    These tasks were planned for Week 2 and successfully completed:
  ]
])

#v(1em)

#text(size: 10pt, fill: gray)[No highlighted issues completed this week.]

#v(2em)

== Notes

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("3").accent.lighten(95%), radius: 4pt, [
  #text(size: 9pt, weight: "bold")[✨ Week Summary:]
  #v(4pt)
  #text(size: 9pt)[No issues completed this week.]
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


#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#44 - #23 - Milestone 2 Presentation Preparation] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL]
  #v(2pt) #text(size: 8pt, fill: gray)[Prepare slides for April 13 presentation.  \#\# Deliverables - Presentation slides - Live demo preparation - Rehearsal  \#\# Deadline - **Presentation...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#43 - #22 - Milestone 2 Documentation] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL]
  #v(2pt) #text(size: 8pt, fill: gray)[Update production dossier with implementation reports from all units.  \#\# Deliverables - Updated production dossier - Implementation reports:   - Em...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#42 - #21 - Core Functionality Prototype] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL]
  #v(2pt) #text(size: 8pt, fill: gray)[Develop functional prototype demonstrating core features.  \#\# Deliverables - Functional prototype - Core features working - Demo video  \#\# Accepta...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#41 - #20 - Audio Assets Integration]
  #v(2pt) #text(size: 8pt, fill: gray)[Integrate original or legally obtained audio assets.  \#\# Deliverables - Audio assets - Asset documentation - License verification  \#\# Acceptance C...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#40 - #19 - Graphical Assets Integration]
  #v(2pt) #text(size: 8pt, fill: gray)[Integrate original or legally obtained graphical assets.  \#\# Deliverables - Graphical assets - Asset documentation - License verification  \#\# Acce...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#39 - #18 - VR/AR Interaction Design]
  #v(2pt) #text(size: 8pt, fill: gray)[Design and implement VR/AR interactions (hand tracking, eye tracking, haptic feedback).  \#\# Deliverables - VR/AR interaction design - Implementation...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#38 - #17 - Sensor-Based Interaction Implementation]
  #v(2pt) #text(size: 8pt, fill: gray)[Implement body tracking, gesture recognition, or AR features.  \#\# Deliverables - Sensor integration - Interaction mapping - Testing documentation  \...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#37 - #16 - Latent Space Experiments]
  #v(2pt) #text(size: 8pt, fill: gray)[Experiment with latent space manipulation for creative outputs.  \#\# Deliverables - Latent space exploration - Creative output samples - Experiment d...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#36 - #15 - Model Training/Fine-tuning]
  #v(2pt) #text(size: 8pt, fill: gray)[Train or fine-tune selected model; document parameters and process.  \#\# Deliverables - Trained/fine-tuned model - Training logs - Parameter document...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#35 - #14 - Deep Learning Model Selection & Dataset Prep] #text(size: 9pt, fill: red, weight: "bold")[HIGH]
  #v(2pt) #text(size: 8pt, fill: gray)[Choose model architecture and prepare training dataset.  \#\# Deliverables - Model selection document - Dataset collected and prepared - Training conf...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#34 - #13 - Agentic AI Loop Implementation]
  #v(2pt) #text(size: 8pt, fill: gray)[Develop initial agentic workflow for autonomous task execution.  \#\# Deliverables - Agentic loop architecture - Autonomous task execution - Safety co...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#33 - #12 - Generative AI Pipeline Development]
  #v(2pt) #text(size: 8pt, fill: gray)[Build prompt engineering pipelines for content generation and task execution.  \#\# Deliverables - Prompt templates - Content generation pipeline - Ta...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#32 - #11 - TouchDesigner Integration Setup] #text(size: 9pt, fill: red, weight: "bold")[HIGH]
  #v(2pt) #text(size: 8pt, fill: gray)[Configure TouchDesigner as core tool for real-time generative behaviours.  \#\# Deliverables - TouchDesigner project structure - Unity-TouchDesigner c...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#31 - #10 - Unity Project Setup]
  #v(2pt) #text(size: 8pt, fill: gray)[Initialize Unity project with proper structure and version control.  \#\# Deliverables - Unity project initialized - Folder structure created - Git co...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#30 - #9 - Task Breakdown & Problem Identification] #text(size: 9pt, fill: red, weight: "bold")[HIGH]
  #v(2pt) #text(size: 8pt, fill: gray)[List all tasks required to complete a functional project; identify potential problems and necessities.  \#\# Deliverables - Complete task list - Risk ...]
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

#text(size: 10pt, fill: gray)[No future week tasks started early.]

#v(2em)

== Next Week Preview

#box(width: 100%, inset: 15pt, fill: muted_bg, radius: 4pt, [
  #text(size: 9pt)[
    *Week 3:* Mar 16 - Mar 22, 2026 \
    Focus on completing remaining Week 2 tasks and starting Week 3 planned work.
  ]
])

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
