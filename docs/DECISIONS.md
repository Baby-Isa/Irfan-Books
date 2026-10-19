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

## 2026-10-08: D31. Tone rules: stance and flow (`docs/TONE.md`)
- **Decision:** all book prose follows `docs/TONE.md` as well as `docs/LINGO.md`. Its rules: each paragraph's first sentence picks up the last paragraph's point and states its own; every sentence passes the relevance test against the section's point note; no lecturing, moralising or asides ("as we should"); no presumption about the reader (intelligence, practice, piety, sex); warm and plain without familiarity; every quotation is spoken to in the sentence after it; every displayed Quran, hadith or duʿa quote carries its Arabic (`.ayah words=` for part of a verse, `.quote ar=` from a held extract, `[VERIFY]` otherwise); no cleverness or suspense; "let's" for walking through a step; short quotations; point notes kept current.
- **Reader:** any believer who prays, fasts and recites duʿas; not named as a community; nothing else assumed about them.
- **Applied to:** prologue and Ch 1 (round 3). Added to CLAUDE.md's "Write or edit a chapter" row and to the chapter-writer agent.
- **Nahj Arabic:** the Nahj extract's Arabic is garbled, so Nahj quotations carry `ar="[VERIFY: …]"` until typed from the printed Qutbuddin edition.

## 2026-10-08: D32. Spelling "Qur'an"; the lectures were a lecture series
- **Spelling:** book prose uses "Qur'an" and "Qur'anic" (user's spelling), including the label on verse blocks. Citations stay "Q 30:21". Quotations keep their source's spelling.
- **Provenance:** the lectures were delivered as a lecture series, which the user's uncle attended. The slides carry a "BA Islamic Studies" heading, but the book must not say the series was part of a BA. The prologue now says "a lecture series on Islamic mysticism given by Sheikh M. S. Bahmanpour". This supersedes the module wording in D11 and ANALYSIS.md.

## 2026-10-08: D33. Chapter 1 round 6 (user voice note)
- **Lecturer quotes:** quote the Sheikh only where his words carry weight; otherwise paraphrase without quotation marks. Minor corrections inside a quote go in square brackets ("[rusted]"). Refer to his "lectures", never "classes". (TONE rule 18)
- **"jannah"** is spelled with a final h.
- **Ch 1 §6** is retitled "The aim is God, not powers". Tabatabaʾi's p. 101 remark on judging a teacher is dropped as repetitive.
- **Layout:** a verse block's reference (and a quote's source) now sits top right, above the Arabic, so the space below the quote matches the space above it.
- **The muqarrabun "given Paradise in this world"** is kept, attributed to the Sheikh (L01 ¶16), and reworded for clarity.

## 2026-10-12: D34. Credits
- **Title page:** "Based on a lecture series by Sheikh M. S. Bahmanpour" and "Edited by Zafar Abbas Juma". The user's uncle, who knows the Sheikh, approved the prologue and Ch 1 and agreed this framing. "Edited" (or "Curated") signals that the book adds no personal opinions. The alternative wordings "Adapted from…" and "Curated by…" are still open.

## 2026-10-12: D35. Paragraph spacing (trial)
- **Layout:** paragraphs now have a half-line gap (`spacing: 1.1em`) as well as the first-line indent. This is what the user asked for, to make long passages easier to read, and it adds about one page per 17. The user should confirm after seeing it. To revert, set `spacing: 0.66em` in `build/template.typ`.
- **Writing rule:** paragraphs of 50–65 words, 110 at most (TONE rule 22).

## 2026-10-12: D36. The prologue and Ch 1 are the exemplar
- **Approval:** the user and his uncle approved them, and commit `32e44c9` on this branch freezes them. `docs/EXEMPLAR.md` records the target numbers and the first-draft → final pairs.
- **Writers:** every writer reads the exemplar in full before drafting.
- **Tone editing:** a new `tone-editor` agent line-edits each draft against the exemplar before the fidelity check.

