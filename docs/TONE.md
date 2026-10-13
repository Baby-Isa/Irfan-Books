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

### 18. Quote the lecturer only where his words are poignant
**Do:** paraphrase the Sheikh where he speaks informally or ungrammatically, without quotation marks. "Sheikh Bahmanpour accepts it as fair for ordinary believers." "Anything beyond them, they say, is made up by the whims and wishes of certain mystics." Quote him where the line carries weight ("has a beginning and no end", "These are shirk"). A small fix to a quoted word goes in square brackets: "a machine inside which is [rusted]".
**Don't:** "that's fair enough", "made up by some mystics according to their vibes and wishes", "the whole terms and conditions are different", "It needs lots of training". Spoken informality reads as the wrong register in print.

### 19. Clarify gently; never correct the reader
**Do:** "For the avoidance of doubt, this invitation from the Qur'an is not an invitation to circumvent the law or to abandon the prescribed wajibat."
**Don't:** "Let's be clear about what this invitation is not: it is not an invitation to go around the law." It sounds as if the reader thought otherwise and is being scolded.

### 20. Finish the thought
**Do:** end a sentence on what it means. "We witness the rain as rain and the marriage as a marriage, and we pass them by without perceiving what they say about their Creator."
**Don't:** stop on an image that leaves the point unsaid ("the rain is rain, the marriage is a marriage, and we pass by").

### 21. Don't state the obvious, or repeat a settled point
**Do:** cut a qualifier no reader doubts ("there is nothing wrong, in the shariʿa, with being rich" becomes "there is nothing wrong with pursuing material wealth"), and cut a paragraph that only re-proves a point already made.
**Don't:** add a fourth authority when three have made the case. Say "in his lectures", never "in his class".

### 22. Keep paragraphs short enough to breathe
**Do:** aim for 50–65 words per paragraph, with 110 at most. Split where a new claim begins, as in the exemplar: "Placing the fault in the receiver has two consequences. The first is… / The second is that the problem can be solved…"
**Don't:** run a definition, a qualification and a quotation together in one block of 150 words or more.

### 23. Name the Sheikh sparingly (D42)
**Do:** let the Sheikh's teaching be the book's own exposition. The prologue says the lectures are the book's core, so his points can be stated straight. Name him:
- when a point is introduced as his and is distinctively his ("Sheikh Bahmanpour defines mysticism as…");
- when he is quoted;
- when he is set beside another scholar.

Once he is named, the rest of that line of thought belongs to him, so don't name him again in the next sentence or the next paragraph. Aim for about one mention per 250 words, and never two in a paragraph. `build/voice.py` flags more than 5 per 1,000 words.
**Don't:** "Allah's light, the Sheikh says, is everywhere…" straight after "Sheikh Bahmanpour speaks of the light differently…". Don't use "he says", "he adds" or "he notes" as filler.
- Before: "Sheikh Bahmanpour names the source with a hadith on knowledge, which Imam Khomeini also quotes in his Forty Hadith."
- After: "A hadith on knowledge, which Imam Khomeini quotes in his Forty Hadith, names it."
- Before: "The light, the Sheikh says, comes to the hearts of the pure, and darkness covers the impure."
- After: "The light comes to the hearts of the pure, and darkness covers the impure."

### 24. Straight prose, not "he said, she said" (D42)
**Do:** make the point in the book's voice and bring in a scholar only where his words add something the argument needs. Two voices on one point are usually enough. Let the logic, not the list of quotations, decide what a section contains.
**Don't:** build a section around fitting in direct quotations; "Khomeini says… Tabatabaʾi writes… Mutahhari adds…" reads as a literature review.
- Before (Ch 2 v1, where reason stops): three loose paragraphs of attributed sayings on positive and negative knowledge.
- After: one chain in plain prose. Reason proves that God is and says what He is not. Positive knowledge needs knowledge by presence. We have knowledge by presence only of our own soul. So God must be found within the soul.

### 25. Every paragraph earns its place in the chain
**Do:** before keeping a paragraph, name the link it adds between the section's opening and its point note. If a section's point is simple, it needs few paragraphs. Build up to the strongest point so it lands as a conclusion the reader has been led to.
**Don't:** keep paragraphs because they are true and sourced. The user's test: does the reader feel the section is bloated?

### 26. Callbacks re-explain enough to be understood a week later
**Do:** when recalling an earlier chapter, give the reader the gist of what was argued there in a sentence or two.
- Before: "Chapter 1 reached the same conclusion by another road, when it placed the fault in the receiver."
- After: "This book's first chapter reached the same conclusion by a different road. Surah al-Rum says that God's signs are for those who reflect, know, listen, and reason, and yet most people pass them by. Nothing in the signs is hidden and nothing is wrong with our eyes; the fault lies with an inner faculty that has rusted and does not receive."

### 27. "Therefore" only after the argument is made
**Do:** build the premises before a "therefore" or "so". If the conclusion has not been argued for in the text above it, argue it first.
- Before: "The severance the prayers ask for is therefore in the heart, not in the household or the marketplace." This came with no earlier mention of the household.
- After: the request is stated, then the worry it raises (leaving family and work), then the prayer that names what is cut away (love of the world), then the friends of God who keep their families. Only then: "The severance the prayers ask for is therefore in the heart."

### 28. Name the referent when it is out of working memory
**Do:** extend rule 13 across sentences. If "the second kind" or "it" points to something that was not in the sentence before, name it.
- Before: "The ʿarif's knowledge of God is of the second kind."
- After: "The ʿarif's knowledge of God is knowledge by presence."

### 29. Explain a source's puzzle, or leave it out
**Do:** when a lecture remark raises a puzzle, explain it in full, or cut it.
- Before: "Sheikh Bahmanpour notes that people unfamiliar with such words sometimes take them for mistakes. The phrase comes from the Munajat itself." (abrupt, and the puzzle is never stated)
- After: "Some who meet these words for the first time think the prayer must be mistaken, since the Qur'an says that sight cannot perceive God (Q 6:103). The Sheikh's answer is that the prayer is not speaking of the eyes in our heads."

### 30. Make doctrine consistent across chapters
**Do:** when two sources seem to pull against each other, reconcile them in the text with a held source. For example, God "puts" light in the heart, yet the light is everywhere. The text reconciles them: God's giving never stops ("no niggardliness in the higher realms", `forty_hadith` p. 331), purification makes the heart able to receive it, and its lighting in any heart is still God's act.
**Don't:** leave a line that a careful reader will find contradicts an earlier one ("Purification is the traveller's part; the light is Allah's to give").

### 31. Vary the rhythm of neighbouring sentences
**Do:** when two sentences in a row share a structure and length, vary the second ("and" in place of a comma, or a different opening).
- Before: "It reaches us from outside, through the senses or by reasoning. We form concepts of the things around us, then analyse those concepts."
- After: "…We form concepts of the things around us and then analyse those concepts."

## Check before handing over
Read only the first sentence of every paragraph in order. If the argument does not follow, fix the openings (rule 1). Then read every sentence against its section's point note (rules 2 and 11). Then count the Sheikh's name (rule 23) and the attribution verbs ("he says", "he adds", "he notes"). Then search for "as we should", "rarely", "never", "lip service", "intelligent", "busy", "you will find", "of course", and for any quotation that is not spoken to in the sentence after it.
