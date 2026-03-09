// Weekly Report - Week 1
// Auto-generated: 2026-03-09
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
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent)[19] \
      #text(size: 7pt)[COMPLETED]
    ]),
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("2").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent)[0] \
      #text(size: 7pt)[INCOMPLETE]
    ]),
    block(width: 100%, inset: 15pt, radius: 8pt, fill: chapter_themes.at("1").accent.lighten(90%), align(center)[
      #text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent)[15] \
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
    #text(size: 9pt)[*Report Date:* March 09, 2026]
    #h(1fr)
    #text(size: 9pt)[*Week Period:* Mar 02 - Mar 08, 2026]
  ])
])

#v(2em)

== Executive Summary

#box(width: 100%, inset: 15pt, fill: muted_bg.lighten(50%), radius: 4pt, [
  #text(size: 9pt)[
    Week 1 progress: 19 of 19 tasks completed (100%).
    15 tasks from future weeks already in progress.
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

#text(size: 10pt, weight: "bold", fill: chapter_themes.at("3").accent)[✨ HIGHLIGHTS]
#v(8pt)
#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#45 - Unity vs TouchDesigner vs Hybrid: Real-Time Microphone Audio Visualization – Evaluation & Final Technology Choice] #text(size: 8pt, fill: gray)[by berlogabob, naydino, electricianv001]
  #v(4pt) #text(size: 9pt)[We need to decide once and for all what we will use for the real-time microphone input + visualization pipeline in Project02:  - Unity only - TouchDesigner only - Hybrid (Unity + TouchDesigner connected)]
])
#v(6pt)

#h(30pt) #box(width: 100%, fill: chapter_themes.at("1").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("1").accent), [
  #text(size: 11pt, weight: "bold")[#5 - TD Test: "Can TD reliably ingest mic audio and turn it into usable control/data?"] #text(size: 8pt, fill: gray)[by berlogabob, naydino]
  #v(4pt) #text(size: 9pt)[Test to answer the question "How can we take a microphone input and transform it"     ]
])
#v(6pt)

#h(30pt) #box(width: 100%, fill: chapter_themes.at("1").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("1").accent), [
  #text(size: 11pt, weight: "bold")[#20 - Unity: Microphone input test completed] #text(size: 8pt, fill: gray)[by electricianv001]
  #v(4pt) #text(size: 9pt)[Performance & Evaluation Data  Time to setup: ~5–10 minutes (including adding components and linking references).  Time to response (microphone reaction delay): ~1 frame (almost real-time, visually instant).  Loading time:  Start Unity → ~10–15 seconds  Open project → ~5–10 seconds  Scene ready → immediate  Stability: The system works consistently without errors once configured correctly. Microphone initialization is stable and does not require additional permissions in this environment.  Resource usage: Very lightweight. Uses a small float buffer (256 samples) and simple RMS calculation per frame.  Personal evaluation: The solution fits our current project needs well. It provides real-time audio input analysis with smooth visual response. The setup is simple, modular, and easy to integrate into other scenes or objects. At this stage of the project, it is sufficient and flexible for further expansion (e.g., frequency-based analysis if needed).     ]
])
#v(6pt)

#h(30pt) #box(width: 100%, fill: chapter_themes.at("1").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("1").accent), [
  #text(size: 11pt, weight: "bold")[#52 - STT->TTT->TTS Pure Python workflow] #text(size: 8pt, fill: gray)[by berlogabob]
  #v(4pt) #text(size: 9pt)[Test pure Python workflow for recognise speech to text, connect text to LLM model fow answering in text and give answer as voice back to user.      ]
])
#v(6pt)

#h(60pt) #box(width: 100%, fill: chapter_themes.at("2").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("2").accent), [
  #text(size: 11pt, weight: "bold")[#13 - TTS - Text to Speech KittenTTS] #text(size: 8pt, fill: gray)[by berlogabob]
  #v(4pt) #text(size: 9pt)[(KittenTTS)( test this model    ]
])
#v(6pt)

#h(60pt) #box(width: 100%, fill: chapter_themes.at("2").accent.lighten(95%), inset: 10pt, radius: 4pt, stroke: (left: 4pt + chapter_themes.at("2").accent), [
  #text(size: 11pt, weight: "bold")[#12 - STT- Speech to Text LLM] #text(size: 8pt, fill: gray)[by berlogabob]
  #v(4pt) #text(size: 9pt)[(moonshine-a)( ) test this model. write feedback    ]
])
#v(6pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#6 - TD Test: "Can TD call a free speech-to-text system and return text back into TD as DAT/CHOP?"] #text(size: 8pt, fill: gray)[by berlogabob, naydino, electricianv001]
  
])
#v(6pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 11pt, weight: "bold")[#1 - How does the plotter connect to the PC?] #text(size: 8pt, fill: gray)[by berlogabob, naydino]
  #v(4pt) #text(size: 9pt)[Plotter could be connected to the PC with:  1. USB-cable directly    - PROS: Speed, low latency. Robust connectivity.   - CONS: wire, visually not so "magic" or "WOW-effect".  2. Wi-Fi.    - PROS: no wires, working like a charm, visually working like "magic" good for our purpuse.    - CONS: Wi-fi point needed, extra piece of technology.  Result: start to work with wire connection, switch to Wi-fi if possible later. ]
])
#v(6pt)


