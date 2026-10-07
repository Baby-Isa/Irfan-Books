# Decisions log

_Append only. Each entry: date, decision, why. To reverse a decision, add a new entry that cites the old one._

## 2026-10-07: D1. Two books, with a pilot before full production
- **Decision:** Book 1 (Faithful) stays strictly to the lecture content. Book 2 (Expanded) is a contextualised rewrite with callouts. One chapter is written in both styles and compared before the full book is produced.
- **Why:** this keeps a real comparison while roughly halving the cost of the most expensive phase.

## 2026-10-07: D2. Toolchain is Markdown → Pandoc → LuaLaTeX
- **Decision:** chapters are written in Pandoc Markdown. A Lua filter maps callout divs and Arabic spans to LaTeX. The output is a PDF (print quality) and an EPUB from the same source.
- **Why:**
  - Markdown is cheap and robust for Claude to edit.
  - LuaLaTeX gives the best free Arabic shaping (via fontspec/babel and HarfBuzz) and print quality.
  - It is free and works from the command line.

## 2026-10-07: D3. Book 1 is written in a neutral third person
- **Decision:** expository prose, not the lecturer speaking as "I".
- **Why:** the user's choice.

## 2026-10-07: D4. Model split
- **Decision:** Sonnet subagents handle extraction (notes) and checking. Opus handles orchestration and book prose.
- **Why:** token budget.

## 2026-10-07: D5. Attribution
- **Decision:** the transcribers are not named, and their names are removed from the filenames. The lecturer appears as `{{LECTURER}}` until the name is confirmed.

## 2026-10-07: D6. Traceability
- **Decision:** transcripts are split into ~120-word numbered segments (¶N) in `transcripts/text/`. All notes and Book 1 prose cite `L{NN} ¶{n}`.
- **Why:** the original docx paragraphs are sometimes thousands of words long, which is too coarse for citing.

## 2026-10-07: D7. No Arabic or scripture from memory
- **Decision:** Quranic Arabic is taken from a verified text file only. Hadith and du'a text is taken from held sources. Anything unconfirmed is marked `[VERIFY]`, and a release build fails while any remain.

## 2026-10-07: D8. Typst replaces LuaLaTeX (supersedes D2)
- **Decision:** the chain is now Pandoc Markdown → Lua filter → Typst → PDF. The EPUB is still built directly by Pandoc.
- **Why:** TeX Live can't be installed in the cloud environment (the apt mirrors and CTAN are blocked). Typst installs from PyPI in seconds (`pip install typst`), has good Arabic shaping (HarfBuzz-based), and builds fast. The user chose this.

## 2026-10-07: D9. Book 2 gets three extra chapters
- **Decision:** A (Prologue: why ʿIrfan), B (Shia ʿIrfan after the Safavids: the living chain), and C (the du'as as a school of ʿIrfan). All three were approved by the user.

## 2026-10-07: D10. Book 2 (Expanded) is the chosen style
- **Decision:** the user chose Book 2. Book 1 is shelved as a reference draft.
- **Voice:** a normal non-fiction voice that talks to the reader. Attribute only occasionally ("Sheikh Bahmanpour argues…", "the lectures turn to…"), not every paragraph.
- **Front matter:** the author's name goes on the cover, and an introduction credits the lecture series.

## 2026-10-07: D11. Lecturer identified
- **Decision:** M. S. Bahmanpour, from the slides (`sources/handouts/`). The series was a BA Islamic Studies module.
- **Note:** check with him how he wants to be named and titled. The user's working form is "Sheikh Bahmanpour".
