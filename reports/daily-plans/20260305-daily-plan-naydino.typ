// Daily Plan for Nadine Allan
// Generated: 2026-03-05 09:28
// Project: The Oracle That Wears Us

// --- CONFIGURATION (from Project02-Plan.typ) ---
#set page(
  paper: "a4",
  margin: (x: 50pt, y: 60pt),
)

#set text(
  font: "Noto Sans",
  size: 10pt,
  fill: rgb("#333333"),
  lang: "en"
)

// --- THEME DEFINITION ---
#let chapter_themes = (
  "1": (
    grad_start: rgb("#2F80ED"),
    grad_end: rgb("#9B51E0"),
    accent: rgb("#33A1C9"),
    page_bg: rgb("#A5C7F3")
  ),
  "2": (
    grad_start: rgb("#eb3349"),
    grad_end: rgb("#f45c43"),
    accent: rgb("#e74c3c"),
    page_bg: rgb("#ff9a9e")
  ),
  "3": (
    grad_start: rgb("#11998e"),
    grad_end: rgb("#38ef7d"),
    accent: rgb("#1b5e20"),
    page_bg: rgb("#c8e6c9")
  ),
  "4": (
    grad_start: rgb("#F2994A"),
    grad_end: rgb("#F2C94C"),
    accent: rgb("#d35400"),
    page_bg: rgb("#fdebd0")
  )
)

#let muted_bg = rgb("#f4f4f4")

// --- REUSABLE COMPONENTS ---
#let report_header(ch_idx, category: "DAILY PLAN") = {
  let t = chapter_themes.at(ch_idx)
  move(dy: -20pt)[
    #box(
      width: 100%,
      height: 30pt,
      fill: gradient.linear(t.grad_start, t.grad_end),
      inset: (right: 15pt),
      align(right + horizon, text(white, weight: "bold", tracking: 1.5pt, size: 8pt)[#upper(category)])
    )
  ]
}

#let section_title(ch_idx, num, title) = {
  let t = chapter_themes.at(ch_idx)
  v(20pt)
  text(fill: t.accent, size: 22pt, weight: "extrabold")[#num]
  v(-12pt)
  text(fill: t.accent, size: 22pt, weight: "bold")[#upper(title)]
  v(20pt)
}

#let page_footer(ch_idx, num) = {
  let t = chapter_themes.at(ch_idx)
  place(
    bottom + right,
    dx: 30pt,
    dy: 30pt,
    square(
      size: 35pt,
      fill: t.page_bg,
      align(center + horizon, text(white, weight: "bold", size: 14pt)[#num])
    )
  )
}

#let priority_badge(priority) = {
  let colors = (
    "critical": (bg: rgb("#B60205"), fg: white),
    "high": (bg: rgb("#D93F0B"), fg: white),
    "medium": (bg: rgb("#F9D0C4"), fg: rgb("#D93F0B")),
    "low": (bg: rgb("#0E8A16"), fg: white)
  )
  let c = colors.at(priority, (bg: gray, fg: white))
  box(
    fill: c.bg,
    inset: (x: 8pt, y: 3pt),
    radius: 3pt,
    text(size: 7pt, fill: c.fg, weight: "bold")[#upper(priority)]
  )
}

#let issue_card(issue_num, title, priority, body, milestone, labels) = {
  #box(
    width: 100%,
    inset: 12pt,
    fill: muted_bg.lighten(50%),
    radius: 4pt,
    stroke: 1pt + gray.lighten(60%),
    [
      #grid(
        columns: (1fr, auto),
        gutter: 10pt,
        [
          #text(size: 12pt, weight: "bold", [#{issue_num} - {title}])
          #if milestone != "" [
            #v(4pt)
            #text(size: 8pt, fill: gray, [Milestone: {milestone}])
          ]
          #if labels != "" [
            #v(4pt)
            #text(size: 8pt, fill: gray, [{labels}])
          ]
        ],
        align(top + right, [
          #if priority != "" [
            #priority_badge(priority)
          ]
        ])
      )
      #if body != "" [
        #v(8pt)
        #text(size: 9pt, fill: gray, {body})
      ]
    ]
  )
}

#let stats_row(total_tasks, high_priority_count) = {
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 15pt,
    box(
      fill: chapter_themes.at("1").accent.lighten(90%),
      inset: 12pt,
      radius: 4pt,
      align(center, [
        #text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent, [{total_tasks}])
        #text(size: 8pt, [Total Tasks])
      ])
    ),
    box(
      fill: chapter_themes.at("2").accent.lighten(90%),
      inset: 12pt,
      radius: 4pt,
      align(center, [
        #text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent, [{high_priority_count}])
        #text(size: 8pt, [High Priority])
      ])
    ),
    box(
      fill: chapter_themes.at("3").accent.lighten(90%),
      inset: 12pt,
      radius: 4pt,
      align(center, [
        #text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent, [05/03])
        #text(size: 8pt, [Date])
      ])
    )
  )
}

// --- PAGE 1: DAILY PLAN ---
#report_header("1")

