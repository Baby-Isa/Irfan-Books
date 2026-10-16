# Fact-check (round 2): Book 2, Chapter 5, "The soul and its worlds"

File: `book2/chapters/05-the-soul-and-its-worlds.md` (rebuilt 2026-10-16). Brief: `docs/briefs/05-case.md`. Checked against `sources/extracts/*.md` (page markers `[p. N]`), `sources/quran/en.qarai.txt`, `sources/bibliography.bib`, `docs/GLOSSARY.md`, `transcripts/text/Irfan04.md` (¶51–89) and `Irfan05.md` (all). Earlier review: `reviews/book2-05.md`.

Counts: **High 1 | Medium 11 | Low 15**

Line numbers are the chapter file's. Where a fix changes a point box, change the matching sentence in the prose too.

## What the rebuild fixed (from `book2-05.md`)

- "Shomali names what this implies about reward and punishment" is gone; Shomali's p. 77 sentence is now quoted correctly (but see H1, M1).
- The "not something prepared somewhere else" sentence is gone.
- The Khomeini "accounts for the different lists" gloss is gone; the p. 32 quotation is now bare.
- The graveside claim about "the one we bury" is gone.
- "Mirza ʿAli Aqa Qadi" is supported: `kernel` line 178 and line 2154 give "Hajj Mirza ʿAli Aqa Qadi". The old Low is closed.
- "fourteenth century" is gone. "until lying costs no effort at all" is now "little effort" (matches p. 20).

---

## HIGH (1)

**H1. The book's own application of Shomali is not marked as the book's, and is partly put in his mouth.**

- Line 137: "Shomali makes the same point about reward and punishment in general: 'Sometimes rewards or punishments are nothing other than the actions. They are just the realities of those actions made manifest in another universe.' [@self_knowledge, p. 77] On this reading, the light of the faithful is their own good deeds, made visible."
- Line 117 (point box, step 5): "The light of the faithful is their own: a reward can be the deed itself made visible."
- Line 137, earlier: "It is their own light."
- Problem:
  - The quotation is exact (p. 77, "C. Unity"). Shomali says "sometimes" and gives it as one of three kinds of relation between acts and rewards. He does not mention Q 57:12 or light.
  - "The same point" claims he made the point about this verse. "On this reading" has no owner; after "Shomali makes…" a reader will assign the reading to him.
  - Nor does the lecture say it. L05 ¶12 reads Q 57:12 as faces and bodies that "carry light which would enlighten their way", which is the shining image body, not a reward made of deeds.
  - The premise box states the inference as fact.
- Fix, prose: "Shomali states a general principle about reward and punishment: [quotation, p. 77]. He does not apply it to this verse. Applied here, it would mean the light of the faithful is their own deeds made visible. That reading is this book's, not his or the lecture's. The lecture takes the light to be the shining of the pious person's body (L05 ¶12)."
- Fix, premise 5: "Shomali holds that some rewards are the deeds themselves made visible; the book suggests the faithful's light may be one."
- Delete "It is their own light." or mark it as the verse's "their light".

---

## MEDIUM (11)

**M1. "In Shomali's words" attached to the book's conclusion (line 139).**

- Sentence: "If a reward can be the deed itself made visible, the form a soul meets after death is largely its own deeds. In Shomali's words, 'our future is now present' [@self_knowledge, p. 77]. The image body is being shaped now, by what we do."
- Problem:
  - The quote is exact, p. 77, but it follows "Heaven and hell have been created now" and "Whoever is good, is now in heaven and criminals or sinners are now in hell". It comes before the typology, not as its conclusion.
  - Shomali is not talking about an image body being shaped.
  - The step from "a reward can be the deed" to "the form is largely its own deeds" is the book's, not a source's.
  - Shomali says "sometimes"; "largely" widens it.
  - L05 ¶12 says the Day of Judgement body is "different from this misaali body", yet the paragraph runs image body, Last Day groups and Q 57:12 together. Khomeini p. 41 does cover both ("whether it is in the Barzakh … or on the Last Day"), which helps.
- Fix: "Shomali draws a related conclusion from heaven and hell already existing: 'our future is now present' (p. 77). The step to the image body is this chapter's: if deeds are shaping the soul now, the form it meets is, in large part, theirs. The lecture adds that the body of the Last Day is not the image body itself (L05 ¶12)."

**M2. Khomeini's "second form" equated with the lecture's *badan mithali* (line 125).**

