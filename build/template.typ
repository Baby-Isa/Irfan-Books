// Irfan Books — Typst template. Visual spec: docs/DESIGN.md
// Used by build/build.py; chapters are Pandoc output that call the functions below.

#let ink    = rgb("#1F1B16")
#let teal   = rgb("#1E5A5A")
#let gold   = rgb("#B08D3C")
#let box-colours = (
  word:    rgb("#1E5A5A"),
  history: rgb("#7A4E2D"),
  story:   rgb("#6B3F69"),
  who:     rgb("#4A5866"),
  reflect: rgb("#B08D3C"),
  try:     rgb("#2E6B3F"),
)
#let box-icons = (word: "ع", history: "⧗", story: "❧", who: "◈", reflect: "✦", try: "➤")
#let box-labels = (word: "Word Study", history: "History", story: "Story", who: "Who's Who", reflect: "Reflection", try: "Try this")

#let serif = ("EB Garamond", "EB Garamond LX", "Amiri")
#let sans  = ("Source Sans 3", "Source Sans 3 LX", "Amiri")

// ---------- ornaments ----------
// Eight-point star: two overlapping squares.
#let star(size: 6pt, fill: gold) = box(width: size, height: size, {
  let sq = rect(width: size * 0.72, height: size * 0.72, fill: fill, stroke: none)
  place(center + horizon, sq)
  place(center + horizon, rotate(45deg, sq))
})

#let star-band(width: 100%, count: 9, fill: gold) = align(center, box(width: width, {
  grid(columns: (1fr, auto, 1fr), align: horizon, column-gutter: 6pt,
    line(length: 100%, stroke: 0.4pt + fill),
    { for i in range(count) { star(size: if calc.rem(i, 2) == 0 { 6pt } else { 3.5pt }, fill: fill); h(5pt) } },
    line(length: 100%, stroke: 0.4pt + fill),
  )
}))

#let corner-motif(fill: gold) = box(width: 14pt, height: 14pt, {
  place(top + left, star(size: 7pt, fill: fill))
  place(top + left, dx: 9pt, dy: 2.2pt, star(size: 3pt, fill: fill))
  place(top + left, dx: 2.2pt, dy: 9pt, star(size: 3pt, fill: fill))
})

// ---------- inline helpers used by the Lua filter ----------
#let ar(body) = text(font: "Amiri", lang: "ar", dir: rtl, size: 1.12em, body)

#let horizontalrule = align(center, block(above: 1.2em, below: 1.2em, star(size: 7pt, fill: teal)))

#let blockquote(body) = pad(left: 1.5em, right: 1.5em, block(above: 0.9em, below: 0.9em, {
  set par(first-line-indent: 0pt)
  text(size: 0.95em, style: "italic", body)
}))

#let ayah(ref: "", arabic: "", body) = block(width: 100%, above: 1.3em, below: 1.3em, breakable: false, {
  if arabic != "" {
    align(center, block({
      set par(justify: false, leading: 1.15em, first-line-indent: 0pt)
      text(font: ("Amiri Quran", "Amiri", "EB Garamond"), lang: "ar", dir: rtl, size: 11.5pt, fill: ink, arabic)
    }))
    v(0.7em)
  }
  align(center, pad(x: 1.5em, { set par(justify: false, first-line-indent: 0pt); text(style: "italic", body) }))
  align(right, text(size: 8.5pt, fill: teal, tracking: 0.06em, smallcaps[Quran #ref]))
})

#let arquote(arabic: "", source: "", body) = block(width: 100%, above: 1.3em, below: 1.3em, breakable: false, {
  if arabic != "" {
    align(center, block({
      set par(justify: false, leading: 1.1em, first-line-indent: 0pt)
      text(font: ("Amiri", "EB Garamond"), lang: "ar", dir: rtl, size: 11pt, fill: ink, arabic)
    }))
    v(0.6em)
  }
  align(center, pad(x: 1.5em, { set par(justify: false, first-line-indent: 0pt); text(style: "italic", body) }))
  if source != "" { align(right, text(size: 8.5pt, fill: teal, tracking: 0.06em, smallcaps(source))) }
})

