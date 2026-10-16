# The voice and chain tests (D37, revised D44)

_Every Book 2 chapter runs these after the tone-editor pass and before the fidelity check. Tools: `build/voice.py`; agents: `voice-judge` (blind authorship) and `chain-auditor` (chain audit). Calibration evidence: `reviews/voice/CALIBRATION.md`._

## What each test is for, and what calibration showed it can do
A test is only worth running if it tells the user's approved prose apart from the drafts he rejected. Calibration (2026-10-16, 41 judge runs) measured this for each test against a fixed corpus (`reviews/voice/corpus/`): Author A is the prologue and Ch 1 as last approved (D43, commit `74fea4c`); the known negatives are the drafts he rejected (Ch 1 `7225b76` and `3d038c5`, prologue `9d02329`, Ch 2 and 3 v1 `2d8143e`, Ch 2 and 3 v2 `19a7da7`).

| Test | Role | Separates approved from rejected? |
|---|---|---|
| 1. Profile (measured) | **Gate** | Yes, for the hard negatives: it fails every v1 and early draft (attribution rate, paragraph length, "you", openers, lingo) and passes the approved text. It cannot see meandering: the v2 drafts pass. |
| 2. Chain audit (editor) | **Edit list, with a ceiling** | Not on its own: Ch 1 scores 22–28% idle paragraphs, Ch 2 v1 22–25%. Repeat runs agree (±3 paragraphs) and its cuts are specific, so it drives the edit. |
| 3. Blind judge (authorship) | **Advisory, optional** | No. Across three designs and 24 judges, held-out Author A and rejected drafts scored alike (AUC 0.43–0.47; 0.5 is chance). The judges' tells are sound but fire as often on Author A. |

The old blind test (v1) passed every chapter, including Ch 2 v1, which the user rejected. Its control check was passing on content: judges caught 28 of 30 control passages that had a near-twin among Author A's passages, but only 32 of 46 without one.

## 1. Profile (gate)
`python3 build/voice.py profile <chapter>` measures the chapter against Author A's ~180-word chunks: words per paragraph and sentence, the longest paragraph, long sentences, the rate of "and", "but/yet", semicolons, colons, dashes, brackets, questions, "you", "we", "let's", "this/these", commas per sentence, And/But openers, colon-then-quote; banned lingo, intensifiers, wordy phrases, bad openers and TONE check words outside quotations; the Sheikh named more than 5 times per 1,000 words (TONE 23). **OFF** = 2+ standard deviations from Author A. The chapter fails on any OFF figure, any hit, or a paragraph over 115 words. Function-word Delta is reported, not gated.

## 2. Chain audit (edit list)
`python3 build/voice.py chain NN-x <chapter>` writes `reviews/voice/NN-x-chain-packet.md`: each section's point note, then its paragraphs numbered ¶1… A fresh `chain-auditor` (Fable) labels every paragraph `advance`, `support`, `restate` or `aside` against its section's point. `python3 build/voice.py chainscore NN-x` prints the counts.
- **Ceiling:** idle paragraphs (restate + aside) no higher than Ch 1's own share under the same judge, 28% (two runs: 22% and 28%). Above that, cut or rework until under it.
- **Below the ceiling,** read every flagged paragraph and either cut it or keep it with a one-line reason in the chapter report. The audit is stricter than the user: he approved Ch 1 with about a quarter of its paragraphs flagged.
- Patterns it flags in every draft so far: a second or third scholar saying what the first said; a chapter-end summary paragraph that restates the section points; a closing question the chapter does not answer.

## 3. Blind judge (advisory)
`python3 build/voice.py blind NN <chapter> [--judges opus,fable,opus] [--round R]` writes one packet per judge (`NN-jK-packet.md`): Author A's reference (prologue and Ch 1 §1–3), then shuffled passages from Ch 1 §4–8 (held out), the chapter, and the control drafts, with no passage a near-twin of any other (4-gram overlap ≤ 10%). Judges rate each passage 0–100 and quote tells; `score NN` reports AUC per judge and a bootstrap interval. Run it only for a new kind of chapter or when re-calibrating; act on its tells only where the same kind of tell was not also raised against Author A in that run.

## The loop that makes the tests better
The tests are only as good as their labels, and the user's reviews are the labels.
1. **Before** the user reads a chapter, record the chain audit's flagged paragraphs (as in `reviews/voice/PREDICTIONS-ch02-07.md`).
2. When his feedback arrives, mark each prediction **hit** or **miss**, and list what he criticised that was not predicted. Report precision and recall.
3. Add what he rejected to the corpus as negatives (and what he approves as Author A), re-run `CALIBRATION.md`'s runs, and keep a test only if it separates the two.
4. A tell that keeps predicting his comments becomes a profile check (measurable) or a TONE rule.

## Rules learned in calibration (keep)
- Author A is the exemplar **as last approved**, not the first freeze: the `32e44c9` text names the Sheikh 8.1 times per 1,000 words and fails today's profile.
- The prologue cannot stand in for chapter prose: judges flag its book-about-the-book passages as a different hand.
- Normalise house style (spelling, honorifics, quote marks, commas before "and"/"or") in every passage, or judges read conventions instead of voice.
- Agent definitions load at session start; a changed judge prompt must be passed in the task prompt until the next session.