- Sentence: "Imam Khomeini describes this second form in his *Forty Hadith*."
- Problem: `forty_hadith` p. 41 speaks of "another form and a different face … heavenly and invisible", in "the Barzakh … or … the Last Day". It never says *badan mithali*. The identification is the book's.
- Fix: "Imam Khomeini describes what looks like the same thing…" or "a comparable second form".

**M3. "The two uses meet" is uncited exegesis, and a source is misattributed (line 56, Word Study).**

- Sentence: "The ʿurafaʾ use the same word for the world of images, which stands between matter and pure intellect. Mohammad Ali Shomali notes that philosophers compare the body of that world with the bodies we see in dreams, and 'call them "Barzakh" or "mithali"' [@self_knowledge, p. 76]. The two uses meet: the barrier between this life and the resurrection is the middle world the dead now live in."
- Problem:
  - The ʿurafaʾ use matches L05 ¶4 and L04 ¶63, so that sentence is fine. Shomali's "philosophers" are a different group, which is fine as written.
  - The last sentence has no source. Q 23:100 gives a barrier "until the day they will be resurrected". It says nothing about a world of images, and no held tafsir is cited.
- Fix: "The lecture links the two: the middle world is called barzakh both because it stands between matter and intellect and because the dead are in it until the resurrection (L05 ¶4, ¶6)." Or cut the sentence.

**M4. Q 23:99–100 generalised and its rebuke dropped (line 56).**

- Sentence: "When death comes, a person asks to be taken back so that he may act righteously in what he left behind. He is told that a barzakh stands before him until the day he is raised (Q 23:99–100)."
- Problem:
  - Qarai: "When death comes to one of them, he says, 'My Lord! Take me back, that I may act righteously in what I have left behind.' 'By no means! These are mere words that he says.' And before them is a barrier until the day they will be resurrected."
  - "Them" in the preceding verses (23:90–96) are those who ascribe partners to God.
  - The chapter makes it any person, drops "By no means!", and makes the barrier a statement to him.
- Fix: "The Qur'an uses it of death too. One of the deniers, when death comes, asks to be sent back to act righteously, and is refused: 'By no means! … And before them is a barrier until the day they will be resurrected' (Q 23:99–100)."

**M5. The lecturer's qualification "with some difference" is lost (lines 32, 49, 51, 53).**

- Sentence (line 49): "In Sheikh Bahmanpour's words, the world of images 'is another dimension of the same world in which we are living', and so is the world of intellects."
- Problem: L05 ¶4 says "aalamul-oqul as well is another dimension but with some difference". L05 ¶15 says the Day of Judgement "is a bit different". The chapter flattens both in line 49, in "each is a deeper dimension of this one" (line 32), and in "Even the resurrection is not a journey elsewhere but a move deeper still" (line 53). ¶6 does say the resurrection is "another deeper and deeper dimension", so the last is fine. Only the intellect and Judgement qualification is lost.
- Fix: "…and so, with some difference, is the world of intellects." In the point box: "the world of images is another dimension of this one, and the world of intellects is too, with some difference."

**M6. The dua's "sleep" is a metaphor, and the opening runs it into literal sleep (lines 11–13).**

- Sentences: "The prayer sets sleep beside the meeting with God. The tradition does the same. *Lantern of the Path*… calls sleep 'the brother of death'."
- Problem: in the Munajat, "sleep" is the figure for neglect (*ghafla*): "my disregard for preparations to meet You has put me to sleep". The Lantern's sleep is literal (it is advice for going to bed). "Does the same" claims one idea in both. That link is the book's.
- Fix: "The prayer uses sleep as a picture of heedlessness. The Lantern… takes real sleep as a lesson in death…" Or drop "The tradition does the same" and start the sentence "The tradition also speaks of sleep…".

**M7. Theology: the world of images "exists on its own / in its own right" (lines 29, 43).**

- Sentences: "our imagination is a sample of a world of images that exists on its own." and "the world of images depends on no one's mind and exists in its own right."
- Problem: the lecture means independent of human minds (L05 ¶21, garbled; L04 ¶64). "On its own" and "in its own right" can be read as independent of God, who creates and sustains the worlds. The lecturer is clear that Allah is the creator (L05 ¶3, "creation of Allah").
- Fix: "…a created world of images that does not depend on anyone's mind." Also line 43: "exists whether or not anyone imagines it."

**M8. Theology: "Pure spirit and a body of clay have nothing in common" (line 76).**

