// Daily Plan Template - Matches Project02-Plan.typ Style
// For use with generate_daily_plan.py

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

// --- THEME DEFINITION (from Project02-Plan.typ) ---
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

#let issue_card(num, title, priority, body, milestone, labels) = {
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
          #text(size: 12pt, weight: "bold", [#num - #title])
          #if milestone != "" [
            #v(4pt)
            #text(size: 8pt, fill: gray, [Milestone: #milestone])
          ]
          #if labels != "" [
            #v(4pt)
            #text(size: 8pt, fill: gray, [#labels])
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
        #text(size: 9pt, fill: gray, [#body])
      ]
    ]
  )
}
