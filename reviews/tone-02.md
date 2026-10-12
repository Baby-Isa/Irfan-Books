# Tone review: Book 2, Chapter 2 ("Knowing about God is not knowing Him")

Chapter: `book2/chapters/02-knowing-about-not-knowing.md`. Brief: `docs/briefs/02-case.md`.
Read against: prologue and Ch 1 (exemplar), EXEMPLAR.md, TONE.md 1–22, LINGO.md, VOICE-TEST.md "The tells the judges used most".
Edits were applied to the chapter (28). No quotation wording, citation or `[VERIFY]` marker was altered.

## Checks in brief
1. **Section points.** Every paragraph serves its `::: {.point}` note. No section carries a second point.
2. **Paragraph links (TONE 1).** The first sentences follow as a chain. Two openers were weak: "Purification has a first step, and the Sheikh names it" and "Where ʿilm divides and defines…". Both were fixed. **Ch 1 → Ch 2:** Ch 1 ends "If the aim is to know and love God, what kind of knowing is that?" The opener answers with the Sheikh's hunger example. Its second paragraph now picks up the question in words ("…and that the aim is to know and love God. The knowing it means is the kind the fasting person has of their hunger").
3. **Paragraph length (TONE 16, 22).** All body paragraphs are under 110 words. The longest is Khomeini on study, at about 90. The average is about 60, which is in range. Two stub paragraphs ("Reason is not left with nothing to do…", 25 words) were merged with the next one.
4. **Sentences.** Most are 14–19 words. Six "and" chains were split, and five unclear referents were named.
5. **Stance.** There is no lecturing, presumption or banned lingo. No sentence opens with So/Well/Look/Now/And/But/Hence. Intensifiers appear only inside quotations ("very minor", "in order to"). "You" appears only in the Sheikh's quotation and in Try this.
6. **Quotations.** Each is spoken to and short. The Sheikh is quoted only for weight-bearing lines. The colon-plus-quotation tell does not occur: every quotation is introduced in its own clause. See the open flag on Try this below.
7. **Repetition.** Four repeats were cut: "none of it is missed" (opener and ¶6), the *husul* gloss (prose and Word Study), "sets fikr against suluk" (twice in §4), and "wait for Allah" (quotation, gloss, and a closing counsel).
8. **Profile.** There was no shell, so `voice.py profile/openings` was not run. The figures above were counted by hand. **Run `python3 build/voice.py profile book2/chapters/02-knowing-about-not-knowing.md` before the judge.**
9. **Judge's tells (hunted on request).** Three inverted openings ("What they cannot say is…", "What is closed is…", "What ʿirfan wants to know… is"), two tidy closers and one comment on the manner of a quotation ("adds at once") were fixed.

## Edits (applied)