- Sentences: "The Qur'an says that God breathed of His spirit into the first human being (Q 15:29). Pure spirit and a body of clay have nothing in common, so something that reaches both stands between them."
- Problem:
  - Read plainly, "His spirit" can't reach clay without a go-between, which limits God.
  - L04 ¶65 says "that ruh and this matter can never come together. A medium was needed", with the *ruh* meaning the world of pure spirit.
  - L05 ¶32 corrects the other reading: "Allah doesn't have ruh because Allah is not composed… this ruh as well is a dignified ruh which is the greatest creation of Allah". "His spirit" is an honorific attribution.
  - "Nothing in common" and "body of clay" are the book's words (Q 15:28 mentions clay but is not cited).
- Fix: "…breathed into him of His spirit (Q 15:29), a spirit the lecture says is God's greatest creation, called His out of honour, since God is not composed (L05 ¶32). Pure spirit and matter cannot meet directly (L04 ¶65), so the soul is the means by which the spirit reaches the body."

**M9. Theology: "in our hands" without God's part (lines 106, 195, point 11 line 156).**

- Sentences:
  - "How far a soul travels is not settled at its creation, as an angel's station is, but by the life the soul lives." (106)
  - "What the soul finally becomes has been entrusted to us, and it is in our hands." (195)
- Problem:
  - The lecturer says "no one knows how far it can go" (¶8) and that the drive to start "comes … [as] the grace of god" (¶19, "Zaalika fadlul laahi").
  - The appointed time of death is Allah's (L04 ¶70).
  - The chapter's heading echoes "entrusted to us… do whatever we want" (¶55) but drops the grace. "Not settled at its creation… but by the life" can read as denying God's decree.
  - Q 12:53 does keep His mercy in view, but the closing summary does not.
- Fix, line 106: "How far a soul travels is not fixed in advance as an angel's station is; no one knows how far it can go (L05 ¶8)." Line 195: "…has been entrusted to us. The drive to begin is itself God's grace (L05 ¶19), and the rest is in our hands."

**M10. "Remembrance alone gives it" and "the first" rest on garbled lecture text and go beyond the verse (lines 152, 183, 189).**

- Sentences:
  - "The first is the remembrance of God (*dhikr*)…"
  - "The rest that this verse promises is the peace of the third state, and remembrance alone gives it."
  - Point 7: "The first act that moves the self is the remembrance of God."
- Problem:
  - L05 ¶57 is garbled ("If you want nafsul mutmainnah, qalb is nafs. If you are nafsul mutmainnah, only remembrance of God can give you peace").
  - D39 says to go around garbled passages. "First" is not in the lecture; the order in the chapter comes from the book.
  - Q 13:28 says hearts find rest in remembrance and does not say "alone".
- Fix: "The lecture names remembrance of God as what refreshes and revives the soul (L05 ¶57), and Q 13:28 promises rest to the hearts that remember." Drop "alone" and "first" (point 7: "Remembrance of God refreshes the soul, and the Qur'an promises rest in it").

**M11. Box: Khomeini's levels folded into a claim about the names (line 180).**

- Sentences: "The ʿurafaʾ give the one soul several names, one for each depth it reaches." and "However they are counted, the names describe one soul at different depths."
- Problem:
  - `light` p. 58 says "sometimes they call it nafs… sometimes qalb…". It does not say "one for each depth". It does say "levels beyond this".
  - Khomeini's "seven… four… three… two" (`forty_hadith` p. 32) concerns the *levels* of the soul's inner life, each with guardian hosts, not the nafs/qalb names or the three-versus-four states.
  - Amuli's four are states of the self ascending (`inner_secrets` p. 192), not depths.
  - The last sentence unifies all three: the book's synthesis, shown as the sources'.
- Fix: "The book's reading is that these lists divide one soul differently; none of the sources says so in those words." Or: "Each list divides the same soul, as Mutahhari says of the names: 'different words for the human soul' (p. 58)."

---

## LOW (15)

**L1. Overstates "can" (lines 98, 195).**
- "Each time, the soul reaches the world of images." and "It passes into the middle world a little each night in sleep."
- L04 ¶68: "you can start perceiving"; "it can go". "A little each night" is not in the lecture.
- Fix: "Each time, the soul can reach…"; "it can touch the middle world in sleep".

