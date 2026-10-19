# Punctuation sweep, Book 2 prologue to Chapter Seven (D49, user 2026-10-19)

Apply `docs/TONE.md` rule 45 (read it in full; it records the user's own decisions and examples) to the chapters named in your task. **Do not edit any chapter.** Write your proposed edits to `reviews/punct/NN.json` (one file per chapter) and reply with a count per chapter.

## Inputs
- `python3 build/voice.py punct book2/chapters/NN-*.md` is not available to you; the flags are in `reviews/punct/flags.txt` (chapter number, flag, sentence). They are candidates, not orders: many are fine.
- Also read each chapter in full: the finder misses things (a list with no "and"; a semicolon before an aside; an echo the pattern does not see).

## What to propose
1. **Tails, echoes, semicolons, colons and lists** by the TONE 45 method, in its order (fold; which/whose clause or participle; semicolon between two full sentences of equal weight; own sentence; colon rarely). Leave a flagged sentence alone when it reads well aloud, and say so only in your count.
2. **Oxford commas:** every list of three or more ends ", and …" or ", or …" (add the "and" where the list has none).
3. **Fronted phrases for variety:** at most two per chapter, only where every condition in TONE 45 holds. Set a high bar; none is fine.
4. Change nothing else: no wording beyond the sentence, no content, no quotation (text inside quotation marks is never changed), no citation, no Arabic, no `::: {.point}` notes.
5. Do not touch these sentences, which the user has just approved: "At many weddings, someone recites a verse most of us know."; "Many of us hear it on Thursday evenings, as the Mafatih recommends"; "The dead are in barzakh, which is the world of images; it is the middle world the soul enters when the hold of the body loosens."; the Chapter Five opening's three paragraphs; "…recited by the Prophet ﷺ every night before sleeping."

## Output format
`reviews/punct/NN.json`: a list of `{"before": "<exact text from the file, unique, at least 8 words>", "after": "<replacement>", "kind": "tail|echo|semicolon|colon|oxford|fronted", "why": "<a few words>"}`. "before" must match the file exactly (copy it), including Markdown such as *italics*.