## 2026-10-12: D37. A voice gate before the user sees a chapter
- **Decision:** after the tone-editor pass, every Book 2 chapter must pass a two-part voice test (`docs/VOICE-TEST.md`) before the fidelity check and before the user sees it.
  - **Measured profile** (`build/voice.py profile`): paragraph and sentence length, TONE habits and lingo, set against the exemplar's own spread.
  - **Blind judge** (`voice-judge` agent): a fresh judge reads the exemplar as "Author A", then marks shuffled passages (held-out exemplar, the new chapter, and a control drafted before D29 that the user rejected) as same or different hand.
- **Rules:** the run is valid only if the judge catches at least 3 of 4 control passages. The chapter passes only if it is flagged no more often than the real author in the same run. Failed tells go to the tone-editor, for up to three rounds; after that, the user decides.
- **Calibration:** both exemplar files pass. All eight rejected drafts fail at least one test. The judges caught 8/8 control passages, with 2/8 false alarms on the real author.
- **Why:** the user asked for a rigorous check that new chapters read as the same author as the prologue and Ch 1, run before drafts reach them.

## 2026-10-12: D38. Part One briefs (Ch 2 and 3) drafted for Gate A
- `docs/briefs/02-case.md` and `docs/briefs/03-case.md`, from ARGUMENT v2.1 and source evidence packs. Ch 2 drops the L06/L10 anchors on 2.3 (neither lecture quotes a duʿa) and takes its occasions from the Mafatih. Ch 3 marks the "study serves" clause of 3.4 as added (Khomeini, Tabatabaʾi), since the Sheikh gives study no role. Awaiting user approval.

## 2026-10-12: D39. The storyline; no questions for the Sheikh; Ch 2 and 3 brief decisions
- **Storyline (`docs/STORYLINE.md`):** the whole book as a slide deck. Each chapter has a heading (its title) and a one-sentence plain-English subheading stating its point, with its steps as bullets beneath. Read alone, the subheadings tell the argument from start to finish. The user reviews it before approving the Part One briefs. It is the plain-English reading of ARGUMENT.md, and the two must stay in step.
- **No questions for the Sheikh (general rule):** questions add time and fuss. Where a lecture passage is unclear, go around it: leave it out, use a clearer passage, word it so it is true on either reading, or set a held source beside it. CLAUDE.md golden rule 5 is updated. The Ch 1 marker on "These are shirk" is removed; the text quotes his words as said. The `[QUERY]` marks still in ARGUMENT.md and OUTLINE.md (6.2, 10.1, 16.3) are resolved this way when each chapter's brief is written.
- **Ch 2:** the whole Munajat Shaʿbaniyyah goes in an appendix. The chapter quotes only the key lines, where it needs them.
- **Ch 3:** the "study serves" clause stays, attributed to Khomeini and Tabatabaʾi. The thousand-doors hadith (L03 ¶10) is left out.

## 2026-10-12: D40. Book 2 restructured around the reader's journey (proposed, awaiting approval)
- **User's direction:** why travel → getting ready → travelling the road → who else you meet on the road → the destination. The book builds to a crescendo about two-thirds of the way through (Ch 12, losing the self) and has no side quests before it. "Isn't this Sufism?" is answered in a line in the prologue and fully in Ch 15.
- **Structure v3:**
  - Part One, The Call (1–3)
  - Part Two, Getting ready (4–7; Finding a guide moves here)
  - Part Three, The Road (8–12)
  - Part Four, Fellow travellers (13–15; old Part Three)
  - Part Five, The Destination (16–17)
  - Epilogue and an Appendix with the full Munajat