#v(2em)

== Notes

#box(width: 100%, inset: 15pt, fill: chapter_themes.at("3").accent.lighten(95%), radius: 4pt, [
  #text(size: 9pt, weight: "bold")[✨ Week Summary:]
  #v(4pt)
  #text(size: 9pt)[- Developed a pure Python STT-to-TTS workflow integrating KittenTTS logic with TouchDesigner audio pipelines.
- Designed real-time microphone audio testing scenarios to compare Unity and Hybrid architectures for text processing.
- Implemented automated weekly and daily planning report generators while establishing version-controlled repository structures for the Blanc project v2.]
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


#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#44 - #23 - Milestone 2 Presentation Preparation] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL] #text(size: 8pt, fill: gray)[(Week 2)]
  #v(2pt) #text(size: 8pt, fill: gray)[Prepare slides for April 13 presentation.  \#\# Deliverables - Presentation slides - Live demo preparation - Rehearsal  \#\# Deadline - **Presentation...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#43 - #22 - Milestone 2 Documentation] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL] #text(size: 8pt, fill: gray)[(Week 2)]
  #v(2pt) #text(size: 8pt, fill: gray)[Update production dossier with implementation reports from all units.  \#\# Deliverables - Updated production dossier - Implementation reports:   - Em...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#42 - #21 - Core Functionality Prototype] #text(size: 9pt, fill: red, weight: "bold")[CRITICAL] #text(size: 8pt, fill: gray)[(Week 2)]
  #v(2pt) #text(size: 8pt, fill: gray)[Develop functional prototype demonstrating core features.  \#\# Deliverables - Functional prototype - Core features working - Demo video  \#\# Accepta...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#41 - #20 - Audio Assets Integration] #text(size: 8pt, fill: gray)[(Week 2)]
  #v(2pt) #text(size: 8pt, fill: gray)[Integrate original or legally obtained audio assets.  \#\# Deliverables - Audio assets - Asset documentation - License verification  \#\# Acceptance C...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#40 - #19 - Graphical Assets Integration] #text(size: 8pt, fill: gray)[(Week 2)]
  #v(2pt) #text(size: 8pt, fill: gray)[Integrate original or legally obtained graphical assets.  \#\# Deliverables - Graphical assets - Asset documentation - License verification  \#\# Acce...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#39 - #18 - VR/AR Interaction Design] #text(size: 8pt, fill: gray)[(Week 2)]
  #v(2pt) #text(size: 8pt, fill: gray)[Design and implement VR/AR interactions (hand tracking, eye tracking, haptic feedback).  \#\# Deliverables - VR/AR interaction design - Implementation...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#38 - #17 - Sensor-Based Interaction Implementation] #text(size: 8pt, fill: gray)[(Week 2)]
  #v(2pt) #text(size: 8pt, fill: gray)[Implement body tracking, gesture recognition, or AR features.  \#\# Deliverables - Sensor integration - Interaction mapping - Testing documentation  \...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#37 - #16 - Latent Space Experiments] #text(size: 8pt, fill: gray)[(Week 2)]
  #v(2pt) #text(size: 8pt, fill: gray)[Experiment with latent space manipulation for creative outputs.  \#\# Deliverables - Latent space exploration - Creative output samples - Experiment d...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#36 - #15 - Model Training/Fine-tuning] #text(size: 8pt, fill: gray)[(Week 2)]
  #v(2pt) #text(size: 8pt, fill: gray)[Train or fine-tune selected model; document parameters and process.  \#\# Deliverables - Trained/fine-tuned model - Training logs - Parameter document...]
])
#v(4pt)

#box(width: 100%, fill: muted_bg.lighten(50%), inset: 10pt, radius: 4pt, [
  #text(size: 10pt, weight: "bold")[#35 - #14 - Deep Learning Model Selection & Dataset Prep] #text(size: 9pt, fill: red, weight: "bold")[HIGH] #text(size: 8pt, fill: gray)[(Week 2)]
  #v(2pt) #text(size: 8pt, fill: gray)[Choose model architecture and prepare training dataset.  \#\# Deliverables - Model selection document - Dataset collected and prepared - Training conf...]
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
