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

## 2026-10-07: D12. Final structure
- **Decision:** five parts and 17 chapters, plus a prologue and an epilogue, from Fable's review and gap analysis (`reviews/structure-*.md`).
- **Parts:** The Call, The Terrain, The Travellers, The Road, The Return.
- **History:** the history comes before the practice.
- **"Finding a guide":** this chapter opens Part Four.
- **Supersedes:** the 19-chapter proposal in ANALYSIS.md and OUTLINE v1. OUTLINE.md v2 is canonical.

## 2026-10-07: D13. The Munajat Shaʿbaniyyah is the framing thread
- **Decision:** one line of the Munajat Shaʿbaniyyah opens each part as an epigraph. Chapter 2 presents the whole prayer, and the epilogue closes with it.
- **Text:** the Arabic comes from Mafatih (held). The English comes from a held translation only.

## 2026-10-07: D14. Length
- **Decision:** a body target of about 65k words (boxes extra), at about 3.5–4.5k words per chapter.
- **Review point:** before the text is finalised, assess what a cut to about 50k would lose, and decide.

## 2026-10-07: D15. Lecture claims that can't be sourced are omitted or reworked
- **Decision:** where the lecture cites a text we can't locate in a held source, or the claim can't be supported, the book omits it or works around it (for example, keeps the idea without the attribution). It does not print a query.
- **Record:** each omission is logged in `docs/OMISSIONS.md` for the review draft.
- **Scope:** `[QUERY]` is kept only for substantive theological points where omitting would distort the lecturer's position.

## 2026-10-07: D16. Karbala
- **Decision:** Karbala is presented as a reflection offered to the reader, grounded in Imam al-Husayn's Duʿa ʿArafah. It is not presented as the lecturer's teaching.

## 2026-10-07: D17. Review process
- **Decision:** no external review (lecturer or others) before the first complete draft.
- **What the draft looks like:** fully styled and formatted as a book, then shared for review.

## 2026-10-07: D18. No devotional-calendar thread
- **Decision:** we don't tie chapters to the Khoja calendar months (Fable's secondary thread is dropped).

## 2026-10-08: D19. Outline v2.1: source alignment
- **Decision:** apply the 18 point, source and content amendments from `reviews/outline-alignment.md`, section 3. There is no structural change.
- **Main changes:**
  - Ch 10's teacher chain follows the Kernel and *Light*.
  - Ch 8 presents the critics through the defenders' answers.
  - The Ch 9 point now acknowledges Shia masters' use of shaykh and pledge.
  - Ch 16 carries a `[QUERY]` on whether the fourth journey is open to non-Imams.
  - The Khoja/pir box, and Knysh and Baldick, are dropped until sources are held.
- **Epigraphs:** the part epigraphs follow the review's section 4 proposal. Each line is to be checked against the Arabic in Mafatih p. 244 before use.

## 2026-10-08: D20. How the book frames its relationship to the lectures and the wider literature
- **Framing:** the book is *heavily inspired and influenced by* Sheikh Bahmanpour's lecture series. It also draws on the wider literature (the Imams' texts, Tabatabaʾi, Mutahhari, Khomeini, Amuli, Maliki Tabrizi and others) to give a more rounded guide to ʿirfan. The prologue says so.
- **Where views differ** (for example, do you need a guide, how much seclusion, who completes the fourth journey): present them side by side, warmly and respectfully, as a conversation among scholars. "Sheikh Bahmanpour emphasises…; ʿAllama Tabatabaʾi, for his part, …".
- **Tone:** no heavy critique, no "the lecturer is wrong". Let the reader see the range.
- **Effect on D15:** this softens it. Where a held source gives a different view, show both rather than dropping the lecturer's. Omit only claims that rest on a citation we cannot locate.

## 2026-10-08: D21. Citations are footnotes
- **Decision:** `[@key, locator]` in Markdown becomes a footnote, "Short form, locator.", for example "Imam Khomeini, *Forty Hadith*, p. 61." This is done by the `Cite` handler in `build/irfan.lua`, using its `SHORT` table. Citeproc is not used.
- **Rule:** when a key is added to `bibliography.bib`, add its short form to `SHORT` as well. The build fails on an unknown key.
- **Page numbers:** "p. N" currently means the PDF page of the held edition. Convert to printed page numbers before print, if needed.
- **Later polish:** shortened repeat citations, and a full bibliography in the back matter.

## 2026-10-08: D22. Every chapter is argued like a legal case, then written warmly
- **Case brief first:** before any prose, each chapter gets a case brief in `docs/briefs/NN-case.md`. The brief has:
  - one conclusion sentence
  - numbered premises, each sourced, MECE, in an order where every step depends only on earlier ones
  - the section headings mapped one-to-one onto the steps.

  The user approves the brief before the chapter is written.