| # | Location | Before | After | Rule |
|---|---|---|---|---|
| 1 | Opener ¶1 | "The hunger is known from the inside, and none of it is missed." | "The hunger is known from the inside." | 14 (repeated in §1 ¶4) |
| 2 | Opener ¶2 | "Chapter 1 argued that the Qur'an invites more than the minimum. The more it invites is the kind of knowing the fasting person has of their hunger:" | "Chapter 1 argued that the Qur'an invites more than the minimum, and that the aim is to know and love God. The knowing it means is the kind the fasting person has of their hunger:" | 1 (picks up Ch 1's hand-off question); 13 ("The more it invites") |
| 3 | §1 ¶1 | "The first is acquired knowledge, *ʿilm al-husuli*; *husul* means to acquire." | "The first is acquired knowledge, *ʿilm al-husuli*." | 14 (the Word Study box glosses *husul*) |
| 4 | §1 ¶2 | "*hadd*, also means a limit, and Sheikh Bahmanpour draws the lesson from the word: to define a thing is to limit it." | "*hadd*, also means a limit. Sheikh Bahmanpour draws the lesson from the word: to define a thing is to limit it." | 12, 15 |
| 5 | §1 ¶4 | "The hunger may even be false, he notes, yet the feeling is real, and it drives us." | "The hunger may even be false, the Sheikh notes, yet the feeling is real and drives us." | 13 ("he" has no antecedent in the paragraph); 12 |
| 6 | §1 ¶4 | "but the feeling comes from inside the soul, and the cause is not the feeling." | "but the feeling comes from inside the soul; the cause is not the feeling." | 12 |
| 7 | §1 ¶6 | "Where ʿilm divides and defines, maʿrifah turns inward, and it is bound up with purifying the self." | "Maʿrifah turns inward, and it is bound up with purifying the self." | judge tell (inverted, balanced opening); 21 (re-states §1 ¶2) |
| 8 | §1 ¶7 | "When they speak of ʿilm they mean maʿrifah, and they do not count…" | "When they speak of ʿilm they mean maʿrifah; they do not count…" | 12 |
| 9 | §1 ¶8 | "Imam Khomeini and Murtada Mutahhari draw the same line between the two kinds of knowing." | "Imam Khomeini and Murtada Mutahhari draw the same line as the Sheikh between the two kinds of knowing." | 1, 13 ("same" as what?) |
| 10 | §1 ¶8 | "The word he uses for that witnessing" | "The word Imam Khomeini uses for that witnessing" | 13 (Imam ʿAli is also in the sentence before) |
| 11 | §2 ¶2 | "…no function for the mind to take hold of. The mind knows by analysing, and in Him it finds nothing to analyse." | "…no function for the mind to take hold of." | judge tell (tidy balanced closer); LINGO aphorism test |
| 12 | Story box | "Sheikh Bahmanpour tells how Ibn Sina, the master of philosophy, changed" | "Sheikh Bahmanpour tells how Ibn Sina changed" | 14 (the epithet was given two lines earlier) |
| 13 | Story box | "is beyond human capacity came before it." | "is beyond human capacity came before he wrote that section." | 13 (L03 ¶25: "this was before he wrote that maqamat") |
| 14 | §2 ¶3 | "Imam ʿAli (ʿa) says the same at the opening of the first oration in *Nahj al-Balagha*, where he praises God." | "Imam ʿAli (ʿa) makes the same point about God at the opening of the first oration in *Nahj al-Balagha*, where he praises Him." | 13 ("the same" across a 160-word box) |
| 15 | §2 ¶5–6 (merged) | "Arguments can show that God exists, the Sheikh says. What they cannot say is what God is. ¶ If reason cannot reach God's essence, it might seem that nothing can be known of Him at all. … What ʿirfan wants to know, he goes on, is God's primordial attributes…" | "Arguments can show that God exists, the Sheikh says, but they cannot say what God is. It might seem to follow that nothing can be known of Him at all. … ʿIrfan, he goes on, wants to know God's primordial attributes…" | judge tell (two inverted openings); 22 (25-word stub merged; the result is about 75 words) |
| 16 | §2 ¶7 | "Such statements are true, and each of them says what God is not." | "Such statements are true; each says what God is not." | 12 |
| 17 | §3 ¶1 | "Sheikh Bahmanpour answers from a hadith on knowledge," | "Sheikh Bahmanpour names the source with a hadith on knowledge," | 13, 20 ("answers" with no question posed) |
| 18 | §3 ¶2 | "The light is not gathered at all; it is placed in the heart, and it is God who places it." | "The light is not gathered at all; God places it in the heart." | 12 |
| 19 | §3 ¶4 | "What is closed is the heart." | "It is the heart that is closed." | judge tell (inverted opening) |
| 20 | §3 ¶4 | "It is all there, and the work of the ʿurafaʾ is to open the heart" | "His knowledge and bounty are all there; the work of the ʿurafaʾ is to open the heart" | 13 ("It"), 12 |
| 21 | §3 ¶6 | "he says, is nonetheless of the second kind, coming" | "he says, nonetheless passes in the second way, coming" | 13 ("second kind" means knowledge by presence everywhere else in the chapter) |
| 22 | §3 ¶7 | "Knowledge that passes from heart to heart usually needs a heart to pass it on. Receiving this light directly from God is possible, the ʿurafaʾ say, but it is difficult, and a traveller usually needs someone else to begin." | "This light usually reaches a traveller through another heart. Receiving it directly from God is possible, the ʿurafaʾ say, but it is difficult; most travellers need someone else to begin." | 1 (near-tautological opener); 12; double "usually" |
| 23 | §4 ¶2 | "Purification is the traveller's part; the light is Allah's to give, and the traveller waits for it." | "Purification is the traveller's part; the light is Allah's to give." | 21 (restates the quotation's "wait") |
| 24 | §4 ¶3 | "Purification has a first step, and the Sheikh names it. The traveller first polishes the soul by doing whatever the Prophet ﷺ has asked; "without this", he says, "there is no maʿrifah"." | "The first step of purification is to polish the soul by doing whatever the Prophet ﷺ has asked; "without this", the Sheikh says, "there is no maʿrifah"." | 1 (same "X has a Y, and the Sheikh names it" shape as §2 ¶1); 15 |
| 25 | §4 ¶4 | "…follows the Prophet completely. His counsel is to put the soul right and wait for Allah's help." | "…follows the Prophet completely." | 14, 21; LINGO closer (third statement of "purify and wait") |
| 26 | §4 ¶7 | "Sheikh Bahmanpour sets fikr against suluk, and three of the great teachers of the tradition speak to how the two relate." | "Three of the great teachers of the tradition speak to how fikr and suluk relate." | 14 (§4 ¶1 already says he sets them against each other) |
| 27 | §4 ¶8 | "He adds at once that "one has to approach a veil…"" | "He adds that "one has to approach a veil…"" | judge tell (commenting on the manner of a quotation) |
| 28 | §5 ¶1 | "The knowing that comes with that nearness is of the second kind." | "The knowing that comes with that nearness is knowledge by presence." | 13 |

## Flagged, not edited (content or quotation; for the writer or the user)
- **Try this:** the tasbih "Glory belongs to my Lord, the Exalted, and Him do I praise" is quoted without its Arabic (TONE 7). Arabic cannot be typed from memory. The writer should add it from a held source or mark it `[VERIFY]`.
- **§4 ¶4 against §3 ¶4 (possible tension):** "The traveller does this in the hope that Allah will choose them" sits two sections after "It is not the case… that Allah picks out some people to receive light". A reader may stumble here. Rewording either line would change content, so it is left to the writer: check L03 ¶47–49.
- **§1 ¶9 closer** "A result in the laboratory is known because it has been observed, not because it has been deduced." This is balanced, but it explains Mutahhari's image (TONE 20). It was kept. If the judge quotes it, cut it.
- **Ending:** the last line is the brief's hand-off word for word ("Purification sounds far off. Is there anywhere an ordinary believer already stands on this path?"). It was kept.
- **Profile not run** (no shell). Run `voice.py profile` and `openings` before the voice-judge.

## Verdict
The chapter is close to the exemplar's voice: the argument chain is clean, paragraphs and sentences are in range, and there is no lecturing or lingo.
The judge's tells were mainly inverted or cleft openings, balanced closers, and "wait for Allah" said three times. All 28 edits are applied.
Ready for the measured profile and a blind judge once the tasbih Arabic and the "choose them" tension are settled.
