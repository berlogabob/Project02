// Daily Plan Template for "The Oracle That Wears Us"
// Simplified version without f-strings

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
      align(right + horizon, text(white, weight: "bold", tracking: 1.5pt, size: 8pt, category))
    )
  ]
}

#let section_title(ch_idx, num, title) = {
  let t = chapter_themes.at(ch_idx)
  v(20pt)
  text(fill: t.accent, size: 22pt, weight: "extrabold", num)
  v(-12pt)
  text(fill: t.accent, size: 22pt, weight: "bold", upper(title))
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
      align(center + horizon, text(white, weight: "bold", size: 14pt, num))
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
    text(size: 7pt, fill: c.fg, weight: "bold", upper(priority))
  )
}

#let issue_card(issue, idx) = {
  #box(
    width: 100%,
    inset: 12pt,
    fill: if calc.even(idx) { muted_bg.lighten(50%) } else { white },
    radius: 4pt,
    stroke: 1pt + gray.lighten(60%),
    [
      #grid(
        columns: (1fr, auto),
        gutter: 10pt,
        [
          #text(size: 12pt, weight: "bold", issue.title)
          #if issue.milestone != none [
            #v(4pt)
            #text(size: 8pt, fill: gray, "Milestone: " + issue.milestone.title)
          ]
          #if issue.labels != () [
            #v(4pt)
            #grid(
              columns: (auto,),
              gutter: 4pt,
              ..issue.labels.map(l => box(
                fill: rgb("#" + l.color),
                inset: (x: 6pt, y: 2pt),
                radius: 3pt,
                text(size: 7pt, fill: white, l.name)
              ))
            )
          ]
        ],
        align(top + right, [
          #if issue.priority != "" [
            #priority_badge(issue.priority)
          ]
          #v(8pt)
          #text(size: 14pt, weight: "bold", fill: chapter_themes.at("1").accent, "#" + str(issue.number))
        ])
      )
      
      #if issue.body != "" [
        #v(8pt)
        #text(size: 9pt, fill: gray, issue.body)
      ]
      
      #if issue.comments != () [
        #v(8pt)
        #line(length: 100%, stroke: 0.5pt + gray.lighten(70%))
        #v(4pt)
        #text(size: 8pt, weight: "bold", fill: chapter_themes.at("1").accent, "Recent Comments:")
        #v(4pt)
        ..issue.comments.map(c => [
          #text(size: 8pt, fill: gray,
            "@" + c.author + " (" + c.date + "): " + c.body
          )
          #v(4pt)
        ])
      ]
      
      #if issue.sub_issues != () [
        #v(8pt)
        #line(length: 100%, stroke: 0.5pt + gray.lighten(70%))
        #v(4pt)
        #text(size: 8pt, weight: "bold", fill: chapter_themes.at("3").accent, "Sub-issues:")
        #v(4pt)
        ..issue.sub_issues.map(sub => [
          #text(size: 8pt,
            "□ " + sub.title
          )
          #v(2pt)
        ])
      ]
    ]
  )
}

#let stats_row(stats) = {
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 15pt,
    box(
      fill: chapter_themes.at("1").accent.lighten(90%),
      inset: 12pt,
      radius: 4pt,
      align(center, [
        #text(size: 20pt, weight: "bold", fill: chapter_themes.at("1").accent, str(stats.total))
        #text(size: 8pt, "Total Tasks")
      ])
    ),
    box(
      fill: chapter_themes.at("2").accent.lighten(90%),
      inset: 12pt,
      radius: 4pt,
      align(center, [
        #text(size: 20pt, weight: "bold", fill: chapter_themes.at("2").accent, str(stats.high_priority))
        #text(size: 8pt, "High Priority")
      ])
    ),
    box(
      fill: chapter_themes.at("3").accent.lighten(90%),
      inset: 12pt,
      radius: 4pt,
      align(center, [
        #text(size: 20pt, weight: "bold", fill: chapter_themes.at("3").accent, str(stats.milestones))
        #text(size: 8pt, "Milestones")
      ])
    )
  )
}

// --- DOCUMENT CONTENT ---
#let member_name = input("member_name", default: "Team Member")
#let member_username = input("member_username", default: "@username")
#let plan_date = input("date", default: datetime.today())
#let issues = input("issues", default: ())

// PAGE 1: DAILY PLAN
#report_header("1")

#section_title("1", str(plan_date.day) + "/" + str(plan_date.month), "Daily Plan")

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
        *Team Member:* \ #member_name \ #text(size: 8pt, member_username) \ \
        *Date:* \ #plan_date.display(short: true)
      ],
      [
        *Project:* \ The Oracle That Wears Us \ \
        *Milestone:* \ #if issues.len() > 0 [
          #issues.first().milestone.title
        ] else [
          -
        ]
      ]
    )
  ]
)

#v(2em)

== Your Tasks for Today

#if issues.len() == 0 [
  #box(
    width: 100%,
    inset: 20pt,
    fill: chapter_themes.at("3").accent.lighten(90%),
    radius: 4pt,
    align(center, [
      #text(size: 12pt, "🎉 No tasks assigned for today!")
      #v(8pt)
      #text(size: 9pt, fill: gray, "Use this time to explore, experiment, or help teammates")
    ])
  )
] else [
  #stats_row((
    total: issues.len(),
    high_priority: issues.filter(i => i.priority == "high" or i.priority == "critical").len(),
    milestones: issues.filter(i => i.milestone != none).len()
  ))
  
  #v(2em)
  
  == Priority Tasks
  ..issues.filter(i => i.priority == "critical" or i.priority == "high").enumerate(start: 1).map((issue, idx) => issue_card(issue, idx))
  
  #v(2em)
  
  == All Tasks
  ..issues.filter(i => i.priority != "critical" and i.priority != "high").enumerate(start: 1).map((issue, idx) => issue_card(issue, idx))
]

#v(2em)

== Quick Planning Tips

#box(
  width: 100%,
  inset: 15pt,
  fill: muted_bg,
  radius: 4pt,
  [
    #text(size: 9pt, [
      1. *Review* each task and its sub-issues \
      2. *Check* recent comments for updates \
      3. *Estimate* time needed for each task \
      4. *Plan* your approach before starting \
      5. *Comment* your progress as you work
    ])
  ]
)

#page_footer("1", "1")
#pagebreak()

// PAGE 2: NOTES & PLANNING
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
    #text(size: 9pt, fill: gray, style: "italic",
      "Write your main goals for today here..."
    )
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
    #text(size: 9pt, fill: gray, style: "italic",
      "List any blockers or questions for the team..."
    )
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
    #text(size: 9pt, [
      □ *Update* issue status (In Progress → Review/Done) \
      □ *Add* progress comments to issues \
      □ *Push* code changes to GitHub \
      □ *Create* PR if work is ready for review \
      □ *Prepare* demo/screenshots for tomorrow \
      □ *Plan* tomorrow's tasks
    ])
  ]
)

#page_footer("2", "2")