- **Part dividers:** title, the reader's question, a two- or three-line answer, the chapter titles and a Munajat line.
- **Detailed outline:** `docs/outline/` holds FRAMEWORK, part-1 to part-5 and REVIEW (presented by Fable). Every quote is allocated once across the book, including a line-by-line Munajat allocation.
- **Supersedes on approval:** Fable's earlier suggestion (keep Part Three before the Road, and move Ch 8 into it). The user rejected it.
- **Pending:** ARGUMENT.md v3, STORYLINE.md and OUTLINE.md are regenerated from `docs/outline/` once the user approves.

## 2026-10-12: D41. Structure v3 approved; Ch 2 and Ch 3 swapped; Fable's fixes adopted
- **Approved:** the D40 structure and titles, the Part dividers, and the detailed outline (`docs/outline/`).
- **Ch 1** is renamed "More than the minimum". Its hand-off now asks "what kind of knowing is that?", and its Word Study points to Ch 2. The file keeps its name.
- **Prologue edits applied:** the thesis order; "How the book is built" (Part titles and ranges for v3); Ch 9 → 15; Ch 8 → 14; the point box order.
- **Swap (user):** Ch 2 is now "Knowing about God is not knowing Him" and Ch 3 "You already know these words". Part One climbs from the invitation, to the kind of knowing it is, to the hope that our prayers already ask for it. The briefs are renumbered and rewritten.
- **Other approvals:** ʿArafah closing-section lines are attributed "as given in the Mafatih"; Qadi al-Nuʿman is left out; Ch 13 opens on a companion.
- **Fable's fixes and the user's tone arc:** recorded in `docs/outline/FRAMEWORK.md` §9. Part Four is the analytical step back after the crescendo; Part Five brings the emotion home.
- **Ch 2 and Ch 3 briefs approved.** Drafting begins.

## 2026-10-13: D42. User's Ch 2/3 review, round 1: style and voice rules
- **Honorifics:** (as) replaces (ʿa) for the Imams. The reader knows "(as)"; "(ʿa)" was an academic transliteration of the same ʿalayhi/ʿalayhim al-salam. (atfs) is used for Imam al-Mahdi. ﷺ stays for the Prophet.
- **Oxford comma** throughout the book; **chapter numbers in words** in prose ("Chapter Two"); **one callout box per section**.
- **Attribution:** name the Sheikh about 70% less (TONE 23). Straight prose, not "he said, she said" (TONE 24). `build/voice.py` now flags more than 5 mentions per 1,000 words.
- **New TONE rules 23–31:**
  - attribution (23)
  - straight prose (24)
  - each paragraph earns its place in the chain (25)
  - callbacks re-explained (26)
  - "therefore" only after the argument is made (27)
  - name the referent (28)
  - explain a source's puzzle or cut it (29)
  - doctrine consistent across chapters (30)
  - varied rhythm (31)
- **Applied:** Ch 2 rewritten as v2; Ch 3 revised; the prologue and Ch 1 got only the mechanical changes (honorifics, Oxford commas, chapter numbers in words). The Sheikh-mention cut in the approved prologue and Ch 1 awaits the user's go-ahead.
- **Content decisions in Ch 2 v2:**
  - "False hunger" is kept as the Sheikh's point, made precise: the felt state cannot be mistaken; only conclusions drawn from it can (L02 ¶31–32).
  - The light-in-the-heart tension is reconciled with `forty_hadith` p. 331 ("no niggardliness in the higher realms") and Q 2:282.
  - The Ibn Sina box is now the held story (`light` p. 29) with its point: an argument cannot take the place of deeds.
  - The unsourced line "knowledge comes from the Imam" (L03 ¶11) is dropped (D39).

## 2026-10-16: D43. Round 2 of the user's Ch 2/3 review; Ch 1 attributions trimmed
- **Ch 1:** the Sheikh is named 9 times instead of 18, and the "he says" lines are gone (8 to 0); only attributions changed. **The prologue stays as it is** (user).
- **Ch 2 fixes:**
  - the false-hunger point is made in two plain sentences;
  - "whereas" replaces semicolons in contrasts;
  - no mic-drop endings;
  - Ibn Sina: the reality of things is beyond the reach of human *reason*;
  - negative knowledge is phrased so that nothing is "removed" from God;
  - the Mulla Sadra box now explains the Peripatetic and transcendent schools in plain English (L09 ¶70–71; L03 ¶28; `light` pp. 35, 40, 42; `kernel` p. 7);
  - the hadith/verse tension on the light is stated and then resolved (rule 37);
  - "quatrain" is glossed.