#let callout(kind: "word", title: none, body) = {
  let c = box-colours.at(kind)
  block(
    width: 100%, breakable: true, above: 1.4em, below: 1.4em,
    fill: c.lighten(93%), stroke: (left: 2.5pt + c), radius: (right: 2pt),
    inset: (left: 11pt, right: 10pt, top: 9pt, bottom: 10pt),
    {
      set text(font: sans, size: 9pt, fill: ink)
      set par(leading: 0.62em, justify: false, first-line-indent: 0pt, spacing: 0.75em)
      text(fill: c, weight: 600, size: 9pt, tracking: 0.04em)[
        #text(font: ("Amiri", "Source Sans 3"), box-icons.at(kind)) #h(3pt) #upper(if title == none { box-labels.at(kind) } else { title })
      ]
      v(0.1em)
      body
    },
  )
}

// "Words you'll meet" strip at the head of a chapter
#let words(body) = block(width: 100%, above: 0.6em, below: 1.4em, inset: (y: 6pt),
  stroke: (top: 0.4pt + gold, bottom: 0.4pt + gold), {
    set text(font: sans, size: 8.5pt, fill: teal)
    set par(first-line-indent: 0pt, justify: false)
    text(weight: 600, tracking: 0.06em, upper[Words you'll meet])
    h(8pt)
    body
  })

// Part opener with Munajat epigraph
#let part(num: "", title: "", question: "", epigraph-ar: "", epigraph: []) = {
  pagebreak(weak: true, to: "odd")
  set par(first-line-indent: 0pt)
  v(40mm)
  align(center, text(size: 10pt, fill: gold, tracking: 0.2em, upper("Part " + num)))
  v(4mm)
  align(center, text(size: 26pt, fill: teal, title))
  v(2mm)
  align(center, text(size: 12pt, style: "italic", fill: ink, question))
  v(10mm)
  star-band(width: 50%)
  v(10mm)
  if epigraph-ar != "" { align(center, text(font: "Amiri", lang: "ar", dir: rtl, size: 14pt, epigraph-ar)); v(3mm) }
  align(center, pad(x: 12mm, text(size: 10.5pt, style: "italic", epigraph)))
  pagebreak()
}

// "Words you'll meet" strip, placed after the chapter's introduction
#let words(body) = block(width: 100%, above: 1.2em, below: 1.4em, inset: (y: 6pt),
  stroke: (top: 0.4pt + gold, bottom: 0.4pt + gold), {
    set text(font: sans, size: 8.5pt, fill: teal)
    set par(first-line-indent: 0pt, justify: false)
    text(weight: 600, tracking: 0.06em, upper[Words you'll meet])
    h(8pt)
    body
  })

// Part opener with Munajat epigraph
#let part(num: "", title: "", question: "", epigraph-ar: "", epigraph: []) = {
  pagebreak(weak: true, to: "odd")
  set par(first-line-indent: 0pt)
  v(40mm)
  align(center, text(size: 10pt, fill: gold, tracking: 0.2em, upper("Part " + num)))
  v(4mm)
  align(center, text(size: 26pt, fill: teal, title))
  v(2mm)
  align(center, text(size: 12pt, style: "italic", fill: ink, question))
  v(10mm)
  star-band(width: 50%)
  v(10mm)
  if epigraph-ar != "" { align(center, text(font: "Amiri", lang: "ar", dir: rtl, size: 14pt, epigraph-ar)); v(3mm) }
  align(center, pad(x: 12mm, text(size: 10.5pt, style: "italic", epigraph)))
  pagebreak()
}

// Draft markers: visible in drafts so nothing slips through.
#let marker-style(it) = highlight(fill: rgb("#FFE8A3"), extent: 1pt, text(font: sans, size: 0.82em, fill: rgb("#8A4B00"), it))