**L2. Dream details are the book's (line 41).**
- "A dream does the same more vividly. People move and speak in it. They have faces, sizes, and coloured clothes, and none of it is matter."
- L04 ¶64 says only "dimensions… colours, but… no matter".
- Fix: "A dream shows a person with dimensions and colours but no matter (L04 ¶64)."

**L3. Added illustrations (lines 39, 47, 41).**
- "things with weight that take up space, such as a table, a hand, or the rain"; "it weighs nothing"; "Pure intellect and matter have nothing in common"; "Only then does it reach the world of matter."
- L04 ¶63 says they "cannot come together" and a medium is needed. The "nothing in common" and "only then" wording is the book's. L04 ¶74 mentions "table" only in passing.
- Fix: use "cannot meet directly" and drop "nothing in common"; keep the examples if the project allows plain illustrations, otherwise mark them.

**L4. Imams "at will" in the book's voice (line 92).**
- "…whereas the Imams (as) can pass between the worlds at will."
- Fine to the lecture (L04 ¶72), but unattributed.
- Fix: "…and the Sheikh adds that the Imams (as) can pass between the worlds whenever they wish."

**L5. "Never deforms" and a garbled source (line 123).**
- "A pious person's face can even carry light. In this world, though, the change is slow and small. It never deforms the body."
- L05 ¶10: "it doesn't deform", from a garbled sentence ("very, very painful you will see light on their face").
- The "pious" reading is likely but not certain (D39). L05 ¶12 supports shining of the image body.
- Fix: "does not deform the body" for "never deforms"; consider dropping the face-light sentence.

**L6. Line 43, "The difference is that the picture in our mind belongs to us…"**
- Rests on L05 ¶20–21, both garbled ("independent of mindless people"). L04 ¶64 is clear: the person seen in the dream is not in your mind.
- Fix: cite L04 ¶64 as the clear passage.

**L7. Q 89:27 cited for "calls back to its Lord" (line 175).**
- "Surah al-Fajr calls this self back to its Lord (Q 89:27)."
- 89:27 is "O soul at peace!" and the return is 89:28. The brief says name 89:27 only.
- Fix: "(Q 89:27–28)".

**L8. "The Qur'an names the self in three states" (line 161).**
- The Qur'an gives three descriptions of the self in three verses. Calling them lowest to highest states of one self is the lecture's (L05 ¶46–48).
- Fix: "The lecture reads three Qur'anic names for the self as three states."

**L9. "The one thing that checks it" (line 167).**
- "The verse admits what this self does and names the one thing that checks it, the mercy of God."
- Contradicted a few lines later by remembrance, fasting and night prayer.
- Fix: "names what overcomes it, the mercy of God".

**L10. "That God swears by this self shows its worth" (line 175).**
- A usual reading but uncited. Fix: attach a source, or "suggests".

