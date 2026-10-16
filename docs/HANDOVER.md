# Handover to a new session (2026-10-12)

_Read this first, then `CLAUDE.md`, `docs/STATUS.md` and `docs/EXEMPLAR.md`. Work up to D36 is on branch `claude/stoic-euler-p7myev`; D37 onwards (voice gate, structure v3, Part One drafts) is on `claude/zealous-edison-mh1dpk`, which contains all of it. Plan the book from `docs/outline/` (FRAMEWORK and part files) and ARGUMENT v3._

## 1. Where we are
The prologue and Chapter 1 of Book 2 are finished and approved. The user's uncle, who knows Sheikh Bahmanpour well, read them and was happy for the work to continue as it is. Together they are the written model for the rest of the book (`docs/EXEMPLAR.md`, commit `32e44c9` on this branch). The argument pyramid is approved (`docs/ARGUMENT.md` v2.1, D25–D28). The next task is **Part One: the Chapter 2 and 3 briefs.**

## 2. Agreed since the last handover
- **Credits (D34):** the title page reads "Based on a lecture series by Sheikh M. S. Bahmanpour" and "Edited by Zafar Abbas Juma". "Edited" signals that the book adds no personal opinions. "Adapted from…" and "Curated by…" are still possible alternatives, so ask once.
- **Provenance (D32):** it was a lecture series, which the uncle attended. Never describe it as part of a BA.
- **Spelling (D32):** "Qur'an", "Qur'anic" and "jannah".
- **Voice:** `docs/LINGO.md` (D29), `docs/TONE.md` rules 1–37 (D30, D31, D33, D35), and the exemplar (D36).
- **Point notes (D30):** under every `##` heading in a draft, a `::: {.point}` note states what that section argues. The user reviews the prose against it. Review builds drop the notes.
- **Arabic with every quote:** every Qur'an, hadith or duʿa quotation carries its Arabic in a small font.
  - Qur'an: `::: {.ayah ref="S:A" words="N-M"}` slices the verified text.
  - Hadith and duʿa: `::: {.quote ar="…"}`, with the Arabic copied from a held extract only.
- **Layout:**
  - The verse reference sits at the bottom right.
  - The gap above and below a quote is balanced.
  - Paragraphs have a half-line gap as well as the indent. This is a trial (D35), so confirm it with the user.
- **Readability:** the user found some paragraphs too long. Keep them to 50–65 words, with 110 at most (TONE 22).

## 3. Plan: how to write the rest of the book to the same standard
Work one Part at a time, in this order: Part One (Ch 2–3), Part Two (Ch 4–6), Part Three (7–9), Part Four (10–15), Part Five (16–17), then the epilogue.

For each chapter:
1. **Gate A, the brief.** Write `docs/briefs/NN-case.md` from the template and ARGUMENT.md. Present it to the user as short bullets: conclusion, points, headings, quotes planned, "Try this", hand-off. Wait for approval. The two briefs in a Part can be presented together.
2. **Draft.** Use the `chapter-writer` (Opus or Fable). It reads the exemplar in full first, writes the point notes before the prose, keeps quotes short, puts Arabic with every quote, and paraphrases the Sheikh's informal speech.
3. **Tone pass.** The `tone-editor` agent line-edits the draft against the exemplar and TONE.md. Apply its edits.
3b. **Voice gate (D37, `docs/VOICE-TEST.md`).** Run `build/voice.py profile`, then a blind `voice-judge` run against a rejected-draft control. The chapter goes on only when both pass; failed tells go back to the tone-editor, up to three rounds. Keep the report in `reviews/voice/NN-report.md` and quote the result to the user when sending the PDF.
4. **Fidelity pass.** The `fidelity-checker` (Sonnet) checks quotes, verses, citations and Arabic against the sources. Fix anything high or medium.
5. **The orchestrator reads the draft itself.**
   - Measure paragraph and sentence length against the targets in EXEMPLAR.md.
   - Read each paragraph's first sentence for the links between paragraphs.
   - Build the draft PDF with point notes.
6. **User review.** Send the PDF plus a GitHub raw link (section 6). Apply the feedback. Add any new, repeatable lesson to TONE.md with its before/after. The user often sends voice notes (section 6).
7. **After each Part,** make a review copy for the uncle (`--review`).

Chapter-specific decisions to honour:
- **Ch 4:** seed "travel means removing veils" in a few sentences, pointing forward to Ch 11 (D26).
- **Ch 9:** keeps four points, including 9.4 (D27).
- **Ch 13:** uses Imam ʿAli on remembrance (Nahj 1.219.1) as its "Try this" (D28).
- **Ch 16:** its conclusion follows the lecturer. Tabatabaʾi's view that wilaya is not exclusive sits gently beside it in 16.3 (D25).

## 4. Open items
- **Arabic of Nahj 3.403** (Ch 1, Imam ʿAli on God's special devotees): copy it from the printed Qutbuddin edition, p. 810. The extract's Arabic is garbled. The review build shows the quote in English only.
- ~~QUERY for the Sheikh on "These are shirk"~~: closed by D39 (no questions for the Sheikh). The Ch 1 text quotes his words as said, which is true on either reading, and the marker is removed.
- **Munajat Shaʿbaniyyah epigraph lines:** check each against Mafatih p. 244 before print.
- **Permissions:** permission is needed for every quoted translation before publishing (SOURCES.md).
- **The Sheikh's preferred title and name form:** "Sheikh M. S. Bahmanpour" is used for now.
- **Paragraph spacing:** the trial (D35) is not yet confirmed.
- **Book 1 (Faithful):** parked at the pilot stage. Ask the user whether it is still wanted.

## 5. Key files
| Purpose | File |
|---|---|
| The model to imitate | `docs/EXEMPLAR.md`; `book2/chapters/00-prologue.md`; `book2/chapters/01-seeking-not-powers.md` |
| Voice rules | `docs/TONE.md` (37 rules with before/after); `docs/LINGO.md` |
| Argument | `docs/ARGUMENT.md` v2.1; `docs/STORYLINE.md` (plain-English deck); `docs/briefs/` |
| Decisions | `docs/DECISIONS.md` (D1–D36) |
| Agents | `.claude/agents/`: `chapter-writer`, `tone-editor`, `fidelity-checker`, `transcript-analyst` |
| Advice to the user on steering tone | `docs/TONE-GUIDANCE.md` |

## 6. Working notes
- **Builds:**
  - Draft with point notes: `python3 build/build.py pdf book2 "0[01]*"` → `samples/prologue-and-ch01.pdf`
  - Clean reader copy: `… --review` → `samples/prologue-and-ch01-review.pdf`
  - Requires `pip install typst`.
- **Mobile downloads:** the user can't download files sent in chat on mobile. Commit the PDF and give the raw link: `https://github.com/Baby-Isa/Irfan-Books/raw/<current branch>/samples/<file>.pdf`.
- **Voice notes (.m4a):** Hugging Face is blocked by the network policy. To transcribe:
  1. `pip install sherpa-onnx soundfile`.
  2. Download `https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-small.en.tar.bz2` and `…/asr-models/silero_vad.onnx` from GitHub.
  3. Convert the audio with `ffmpeg -ar 16000 -ac 1`.
  4. Run Whisper with VAD segmentation. Expect some garbling, and confirm unclear points with the user.
- **Reporting:** lead with the conclusion, use short bullets, and quote changed lines in full so the user can check them without opening the file.
- **Commits:** commit and push after each unit of work. Don't open a PR unless asked.
