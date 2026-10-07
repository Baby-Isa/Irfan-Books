# Style guide

## Audience
The readers are English-speaking Khoja Shia Ithna'ashari Muslims, mostly in the UK, East Africa and North America. They:
- know the basics of practice (salah, Muharram majalis, du'a Kumayl)
- know common words such as *wajib*, *mustahab*, *jannah*, *ma'rifah* and *ahl al-bayt*
- are mostly new to Irfan as a discipline.

## Book 1: Faithful
- **Content:** only what the lectures say. You may reorder, merge repeated passages, drop filler (classroom logistics, "inshaAllah next week", false starts) and fix grammar.
- **What you must not add:** examples, arguments, references or facts. If the lecturer leaves a reference vague ("a famous hadith says…"), keep it vague and add `[VERIFY]` if it needs a citation.
- **Voice:** neutral third-person exposition. Prefer plain statement ("Irfan seeks knowledge of God through…") over constant "the lecturer says". Use attribution ("as the lectures put it") only where the claim is clearly the lecturer's personal view or interpretation.
- **Stories and anecdotes:** keep them, because they carry the teaching.
- **Q&A segments:** fold them into the text where they fit, or keep them as a short "Questions" section at the end of the chapter.
- **Sources:** each paragraph ends with `<!-- src: LNN ¶a-b -->`.
- **Allowed apparatus:** footnotes are allowed only to identify a reference the lecturer made, such as surah and verse. No callout boxes.

## Book 2: Expanded
Everything in Book 1, plus the following.
- **Prose:** warmer and more explanatory. Define each term the first time it appears. Bridge gaps in the argument. Add brief context where the lecture assumes knowledge. Each addition is cited.
- **Callout boxes** (Pandoc fenced divs), roughly 1–3 per 2,000 words, each 60–200 words:

| Class | Title style | Use |
|---|---|---|
| `.box-word` | "Word Study: *ma'rifah*" | Root, literal meaning, use in Quran and hadith |
| `.box-history` | "History" | Historical background: people, schools, events |
| `.box-story` | "Story" | Expands a story the lecture mentions in passing |
| `.box-who` | "Who's Who: 'Allama Tabataba'i" | A short biography of a figure the lecture names |
| `.box-reflect` | "Reflection" | A question for the reader to sit with, at most one per chapter |
| `.box-try` | "Try this" | One small, sourced practice at the end of each chapter. Never invented. |

  Syntax: `::: {.box-word title="Word Study: ma'rifah"}` … `:::`
- **Sourcing:** use only held sources (SOURCES.md), Tier A first. No uncited historical claims.
- **Tone:** devotional but not preachy. Avoid New-Age vocabulary. "Mysticism" is acceptable as a gloss, but prefer "Irfan".

## Book 2 voice and chapter shape (D10, OUTLINE v2)
- **Voice:** talk to the reader, as in a normal non-fiction book. Name Sheikh Bahmanpour occasionally, where the view is distinctively his ("Sheikh Bahmanpour argues…"). Don't write "the lecture says" in every paragraph.
- **Chapter shape:** the order of introduction, then `::: {.words}`, then body, then "Try this" is set in OUTLINE v2.
- **Quran:** use `::: {.ayah ref="S:A"}` with **Qaraʾi's English**, from `python3 build/quran.py S:A`. When the lecturer paraphrases a verse, quote Qaraʾi and keep his point in the prose.
- **Unsourced lecture claims:** omit or rework them, and log each one in `docs/OMISSIONS.md` (D15).

## Both books
- **Honorifics:**
  - Use ﷺ after the Prophet's name, the first time per section.
  - Use (ʿa) for the Imams and Lady Fatima, and (ʿaj) for Imam al-Mahdi.
  - Use "God" or "Allah": Allah in devotional contexts, God in philosophical ones. Be consistent within a paragraph.
- **Transliteration (light):**
  - Write ʿayn as ʿ and hamza as ʾ (not at the start of a word).
  - No macrons in running text. Italicise a term on first use only.
  - The spelling always follows GLOSSARY.md, e.g. *ʿirfān* → **ʿIrfan** (capitalised as a discipline), *maʿrifah*, *sayr wa sulūk* → *sayr wa suluk*.
  - Use common forms for well-known names: Imam ʿAli, Imam Khomeini, Ibn ʿArabi.
- **Quran:**
  - Arabic comes from `sources/quran/` only. Give the English translation and cite it as `(Q 2:156)`.
  - Follow the translation chosen in SOURCES.md.
- **Hadith and du'a:**
  - Use the English text, with Arabic only if it comes from a held source.
  - Cite collection, volume and page or number, e.g. `[@kafi, 2:123]`.
- **Spelling and headings:** British spelling. Sentence case for headings.
- **Markers:**
  - `[VERIFY: …]`: a fact or text needs checking against a source.
  - `[QUERY: …]`: a question for the lecturer.
  - `[GAP: …]`: the transcript is garbled or material is missing.