// ---------- review note (D30): the point a section makes; drafts only ----------
#let point(body) = block(width: 100%, above: 0.4em, below: 1em, inset: (left: 8pt, y: 4pt),
  stroke: (left: 2pt + rgb("#B5482B")),
  text(font: sans, size: 0.8em, fill: rgb("#B5482B"), style: "italic")[*Point:* #body])

// ---------- chapter opener ----------
#let chapter(num: none, title: [], title-ar: "") = {
  pagebreak(weak: true, to: "odd")
  set par(first-line-indent: 0pt)
  v(18mm)
  if num != none {
    align(center, text(font: serif, size: 34pt, fill: teal, weight: 400, str(num)))
    v(4mm)
  }
  star-band(width: 60%)
  v(6mm)
  align(center, text(font: serif, size: 20pt, fill: ink, weight: 500, title))
  if title-ar != "" {
    v(3mm)
    align(center, text(font: "Amiri", lang: "ar", dir: rtl, size: 18pt, fill: gold, title-ar))
  }
  v(14mm)
  // heading hidden from the page but kept for the outline / running head
  hide(place(heading(level: 1, outlined: true, title)))
}

// ---------- book-level setup ----------
#let book(title: "", subtitle: "", edition: "", draft: true, doc) = {
  set document(title: title)
  set text(font: serif, size: 11pt, fill: ink, lang: "en", region: "GB", hyphenate: true,
    features: ("onum", "liga", "kern"))
  set par(justify: true, leading: 0.66em, first-line-indent: (amount: 1.2em, all: false), spacing: 0.66em)
  set page(
    width: 6in, height: 9in,
    margin: (inside: 22mm, outside: 18mm, top: 22mm, bottom: 24mm),
    header: context {
      let p = here().page()
      if p <= 2 { return }
      let chs = query(heading.where(level: 1).before(here()))
      let starts = query(heading.where(level: 1)).filter(h => h.location().page() == p)
      if starts.len() > 0 { return }
      let left-side = calc.even(p)
      set text(size: 8pt, fill: teal, tracking: 0.08em)
      grid(columns: (auto, 1fr, auto), align: (left + horizon, center + horizon, right + horizon),
        if left-side { corner-motif() } else { smallcaps(title) },
        [],
        if left-side { smallcaps(if chs.len() > 0 { chs.last().body } else { title }) } else { corner-motif() },
      )
      v(-4pt)
      line(length: 100%, stroke: 0.3pt + gold)
    },
    footer: context {
      let p = here().page()
      if p <= 2 { return }
      align(center, text(size: 8.5pt, fill: teal, counter(page).display("1")))
    },
  )
  show heading.where(level: 2): it => {
    set par(first-line-indent: 0pt)
    block(above: 1.6em, below: 0.9em, breakable: false, {
      text(size: 12.5pt, weight: 500, fill: teal, it.body)
    })
  }
  show heading.where(level: 3): it => block(above: 1.2em, below: 0.6em,
    text(size: 11pt, style: "italic", weight: 500, it.body))
  show footnote.entry: set text(size: 8.5pt)
  show regex("\[(VERIFY|QUERY|GAP):[^\]]*\]"): it => if draft { marker-style(it) } else { it }

  // Title page
  page(header: none, footer: none, {
    v(30mm)
    star-band(width: 70%)
    v(10mm)
    align(center, text(size: 26pt, weight: 500, fill: ink, title))
    v(4mm)
    align(center, text(size: 13pt, style: "italic", fill: teal, subtitle))
    v(10mm)
    star-band(width: 70%)
    v(1fr)
    align(center, text(size: 10pt, fill: teal, smallcaps(edition)))
    if draft { v(4mm); align(center, text(font: sans, size: 8pt, fill: rgb("#8A4B00"))[DRAFT — not for distribution]) }
  })
  page(header: none, footer: none, [])
  doc
}
