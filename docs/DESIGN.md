# Design language

_Goal: it should look like a designed publication, not a type-up. Ornament stays restrained: about 5% of the page, never competing with the text._

## Format
- **Trim size:** 6 × 9 in (a standard print-on-demand size; it also reads well as a PDF on a tablet).
- **Margins:** inner 22mm, outer 18mm, top 20mm, bottom 24mm.
- **Outputs:** PDF (primary) and EPUB (reflowable; the boxes become styled asides, and the ornaments are dropped).

## Type
| Role | Font (free / OFL) |
|---|---|
| Body | EB Garamond 11/15pt |
| Headings | EB Garamond small caps, or Cormorant Garamond |
| Arabic (general) | Amiri |
| Quranic Arabic | Amiri Quran |
| Callout box text | Source Sans 3, 9.5pt (contrast with the body) |

## Colour (print-safe, also works in greyscale)
- **Ink:** near-black `#1F1B16`
- **Accent:** deep teal `#1E5A5A`, used for rules, chapter numbers and box frames
- **Secondary accent:** muted gold `#B08D3C`, used for ornaments only
- **Box backgrounds:** a tint of each box type's colour at about 6–8%

## Ornament
- **Chapter opener:** a large chapter number, the English title, the Arabic title in Amiri beneath it, and a thin geometric band (an eight-point star pattern drawn in Typst, in gold).
- **Pages:** a small geometric corner motif on the outer header corner. Hairline rules on the header and footer. No full-page borders.
- **Section breaks:** a single eight-point star ✶ glyph in the accent colour.
- **Quran verses:** centred Arabic, translation beneath it in italics, with the reference set flush right in small caps.

## Callout boxes (Typst `block`s)
Each type has one colour and one small icon glyph:

| Type | Colour | Icon |
|---|---|---|
| Word Study | teal | ع |
| History | brown | ⧗ |
| Story | plum | ❧ |
| Who's Who | slate | ◈ |
| Reflection | gold | ✦ |

- **Shape:** rounded corners at 2pt, a left accent bar, and the title in small caps.
- **Placement:** full-width at a paragraph break. This gives the magazine feel without the fragility of margin notes.

## Front matter and back matter
- **Front:** half title, title page (with an Arabic calligraphic title), copyright and permissions, contents, the note on transliteration, preface.
- **Back:** glossary, bibliography, index of Quranic verses, general index (optional).
