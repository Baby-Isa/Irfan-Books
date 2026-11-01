# Audit: Book 2, Epilogue "First steps" (`book2/chapters/18-epilogue.md`)

Audited against `docs/ladders/18-epilogue.md`, `docs/briefs/18-epilogue-case.md`, `docs/LINGO.md`, `docs/GLOSSARY.md`, the extracts (`journey`, `nahj`, `kernel`, `light`, `forty_hadith`, `duas-munajat-shabaniyah`), transcripts L01, L07, L08, L10, L13, L14, `sources/quran/en.qarai.txt`, `sources/bibliography.bib`, and the printed Ch 6, 7, 8, 9, 10, 15, 17 and the Try this boxes of Ch 1-17. The chapter was not edited. The PDF was not built. I could not run `build/quran.py` or the Lua filter, so the `words="5-6"` rendering of Q 3:17 is checked by hand only.

Body length is about 2,400 words (limit about 3,600). No jokes, no rhetorical-question chains, no LINGO banned words or So/Well/Look/Now openers (grep clean). All nine citation keys used (`journey`, `nahj`, `mafatih`, `kernel`, `forty_hadith`, `lantern`, `sahifa`, `light`, `duas_munajat_shabaniyah`) are in `bibliography.bib`.

## Findings

| Sev | Location | Issue (exact text / source text) | Suggested fix |
|---|---|---|---|
| **High** | Para 2 (after the opening), "as Chapter Seventeen asked in closing, how a believer begins this week" | Misdescribes Ch 17. Ch 17 as printed ends on the thesis paragraph, the Q 89:27-28 block and the Try this box. It has no closing question. `docs/ladders/17.md` line 91: "the closing question was cut, since the chapter does not answer it; the epilogue takes up how to begin". The ladder's Opening step 1 ("Chapter Seventeen ends: 'So how does one begin, this week?'") is stale. The brief says "Hand-off: none". | Cut the clause. For example: "It leaves open what is kept for the year and how a believer begins this week." Or point to Ch 17's Try this instead. |
| **Med** | §1, Imam ʿAli's bread, "and that the Imam's words to others are 'instruction for level one'" | L08 ¶83: "Well he's in level 1000 we just want to start level one. And this is this is instruction for level one. So he was telling people not to imitate him." The "this" is most naturally the lecturer's own instruction (the course, for beginners), and "So he was telling people not to imitate him" follows from it. The chapter assigns the phrase to the Imam's words, which is one reading only. D39 asks for wording that is true on either reading. | Quote only "he's in level 1000 we just want to start level one". Optionally add the Sheikh's closing line, ¶83: "that level was not something that could be imitated by anyone". Drop "instruction for level one" or attribute it to the Sheikh ("this is instruction for level one"). The point box (hidden) says "Imam's words to others" and needs the same edit. |
| **Med** | §2 prose and table row 6: "Chapter Six's one prayer at the start of its time, kept free of other plans"; "Pray one prayer at the start of its time, and keep that time free [@forty_hadith, p. 375]" | Ch 6's Try this does not say "start". It says "keep its time free, with nothing planned straight after it" and "in the most meritorious part of its time". `forty_hadith` p. 375: "carry it out in the most meritorious part of its time, refraining from engaging in any other work during those times". "Start of its time" is a new gloss that the source does not give. | Use Ch 6's wording: "one prayer in the most meritorious part of its time, with that time kept free." Fix both the prose and the table. |
| **Med** | §2: "Most of the steps belong to the prayer, which we already keep five times a day" | Miscount. The prayer group has five steps (Ch 2, 4, 6, 10, 12). The Qur'an and duʿa group has four, the night group four, and the people group two. Five of fifteen is not "most". | "The largest group belongs to the prayer…" or "Five of the steps belong to the prayer…". |
| **Med** | §3, Ramadan: "Chapter Seventeen's step … can be kept every day, as Maliki Tabrizi's etiquette for the month asks." | No citation attached (the key `journey`, p. 46 appears only in the table). `journey` pp. 45-46 give the etiquette of Qur'anic recital "as far as the Holy Month of Ramadhan is a month of Qur'an": "as though all of them have been revealed especially for him". It does not say "every day". The "every day" is the book's. | Add `[@journey, pp. 45-46]` and state "every day" as the book's arrangement, or drop "every day". |
| **Med** | Table row 9 ("Once, first; again on a Sunday of Dhu'l-Qaʿdah") and §3 "Dhu'l-Qaʿdah brings back the prayer of repentance from the first week"; §2 "it is prayed once"; point box "repentance once" | L08 ¶29-33 give a single prayer: "you could do it at any time, but the high time is on a Sunday, in Zilqadah". Nothing says to repeat it. Ch 9 says repentance is "a continuous process" and is renewed on falling. "Repentance once" can read as one-off repentance, against Ch 9 §2. | Say that the prayer (not repentance) is prayed once. Phrase the Dhu'l-Qaʿdah step as "if the month falls in the rung, the Sunday of Dhu'l-Qaʿdah is the best time for this prayer". Remove "again" and "brings back". |
| **Med** | §4: "The title is God's to give, so the year is kept in that hope." | The Sheikh states it outright (L10 ¶27): "then the title would actually is speaking for you. I mean, you are under that title of mustagfireen bil as haar". The qualifier is the writer's theology, uncited. D39 and golden rule 5 apply. The preceding sentence already attributes the claim ("In the Sheikh's account"). | Delete the sentence, or replace it with a held source on acceptance (`journey` p. 161 is already cited two paragraphs later). |
| **Med** | Opening, `[VERIFY: a printed source for this hadith of Imam al-Sadiq (as)…]` | One open `[VERIFY]` in reader-visible body text. `build.py --final` will refuse to build. The text already presents the hadith as "Sheikh Bahmanpour reports … As he tells it", which satisfies D47. | Remove the marker (D39: go around it). The attribution to the Sheikh's report stays. |
| **Med** | §1 young man: "the elder wanted 'a linear gradual improvement' in place of a burst of effort that leaves a person abandoned by his own soul" | The phrase is verbatim from L08 ¶26. But Ch 9 gives the comparison ("fasting suddenly for three months … abandoned by your own soul") to the lecture ("The lecture compares such rushing with someone who suddenly fasts…"), not to the elder. The elder's quoted words in Ch 9 end at "You are rushing." The epilogue differs from Ch 9 on who says what. | "Chapter Nine told of the young man … The Sheikh draws the lesson: 'a linear gradual improvement', not a burst of effort that leaves a person abandoned by his own soul." |
| Low | Tone: "That answer measures the road in time rather than in feats." and "The year is no finish line." | Tidy aphorisms (LINGO). Neither adds a fact beyond the neighbouring sentences. | Delete both. The sentences around them carry the content. |
| Low | §2: "Where the heart is most present with the Qur'an and the duʿas, the steps are readings." | Muddled: the group is by time of day, and this sentence reads as if the heart is "with" the Qur'an. | "With the Qur'an and the duʿas, the steps are readings." |
| Low | §1: "recommended acts are built on the obligations rather than standing in for them" | Within a sentence about the lectures (L07 ¶15), but L07 ¶15 says only that the extra acts are also to be done ("they have to do them as well"). L07 ¶17: "there is nothing which goes outside Sharia". The "built on" framing is the book's. | Cite L07 ¶15, ¶17 in the src comment, or rephrase as the book's reading. |
| Low | §1: "Mirza Jawad Maliki Tabrizi tells the wayfarer to review his affairs and his workload first" (and §3 reuse) | `journey` p. 109 sits in his Ramadan programme (the sentence runs straight into "one thousand ra'kats … during this month"). The chapter presents it as general advice. The lecturer's own version (L07 ¶18: "one can never do all the mustahabaat … you have to choose which one is more important") is a better first source. | Add "in his programme for Ramadan", or add L07 ¶18 as the lecturer's support. |
| Low | §3: "the hundred rakʿas he sets for the Night of Power are of the same kind [@journey, p. 155]" | p. 155 reads "he should offer 100 rak'ats special prayer for the Night of Power". It carries no "if mood allows" condition. "Of the same kind" borrows the p. 109 condition. | "are also heavy" or "are likewise a large programme". Drop "of the same kind". |
| Low | §2: "the lectures' advice that every traveller should find a practice of their own, since no two travellers are alike" | L14 ¶71: "Everyone should find his or her own suitable type of practice and worship." "No two travellers are alike" is Ch 15's gloss, not the lecture's. | Cut "since no two travellers are alike", or attribute it to Ch 15. |
| Low | §4: "the time the teachers of this road asked a student to keep one practice" | L10 ¶26: "at least a year or so". Ch 10 says "at least a year". "At least" is lost. Nuance only. | "a year at least". |
| Low | Table intro: "Each chapter's step, with its source"; rows 1, 12, 14, 15 | These rows carry no key (row 1 nothing; rows 12, 14, 15 "(the lectures)"). The ladder had L01, L09 ¶66-68, L13 ¶64-65, L14 ¶70-71. | Add the L-refs in the table or in the src comments. |
| Low | §4 "He adds that Allah accepts even insignificant deeds and rewards them handsomely." and §1 "ʿAllama Tabatabaʾi's general teacher" | No citation on the sentence. Sources: `journey` p. 161 ("accept quite insignificant deeds, rewards handsomely"); `kernel` pp. 80-81. | Add `[@journey, p. 161]` and `[@kernel, pp. 80-81]`. |
| Low | §1 guide test: "Any teacher who is found is tested as Chapter Seven tested a guide … Only long company shows how far he has travelled" | Ch 7 applies long company to the guide who is submitted to. The epilogue's subject is a teacher of practices, "consulted as one consults anyone learned". The test is correct as Ch 7 states it, but a mismatch of scope. | Say "a teacher who is followed closely is tested…". |
| Low | Closing Arabic (see below) | Codepoint order differs from the extract in the shadda/fatha pair (see "Arabic" section). The two render identically. | Optional: copy the string from the extract byte for byte. |

