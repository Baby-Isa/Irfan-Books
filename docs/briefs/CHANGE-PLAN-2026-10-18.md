# Change plan: proof ladders in every written chapter (D48)

_Ready to execute once the user approves each chapter's change list. Nothing below has been applied yet._

## What the user approves
| Chapter | Ladder and change list | Changes | Kind |
|---|---|---|---|
| Book chain | `docs/ladders/00-book-chain.md` | one-line chapter points, B1–B5, thesis | wording of ARGUMENT/STORYLINE |
| 1 More than the minimum | `docs/ladders/01.md` | 6 (5 small edits + notes) | edits |
| 2 Knowing about God is not knowing Him | `docs/ladders/02.md` | 4 | edits |
| 3 You already know these words | `docs/ladders/03.md` | 5 | edits |
| 4 Know yourself, know your Lord | `docs/ladders/04.md` | 6 | edits |
| 5 The soul and its worlds | `docs/ladders/05.md` (accepted) | restructure | full rewrite |
| 6 No path outside the law | `docs/ladders/06.md` | 7 | edits |
| 7 Finding a guide | `docs/ladders/07.md` | 6 | edits |

## Steps, in order
1. **Book chain.** On approval, put the one-line chapter points into `docs/ARGUMENT.md` (each chapter's **Conclusion**) and `docs/STORYLINE.md`; check that the prologue's map of the book (Ch 0) still matches, and list any line that needs changing for approval.
2. **Point notes (all seven chapters).** Replace each `::: {.point}` note with its section's ladder from `docs/ladders/NN.md` (point, then numbered steps with nested a/b/c; story boxes as italic notes). Check the draft PDF renders nested lists in the note. Orchestrator, by script.
3. **Edits, Chapters 1–4, 6, 7.** Apply exactly the approved before → after changes, nothing else. Orchestrator, by script with exact-match asserts. Then `voice.py profile` on each (the gate must still pass).
4. **Chapter Five rewrite.** `chapter-writer` (Opus) rewrites the prose on `docs/ladders/05.md`, keeping every citation, quotation, box and story; 2,800–3,600 body words. Then Fable review (`reviews/fable/REVIEW-BRIEF.md`, adding TONE 40a), apply, then the three tests (profile, chain audit 15–28%, blind judge), and the fidelity check.
5. **Chain audit** on Chapters 6 and 7 (the two with a structural edit) to confirm the idle share stays 15–28%.
6. **Build** `samples/parts-one-two-v3.pdf` (draft, red ladders) and `-review.pdf` (clean), with chapters starting on the next page (template changed 18 Oct); send raw links.
7. **Docs.** STATUS, HANDOVER; `docs/briefs/_TEMPLATE.md` gains the proof-ladder form so the Part Three briefs (Ch 8–12) are written in it from the start.

## Cost
Steps 1–3, 5–7: orchestrator work, small. Step 4: one Opus rewrite, one Fable review, one chain audit (Fable), one blind judge (Opus), one fidelity check (Sonnet).

## Open with the user
- The Chapter One story box ("What was enough for jannah"): kept or not.
- Story-source differences: case by case, later (D48).
