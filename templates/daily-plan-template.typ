// templates/daily-plan-template.typ
// Reusable template for daily plans and weekly reports

#let chapter_themes = (
  "1": (grad_start: rgb("#2F80ED"), grad_end: rgb("#9B51E0"), accent: rgb("#33A1C9"), page_bg: rgb("#A5C7F3")),
  "2": (grad_start: rgb("#eb3349"), grad_end: rgb("#f45c43"), accent: rgb("#e74c3c"), page_bg: rgb("#ff9a9e")),
  "3": (grad_start: rgb("#11998e"), grad_end: rgb("#38ef7d"), accent: rgb("#1b5e20"), page_bg: rgb("#c8e6c9")),
  "4": (grad_start: rgb("#F2994A"), grad_end: rgb("#F2C94C"), accent: rgb("#d35400"), page_bg: rgb("#fdebd0"))
)

#let muted_bg = rgb("#f4f4f4")

// PAGE NUMBERING ON EVERY PAGE - Using Typst's built-in numbering with custom footer
#set page(
  paper: "a4",
  margin: (x: 50pt, y: 60pt),
  footer: context {
    let page_num = counter(page).at(here())
    let theme_idx = calc.min(page_num, 4)
    let t = chapter_themes.at(str(theme_idx))
    
    align(
      right,
      square(
        size: 35pt,
        fill: t.page_bg,
        align(center + horizon, text(white, weight: "bold", size: 14pt)[#page_num])
      )
    )
  },
)

#set text(
  size: 10pt,
  fill: rgb("#333333"),
  lang: "en"
)

#let report_header(ch_idx, category: "DAILY PLAN") = {
  let t = chapter_themes.at(ch_idx)
  move(dy: -20pt)[
    #block(
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

#let issue_card(num, title, priority, body, milestone, labels, ch_idx: "1") = {
  let t = chapter_themes.at(ch_idx)
  let bg = if priority == "critical" { rgb("#ffebee") }
           else if priority == "high"    { rgb("#fff3e0") }
           else if priority == "medium"  { rgb("#e8f5e9") }
           else                          { muted_bg }

  let border = if priority == "critical" { rgb("#c62828") }
               else if priority == "high"    { rgb("#f57c00") }
               else                          { gray.lighten(60%) }

  block(
    width: 100%,
    inset: 12pt,
    radius: 6pt,
    fill: bg,
    stroke: 1pt + border,
    [
      #text(weight: "bold", fill: t.accent)[Issue #num: #title] \
      #if priority != "" [#text(fill: red, weight: "semibold")[#upper(priority)]] \
      #h(1fr) #text(size: 9pt, fill: gray)[#milestone] \
      #v(0.4em)
      #text(size: 9.5pt)[#body]
      #v(0.3em)
      #text(size: 8.5pt, fill: gray)[Labels: #labels]
    ]
  )
}

// MANUAL PAGE FOOTER - call on each page: #page_footer("1", "1")
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
