# Narration style guide

These scripts are written to be heard, read by a synthetic voice (Kokoro,
British English), by someone driving. Everything below follows from that.

## Listening, not reading

- Short sentences. One idea per sentence. If a sentence needs a comma to
  breathe twice, split it.
- No lists, tables, footnotes, brackets or abbreviations. Say "peace be
  upon him" in full where it is said at all; never "(s)" or "(A)".
- Say where we are often: "We are now in the bow." "Back to the word
  *Rabb*." A listener cannot glance back up the page.
- Repeat key phrases on purpose. Repetition on a page is padding; in the
  ear it is a handrail.
- No visual instructions ("see above", "as the table shows").
- Nothing that asks the listener to close their eyes, recite along with
  gestures or do anything but listen. They are driving.

## Arabic

- Write Arabic in simple transliteration in *italics*, then give the
  meaning straight after, in the same or the next sentence:
  "*Allahu akbar*. God is greater."
- Use one fixed spelling per word throughout (see `pronunciations.tsv`;
  the build applies respellings for the voice only, so the script stays
  readable).
- Keep Arabic passages short. Long Arabic stretches are where a synthetic
  voice sounds worst. Give the first few words in Arabic and the rest in
  English.
- Do not use Arabic script in the scripts.

## Sources and honesty

- Every quotation and story must come from the source books in this
  repository. Name the source in the sentence: "In the Lantern of the
  Path, Imam Ja'far al-Sadiq says..." Never invent a hadith, a story or an
  attribution, and never stretch a quotation.
- Light paraphrase of a source is fine when it is introduced as such:
  "Imam Khomeini makes a point here, which I'll put simply."
- The outward rulings follow the Ja'fari school. Keep them to what is
  needed to place the inner meaning; this is not a manual of fiqh.

## Tone

- Warm, unhurried, direct. "You" and "we", not "the worshipper".
- Mindfulness, not anxiety. Imam Khomeini warns against obsessive
  scrupulousness (*waswas*); the series should lead to calm attention,
  not to straining over every letter.
- End each track with one or two concrete things to hold in the heart
  next time.

## Format

- One Markdown file per track in `script/`, named `NN-slug.md`.
- First line: `# Track N: Title`. That line is spoken as the track
  opening.
- Plain paragraphs. A line with only `---` marks a longer pause between
  sections.
- Use `*italics*` for Arabic only.