## Verified clean (no finding)

**Quotations checked verbatim**
- `journey` p. 109: "he should select the proper program which is suitable for him"; "spiritual condition and mood allow him". Also the review sentence ("low, moderate, and high mood").
- `journey` p. 161: "he should perform it, as much as possible"; "what is important and useful for the servant is that Allah (the Glorious, the Exalted), accepts deed, and not its being small or big". The comma after "Exalted)" is kept.
- `nahj` 2.45.2, p. 626: "his two shabby garments and his two pieces of bread"; "You will not be able to do what I do—but help me by practicing restraint and striving for good". The dash matches. Basra and the governor match the heading (the footnote's Sahl variant is not needed).
- L08 ¶83: "he's in level 1000 we just want to start level one" (see the Med finding for the second phrase).
- L08 ¶26: "a linear gradual improvement".
- L10 ¶26: "one year is enough". L10 ¶27: "doesn't mean that after one year you stop it"; "more power to ask for more"; "revert back to our lower position" in words.
- Q 57:3 inline: "He is the First and the Last, the Manifest and the Hidden" matches Qaraʾi.
- Q 3:17 block: Qaraʾi text matches. Words 5-6 of the Arabic are wa-l-mustaghfirina bi-l-asḥar, which suits "and they plead for [Allah's] forgiveness at dawns".
- `light` p. 166: "make me one of those who always remember You" (a fragment of a longer sentence, which is fine).

**Pointers checked against the chapter named**
- Ch 1, 2, 3, 4, 5, 7, 8, 9, 10 (Tasbih), 11, 12, 13, 14, 15, 16 and 17: each step in the prose and the table matches its printed Try this, except Ch 6 (above). All 17 chapters appear once in the table.
- Ch 6 (law holds to the last breath), Ch 7 (three accounts; guide test; Qadi's year), Ch 8 (none dropped; Qadi in its Try this), Ch 9 (law kept strictly is polishing, the first stage; people first; the young man), Ch 10 (half an hour; going past the limit and quitting; the measure is the person's, not the Prophet's; the medicine image; al-Muzzammil about three minutes; Ramadan opening): all described accurately.
- Part Five divider epigraph (`parts/5-the-destination.md`) matches the paraphrase in the close. Ch 6's epigraph is §126-127, which follows §124.

**Rules stated as the earlier chapters state them**
- Measured dose (Ch 10 §4): "a dose measured to the person", small and kept up. Correct.
- Law first (Ch 6 §4, Ch 8, Ch 9): correct. "Only the reason for keeping it changes" is not repeated, which is acceptable.
- Guide test (Ch 7 §4): law rules out; wonders prove nothing; long company; where he turns people. In the right order. D20: the three accounts are recalled in a clause only and not argued. Fine.

**Arabic**
- One string outside the Qur'an block: "وَأَنْ تَجْعَلَنِي مِمَّنْ يُدِيمُ ذِكْرَكَ". The source is `duas-munajat-shabaniyah.md` §124. The letters, vowels and spacing match. Codepoint level: in "مِمَّنْ" the chapter stores fatha then shadda (the normalised order) and the extract stores shadda then fatha. Rendering is identical. No Arabic is invented. `title-ar` is empty.

**Glossary and spellings**
- Spellings follow GLOSSARY: *wajibat*, *tawba*, *istighfar*, *muhasaba*, Musabbihat, Tasbih of al-Zahraʾ (as Ch 10 prints it), Dhu'l-Qaʿdah, Shaʿban, Mirza Jawad Maliki Tabrizi, Mirza ʿAli Aqa Qadi, ʿAllama Tabatabaʾi, Surah Al ʿImran (as Ch 1).
- The words box's "five surahs" follows Ch 7 and the glossary. The Kafi's six are noted in Ch 8, so there is no conflict.

**Argument (D22)**
- All brief premises are present and in order. The headings are one to one with the brief (How to begin / This week / This month / This year). Nothing relies on a later section. §2 uses §1's rules, §3 keeps §2's act, and §4 keeps §3's. The conclusion follows, and the Munajat §124 close answers "the keeping itself is asked of God". No new `[QUERY]` or `[GAP]`; one `[VERIFY]` (above). The ladder's rule "nothing new" holds: every act is a chapter's own, and the new quotations are the ones listed in the ladder (all verified above).

**Tone / LINGO**
- Beyond the two aphorisms flagged above, the chapter is plain prose with no bullets in the body (numbered lists are inside the `.point` scaffolding boxes), no banned words, and no intensifiers. Each section ends with a one-sentence "therefore" line as the D22/D23 pyramid requires. The chapter ends on the quotation with no closing remark (D29).

## Verdict

**PASS WITH FIXES.** One High (the Ch 17 hand-off that Ch 17 does not contain) and eight Medium fixes: the "level one" attribution, Ch 6's "start of its time", the "most of the steps" count, the uncited Ramadan claim, the repeated repentance prayer, the added "title is God's to give" theology, the open `[VERIFY]`, and the young-man attribution. No invented scripture, no unsupported quotation, no missing bibliography key, and no change to the lecturer's stated position beyond the §4 qualifier.

## Fixes applied (2026-11-01)

**High**
- Ch 17 hand-off: the "as Chapter Seventeen asked in closing" clause is cut. Ch 17 ends on its Try this (a few verses read slowly each day this week), so the opening now points to that step: "down to Chapter Seventeen's few verses read slowly each day".

**Medium**
- Bread story: only L08 ¶83's clear line is quoted ("he's in level 1000 we just want to start level one"); "instruction for level one" dropped. The Nahj letter (packet ¶7, a restatement) is folded into the same paragraph; the Maliki Tabrizi "as much as possible" tag, which nothing used, is cut.
- Ch 6 step: "in the most meritorious part of its time, with that time kept free" in the prose and the table, matching Ch 6 and `forty_hadith` p. 375.
- Count: "Five of the steps belong to the prayer".
- Ramadan: cited `[@journey, pp. 45–46]` as the month of the Qur'an whose etiquette of recital Ch 17's step follows; "every day" removed.
- Repentance: described as Ch 9 does (a continuous process, renewed whenever the traveller falls; src L08 ¶13-15). The prayer of repentance marks the setting out; no repeat is stated. Dhu'l-Qaʿdah is now the prayer's best time for a reader who sets out in that month ("again", "brings back", "repentance once" removed from prose, table and point boxes).
- "The title is God's to give" sentence cut; the Sheikh's claim stands as his account.
- `[VERIFY]` removed from the opening; "Sheikh Bahmanpour reports … As he tells it" kept.
- Young man: the elder's words end at "rushing"; "a linear gradual improvement" and the three months' fast comparison are given to the lecture, as Ch 9 gives them.
- Munajat §124 Arabic pasted by script from `sources/extracts/duas-munajat-shabaniyah.md` (byte-identical).

**Low**
- Aphorisms cut ("That answer measures the road…", "The year is no finish line.").
- "With the Qur'an and the duʿas, the steps are readings."
- "a year, which the teachers … set as the least time" (L10 ¶26 "at least").
- "No two travellers are alike" replaced with L14 ¶70's own point (the way each of us finds to God differs from that of the person beside us); src L14 ¶70-71.
- Table rows 1, 12, 14, 15 carry "(the lectures)", with a hidden src comment under the table (L01 ¶6-9; L09 ¶65-66; L13 ¶64-65; L14 ¶70-71).
- Guide test scoped as Ch 7 scopes it: "A teacher who is followed closely is tested…".
- Also: "built on the obligations" restated from L07 ¶15, ¶17; L07 ¶18 added for choosing among recommended acts, and p. 109 placed "in his programme for Ramadan"; Night of Power "likewise a large programme"; `[@journey, p. 161]` and `[@kernel, p. 80]` added.

**Chain audit**
- ¶7 folded into ¶6; ¶31 (whole-chapter summary) cut; one-line section closers ¶11, ¶19, ¶25 cut. ¶22's unused Ch 10 tag cut. The close now runs from God's acceptance (¶30) to asking Him for the keeping, and ends on Munajat §124; Ch 6 location note dropped.

**Checks**: `voice.py profile` PASS (read-twice 2.4%); `punct` leaves three advisory flags (an Oxford-comma list that has its "and", the semicolon list of the five prayer steps, and the colon before the closing quote). `build.py pdf book2 "18*"` builds. No markers remain in the chapter.
