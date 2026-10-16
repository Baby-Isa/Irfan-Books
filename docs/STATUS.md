# Status

_Update at the end of every task. Keep it short. History lives in git and DECISIONS.md._

## Current phase
**Phase 5, chapter production.** Every chapter goes through two gates (D22):
- **Gate A:** case brief, approved by the user.
- **Gate B:** prose, then the fact-check, then the PDF.

**Now:** Prologue and Ch 1 (Book 2) approved by the user and his uncle, and frozen as the exemplar (D36, commit `32e44c9`). See `docs/HANDOVER.md`.

**Now (2026-10-13):** Ch 2 rewritten (v2) and Ch 3 revised after the user's first review (D42), with a Fable edit and a fidelity check; voice gate re-run with house-style normalisation. PDFs: `samples/part-one.pdf`, `samples/part-one-review.pdf`. Awaiting the user's read of Ch 2–3.

**2026-10-16:** Ch 2 and Ch 3 tightened after the user said they still meander next to the prologue and Ch 1 (Ch 2 body 2,024 → 1,826 words; Ch 3 1,739 → 1,576). Cuts: the light/hadith contradiction resolved once instead of twice (Ch 2), the Mutahhari contrast and Khomeini order sentence in "The path is purification" (Ch 2), the Mutahhari "sublime ideas" paragraph (Ch 3), restated conclusions and quote paraphrases. Voice profile PASS on both.

**2026-10-16, Part Two drafted (Ch 4–7).** Pipeline per chapter: brief (`docs/briefs/04`–`07-case.md`, from `docs/outline/part-2.md`) → Opus draft → Fable structural edit with each section's point → own read-through against `docs/briefs/LESSONS.md` → voice profile and blind judge → fact-check (`reviews/book2-04`–`07.md`), Medium items fixed. Voice: all four profiles PASS; blind PASS for 04 (0/4 flagged), 05 (1/4, false alarms 1/4), 06 (0/4), 07 (0/4). Ch 2/3 tightening fact-checked (`reviews/book2-02-03-tighten.md`) and fixed; Ch 2 blind rounds 7–8 invalid (judges missed the control), last valid round r5 PASS (see `reviews/voice/02-report.md`). PDFs: `samples/parts-one-two.pdf`, `samples/parts-one-two-review.pdf`.

**Next:** the user's read of Part Two (and of the tightened Ch 2–3); then the Part Three briefs (Ch 8–12). Open: Ch 7 names 7 teachers in prose (guideline 5); [VERIFY] Arabic in Ch 6 (Kubra image; the Prophet's grateful-servant reply) and Ch 7 (ʿIsa's saying) need printed editions.


**2026-10-16, voice test rebuilt (D44).** The user asked for a good, improvable voice test. Calibrated against his approved text and the drafts he rejected (`reviews/voice/CALIBRATION.md`, 41 judge runs): the profile stays the gate; the blind judge cannot separate approved from rejected and is now advisory; a new chain audit (Fable labels each paragraph against its section's point) is the edit list, ceiling 28% idle paragraphs (Ch 1's level). Author A is now the D43 text. Predictions for Ch 2–7 recorded before the user's feedback (`reviews/voice/PREDICTIONS-ch02-07.md`): Ch 6 (44% idle) and Ch 3 (32%) most at risk. Branch `claude/irfan-books-part-three-kh8nd2` (based on `claude/zealous-edison-mh1dpk`).

**2026-10-16, Parts One and Two rebuilt after the user's review (D45).** The user stopped reading in Ch 4 (points unclear, sentences hard to read, slow opening). New rules TONE 26, 38–44 and LESSONS 22–26: point ladders (one short section point + one step per paragraph, shown in the draft PDF's point notes), plain sentences (profile gates "read twice" sentences at 9%), title-word openings, which Imam, bracket glosses, scholars only for nuanced points, idle paragraphs 15–28%. Ch 4–7 rebuilt (Opus) and Ch 2–3 revised, each then: Fable logic/structure review → edits → profile, chain audit, blind judges → fact-check → fixes → verification of the fixes (`reviews/fix-verify-2026-10-16.md`, no High). Ch 1: four small judge-led edits. Part pages: equal spacing; Part Two names "the Imams (as)". Final chain audits: Ch 2 21%, 3 15%, 4 22%, 5 18%, 6 19%, 7 16% idle (all in band); all profiles PASS. PDFs: `samples/parts-one-two-v2.pdf` (draft with ladders), `samples/parts-one-two-v2-review.pdf`. Predictions for the next read: `reviews/voice/PREDICTIONS-v2-ch02-07.md`.

