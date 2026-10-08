# Tone: stance and flow

_Companion to `docs/LINGO.md` (D29, D30), which holds the voice rules and the banned words. This file covers how the prose stands towards the reader and how it moves from paragraph to paragraph. Writers read both before drafting; the fidelity-checker checks against both. Every example below is from the prologue and Chapter 1 drafts the user rejected, with the version that replaced it._

## The reader
A believer who prays, fasts and recites duʿas, and who has wondered whether there is more to those acts than getting them right. Nothing else is assumed: not their sex, their learning, their piety, their age or how much they practise. The book should read as well to a woman as to a man, and to someone who has not opened a book of fiqh as to someone who has. The register is a clear, logical, warm introduction, not a sermon and not a chat.

## Rules

### 1. Each paragraph picks up the last one
**Do:** make the first sentence of every paragraph do two jobs: take the point the previous paragraph ended on, and state the point this paragraph will make. The reader should be able to read only first sentences and follow the argument.
**Don't:** start a paragraph on a new subject and leave the reader to work out the link.
- Before: paragraph 1 ends "The Imams (ʿa) gave them to ordinary believers to say." Paragraph 2 begins "Most of our religious life sits elsewhere."
- After: "Despite saying these words in our munajats and on auspicious occasions, we find that seeking to know God does not feature in our day-to-day routine."

### 2. The sentence-relevance test
**Do:** for every sentence, ask what it adds to the point of its paragraph (which is the point in the `::: {.point}` note). If the answer is nothing, cut it, even if it is true and well made.
**Don't:** keep sentences because they sound like a book.
- Cut: "Just before it, the prayer asks for 'complete severance of my relations with everything else and total submission to You'." (True, cited, and nothing in the paragraph needed it.)
- Cut: "The book does assume a reader who is intelligent and busy, so each chapter makes one point, proves it and stops." (Says nothing about ʿirfan, and reads as "if you are not intelligent, don't read on".)

### 3. No lecturing, moralising or asides
**Do:** state what people do and what the Quran or the Imams ask, as facts.
**Don't:** add judgements on the reader's practice, however small, and never in a subordinate clause.
- Before: "We pray, fast and pay what is due, and we try to do these things correctly, as we should."
- After: "Praying, fasting and paying what is due, the wajibat, are the dominant undertaking."
- Also banned: "we rarely stop to ask", "we never", "we pay lip service". Write "does not feature in our day-to-day routine" or "is less practised".

### 4. No presumption about the reader
**Do:** describe the book by what it offers.
**Don't:** describe the reader by what they are (clever, busy, devout, lax, male) or tell them what they will find easy or hard.
- Before: "The book does assume a reader who is intelligent and busy."
- After: "The book is meant as a welcoming introduction to ʿirfan and a guide to beginning the journey, and it strives for brevity and clarity."
- The same rule covers the lecturer's classroom asides ("I don't know about you", "is there anyone here whose heart trembles?"). They are not carried.

### 5. Warm and plain, without familiarity
**Do:** use ordinary words, "we" and "us" for what believers share, and human language for human things.
**Don't:** reach for the solemn or the abstract when a plain sentence exists, and don't slide into chattiness (no "you know", no jokes, no "honestly").
- Before: "They were not written for a few saints. The Imams gave them to ordinary believers to say."
- After: "These requests to see God with the heart and to be near Him were written for us, by the Imams, as an endeavour for the ordinary believer."
- Before: "Nothing in this chapter asks you to doubt the first claim."
- After: "This claim is not contested."

### 6. Every quote is spoken to
**Do:** after any quotation, epigraph included, say in the next sentence what it says and why it is here. Name the source in plain words (which prayer, which surah, where it is recited).
**Don't:** place a quotation and move on, or quote something the text never uses.
- Before: the prologue opened with the Munajat line and the first paragraph did not mention it.
- After: "These words come from the Munajat Shaʿbaniyyah, a prayer many of us recite in the month of Shaʿban. The line asks God for one thing: to light up the eyes of our hearts..."

