# Voice-test calibration, 2026-10-16 (D44)

Question: does each test tell the user's approved prose from the drafts he rejected? Corpus: `corpus/A-*.md` (Author A, as last approved, `74fea4c`), `corpus/Z-*.md` (the older `32e44c9` freeze), `corpus/X-*.md` (rejected drafts). AUC = chance that a random Author A passage is rated above a random other passage; 0.5 is chance, 1.0 perfect.

## Blind judge (24 runs; 4 judges each, 2 Opus and 2 Fable)
| Run | Author A | Candidate | Prompt | Passages | Validity AUC (A > control) | A > candidate |
|---|---|---|---|---|---|---|
| calneg (it. 0) | 32e44c9, folds A+B | Ch 2 v1 | v1 (same/different) | 120–260 w | 0.23 | 0.14 |
| calpos (it. 0) | 32e44c9, Ch 1 §0–3 only | prologue (true author) | v1 | 120–260 w | 0.41 | 0.86 (wrongly flags the true author) |
| calneg2 (it. 1) | 32e44c9, fold A | Ch 2 v1 | v2 (profile first, 0–100) | 120–260 w | 0.44 | 0.27 |
| calneg3 (it. 1) | 32e44c9, fold A | Ch 2 v1 | v3 (rejected-draft framing) | 200–340 w | 0.47 | 0.44 |
| calneg4 (it. 2) | 74fea4c, fold A | Ch 2 v1 | v3 | 200–340 w | 0.45 | 0.43 |
| calneg5 (it. 2) | 74fea4c, fold A | Ch 2 v2 | v3 | 200–340 w | 0.47 | 0.33 |

Findings:
- No design separates Author A from rejected drafts. Judges raise each kind of tell (restating, "he says" filler, stacked quotations, tidy closers, idle asides, drama) at about the same rate against Author A (11–27% of passages per kind) as against the drafts (8–24%).
- The prologue as held-out text (fold B, calpos) is flagged for its front-matter register: unusable as a stand-in for chapter prose.
- The 32e44c9 freeze contains habits the user later cut (8 "he says", the Sheikh named 8.1 per 1,000 words). Author A is now the D43 text.
- v1 history (`02`–`07`, `cal1`–`cal2`): controls with a near-twin among Author A's passages were caught 28/30, without one 32/46. Chapters were flagged 10/76, Author A 9/76: every chapter passed, Ch 2 v1 included.

## Profile
Fails Ch 1 `7225b76`, `3d038c5`, prologue `9d02329`, Ch 2 v1, Ch 3 v1 (attribution rate, long paragraphs, "you", openers, lingo); passes Author A, Ch 2 v2, Ch 3 v2 and the current Ch 2–7. It separates the hard negatives, not the meandering ones.

## Chain audit (13 Fable runs; `chain-calibration.txt`)
| Text | Status | Idle paragraphs (restate + aside) |
|---|---|---|
| Ch 1 (two runs) | approved | 28%, 22% |
| Ch 2 v1 (two runs) | rejected (rewritten) | 22%, 25% |
| Ch 2 v2 | criticised: meanders | 27% |
| Ch 2 current | awaiting review | 24% |
| Ch 3 v1 | revised after review | 28% |
| Ch 3 v2 | criticised: meanders | 35% |
| Ch 3 current | awaiting review | 32% |
| Ch 4, 5, 6, 7 | awaiting review | 21%, 18%, **44%**, 20% |

Findings: repeatable (repeat runs within 3 paragraphs), and its cuts are specific, but it does not separate Ch 1 from Ch 2 v1. It is used as an edit list with a ceiling at Ch 1's level (28%). Predictions for the user's review: `PREDICTIONS-ch02-07.md` (Ch 6 and Ch 3 most at risk of "meanders").

## Next calibration
Score `PREDICTIONS-ch02-07.md` against the user's feedback (precision, recall). Add what he rejects to the corpus. Re-run the blind judge and the chain audit only when the labelled set has grown.
