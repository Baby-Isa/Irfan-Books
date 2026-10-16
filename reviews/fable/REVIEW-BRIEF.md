# Fable review after the Opus rebuild (2026-10-16)

You are the structural and line editor for one chapter of Book 2. The user stopped reading Chapter Four because "the points being made are not clear and well structured and punchy, and the style of writing is just hard to read." The chapter has just been rebuilt by another model on a **point ladder**: under each `##` heading, the `::: {.point}` note gives the section's point, then one numbered step per body paragraph.

Read: `docs/briefs/REWRITE-2026-10-16.md` (the user's feedback), `docs/TONE.md` rules 1, 25–27, 38–44, `docs/briefs/LESSONS.md`, the approved exemplar `book2/chapters/01-seeking-not-powers.md` (for density and voice), then the chapter. Do **not** edit the chapter. Write your review to the file named in your task.

## Check, in this order
1. **The ladder alone.** Read only the chapter point and the point notes. Is each section point one short, plain claim a reader could repeat? Is each paragraph step a short claim (not a description)? Does each step follow from the ones before, with no gap or jump, and does the last one land the section point? Do the sections, in order, prove the chapter point? Propose sharper wording for any point that needs a second reading.
2. **Prose against ladder.** For each paragraph: does it deliver its step, and only its step? Flag material that belongs to no step, steps the prose skips, and steps delivered in the wrong paragraph.
3. **The opening.** Is the reader hooked within two or three paragraphs? Does the chapter say, in its title's words, what it establishes? Are callbacks one or two sentences, with no tour of earlier chapters?
4. **Sentences.** Quote every sentence a reader would have to read twice, with a plain rewrite (TONE 38). Be thorough: this is what made the user stop.
5. **Rules.** Which Imam is named every time (41); Arabic glosses in brackets (42); several scholars only for nuanced points (43); no mic-drop endings (32); theological care (33); the closing question kept and plainly worded.

## Output (markdown)
- **Verdict:** one line: would the user enjoy reading this and find the points clear? What is the single biggest remaining problem?
- **Ladder edits:** before → after, per section.
- **Structural edits:** by paragraph, each a concrete instruction (cut, merge, move, add a link sentence: give the sentence).
- **Sentence rewrites:** before → after, every one.
- **Rule fixes:** before → after.
Keep it concrete. Each item must be something the writer can apply without asking.
