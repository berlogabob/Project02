// --- CONFIGURATION ---
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
#let report_header(ch_idx, category: "PROJECT") = {
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

#let task_table(rows) = {
  table(
    columns: (1fr, 1fr),
    inset: 10pt,
    stroke: 0.5pt + gray.lighten(50%),
    fill: (x, y) => if y == 0 { muted_bg } else { white },
    [*Task*], [*Deliverable*],
    ..rows
  )
}

// --- DOCUMENT START ---

// PAGE 1: INTRODUCTION & STRATEGY
#report_header("1")

#section_title("1", "1.0", "The Oracle That Wears Us")

#table(
  columns: (1fr),
  inset: 12pt,
  stroke: none,
  fill: muted_bg,
  [
    #grid(
      columns: (1.2fr, 2fr),
      gutter: 15pt,
      [
        *Project:* \ Interactive Installation \ \
        *Field:* \ Fashion & Emerging Tech
      ],
      [
        *Team:* \
        #grid(
          columns: (1fr, 1fr, 1fr),
          gutter: 5pt,
          [Nadine Allan \ #text(size: 8pt)[#20250828]],
          [Andrey Dyakov \ #text(size: 8pt)[#20251186]],
          [Dmitri Kazantsev \ #text(size: 8pt)[#20220711]]
        )
      ]
    )
  ]
)

#v(2em)

*The Oracle That Wears Us* is an arcade-style installation housed within a projection-mapped tent. Authorship shifts from designer to machine to public as inputs are captured, processed through AI engines, and materialized via a robotic pen plotter onto fabric fragments.

== Terms and Abbreviations
#v(1em)
#table(
  columns: (auto, 1fr),
  inset: 8pt,
  stroke: none,
  fill: (x, y) => if calc.even(y) { muted_bg.lighten(50%) },
  [*Term*], [*Definition*],
  [Big M], [Major stage marked as GitHub Milestones (e.g., Research).],
  [OSC], [Open Sound Control — real-time communication protocol.],
  [Typst], [Modern typesetting system used for automatic beautiful reports.],
  [MVP], [Minimum Viable Product — core working version of the installation.],
  [PR], [Pull Request — code review step before merging.],
  [Tiny Sprint], [Small daily or 2-day task (1–4 issues per person).],
  [Project Board], [GitHub Kanban board for task tracking (Backlog → Done).]
)

== How the Project Timeline Works
The timeline uses a "Main + Daily Sub-lines" structure to guarantee visibility:
- *Main timeline:* Protected `main` branch (only stable, reviewed code).
- *Weekly phases:* Temporary `week-XX` branches for one-week goals.
- *Student sub-lines:* Personal branches starting with `name/`.

#v(1em)
*Weekly Flow:*
1. Monday: Team meeting, issues moved to "This Week".
2. During week: Work in individual branches with tiny PRs.
3. Sunday night: GitHub Action generates this PDF report.
4. Monday morning: Report + live demo to the professor.

#page_footer("1", "1")
#pagebreak()

// PAGE 2: CORE CONCEPT & ROLES
#report_header("2")
#section_title("2", "2.0", "Core Concept & Structure")

=== Tech Summary
- *Hardware:* Plotter, arcade console, projector, camera.
- *Software:* Unity, TouchDesigner, OSC, Python, Generative AI.

=== Team Roles (High-Level Responsibility)
- *Nadine Allan:* System Architecture & Integration.
- *Andrey Dyakov:* Plotter & Materialization.
- *Dmitri Kazantsev:* Generative Concepts & Fabrication.

=== Agile Setup
- *Big Milestones:* 6 Phases (GitHub Milestones).
- *Small Milestones:* One per week (due Sunday).
- *Tiny Sprints:* Daily/2-day GitHub Issues.

#v(2em)
#box(
  fill: muted_bg,
  inset: 15pt,
  radius: 4pt,
  width: 100%
)[
  *Important Notes & Flexibility:* \
  The project can (and will) morph based on research and testing. Possible changes include single cumulative fabric vs modular pieces or UV-hidden layers. All decisions will be documented in weekly reports.
]

#page_footer("2", "2")
#pagebreak()

// PAGE 3: TIMELINE & PHASES
#report_header("3")
#section_title("3", "3.0", "Project Timeline")

#set par(justify: true)

=== Phase 1 – Research
#task_table((
  [Research core problems: algorithmic mediation & collective creation], [Problem statement + literature summary],
  [Review similar interactive installations], [Comparison table & lessons learned],
  [Hardware/Software evaluation], [Final tech stack (Plotter, OSC, AI)],
))

=== Phase 2 – Experimentation
#task_table((
  [Test interaction methods (gestures/buttons)], [Working prototypes (2-3 approaches)],
  [Generative techniques & visual styles], [Pattern output comparison],
  [Plotter control & fabric tests], [Selection report + test drawings],
))

=== Phase 3 – System Architecture
#task_table((
  [Finalize OSC schema & signal chain], [Locked architecture document],
  [Unity arcade prototype with OSC], [Working input & timing capture],
  [OSC Layer (Unity <-> TD <-> Python)], [Stable real-time data flow],
))

#page_footer("3", "3")
#pagebreak()

// PAGE 4: FABRICATION & POLISH
#report_header("4")
#section_title("4", "4.0", "Fabrication & Finalization")

=== Phase 5 – Fabrication & Spatial Setup
#task_table((
  [Projection mapping on tent surface], [Calibrated projection],
  [Physical arcade machine build], [Finished console],
  [Safety & risk plan], [Complete safety document],
))

=== Phase 6 – Testing & Polish
#task_table((
  [Full system rehearsals], [Stable end-to-end installation],
  [Bug fixing & latency optimization], [Tuned and reliable system],
  [Final documentation & video], [Complete Delivery 2 materials],
))

#v(2em)
#box(
  fill: chapter_themes.at("4").accent.lighten(90%),
  inset: 15pt,
  radius: 4pt,
  width: 100%
)[
  *MVP and Extra Ideas Pool:* \
  We maintain a clear MVP edition (arcade → patterns → fragments). Extra ideas (UV-hidden layers, degeneration logic) will be activated only after MVP sign-off and ahead-of-schedule progress.
]

#page_footer("4", "4")
