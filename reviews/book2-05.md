# Fidelity review: Book 2, Chapter 5, "The soul and its worlds"

File: `book2/chapters/05-the-soul-and-its-worlds.md`. Brief: `docs/briefs/05-case.md`. Sources checked: `sources/extracts/*.md`, `sources/quran/`, `transcripts/text/Irfan04.md`, `transcripts/text/Irfan05.md`.

Counts: **High 0 | Medium 5 | Low 10**

## Findings

| Sev | Line | Issue | Fix |
|---|---|---|---|
| Medium | 109 and 111 | An inference is put in Shomali's mouth. Line 109: "Shomali names what this implies about reward and punishment" links his "Unity" point to Q 57:12, but `self_knowledge` p. 77 never mentions that verse. Line 111: "Shomali draws the conclusion that 'our future is now present'" after "If a reward can be the deed itself…". In p. 77 the sentence comes *before* the typology and rests on heaven and hell already existing ("Heaven and hell have been created now", p. 76). | Line 109: "Shomali states the principle in general terms. 'Sometimes rewards or punishments are…'". Line 111: "Shomali also writes that 'our future is now present', since heaven and hell already exist [p. 77]." Keep the step from deed to image body as the chapter's own, cited to the lecture (L05 ¶10–14). |
| Medium | 39 | "What the dead meet in the middle world is the deeper side of the life they lived here, not something prepared somewhere else." This is not in L04/L05. L05 ¶5 says the Qur'an's pleasures are in the middle world, and Shomali p. 76 says heaven and hell "have been created now". "Not something prepared" can read as denying what God has prepared. | Cut the sentence, or: "…they have passed into a deeper dimension of the world they lived in." |
| Medium | 42 (Word Study, last two sentences) | Uncited exegesis. Q 23:99–100 (Qarai) reads "When death comes to one of them, he says, 'My Lord! Take me back, that I may act righteously in what I have left behind.'" "Those who die unprepared", "the good they left undone" and "The barrier divides a life in which deeds can still be put right from one in which they can no longer be" are the chapter's glosses. | Quote Qarai's wording and drop the last sentence, or cite a held tafsir. None is held for this verse. |
| Medium | 142 (Word Study) | "Imam Khomeini accounts for the different lists" and "every list divides the same soul". `forty_hadith` p. 32 only says the soul's levels "are generally divided sometimes into seven sections and sometimes into four… three… two". It does not mention nafs/qalb/ruh/sirr, and gives no account of why lists differ. | "Imam Khomeini notes that the soul's levels are divided 'sometimes into seven sections and sometimes into four', and sometimes into three or two [p. 32]. The lists differ in how they divide, not in what they divide." |
| Medium | 111 (last sentence) | "the one we bury at a graveside has gone on in the shape their deeds gave them" is a claim about the actual deceased. No source says it. Khomeini p. 41 says the form follows the state of the soul at departure, and the Sheikh says nothing about particular dead. It is also pastoral ground. | Cut it, or put it generally: "each soul goes on in the form its deeds have been giving it." |
| Low | 37 | L05 ¶4 says the world of intellects is "another dimension but with some difference". L05 ¶15 says the Day of Judgement "is a bit different". "so is the world of intellects" and "each is a deeper dimension" drop that qualification. | "…and so, with some difference, is the world of intellects." |
| Low | 27, 29, 35, 51 | Embellishments beyond the lecture and cited sources. "things with weight … a table, a hand, or the rain" (Shomali says "mass" only for the image body). "people who move and speak … clothes of a certain colour" (L04 ¶64 says only dimensions and colours, no matter). "without its weight". "a body of clay" (not in L04 ¶65). | Cut or soften: "no matter" in place of "no weight", drop the clothes, "a body of matter". |
| Low | 69 | "he spoke of them as a gift" attributes to Tabatabaʾi what the Sheikh says of mystics in general (L04 ¶72: "For mystics it is just opportunity given by Allah"). Tabatabaʾi's own words in ¶72 are "the more I have muraqabah… more clearly I can see". | "They came when God gave them, the Sheikh says of such experiences, not when he chose;…" |
| Low | 72 (Story box) | The source says "Hajj Mirza Aqa Qadi"; the box writes "Mirza ʿAli Aqa Qadi". Qadi and Shahabadi/Amuli are not in GLOSSARY. | Use the source's form, or add a glossary entry stating the identification. |
| Low | 139 | "a Shia master of the fourteenth century" is an added fact with no citation. | Cite or drop the date. |
| Low | 89 | "until lying costs no effort at all": Shomali p. 20 says "with little effort or discomfort". | "…until lying costs little effort." |
| Low | 89 | The framing ("it can seem that what we do here changes little") is the chapter's own. The Sheikh's actual answer to "what's the point?" (L05 ¶18–19) is a different one: the forerunners here are forerunners there, and the drive is a grace. It is not attributed, so not wrong. | No change needed, unless the answer is later credited to the Sheikh. |
| Low | 7 (Arabic) | Text matches §118–119. The marks in "نَبَّهَتْنِي" are stored fatha+shadda in the chapter and shadda+fatha in the extract. Same reading, not byte-identical. | Copy the string from `duas-munajat-shabaniyah.md` §118–119. |
| Low | 119, 16, 142 | GLOSSARY departures. The chapter writes "al-nafs al-ammara / al-lawwama / al-mutmaʾinna"; the glossary has "nafs al-ammara" etc. Line 142 glosses *sirr* as "the mystery" (Mutahhari, `light` p. 58); the glossary and L05 ¶33 say "secret". | Align to the glossary, or add the variant. |
| Low | 93 | "Imam Khomeini describes this second form" equates his "heavenly and invisible" form with the lecture's *badan mithali*. Plausible, but Khomeini does not say so. | "describes a comparable second form". |