**L11. Arabic not byte-identical (line 7).**
- Words match `duas-munajat-shabaniyah.md` §118–119, but the marks on نَبَّهَتْنِي differ in order between the chapter and the extract (grep for the extract's form fails).
- Fix: copy the string from the extract.

**L12. GLOSSARY departures (lines 161–177, 180).**
- Chapter: *al-nafs al-ammara / al-lawwama / al-mutmaʾinna*; glossary: *nafs al-ammara / al-lawwama / al-mutmaʾinna* (lines 138–141).
- The box glosses *sirr* as "the mystery" (Mutahhari's translation) while the glossary (line 176) and L05 ¶33 say "the secret layer".
- Tabatabaʾi, Qadi and Amuli are in no glossary entry.
- Fix: align the spellings, or add the variants.

**L13. Opening framing (line 13).**
- "…and many of us picture a waiting room somewhere far away."
- The brief approves it, but it is the book's observation, not the lecture's.
- Fix: leave, or "a picture many of us carry".

**L14. Trimmed Lantern quote (line 200).**
- "be aware of the fact that you are incapable and weak" is exact (p. 24), but the next sentence is cut: "You have no power over any of your movements and stillnesses, except by the judgement and measure of Allah."
- The cut makes the weakness about the self instead of about God's sovereignty.
- Fix: include the clause, or say "followed by".

**L15. "A Shia master of an earlier age" (line 180) and bibliography marker.**
- Amuli's era has no citation; the held book is the only source. `bibliography.bib` line 69 (`inner_secrets`) still carries a `[VERIFY]` on the Arabic title.
- Fix: "a Shia master" with no date, and resolve or leave the bib note.

---

## Verified clean

**Citation keys.** All seven exist in `bibliography.bib`: `light`, `duas_munajat_shabaniyah`, `lantern`, `self_knowledge`, `forty_hadith`, `kernel`, `inner_secrets`.

**Quotations, word for word, at the cited page** (page markers in the extracts):
- `light` p. 166: epigraph English exact.
- `light` p. 58: the Mutahhari quotes ("dominated and ruled by desires and passions they call it nafs"; "the light of Divine love dawns within it"); khafi/akhfa.
- `lantern` p. 24: "the brother of death"; the intention ("to lighten your burden on the angels and disengage the self from its appetites, and to examine yourself by your sleep"); "be aware of the fact that you are incapable and weak".
- `lantern` p. 25: "last affair in this world"; "with your heart and your tongue".
- `self_knowledge` p. 20: "the soul becomes inured to the effects".
- `self_knowledge` p. 21: "according to their true natures".
- `self_knowledge` pp. 75–76: "but to a lesser degree than waking"; "belongs to another body which has the qualities of a material body like shape and size without the mass".
- `self_knowledge` p. 76: "call them 'Barzakh' or 'mithali'".
- `self_knowledge` p. 77: both quotations.
- `forty_hadith` p. 41: both quotations.
- `forty_hadith` p. 32: "sometimes into seven sections and sometimes into four", plus "three… two".
- `kernel` p. 17: "these lights belong to the class of entities of the realm of Barzakh"; "he might see himself standing before himself"; the Qadi paragraph exact (including the mole).
- `inner_secrets` p. 192: the four terms.

**Qur'an text** (Qarai) exact and Arabic `words=` ranges correct:
- 39:42 `words="1-10"`
- 57:12 `words="1-9"`
- 12:53 `words="4-11"`
- 13:28 `words="7-11"`
- Full verses: 37:164, 75:2, 78:18.
- Described accurately: 25:53, 15:29. Q 23:99–100 is described inexactly (see M4).
- Q 57:12 correctly replaces the lecture's "56:12".

**Lecture claims, in cited ¶ and fairly put (except as noted above):**
- L05 ¶3–6: the three worlds, "envelope", "we don't go anywhere".
- L05 ¶7–9: the image body; angels' "known place" (37:164); soul and Adam.
- L05 ¶10, ¶12: sin deforms, piety shines.
- L05 ¶21–23: imagination and intellect as samples.
- L05 ¶33: sirr "not known but to Allah"; khafi hidden "even to the angels".
- L05 ¶46–49: one nafs, "we don't have different types of nufus", the three states, worry for children and a job.
- L05 ¶50–53: habit, fasting, Ramadan light, night prayer.
- L05 ¶54–56: elastic soul, "would remain with us forever".
- L04 ¶61–66: the soul as compact copy; mulk/mithal/uqul; barzakh as intermediary.
- L04 ¶67–68: time; sleep, "if it comes out completely you are gone".
- L04 ¶69: "The body is not carrying the soul but the soul is carrying the body".
- L04 ¶70–72, ¶76: muraqaba; Tabatabaʾi; "I don't mean that your soul comes out of the body".
- Cuts respected: no Hasanzadeh, Nakhudaki/Reza Shah, Friday-night hadith, animal faces, Plato or "recite and ascend". Q 89:27 is named, not quoted.

**Markers.** No `[VERIFY]`, `[QUERY]` or `[GAP]` in the chapter (only the bib note in L15).

**Theology.** Nothing says God is acted upon or diminished in the chapter's own voice, other than the readings in M7–M9. These stay in the lecturer's own words and need no change:
- "God pours down His light" (L05 ¶51)
- "closer to the majesty and beauty of God" (L05 ¶6)
- "God takes the soul" (Q 39:42)

**Argument vs brief.**
- Section order and the four headings match the brief's 5.1–5.4; steps 1–9, 1–10, 1–6 and 1–11 are in dependency order.
- Step 5 of section 3 (H1) is stated as established when it is the book's inference; the conclusion (step 6) rests on it.
- Section 3 also moves from the image body to the Last Day without saying so (M1).

**Not checked.** Tone and `LINGO.md` were out of scope for this pass. Body text is an estimate of about 3,400–3,800 words (not counted), so it may sit at the 3,600 cap.

---

**Verdict: PASS WITH FIXES.** One High (H1): mark the Shomali-to-light step as the book's own inference in the prose and the premise box. It is a quick edit. The Mediums are all attribution, nuance or theological-wording fixes, none factual errors in a quotation.
