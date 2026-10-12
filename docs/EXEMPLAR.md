# The exemplar: prologue and Chapter 1 (D36)

The approved prologue (`book2/chapters/00-prologue.md`) and Chapter 1 (`book2/chapters/01-seeking-not-powers.md`) are the written model for every later chapter. They were revised with the user over seven rounds, and the user's uncle, who knows Sheikh Bahmanpour, approved them. Git commit `32e44c9` freezes this version.

**Every writer reads both files in full before drafting**, then `docs/TONE.md` and `docs/LINGO.md`. Imitate the exemplar's rhythm, not only its rules.

## The exemplar in numbers (match these)
| Measure | Prologue | Ch 1 | Target for new chapters |
|---|---|---|---|
| Average words per paragraph | 58 | 56 | 50–65 |
| Longest paragraph | 114 | 103 | 110 at most; split at the point where a new claim begins |
| Average words per sentence | 17 | 17 | 15–19 |
| Body words | ~1,250 | ~2,700 | 2,600–3,200 per chapter |

## What changed between the first drafts and the final version
Each pair below is real. "Before" comes from the drafts the user rejected; "after" is the approved text. The full rule set, with more pairs, is in TONE.md rules 1–22.

1. **Name things; no suspense.**
   - Before: "Many of us first heard the verse at a wedding."
   - After: "There is a verse often recited at weddings, one most of us know. In Surah al-Rum, God says…"
2. **An epigraph is explained by the text that follows it.**
   - The chapter opens on "There are indeed signs in that for a people who reflect", and the first paragraph says where those words come from and what they mean.
3. **Set out the argument plainly, with "let's".**
   - Before: "Start with what is not in dispute… Nothing in this chapter asks you to doubt the first claim. The floor is real, and it saves."
   - After: "Let's start with two claims. The first is… This claim is not contested."
4. **Each paragraph opens on the last one's point and states its own.**
   - After: "Despite saying these words in our munajats and on auspicious occasions, we find that seeking to know God does not feature in our day-to-day routine."
5. **Never lecture, scold or presume.**
   - Cut: "as we should"; "The book does assume a reader who is intelligent and busy".
   - Before: "Let's be clear about what this invitation is not."
   - After: "For the avoidance of doubt, this invitation from the Qur'an is not an invitation to circumvent the law…"
6. **Human language for sacred things.**
   - Before: "They were not written for a few saints. The Imams gave them to ordinary believers to say."
   - After: "Requests like this one were written for us, by the Imams (ʿa), as an endeavour for the ordinary believer."
7. **One point per paragraph.** Three principles get three paragraphs: "The first… / The second… / The third principle is the most important:".
8. **Fewer "and"s.** Use semicolons, colons and short sentences.
   - After: "The signs are all around us: in marriage, in the people we meet, in sleep, in work, in the weather. Yet they are for those who reflect, know, listen and reason."
9. **Finish the thought.**
   - Before: "the rain is rain, the marriage is a marriage, and we pass by."
   - After: "…and we pass them by without perceiving what they say about their Creator."
10. **Quote the Sheikh only where his words carry weight.** Paraphrase his spoken informality.
    - Before: "fair enough", "made up by some mystics according to their vibes and wishes".
    - After: "accepts it as fair for ordinary believers", "made up by the whims and wishes of certain mystics".
    - Keep: "has a beginning and no end".
11. **Short quotations, with their Arabic.** Three verse endings with their Arabic replace a four-verse block. Every Qur'an, hadith or duʿa quote carries its Arabic.
12. **Cut whatever re-proves a settled point.** Two passages went for this reason: Tabatabaʾi's p. 101 paragraph, and the claim that the muqarrabun are "given Paradise in this world", which the quoted verses do not support.
13. **No tidy aphorisms, and no recaps.** The conclusion is stated once.
14. **Go easy on "you" in exposition.** "A reader should feel able to say…" "You" belongs in "Try this".

## How to use it
- **Before drafting:** read the two exemplar files, then the brief. Write the `::: {.point}` note for each section first; the prose serves the note.
- **While drafting:** check each paragraph against the exemplar's numbers, and against TONE rule 1 (its opening links to the last paragraph).
- **After drafting:** run the `tone-editor` agent. It compares the draft with the exemplar and TONE.md and returns line edits. Then run the voice test (`docs/VOICE-TEST.md`): the measured profile and a blind judge who must tell the new chapter from the exemplar and fails to. Then run the `fidelity-checker`.