## Verified clean

- **Citation keys** exist in `bibliography.bib`: `light`, `duas_munajat_shabaniyah`, `lantern`, `self_knowledge`, `forty_hadith`, `kernel`, `inner_secrets`.
- **Duʿa** (§118–119, `light` p. 166): English exact, and the Arabic is textually identical (marks aside, see low item).
- **Qur'an English and `words=` ranges** (Qarai text, whitespace word-count):
  - 39:42 `words="1-10"` (…في منامها): exact.
  - 57:12 `words="1-9"` (…وبأيمانهم): exact.
  - 12:53 `words="4-11"` (إن النفس لأمارة بالسوء إلا ما رحم ربي): exact.
  - 13:28 `words="7-11"` (ألا بذكر الله تطمئن القلوب): exact.
  - Full verses 37:164, 75:2, 78:18: exact.
  - Cited, not quoted: 25:53, 23:99–100, 15:29, 89:27.
  - Q 57:12 correctly replaces the lecture's "56:12".
- **Quotations exact at the cited page:**
  - `lantern` p. 24 ("the brother of death", the Try-this intention, "incapable and weak") and p. 25 ("last affair in this world", "with your heart and your tongue").
  - `self_knowledge` p. 20 (lying); p. 21 (true natures; veil lifted; bug/angels); pp. 75–76 (sleep/death, "shape and size without the mass"); p. 76 ("Barzakh" or "mithali"); p. 77 (both quotations).
  - `forty_hadith` p. 41 (both quotations) and p. 32 (the quotation itself).
  - `light` p. 58 (Mutahhari's four, khafi/akhfa).
  - `kernel` p. 17 (all three quotations, including the Qadi mole story).
  - `inner_secrets` p. 192 (four states, both verse lines).
- **Transcript claims:** fairly put and in the cited ¶s. All of these are fine.
  - L05 ¶3–6: the dimensions, envelope, resurrection not a journey, and "we don't go anywhere" at ¶6.
  - L04 ¶61–66, ¶85–86: the three worlds, the intermediary.
  - L05 ¶21–23: imagination and intellect as samples.
  - L04 ¶64, ¶67–68: sleep and dreams.
  - L04 ¶69: "The body is not carrying the soul but the soul is carrying the body".
  - L04 ¶70–72, ¶76: muraqaba, "I don't mean that your soul comes out of the body", Tabatabaʾi.
  - L05 ¶7–8: angels with a known place and the soul with none.
  - L05 ¶10–14: sin deforms and piety brightens the image body.
  - L05 ¶46–50: one nafs, "we don't have different types of nufus", the three states.
  - L05 ¶33, ¶43–44: the lecture's list in the box.
  - L05 ¶50–53: fasting and the night prayer.
  - L05 ¶54–57: the elastic soul and "would remain with us forever".
- **Cuts respected:** Hasanzadeh, Nakhudaki/Reza Shah, Friday-night hadith, animal-faced seers, Plato, and "Recite and ascend" are all absent. Q 89:27 is named only.
- **God acted upon or diminished:** none. "Allah pours down His light" (L05 ¶51) and "closer to the majesty and beauty of God" (¶6) are the lecturer's own.
- **Theology:** nothing changes the lecturer's position. "In our hands" is the lecturer's own framing (¶55–56). Q 12:53 keeps God's mercy in view.
- **Cross-references:** Ch 1 "not powers", Ch 4 (Q 15:29, Q 59:19), Ch 8 and Ch 17 all exist.
- **`[VERIFY]` / `[QUERY]` / `[GAP]` markers:** none.

**Verdict: PASS WITH FIXES.** Five medium items: the Shomali attributions (109, 111), the "not prepared" sentence (39), the 23:99–100 box gloss (42), the Khomeini "accounts for" gloss (142), and the graveside claim (111).
