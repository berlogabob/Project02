// Daily Plan for Dmitri Kazantsev
// Generated: 2026-03-05 09:32

#set page(paper: "a4", margin: (x: 50pt, y: 60pt))
#set text(font: "Noto Sans", size: 10pt, fill: rgb("#333333"), lang: "en")

// Colors from Project02-Plan.typ
#let accent_blue = rgb("#2F80ED")
#let accent_red = rgb("#eb3349")
#let accent_green = rgb("#11998e")
#let accent_yellow = rgb("#F2994A")
#let muted_bg = rgb("#f4f4f4")

// Header
#align(center)[
  #text(size: 24pt, weight: "bold", fill: accent_blue, "📅 Daily Plan")
  #v(10pt)
  #text(size: 18pt, "05/03")
  #v(15pt)
  #text(size: 14pt, "Dmitri Kazantsev")
  #text(size: 10pt, fill: gray, " (@electricianv001)")
]

#v(20pt)
#line(length: 100%, stroke: 1pt + accent_blue)
#v(20pt)

// Stats
#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 15pt,
  #box(
    fill: accent_blue.lighten(90%),
    inset: 12pt,
    radius: 4pt,
    align(center, [
      #text(size: 20pt, weight: "bold", fill: accent_blue, "4")
      #v(4pt)
      #text(size: 8pt, "Tasks")
    ])
  ),
  #box(
    fill: accent_red.lighten(90%),
    inset: 12pt,
    radius: 4pt,
    align(center, [
      #text(size: 20pt, weight: "bold", fill: accent_red, "0")
      #v(4pt)
      #text(size: 8pt, "High Priority")
    ])
  ),
  #box(
    fill: accent_green.lighten(90%),
    inset: 12pt,
    radius: 4pt,
    align(center, [
      #text(size: 20pt, weight: "bold", fill: accent_green, "05/03")
      #v(4pt)
      #text(size: 8pt, "Date")
    ])
  )
)

#v(30pt)
#line(length: 100%, stroke: 1pt + gray.lighten(70%))
#v(20pt)

== Your Tasks

#if 4 == 0 [
  #box(
    width: 100%,
    inset: 20pt,
    fill: accent_green.lighten(90%),
    radius: 4pt,
    align(center, [
      #text(size: 12pt, "🎉 No tasks for today!")
      #v(8pt)
      #text(size: 9pt, fill: gray, "Use this time to explore or help teammates")
    ])
  )
] else [
=== #45 - Unity vs TouchDesigner vs Hybrid: Real-Time Microphone Audio Visualization – Evaluation & Final Technology Choice
*Milestone:* 1st milestone: Documentation
*Labels:* type: research, type: testing

We need to decide once and for all what we will use for the real-time microphone input + visualization pipeline in Project02:  - Unity only - TouchDes

---

=== #20 - Unity: Microphone input test completed
*Milestone:* 1st milestone: Documentation
*Labels:* type: research, type: testing

Performance & Evaluation Data  Time to setup: ~5–10 minutes (including adding components and linking references).  Time to response (microphone reacti

*Comments:*
- @berlogabob: @electricianv001  please add some data as comment for this issue. something we can measure to use fo

---

=== #6 - TD Test: "Can TD call a free speech-to-text system and return text back into TD as DAT/CHOP?"

*Comments:*
- @naydino: - successfully installed a free text to speech transcription model through my computer's terminal

---

=== #4 - Define characteristics of AI Oracle

---


#v(30pt)
#line(length: 100%, stroke: 1pt + gray.lighten(70%))
#v(20pt)

== Planning Notes

=== Today's Goals
#box(
  width: 100%,
  height: 100pt,
  inset: 15pt,
  fill: muted_bg,
  radius: 4pt,
  [
    #text(size: 9pt, fill: gray, "Write your goals here...")
  ]
)

=== Time Blocks
#table(
  columns: (auto, 1fr),
  inset: 8pt,
  stroke: 0.5pt + gray.lighten(50%),
  fill: (x, y) => if calc.even(y) { muted_bg.lighten(50%) },
  [*Time*], [*Plan*],
  [09:00-10:00], [],
  [10:00-11:00], [],
  [11:00-12:00], [],
  [12:00-13:00], [Lunch],
  [13:00-14:00], [],
  [14:00-15:00], [],
  [15:00-16:00], [],
  [16:00-17:00], [],
)

=== End of Day Checklist
#box(
  width: 100%,
  inset: 15pt,
  fill: muted_bg,
  radius: 4pt,
  [
    #text(size: 9pt, [
      □ Update issue status
      □ Add progress comments
      □ Push code changes
      □ Create PR if ready
      □ Plan tomorrow
    ])
  ]
)
