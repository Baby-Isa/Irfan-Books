# Fidelity review: Book 2, Chapter 4, "Know yourself, know your Lord"

File: `book2/chapters/04-know-yourself.md`. Brief: `docs/briefs/04-case.md`. Sources checked: `sources/extracts/*.md`, `sources/quran/`, `sources/handouts/`, `transcripts/text/Irfan04.md`.

Counts: **High 0 | Medium 4 | Low 8**

## Findings

| Sev | Line | Issue | Fix |
|---|---|---|---|
| Medium | 73 | `[VERIFY]` on the hadith Arabic can be resolved from held material. `sources/handouts/Irfan_1_Theory.txt` line 471 gives "من عرف نفسه فقد عرف رّبه", attributed there to Amir al-Mu'minin (`bahmanpour_slides` is in the bib). `self_knowledge` p. 9 has the same words in garbled presentation forms, but they read the same when reversed. | Replace the marker with the slide text and add `[@bahmanpour_slides]` to the quote line. The slide text is unvocalised, so do not add vowels from memory. |
| Medium | 103 | "The two readings meet at the same point, that through the soul God is known in part and never completely" is the chapter's synthesis. L04 ¶29 (the denial reading) says "no one can know the lord". L04 ¶33 says the other narrations show "the possibility of knowledge is meant by this hadith and not impossibility of knowledge". The Sheikh never says the two converge. | "The lectures allow the first reading and prefer the second; on either, a complete knowledge of God is out of reach and some knowledge through the soul is not." This is true on both readings (brief wording for ¶29 vs ¶33). |
| Medium | 105 | "God cannot be fathomed, so the meeting the mystics speak of is a nearness, *qurb*, and never a grasp of Him." Khomeini, `forty_hadith` p. 398, says only that those who keep liqaʾ Allah open do not mean "that it is permissible to fathom the mystery of the Divine Essence". He calls the meeting *mushahadah* (witnessing). "Nearness/qurb" is not in p. 398. L04 ¶42–44 defines the meeting as seeing the soul as a reflection of God, not as nearness. | Keep the quotation as the limit only. Then: "So the meeting is no grasp of the Essence. The Sheikh's own picture is a nearness we already stand in (L04 ¶54)." |
| Medium | 15 | Recap of Ch 2: "God … must be found within our own soul". Read literally this puts God inside the soul, which the lecture denies (L04 ¶5: the soul "cannot encompass God"). Ch 2 line 40 says the *knowing* (knowledge by presence) must be found within the soul. | "…the knowing of God, if it is to be more than knowing about Him, must be found within our own soul, because…" |
| Low | 44 (Who's Who) | "one of the most demanding books of mystical theory" is not in `forty_hadith` p. 8, which says only that Shahabadi taught the *Fusus*. The "however, he sent them to the Qur'an" contrast is also the chapter's. | Cut the characterisation or source it. Reword "For the care of the soul, he also told them to attend…". |
| Low | 44 | "their relationship 'was that of a murid with his murshid'" follows "The Imam calls him *shaykhuna*", so it reads as Khomeini's words. In `forty_hadith` p. 8 it is the editor's introduction. | "The introduction to the *Forty Hadith* describes the relationship as 'that of a murid with his murshid'." |
| Low | 41 | "The Munajat's confession names the failure the surah describes, a soul not looked after" links the prayer to 91:10 ("betrays it fails"). No lecture or source makes this link. It also tells a reader reciting the Munajat that they are among those who "fail". | Cut the sentence, or: "The Munajat's confession and the surah's warning both speak of the care the soul needs." |
| Low | 27 | "argued much as philosophy is argued" drops L04 ¶3: the mystics "use arguments which are not used by philosophers", namely what they have unveiled. | "…set out as an account of existence, … in the manner of philosophy, though its starting point is what the mystics have seen." |
| Low | 69 | The lecture names "evolution of matter" (L04 ¶18). The chapter's "theories that put everything down to chance" is a gloss, and evolution is not a theory of chance. | Use the lecturer's terms: "a person can suppose that matter evolved into it". Keep "in the lectures' account". |
| Low | 82 (Word Study) | "shares its root with maʿrifah and ʿirfan" has no citation. The line also gives "Muhammad Ali Shomali", but the bib and Ch 1 and Ch 5 write "Mohammad". | Cite the glossary or drop the clause. Use "Mohammad Ali Shomali". |
| Low | 9 (Arabic) | The Arabic matches §32 as text, but the combining marks in "ٱلنَّظَرِ" are stored fatha+shadda, while the extract stores shadda+fatha. Same reading, but not byte-identical. | Copy the string from `duas-munajat-shabaniyah.md` §32 (dropping only "إِلٰهِي"). |
| Low | 44, 116 | Person names (Shahabadi, Maliki Tabrizi) are not in GLOSSARY. | Add before final. |

## Verified clean

- **Citation keys** exist in `bibliography.bib`: `light`, `duas_munajat_shabaniyah`, `forty_hadith`, `lantern`, `self_knowledge`, `journey`.
- **Duʿa** (§32, `light` p. 163): English word-for-word, including "confession of my sins" on p. 163.
- **Qur'an English and `words=` ranges** (Qarai text, whitespace word-count as in `build/irfan.lua`):
  - 91:7–8 (inline), 91:9–10, 59:19, 6:20 `words="8-"` (الذين خسروا أنفسهم فهم لا يؤمنون), 6:31 `words="1-6"` (قد خسر الذين كذبوا بلقاء الله), 5:105, 15:29, 59:18. All exact.
- **Quotations exact at the cited page:**
  - `light` p. 7 ("must see Allah through the window of his own soul"; the Prophet's saying also cited there).
  - `lantern` p. 9.
  - `self_knowledge` pp. 8–9 ("difficult to find a book on ethics (Akhlaq), which has not quoted it").
  - `journey` p. 125 (both quotations).
  - `forty_hadith` p. 8; p. 201 ("very effective for curing the soul…" and the Try-this quotation); p. 398.
- **Transcript claims:** the following are all in L04 and fairly put.
  - ¶7: soul "the means to understand and to learn".
  - ¶12: the whole story of a human being is the soul.
  - ¶13–14, ¶16: most of us have forgotten our souls, with no punishment implied.
  - ¶18–19: the soul that is seen points to its Maker.
  - ¶21–23: the two-way saying, and "the spirit of God is not God".
  - ¶22: the stages of return.
  - ¶31, ¶33: "some understanding, not complete".
  - ¶42–44: removing the layers, the soul as a reflection of God, not God.
  - ¶49: the soul perceives itself.
  - ¶54: quoted exactly, with "We are actually in his presence at the moment. However, he is not in our presence."
- **Cross-chapter callbacks** check out: Ch 1 "rusted" and "muqarrabun/veil removed", Ch 2 knowledge by presence and hunger, the prologue's "veils of light", Ch 3's closing hand-off. Ch 8 and Ch 17 exist in the outline.
- **God acted upon or diminished:** none. Line 107 handles "he is not in our presence" correctly, putting the lack on the soul's side.
- **Markers:** one `[VERIFY]` (line 73, above). No `[QUERY]` or `[GAP]`.
- **Brief compliance:**
  - Cuts respected: no orientalists, Buddhists, Adam "in his image", Cardinal story or angels Q&A.
  - Q 50:16 not used.
  - Not an error: the planned Shomali p. 8 "forgetting Him causes us to forget ourselves" quote is omitted.

**Verdict: PASS WITH FIXES.** Four medium items to fix before sign-off: resolve the `[VERIFY]`, soften the "readings meet" claim, source or reword the qurb inference, and fix "God found within our soul".
