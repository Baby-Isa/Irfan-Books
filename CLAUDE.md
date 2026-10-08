# Irfan Books — project guide for Claude

## What this is
We are turning a 16-lecture series on **Irfan** (Islamic mysticism, Shia tradition) into two books:
- **Book 1 (Faithful):** the lecture content only. It is cleaned up, reordered by theme, and written in a **neutral third person** ("The lecture explains…", or plain exposition). Nothing is added.
- **Book 2 (Expanded):** a reader-friendly rewrite for the Khoja Shia Ithna'ashari community, aimed at readers who are new to Irfan. It adds context in the prose and uses callout boxes. Every addition is cited.

Both books start as a pilot chapter. The chosen style then goes into full production (see `docs/DECISIONS.md`).

## Read first, every session
1. `docs/STATUS.md` shows where we are and what is next. If `docs/HANDOVER.md` exists, read it first.
2. Then read only the docs your task needs:

| Task | Read |
|---|---|
| Write or edit a chapter | `docs/LINGO.md`, `docs/TONE.md` (stance and paragraph flow; every rule has a before/after), `docs/ARGUMENT.md`, that chapter's brief in `docs/briefs/`, `docs/STYLE_GUIDE.md`, `docs/GLOSSARY.md`, that chapter's entry in `docs/OUTLINE.md`, the relevant `notes/` and transcript ¶ ranges |
| Typesetting or layout | `docs/DESIGN.md`, `build/` |
| Sources or citations | `docs/SOURCES.md`, `sources/bibliography.bib` |
| Any decision with lasting effect | Append it to `docs/DECISIONS.md` |

Don't load all the transcripts or notes into one context. Delegate per-lecture or per-chapter work to subagents (`.claude/agents/`).

## Golden rules
1. **Never invent scripture or quotations.** Don't write any Quran verse, hadith, du'a, poem or Arabic text from memory.
   - Quranic Arabic is copied from `sources/quran/` only.
   - Anything unconfirmed gets the marker `[VERIFY: what needs checking]`.
2. **Book 1 traceability.** Each paragraph ends with a hidden source comment, for example `<!-- src: L03 ¶12-15 -->`. If a claim isn't in the transcripts, it doesn't go in Book 1.
3. **Book 2 additions are cited.** Use Pandoc citations (`[@key, p. 12]`) with keys from `sources/bibliography.bib`. Use only held or clearly identified sources (see SOURCES.md tiers). If there is no source, use `[VERIFY]` or leave the addition out.
4. **Glossary first.** A term's spelling and transliteration come from `docs/GLOSSARY.md`. Add a new term there before using it.
5. **The lecturer's views are theirs.** Don't "correct" their theology. Flag apparent errors with `[QUERY: …]` for the user to raise with the lecturer.
6. **Transcripts are canonical and read-only.** `transcripts/text/IrfanNN.md` is cited as `L{NN} ¶{n}`.
7. **Update `docs/STATUS.md`** at the end of every task. Log decisions in `docs/DECISIONS.md`.
8. **Be economical with tokens.**
   - Read the specific ¶ ranges, not whole transcripts, unless the task is per-lecture.
   - Use Sonnet subagents for extraction and checking; use Opus for prose.

## Layout
```
transcripts/raw/        original .docx (transcribers' names removed from filenames)
transcripts/text/       numbered plain text, ~120-word segments ¶N
notes/                  per-lecture detailed notes (phase 1), template in notes/_TEMPLATE.md
docs/                   STATUS, DECISIONS, STYLE_GUIDE, DESIGN, GLOSSARY, SOURCES, OUTLINE
sources/                bibliography.bib, quran/ (verified text), extracts/ (text of held PDFs)
book1/ book2/           chapters/NN-slug.md, front/, back/
build/                  Pandoc → Typst template, Lua filter, fonts, Makefile
.claude/agents/         transcript-analyst, chapter-writer, fidelity-checker
```

## Workflow (phases)
0. Scaffold
1. Per-lecture notes
2. Outline, glossary and reading list (user checkpoint)
3. Design template and sample PDF
4. Pilot chapter in both styles (user checkpoint)
5. Chapter production, one chapter at a time, in two gates:
   - **Gate A: case brief.** Write `docs/briefs/NN-case.md` from `docs/briefs/_TEMPLATE.md` and present it to the user as bullet points. Wait for their approval. No prose is written before approval.
   - **Gate B: prose.** Write the chapter on top of the approved brief, run the fidelity check, then send the PDF.
6. Assembly: PDF and EPUB

## How the user works (applies to everything)
- **The argument is a pyramid** (`docs/ARGUMENT.md`, D23): the book thesis, then book points B1–B5, then chapter points N.x (each tagged [Bn]), then section headings (each tagged [N.x]). Every element answers its parent.
- **Structure must be bulletproof.** It is argued like a lawyer's case:
  - one conclusion per chapter
  - numbered, sourced premises in an order where each step depends only on earlier ones
  - MECE coverage
  - headings mapped one-to-one onto steps.

  The judge (the reader) should find the conclusion self-evident.
- **Gentle text on a rigorous spine.** The prose can be warm and flowing, but the logical link from heading to heading must be visible.
- **The reader** is an intelligent, interested, impatient friend who will close the book at the first sign of throat-clearing:
  - no jokes, ever, including the lecturer's asides
  - no rhetorical-question chains
  - no new questions the chapter doesn't answer
  - nothing condescending
  - aim for about 20% less than feels natural
  - follow `docs/LINGO.md` (D29): prose over bullets, plain English, no tidy aphorisms or closing remarks, and no banned words, openings, intensifiers or wordy constructions.
- **Reporting style:** clarity from complexity. Give summaries as structured bullets, led by the conclusion.

## Build
- `python3 build/build.py pdf book1` → `build/out/book1.pdf` (drafts highlight markers; add `--final` for release, which refuses to build while markers remain)
- `python3 build/build.py check` lists open `[VERIFY]`/`[QUERY]`/`[GAP]` markers
- `python3 build/quran.py 30:21-22` prints verified Arabic
- Verse blocks only need `::: {.ayah ref="30:21"}` + English; the build inserts the Arabic itself
- Setup: `pip install typst` (pandoc ≥3.1 is preinstalled). Fonts are committed in `build/fonts/` (OFL).

## Conventions
- **Branch:** work on the branch given by the session. Commit after each completed unit, using short imperative messages.
- **Chapter files:** `bookN/chapters/NN-slug.md` (Pandoc Markdown). Callouts use fenced divs, for example `::: {.box-word}` (the types are in STYLE_GUIDE).
- **Arabic in Markdown:** `[نص]{lang=ar}` inline; `::: {.ayah ref="2:156"}` for a verse block.
- **Lecturer:** written as `{{LECTURER}}` until the name is confirmed. Transcribers are not named.