### 7. Arabic with every displayed Quran, hadith or duʿa quote
**Do:** display a Quran quotation as `::: {.ayah ref="30:21" words="15-"}` and a hadith or duʿa as `::: {.quote ar="…" source="…"}`, so the build sets the Arabic above the English in a small size. Quote only the words that carry the point (`words=` for part of a verse). A short phrase inside a sentence may stay English-only when its verse is displayed with Arabic nearby.
**Don't:** display a long run of Arabic and English, and never type Arabic from memory. If no held extract has clean Arabic, write `ar="[VERIFY: …]"`.
- Before: Q 30:21–24 as one four-verse block, Arabic and English.
- After: three five-word endings, each displayed with its Arabic, and the rest of the verses paraphrased in prose.

### 8. No cleverness, no suspense
**Do:** set the scene by naming things: which verse, which prayer, which occasion. Engagement comes from the content.
**Don't:** withhold a name to create a reveal, or open with a flourish that the reader has to decode.
- Before: "There is a verse often recited at weddings." (The reader is left guessing which.)
- After: "There is a verse often recited at weddings, one most of us know. In Surah al-Rum, God says that He created spouses for us from among ourselves 'that you may take comfort in them'..."

### 9. "Let's" for walking through an argument
**Do:** when the chapter is about to lay out a step, say so plainly: "Let's start with two claims." "Let's turn to the Quran." "Let's be clear about what this invitation is not."
**Don't:** use "we shall now consider", "it is worth noting", "the reader will observe", or a rhetorical question to do the same job. "Let's" is a signpost, not an invitation to chat; one per section is usually enough, and "let's ask ourselves" stays banned (D22).

### 10. Short quotations
**Do:** quote the words that carry the point and paraphrase the rest, both from the Quran and from the lecturer.
**Don't:** quote a verse in full when its last clause makes the point, or carry three sentences of a scholar when one does.

### 11. The point note under every heading
**Do:** keep the `::: {.point}` note under each `##` heading at one or two sentences stating the point the section makes, and update it when the section changes. Everything in the section serves that note (rule 2).
**Don't:** let the note drift from the prose, or let a section carry a second point the note does not name.

### 12. Fewer "and"s; one idea per sentence
**Do:** break "X and Y and Z" chains into short sentences, or use a semicolon where two clauses balance. Give each item in a list its own line when the items are separate (the five Parts each get a paragraph).
**Don't:** "It answers that the Quran invites more than the minimum and that the goal of ʿirfan is already on our lips in the duʿas." Write: "It answers that the Quran invites more than the minimum, with the goal of ʿirfan already on our lips in our duʿas."

### 13. Say what "it" is
**Do:** name the thing when a pronoun could point two ways. "The landscape a traveller passes through on the journey towards ʿirfan."
**Don't:** "what the journey passes through and what keeps it safe" (what is "it"?).

### 14. Don't explain the same thing twice
**Do:** say a feature of the book once, in the place it belongs.
**Don't:** describe "Words you'll meet" in one paragraph and again in the next.

### 15. One sentence, one clear claim
**Do:** split a sentence that stacks a claim, a colon and a quotation. "It is knowing Him from close, with the heart, which is what the Munajat asks for. In Murtada Mutahhari's words, the ʿarif 'wishes to reach…'"
**Don't:** "It is knowing Him from close, with the heart, as the Munajat asks: the ʿarif, in Murtada Mutahhari's words, wants to reach God, 'to become connected to it and witness it'."

### 16. One distinct point per paragraph
**Do:** when a section makes three points, give each its own paragraph, introduced in order ("The first… The second… The third…"). Very small points may share one paragraph, but then all of them share it.
**Don't:** put the first two points in one paragraph and the third in another; or open "There are three things…" and then give a point that does not grammatically follow ("The second is a sect or an order").

### 17. Go easy on "you"
**Do:** in expository passages, write about "a reader", "the believer" or the subject itself. "A reader should feel able to say what ʿirfan is."
**Don't:** "You will not be asked to…", "By the end, you should…". "Let's" for walking an argument (rule 9) and the "Try this" boxes are fine.

## Check before handing over
Read only the first sentence of every paragraph in order. If the argument does not follow, fix the openings (rule 1). Then read every sentence against its section's point note (rules 2 and 11). Then search for "as we should", "rarely", "never", "lip service", "intelligent", "busy", "you will find", "of course", and for any quotation that is not spoken to in the sentence after it.