- **Ch 3 fixes:** "physical eyes" vs "the eye of the heart"; "whereas"; the closing sentence of the conclusion made clearer; "Abu Hamza" used throughout. The only "Abi Hamzah" was inside Mutahhari's quotation, which is now paraphrased with just its key phrase quoted.
- **Inline Arabic:** set in an isolated box at body size with fixed line edges, so it no longer opens up the line spacing or reorders the brackets and footnote marks around it.
- **TONE rules 32–37:**
  - no mic-drop endings (32)
  - theological care (33)
  - explain technical ideas in plain English, with brief bracketed glosses (34)
  - "whereas" for contrasts (35)
  - fine points in short clean sentences (36)
  - state an apparent contradiction, then resolve it (37)

## 2026-10-16: D44. Voice test rebuilt and calibrated; chain audit added
- **Why:** the user asked for a good voice test that can be iterated. The v1 blind test passed every chapter, including Ch 2 v1, which he rejected; its control check passed on content (near-twin passages), not voice.
- **Calibration** (41 judge runs; `reviews/voice/CALIBRATION.md`), against a fixed corpus of his approved text and the drafts he rejected:
  - the **profile** separates the hard negatives and stays the gate;
  - the **blind judge** cannot separate approved from rejected (AUC 0.43–0.47 over three designs), so it is now advisory and optional;
  - the new **chain audit** (each paragraph labelled against its section's point by a fresh Fable `chain-auditor`) is repeatable and gives specific cuts, but rates Ch 1 and Ch 2 v1 alike; it is used as an edit list with a ceiling at Ch 1's level (28% idle paragraphs).
- **Author A** is the prologue and Ch 1 as last approved (D43, `74fea4c`), snapshotted in `reviews/voice/corpus/`; the `32e44c9` freeze fails today's profile.
- **The user's reviews are the labels:** predictions are recorded before he reads (`reviews/voice/PREDICTIONS-ch02-07.md`) and scored against his feedback; a test stays only if it predicts it (`docs/VOICE-TEST.md`).

## 2026-10-16: D45. The user's review of Parts One and Two: point ladders and plain sentences; Ch 2–7 rebuilt
- **The user stopped reading in Ch 4:** points not clear or punchy, sentences hard to read, the opening re-labouring earlier chapters. Rules added: TONE 26 (callbacks one or two sentences, no chapter tour), 38 (plain sentences; profile gates "read twice" sentences at 9%), 39 (open on the title's words), 40 (point ladder: one short section point plus one short step per paragraph, in the `::: {.point}` note), 41 (always say which Imam), 42 (Arabic glosses in brackets), 43 (several scholars only for nuanced points), 44 (idle paragraphs 15–28%). LESSONS 22–26.
- **The three tests (user):** profile = gate; blind judge = run in the pre-review stage, act on its fair tells, Ch 1 included; chain audit = ceiling 28% (Ch 1's level), floor 15% (the user: roughly one paragraph in four can recap; too few reads breathless). Keep: a short end-of-chapter recap; the closing page-turner question; a second or third scholar on a nuanced point.
- **Ch 1:** the "For the muqarrabun, the terms are entirely different…" line stays (user). Four small edits from the blind judges' repeated tells (tidy closer, restated line, "the real thing", the staged "Then:").
- **Part pages:** equal space above and below the chapter list. Part Two's line names "the Imams (as)" (L14 ¶8–10 means the line of Imams, confirmed by the fact-check).
- **Pipeline run (2026-10-16):** Opus rebuild on a point ladder (Ch 4–7) or light revision (Ch 2–3) → Fable logic/structure review → edits → profile, chain audit, blind judges → fact-check → fixes.
- **Structural changes from the approved briefs:** Ch 6 drops the islam/iman/ihsan detour and the forty-day-fasting detour as standalone paragraphs (chain audit, 44% idle; the user's "no detours"), and §2 is split in two (Fable: two points in one section). Ch 7 trims the named teachers to five and states the scholars' real difference on when a guide is needed. Ch 4 is short (~1,400 words); both reviewers advised against padding.

## 2026-10-16: D46. The Sheikh's correction: name the Prophet with the Qur'an and the Imams
- **The Sheikh (via the user):** the book "repeats talking about the teachings of the Qur'an and the Imams. There is no mention of the Prophet (s)." His wording: "teachings of the Qur'an, the Prophet, and the Imams from his Ahl al-Bayt".
- **Applied:** all three prologue sentences, and the thesis and B4 lines in ARGUMENT, STORYLINE, FRAMEWORK and part-4. Wherever the book names the sources of ʿirfan, it names the Prophet ﷺ with them.

## 2026-10-16: D47. The Sheikh's stories go in (the user's uncle: "they are the best bit")
- **Audit** (`reviews/stories-audit.md`): the Sheikh tells 61 stories; Ch 0–7 told only 2 (neither in his telling), 3 as allusions; most were cut early for want of a printed source.
- **Rule (user):** every chapter carries at least one of the Sheikh's own stories, told in full, where it carries a section's point and meets the quality mark (clear in the transcript, not a joke, not garbled). A story from the lectures needs no printed source: it is told as the Sheikh's account ("Sheikh Bahmanpour tells…"), in a `::: {.box-story}` box or a short prose paragraph. Stories whose point is a joke, and those too garbled to retell, stay out (D39).
- **Now:** stories added to Ch 1–7 where they hit the mark (Ch 3 and 4 included, user); each addition marked in the draft's point notes. Ch 1 additions are shown to the user before they are kept.
- **Next:** the Part Three briefs plan a told story per chapter; the Part Four and Five outlines are revised to match.
- **Second screen (user, 16 Oct):** the Ch 4 Musa box is kept. "Add in others if they are both high quality and nicely relevant. If not, leave them." Eighteen untold stories were screened against the transcripts (`reviews/stories-screen.md`). Added to the outlines: Hatim "the Deaf" (Ch 9.3), the Sheikh finding Tabatabaʾi in Ibn ʿArabi (Ch 14.2), and the Prophet's prayer at the Miʿraj (Ch 12 opener, only if its hadith is found in a held source). Left: Rabiʿa's twelve years without dates (the Sheikh doubts it; Ch 11 already tells her torch) and fourteen others (not a real story, garbled, political or sectarian, a powers story, or a point already made). No new story fits Ch 1–7. The two-per-chapter cap becomes a default; a third goes in only where it clearly earns its place.

## 2026-10-18: D48. The point ladder is a proof (user)
- **Rule:** every chapter's ladder reads like a maths proof (TONE 40a, LESSONS 28): each step follows only from earlier ones and uses their words; section points chain into the chapter point; explanations needed before an argument are nested steps (2a, 2b…) and the reader is told what is coming. The same style runs at book level: one line per chapter, chaining through B1–B5 to the thesis (`docs/ladders/00-book-chain.md`).
- **Chapter Five:** the proof ladder is accepted (`docs/ladders/05.md`); the rewrite waits for the go.
- **All written chapters:** ladders and change lists in `docs/ladders/NN.md`; Chapters One to Four change only with the user's line-by-line approval.
- **Story sources** (`reviews/story-sources.md`): (1) every story stays told as the Sheikh's account; (2) a citation is added where a held book or a page-checked classical source tells the same story; (3) every "Likely" source is checked on the page in the fact-check stage. Where a source's version differs from the Sheikh's, the user decides case by case later (not "follow the Sheikh" by default).
- **Layout:** chapters start on the next page, not the next right-hand page (no blank pages between chapters).

## 2026-10-18/19: D49. Punctuation and sentence shape (user)
- The user's style profile, discussed rule by rule, is TONE 45: colons sparingly (about one per paragraph); semicolons only between two full sentences of equal weight, or in heavy lists; no echo or long phrase hung on a sentence's last comma (fix by fold, which-clause or participle, semicolon, own sentence, colon rarely); an Oxford comma and an "and" on every list; one vivid word welcome ("living realm"), echo phrases not; a fronted phrase now and then for variety, under a strict bar; no dashes; plain diction.
- `voice.py punct` (and every `profile`) flags the sentences; writers fix or keep each before replying, editors check it. A one-off sweep applied it to the prologue and Chapters One to Seven; future chapters need no sweep.
- Chapter Five's opening is approved (19 Oct). Chapter One opens "At many weddings, someone recites a verse most of us know."


## 2026-10-19: D50. Part Three is one stage per chapter (user)
The user could not see how the two parts, four stages, five disciplines and repentance fitted together. After a Fable review (`reviews/part3-framework-fable-2026-10-19.md`), Part Three is rebuilt as a map and four stages:
- Ch 8 is the map: four stages, two ours (polishing, emptying) and two God's (adornment, passing away), in a fixed order, none dropped; a table "The road at a glance".
- Ch 9 = Stage 1, polishing (repentance, the law, people first); Ch 10 = Stage 2, emptying (the five disciplines are its tools); Ch 11 = Stage 3, adornment (God's gifts, among them love); Ch 12 = Stage 4, passing away and the sober return.
- Chapter titles show the stage: "Polishing: setting out", "Emptying: the five disciplines", "Adorning: love as the engine", "Passing away: losing the self, finding God". Ch 8 keeps "The stages of the journey".
- Two fidelity cautions kept in the prose: placing the five disciplines in emptying is the book's synthesis (they are recommended acts aimed at the heart); love is among the gifts of adornment, not the whole of it.
- Ch 12's point: "seeing only God" → "seeing God in all things while remaining oneself" (held sources: `kernel` p. 60, `light` pp. 57, 63, `forty_hadith` pp. 515–516, `inner_secrets` p. 116).
- Ch 8 carries no told story: none fits the map; the Sheikh's swimming image goes to Ch 10 §1.
- The Miʿraj prayer story (#26) stays out (no held source).
- (user, 2026-10-19) Stage 3 is named "adorning", so the four stage names match: polishing, emptying, adorning, passing away. Ch 11 title: "Adorning: love as the engine". Plain "adornment" may stay where a sentence needs a noun ("the soul's adornment").
- (user, 2026-10-19) Ch 11 title: "Adorning: love as the engine" (no comma; keeps the meaning that love drives the traveller).
- (user, 2026-10-19) Stage 4 is named "annihilating" (noun "annihilation", the held translations' word for *fanaʾ*), so the stage names read polishing, emptying, adorning, annihilating. Ch 12 title: "Annihilating: losing the self, finding God"; file `12-annihilating.md`.

## 2026-10-19: D51. Less mechanical prose (user)
A blind judge rated the book's passages 54–78 for AI-likeness (anchor text 84; human controls 4), the approved exemplar as high as the new chapters (`reviews/ai/REPORT-2026-10-19.md`). The user chose line by line from sixteen examples (`reviews/ai/examples-2026-10-19.md`): yes to 1b (paraphrased), 2a, 3a, 3b, 5b, 6 (reworked), 7a, 7b, 8a, 8b; no to 1a, 2b, 4a, 4b, 5a. Rules in TONE 46 and LESSONS 33. Applied to Part Three; a sweep of the rest of Part Three is proposed for approval.
