# The voice test: does a new chapter read as the same author? (D37)

_Every Book 2 chapter must pass this test before the user sees it. It runs after the tone-editor pass and before the fidelity check. The tool is `build/voice.py`; the blind judge is the `voice-judge` agent._

## Why two tests
The tone-editor applies the rules in TONE.md and LINGO.md. A chapter can obey every rule and still read as a different writer, so the test asks a separate question: could a careful reader tell that this chapter was not written by the author of the prologue and Chapter 1? That question has two parts, and each test answers one.

1. **The profile (measured).** `python3 build/voice.py profile <chapter>` measures the chapter against the exemplar (commit `32e44c9`):
   - words per paragraph and per sentence, the longest paragraph, and the share of sentences over 30 words
   - the rate of "and", "but/yet", semicolons, colons, dashes, brackets, questions, "you", "we/us/our", "let's", "this/these", and commas per sentence
   - banned lingo, intensifiers, wordy constructions, bad sentence openers and the TONE.md check words, ignoring words inside quotations
   - Burrows' Delta on function words, the standard measure in authorship attribution.

   Each figure is compared with its spread across the exemplar's own ~180-word chunks. **OFF** means at least 2 standard deviations away from what the exemplar's author does; **drift** means 1–2. The profile fails on any OFF figure, any lingo hit, or any paragraph over 115 words. (TONE 22 sets 110 as the target; the exemplar's own longest paragraph is 114.)

2. **The blind judge (read).** `python3 build/voice.py blind NN <chapter>` builds an anonymised packet:
   - **Reference, "Author A":** the prologue and Ch 1 sections 1–3.
   - **12 test passages, shuffled:** 4 held-out passages from Ch 1 sections 4–8 (the real author), 4 from the new chapter, and 4 from a **control**, a Ch 1 draft the user rejected (commit `7225b76`, before D29).
   - Quotations show as `[verse]` or `[quotation]`; point notes, citations and markers are removed.

   A fresh `voice-judge` agent, which has seen neither the chapter nor the key, marks each passage "same hand" or "different hand" and quotes the tells. `python3 build/voice.py score NN` scores the answers against the key.
   - **Valid** only if the judge catches at least 3 of the 4 control passages. A judge who cannot spot the rejected drafts proves nothing, so the run is repeated with a fresh judge.
   - **Pass** if the chapter's passages are flagged no more often than the exemplar's own passages in the same run (the judge's false alarms). There is no free allowance.
   - Whatever the verdict, every tell quoted against a chapter passage goes to the tone-editor, unless the same kind of tell was also raised against the real author in that run (the score prints those false alarms so they can be discounted).

The control is what makes the test rigorous. The control drafts are on the same subject as the exemplar, so a judge who catches them is reading voice, not topic.

## Calibration (2026-10-12)
The test was run on the exemplar and on the drafts the user rejected, to check that it can tell them apart. Raw files: `reviews/voice/cal1-*`, `reviews/voice/cal2-*`.

**Profile:**

| Text | Verdict | Why |
|---|---|---|
| Prologue (exemplar) | PASS | |
| Ch 1 (exemplar) | PASS | |
| Ch 1, `7225b76` (v3, pre-D29) | REWRITE | longest paragraph 143; "you" OFF; And/But openers OFF; 8 lingo hits |
| Ch 1, `5856b3c` (D29) | REWRITE | paragraph 118; "you" OFF; "fair enough" |
| Ch 1, `3d038c5` (D30) | REWRITE | paragraph 144; "you" OFF; "fair enough", "of course", "we shall" |
| Ch 1, `9ed0c2b` (D31, round 3) | REWRITE | paragraph 145; "fair enough", "of course" |
| Prologue, `9d02329` (first draft) | REWRITE | paragraph 159; "you" and questions OFF; "rarely", "intelligent", "busy" |
| Prologue, `3d038c5` (D30) | REWRITE | "you" OFF (7.5 sd); "as we should", "rarely" |

**Blind judge (two fresh Opus judges; 4 passages per source):**

| Run | Candidate | Control caught | Exemplar false alarms | Candidate flagged | Verdict |
|---|---|---|---|---|---|
| cal1 | `9ed0c2b` (round 3, close to final) | 4/4 | 2/4 | 0/4 | PASS |
| cal2 | `3d038c5` (D30) | 4/4 | 0/4 | 1/4 | REWRITE |

**What this shows:**
- The judge catches a clearly different hand every time: 8 of 8 control passages.
- It sometimes flags the real author (2 of 8), so a single judge is noisy. That is why the pass mark is set against the same run's false alarms, not against zero.
- Drafts that are close to the final text get past the judge but not the profile. A chapter must pass **both**.
- Function-word Delta does not separate the drafts from the exemplar out of sample (median 0.88–0.91 against the exemplar's own 0.89), because the reference is only about 3,300 words. It is reported but is not a gate.
- In the first run, the spelling "Quran" for "Qur'an" gave the control away; the packet now normalises spelling.
- **House style is normalised in every passage (2026-10-13).** In round 2 for Ch 2 and Ch 3, the judges' strongest tells were conventions the user adopted after the exemplar was frozen: chapter numbers in words, the Oxford comma and "(as)" (D42). They were reading style, not voice. Every passage, the reference included, now passes through `house_style()`, which applies the current conventions, before the judge sees it. The round-2 runs are recorded but not counted. In round 3 the comma rule added commas heuristically and created a false "comma before a pair" habit, so from round 4 every comma before "and"/"or" is stripped from every passage alike.

**The tells the judges used most** (for writers and the tone-editor):
- a claim, a colon and a quotation stacked in one sentence (TONE 15)
- a tidy or balanced closing line ("It describes them as believers.")
- sentences opening with "And", "But" or "Hence"; inverted openings ("Higher still is…")
- commenting on the manner of a quotation ("He puts it bluntly:")

The profile now also measures "And/But" openers and colon-then-quote.

## The rewrite loop
1. Run the profile. Fix every OFF figure and lingo hit.
2. Build the packet and run a fresh `voice-judge`.
3. If the verdict is REWRITE, the judge's quoted tells go to the tone-editor as line edits. Apply them, then rebuild with `--round 2`, which samples different passages, and run a new judge.
4. If round 3 still fails, stop. Send the user the draft with the remaining tells listed, and ask which they agree with. A tell they reject is noted in TONE.md as acceptable.
5. Record each run in `reviews/voice/NN-report.md`: the profile table, the score, and the tells acted on.

Repeated tells across chapters become TONE.md rules, with the before/after taken from the judge's quotes.
