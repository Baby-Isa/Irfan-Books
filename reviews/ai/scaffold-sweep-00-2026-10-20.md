# Scaffold sweep (D52): Prologue, An invitation (2026-10-20)

Applied directly with the user's authorisation. Scaffolding only (TONE 46, "Scaffolding" and "Variation"). The prologue is the approved exemplar, so only two edits.

## Edits

1. **List label said mechanically** (count kept, content carries the order).
   **Before:** Three guiding principles frame the discussions in the chapters that follow. The first is that ʿirfan is never pursued for the sake of powers, such as reading minds or foreseeing future events.
   **After:** Three guiding principles frame the discussions in the chapters that follow. The first concerns powers such as reading minds or foreseeing future events: ʿirfan is never pursued for their sake.

2. **Stock attribution** ("X and Y agree on this").
   **Before:** Sheikh Bahmanpour and the wider literature agree on this, as Chapter One shows.
   **After:** As Chapter One shows, Sheikh Bahmanpour and the wider literature both hold to this principle.

## Left as they are (the user kept them on the 10-19 sweep)
- "The book is built in five parts. Each answers one question and depends on the one before." (sweep #1 not taken)
- "The second is that there is no separate sect or order through which ʿirfan must be gained. Shia ʿirfan has no institution of authority beside the Imam." (sweep #2 not taken). Read beside the edited first principle and "The third principle is the most important", the three openings now vary.
- "ends not in withdrawal from the world but in return" (the Part Five point; kept on the 10-19 sweep).

## Checks
- `voice.py punct`: one TAIL-COMMA removed (the old first-principle sentence); no new TAIL-COMMA, TAIL or NOT-BUT. A new OXFORD? on edit 2 is a false positive (a two-item phrase).
- `voice.py profile`: REWRITE, as before the edits (the Sheikh named 5.2 times per 1,000 words against a cap of 5; unchanged by these edits).