#section_title("1", "05/03", "Daily Plan")

#table(
  columns: (1fr),
  inset: 12pt,
  stroke: none,
  fill: muted_bg,
  [
    #grid(
      columns: (1fr, 1fr),
      gutter: 15pt,
      [
        *Team Member:* \ Nadine Allan \ #text(size: 8pt)[@naydino] \ \
        *Date:* \ 05 March 2026
      ],
      [
        *Project:* \ The Oracle That Wears Us \         *Milestone:* \ 1st milestone: Documentation
      ]
    )
  ]
)

#v(2em)

== Your Tasks for Today

#if 6 == 0 [
  #box(
    width: 100%,
    inset: 20pt,
    fill: chapter_themes.at("3").accent.lighten(90%),
    radius: 4pt,
    align(center, [
      #text(size: 12pt)[🎉 No tasks assigned for today!]
      #v(8pt)
      #text(size: 9pt, fill: gray)[Use this time to explore, experiment, or help teammates]
    ])
  )
] else [
  #stats_row({total}, {high_priority})
  
  #v(2em)
  
  == Priority Tasks
  #line(length: 100%, stroke: 1pt + chapter_themes.at("2").accent)
  #v(10pt)
  
  
=== #45 - Unity vs TouchDesigner vs Hybrid: Real-Time Microphone Audio Visualization – Evaluation & Final Technology Choice 
*Milestone:* 1st milestone: Documentation
*Labels:* type: research, type: testing

We need to decide once and for all what we will use for the real-time microphone input + visualization pipeline in Project02:  - Unity only - TouchDesigner only - Hybrid (Unity + TouchDesigner connect

---

=== #7 - TD Test: "Can TD push that text out (on-screen now; Unity later if needed)?" 

---

=== #6 - TD Test: "Can TD call a free speech-to-text system and return text back into TD as DAT/CHOP?" 

*Recent Comments:*
- @naydino (2026-03-03): - successfully installed a free text to speech transcription model through my computer's terminal

---

=== #5 - TD Test: "Can TD reliably ingest mic audio and turn it into usable control/data?" 
*Milestone:* 1st milestone: Documentation
*Labels:* type: research, type: testing

Test to answer the question "How can we take a microphone input and transform it"

*Recent Comments:*
- @berlogabob (2026-03-04): @naydino  please add some data as comment for this issue. something we can measure to use for compar

---

=== #3 - Define characteristics of AI Oracle 

---

=== #1 - How does the plotter connect to the PC? 
*Milestone:* 1st milestone: Documentation

---

  
  #v(2em)
  
  == Planning Notes
  
  #box(
    width: 100%,
    inset: 15pt,
    fill: muted_bg,
    radius: 4pt,
    [
      #text(size: 9pt)[
        1. *Review* each task and its comments         2. *Check* recent updates         3. *Estimate* time needed         4. *Plan* your approach         5. *Comment* your progress
      ]
    ]
  )
]

#page_footer("1", "1")
#pagebreak()

// --- PAGE 2: PLANNING ---
#report_header("2")

#section_title("2", "2.0", "Planning Notes")

== Today's Goals

#box(
  width: 100%,
  height: 150pt,
  inset: 15pt,
  fill: muted_bg.lighten(50%),
  radius: 4pt,
  stroke: 1pt + gray.lighten(60%),
  [
    #text(size: 9pt, fill: gray, style: "italic")[
      Write your main goals for today here...
    ]
  ]
)

#v(2em)

== Time Blocks

#table(
  columns: (auto, 1fr),
  inset: 8pt,
  stroke: 0.5pt + gray.lighten(50%),
  fill: (x, y) => if calc.even(y) { muted_bg.lighten(50%) },
  [*Time*], [*Plan*],
  [09:00 - 10:00], [],
  [10:00 - 11:00], [],
  [11:00 - 12:00], [],
  [12:00 - 13:00], [Lunch Break],
  [13:00 - 14:00], [],
  [14:00 - 15:00], [],
  [15:00 - 16:00], [],
  [16:00 - 17:00], [],
)

#v(2em)

== Blockers & Questions

#box(
  width: 100%,
  height: 100pt,
  inset: 15pt,
  fill: chapter_themes.at("2").accent.lighten(95%),
  radius: 4pt,
  stroke: 1pt + chapter_themes.at("2").accent.lighten(70%),
  [
    #text(size: 9pt, fill: gray, style: "italic")[
      List any blockers or questions for the team...
    ]
  ]
)

#v(2em)

== End of Day Checklist

#box(
  width: 100%,
  inset: 15pt,
  fill: muted_bg,
  radius: 4pt,
  [
    #text(size: 9pt)[
      □ *Update* issue status (In Progress → Review/Done)       □ *Add* progress comments to issues       □ *Push* code changes to GitHub       □ *Create* PR if work is ready for review       □ *Prepare* demo/screenshots for tomorrow       □ *Plan* tomorrow's tasks
    ]
  ]
)

#page_footer("2", "2")
