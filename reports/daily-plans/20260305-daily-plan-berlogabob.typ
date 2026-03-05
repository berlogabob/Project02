// Daily Plan for Andrey Dyakov
// Generated: 2026-03-05 09:39

#set page(paper: "a4", margin: (x: 50pt, y: 60pt))
#set text(font: "Noto Sans", size: 10pt, fill: rgb("#333333"), lang: "en")

#let accent_blue = rgb("#2F80ED")
#let accent_red = rgb("#eb3349")
#let accent_green = rgb("#11998e")
#let muted_bg = rgb("#f4f4f4")

#align(center)[
  #text(size: 24pt, weight: "bold", fill: accent_blue, "📅 Daily Plan")
  #v(10pt)
  #text(size: 18pt, "05/03")
  #v(15pt)
  #text(size: 14pt, "Andrey Dyakov")
  #text(size: 10pt, fill: gray, " (@berlogabob)")
]

#v(20pt)
#line(length: 100%, stroke: 1pt + accent_blue)
#v(20pt)

#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 15pt,
  #box(
    fill: accent_blue.lighten(90%),
    inset: 12pt,
    radius: 4pt,
    align(center, [
      #text(size: 20pt, weight: "bold", fill: accent_blue, "7")
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

=== #45 - Unity vs TouchDesigner vs Hybrid: Real-Time Microphone Audio Visualization – Evaluation & Final Technology Choice
*Milestone:* 1st milestone: Documentation
*Labels:* type: research, type: testing

We need to decide once and for all what we will use for the real-time microphone input + visualization pipeline in Project02:  - Unity only - TouchDes

---

=== #13 - TTS - Text to Speech KittenTTS
*Milestone:* 1st milestone: Documentation

(KittenTTS)(https://github.com/KittenML/KittenTTS) test this model

---

=== #12 - STT- Speech to Text LLM
*Milestone:* 1st milestone: Documentation
*Labels:* type: research, type: testing

(moonshine-a)(https://github.com/moonshine-ai/moonshine ) test this model. write feedback 

---

=== #11 - plan tasks for next week
*Milestone:* 1st milestone: Documentation

---

=== #6 - TD Test: "Can TD call a free speech-to-text system and return text back into TD as DAT/CHOP?"

*Comments:*
- @naydino: - successfully installed a free text to speech transcription model through my computer's terminal
- @naydino: <img width="1427" height="521" alt="Image" src="https://github.com/user-attachments/assets/6bdec671-

---

=== #5 - TD Test: "Can TD reliably ingest mic audio and turn it into usable control/data?"
*Milestone:* 1st milestone: Documentation
*Labels:* type: research, type: testing

Test to answer the question "How can we take a microphone input and transform it"

*Comments:*
- @berlogabob: @naydino  please add some data as comment for this issue. something we can measure to use for compar

---

=== #1 - How does the plotter connect to the PC?
*Milestone:* 1st milestone: Documentation

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