- **Prose rules:** the prose on top of the brief is warm and free-flowing. It must also follow these rules:
  - **No jokes, ever**, including the lecturer's asides.
  - **No throat-clearing.** Don't open new questions the chapter won't answer, and don't make rhetorical-question chains.
  - **Not condescending.** The reader is an intelligent, interested, impatient friend.
  - **About 20% shorter than v2.** That means about 3,000–3,600 words of body per chapter, and a book body of about 52k (this revises D14).

## 2026-10-08: D23. The book's argument is a pyramid
- **Canonical file:** `docs/ARGUMENT.md`.
- **Structure:** one book thesis, then five book points B1–B5 (one per Part: why, what, whose, how, to what end), then numbered chapter points N.x (each tagged with the B it serves), then section headings (each tagged with the N.x it serves, set in the chapter's brief).
- **Rule:** no element exists without a parent. ARGUMENT.md is approved before the chapter briefs, and briefs must match it.
- **Ch 1** now explicitly argues that ʿirfan is worth pursuing (point 1.3).

## 2026-10-08: D24. Epigraph English comes from *Light Within Me*
- **Decision:** the Munajat Shaʿbaniyyah epigraphs use the *Light Within Me* translation (pp. 163–166). Each line is checked against the Arabic in Mafatih p. 244.
- **Permissions:** permissions for every quoted translation (*Light*, Chittick, Qutbuddin, Qaraʾi and the others) will be obtained before publishing. This is tracked in SOURCES.md.

## 2026-10-08: D25. Chapter 16's conclusion follows the lecturer; Tabatabaʾi is kept, gently
- **Decision:** Option A. The conclusion stays: *"The path's completion is a return to people, with God, shown fully in the Prophet and the Imams."*
- **16.3:** how far ordinary believers share in that return is shown as an open question, with both views side by side. The lecturer reserves the completed fourth journey for the Prophet and the Imams (L09 ¶87–89). ʿAllama Tabatabaʾi holds that wilaya "is not at all exclusive", so others can reach it in their measure (`kernel` p. 20; `light` p. 64).
- **Why:** the book rests on the lectures, so the headline must be true under the lecturer's view. Tabatabaʾi's standing means his view cannot be left out. It is stated softly and respectfully, not as a correction (D20).

## 2026-10-08: D26. "Travel means removing veils" is seeded in Ch 4 and developed in Ch 11
- **Decision:** Option C. Chapter 4 plants the idea, in a short passage of a few sentences rather than a single line, as a consequence of 4.3: God is already near, so the journey through the self removes veils rather than covering distance. Chapter 11 (11.1) develops it fully as the frame of the stages.
- **Rule:** Ch 4 states the idea and points forward. It does not take over Ch 11's exposition (the veils, the stages).

## 2026-10-08: D27. Chapter 9 keeps four points
- **Decision:** Option A. Point 9.4 stays: set techniques are secondary, because each soul receives grace in its own shape, so a seeker needs a trustworthy guide, not a lineage (L14 ¶65–71). It hands off to Ch 10.

## 2026-10-08: D28. Chapter 1's "Try this" is the four signs of Surah al-Rum
- **Decision:** Option A. Read Q 30:21–24 slowly, once a day for a week, and notice one of the signs in your own day.
- **Kept for Ch 13:** Imam ʿAli on remembrance as the polish of hearts (Nahj 1.219.1).
- **With D25–D27, ARGUMENT.md v2.1 is approved.**

## 2026-10-08: D29. House voice and banned lingo
- **Decision:** all book prose follows `docs/LINGO.md`. That means writing for a smart, slightly impatient friend; prose over bullet points; short over long; plain English over buzzwords; no hedges the argument does not need; and no summary line or tidy closing remark (stop on the last concrete detail).
- **Banned:** a list of stock phrases; sentences opening with So, Well, Look or Now; intensifiers; wordy constructions; and the "tidy aphorism", the short balanced sentence that adds no fact (for example "It is beautiful, and it is true." and "The floor is real, and it saves.").
- **Kept:** the chapter's conclusion (D22/D23) is still stated once, plainly, in the last section. Scholarly differences (D20) are content, not hedges.
- **Applied to:** the prologue and Ch 1 v3. Writers and the fidelity-checker now check against it.

## 2026-10-08: D30. Plain, direct drafting with review notes
- **Review notes:** every draft section opens with a `::: {.point}` note (one or two sentences) stating the point it makes, for the user to judge the prose against. Drafts show it; `--final` builds drop it.
- **Plain and direct:** no suspense devices; name things. An epigraph is spoken to directly. Quotations kept short. "Let's" is welcome; arch phrasing is not. Don't repeat what the prologue says. Added to `docs/LINGO.md`.
- **"Words you'll meet"** lists each term with a brief meaning.
- **Prologue order:** What is ʿirfan?; Who this book is for; How the book is built; Where this book comes from; What you can expect (which now carries "what ʿirfan is not"). The audience is any believer, not named as a community. The epigraph is the Munajat's "Enlighten the eyes of our hearts…" line, explained in the text, and the opening explains the word ʿirfan.
- **Ch 1 opening:** epigraph is the end of Q 30:21; the wedding verse is named outright.