**2026-10-16, the Sheikh's correction (D46) and stories (D47).** The prologue names the Prophet with the Qur'an and the Imams. Eight of the Sheikh's stories added to Ch 1–7 (one per chapter, two in Ch 5), each Fable-reviewed and fact-checked against its transcript; marked "New story (D47)" in the draft's point notes; the Ch 1 story awaits the user's approval. Parts 3–5 outlines now plan a told story in every chapter. The user kept the Ch 4 Musa box; a second screen added three more to the outlines (Hatim, Ch 9.3; Tabatabaʾi in Ibn ʿArabi, Ch 14.2; the Miʿraj prayer, Ch 12 opener, if sourced): 25 of the 61 now told or planned in full. Glossary: six story terms added.

**Next:** the user's read of `parts-one-two-v2`; score the v2 predictions; then the Part Three briefs (Ch 8–12) with point ladders (brief template updated).

## Open questions for the user or lecturer
1. The lecturer is M. S. Bahmanpour (from the slides). Confirm his preferred title and name format.
2. **The class slides and hand-outs.** The lectures refer to slides, a "chart" of the branches, an Ibn Sina hand-out, a Miʿraj hand-out and a Chodkiewicz hand-out. Do these still exist?
3. **Missing sessions?**
   - L01 refers back to an earlier talk on the four categories of muqarrabun.
   - L15 says "two sessions left" and promises to continue the Ibn Sina text, but L16 covers a different topic.
   - L14 promises a "Shia tariqa" talk that never appears.

   Were there sessions that weren't transcribed?
4. ~~Quran translation~~: decided, Qaraʾi (Tanzil).

## Source review findings (sources/maps/)
- **Sahifa:** the lecture's Whispered Prayer of the Lovers lines match Chittick (pp. 656–657). "Heart burn with the love of seeking you" (L01 ¶31) is not in it, so it needs a QUERY.
- **Mafatih:** the du'as are **Arabic only**, so an English source for the du'as is still needed.
  - Munajat Shaʿbaniyyah: 8 of the 9 lines match (p. 244). Mafatih attributes it to Imam ʿAli and the Imams, not to Zayn al-ʿAbidin, so it needs a QUERY.
  - Dhu'l-Qaʿdah rite: Mafatih says 100 istighfar (the lecture says 70) and adds al-Falaq.
- **Nahj (Qutbuddin numbering):**
  - "Sermon 432" = saying 3.403.
  - Hammam = 1.191.
  - 11 of the lecture citations are located. 3 are NOT FOUND (L10 small constant deed, L12 concealing zuhd, L11 "full of love").

## Lectures → notes
All 16 sets of notes are done (`notes/Irfan01–16.md`, about 76k words in total). Several flag garbled passages and mis-numbered verses in section 7. They have not been human-checked.

## Chapters
| Ch | Book 1 | Book 2 | Fidelity check | Typeset |
|---|---|---|---|---|
| 1 | ☑ draft (pilot, `book1/chapters/01-seeking-not-powers.md`; revised after `reviews/book1-01.md`; 16 ayah blocks; 19 VERIFY, 7 QUERY, 2 GAP) | ☑ v3 (rewritten on brief v3; ~3.4k body + 0.35k in 3 boxes; 1 QUERY on \"these are shirk\") | ☑ `reviews/book2-01-v3.md` | ☑ `samples/ch01-seeking-not-powers.pdf` |
| 2–17 | ☐ | ☐ | ☐ | ☐ |
| B2 A, B, C | n/a | ☐ | ☐ | ☐ |
