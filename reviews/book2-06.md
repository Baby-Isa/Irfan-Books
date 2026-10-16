# Fidelity check: Book 2, Chapter 6 "No path outside the law"

Chapter: `book2/chapters/06-no-path-outside-the-law.md`. Brief: `docs/briefs/06-case.md`. Checked against the held extracts, `sources/quran/`, `sources/extracts/duas-munajat-shabaniyah.md`, L06 ¶1-72 (plus L09 ¶70-72), and `sources/bibliography.bib`. Line numbers are the chapter's.

Counts: **High 0 | Medium 2 | Low 11** (one low is a no-change note)

## Findings

| Sev | Location (line) | Issue | Fix |
|---|---|---|---|
| medium | l.61 "Shaykh Muhammad Bahari, one of the Shia teachers whose chain Chapter Seven follows [@light, p. 106]" | The identity is an inference. L06 ¶21 says "Ayatullah Muhammadu Bahari ... a contemporary mystic ... an Iranian mystic he has recently passed away". `light` p.106 and `kernel` p.89 name Shaykh Muhammad Bahari as a pupil of Akhund Hamadani, a 19th-century figure. No held source says they are the same man, and "contemporary / recently passed away" does not fit. The brief only says the "recently passed away" was dropped. This puts the chain-member's name on the lecturer's quotation. It is also a forward reference to Ch 7 (D22). Ch 7 l.67 repeats the link ("Bahari gave Chapter Six its rule"). | D39: go around it. Write "Ayatullah Muhammad Bahari, whom the Sheikh quotes, taught that jurisprudence is 'an introductory means'..." and drop "one of the Shia teachers whose chain Chapter Seven follows [@light, p. 106]". Remove the matching clause in Ch 7 l.67. |
| medium | l.13 "The prayer is still valid, since every rule has been kept" | Uncited juristic claim. L06 ¶30 does not say the prayer is valid; it says only that the mind goes elsewhere. L06 ¶9-10 does say jurists would rule two prayers "correct" on form alone. On the same page Khomeini is cited later (l.77), `forty_hadith` p.375: "a worship performed without an attentive heart is devoid of value". A reader may see a clash. A held source separates the two: `forty_hadith` p.293 (extract lines 9887-9891): "there is no necessary relation between the (legal) validity of 'ibadah and its acceptability". | Cite it: "The prayer is legally valid, since every rule has been kept [@forty_hadith, p. 293], yet..." or cut "still valid" and say "every rule has been kept". |
| low | l.33 `[VERIFY: Kubra's ship, sea and pearl, Fawaʾih al-jamal]` | Cannot be resolved from a held extract. I searched all 15 extracts: no Fawaʾih or ship/sea/pearl for Kubra. `inner_secrets` p.50 gives a different image ("river... sea... boats"), as the brief says. The text already says "that he credits to", and L06 ¶15 supports that credit ("what I mentioned in the parable of ship and sea and pearl is from Shaikh Najmal din kubra"). So the marker adds no claim the text needs. | Delete the marker; the sentence is already the Sheikh's credit (L06 ¶15, ¶17). |
| low | l.33 quotation marks "cannot be found except by sailing through the sea, and you cannot sail without a ship" | Word-for-word the Sheikh's own wording (L06 ¶13), not Kubra's text. The sentence says "Sheikh Bahmanpour gives an image" so it is attributed correctly. L06 ¶17 garbles it ("the path is like a ship"); the chapter correctly follows ¶13 (sea). | None needed. Do not add Kubra's name to the quotation itself. |
| low | l.93 `ar="[VERIFY: Arabic of the Prophet's reply, Kernel of the Kernels p. 30]"` | Not resolvable. `kernel` p.30 (extract line 851) gives the reply in English only, and the Arabic is printed only for the Q 48:2 clause. No `duas-*` extract holds it. The placeholder in the `ar` attribute will print in the Arabic slot. | Set `ar=""` (as in the other quotes) and keep the English, or leave the marker for the user. Golden rule 1: no unconfirmed Arabic. |
| low | l.89 "Tabatabaʾi's test matches Kubra's" | They do not quite match. Kubra (L06 ¶18-20): any abandoned injunction means "liars", and the act is magic. Tabatabaʾi (`kernel` p.30): "a hypocrite", excepting "error, an excuse or ... forgetfulness". The chapter states the exception in the same sentence, so only "matches" is loose. | "Tabatabaʾi's test is close to Kubra's." |
| low | l.69 "Sheikh Bahmanpour warns that anyone, of any belief, who goes forty days..." | In L06 ¶66, ¶69 the Sheikh credits this to Tabatabaʾi ("a very nice quotation from Allama Tabatabaii"). It is not in the held Kernel, and `docs/OMISSIONS.md` (L10 ¶44-45) records the rework as the lecturer's own caution. The credit is dropped by design. | Acceptable under D15. Optionally "Sheikh Bahmanpour, recalling a remark of Tabatabaʾi's, warns...". |
| low | l.45 "each of these levels is built on the one below it, and none stands without it" + Amuli footnote | The Sheikh equates islam/iman/ihsan with law/path/truth (L06 ¶43-45). The Amuli rule (`inner_secrets` p.48) is stated only for shariʿa/tariqa/haqiqa. Extending it to islam/iman/ihsan is the chapter's inference. Q 49:14 itself shows islam without iman. | "Like the law, the path, and the truth, each of these is a step above the last" (drop "none stands without it"), or word the footnote as covering the first triad only. |
| low | l.59 Word Study: "A karama ... appears at the hands of someone close to God" | L06 ¶18: "Karama is done by those people who are close to Allah or who ... have found some power". The "or" is what lets Kubra's rule work (a power-holder who is not close to God). | Add "or has found the power of the soul". |
| low | l.106 Try this: "pray at the start of its time ... Imam Khomeini advises ... 'in the most meritorious part of its time'" | Khomeini (`forty_hadith` p.375) says "most meritorious part of its time", not "start". The juxtaposition reads as if he said "start". | "pray in the most meritorious part of its time, with nothing planned straight after it, as Imam Khomeini advises". |
| low | l.77 "A book can hold the mind entirely, so the faculty of attention is not missing." | The chapter's gloss on Khomeini's rhetorical question (`light` p.135, Khomeini's section, Part 3.1). Not his statement. | Present as the chapter's reading, or cut. |
| low | l.11 "Remembering God and keeping His law are asked for in one line." | Tidy closing line (LINGO). The Munajat asks for remembering and thanks and obeying across §124-127, not "one line". | Cut, or "...asked for together." |
| low | l.35, 37, 45 footnote text | The `Cite` filter joins prefix and short form without a separator. The notes will read `...kernel of the kernel." Mutahhari, Tabatabaʾi, and Khomeini, Light Within Me, p. 15.` | Check the rendered PDF; consider ending the prefix with a colon-free "See" form. |

## Verified (no change needed)

- **Quotations, word for word, at the cited page:**
  - `light` p.15 (Mutahhari, "kernel of the kernel") ✓
  - `light` p.135 (Khomeini, "study of a book...") ✓
  - `light` p.166 (Munajat English) ✓
  - `inner_secrets` p.32 (hadith "The shari`ah is my words, tariqah my actions, haqiqah my states"; "Surely prayer is service, a coming closer and an arrival") ✓
  - `inner_secrets` p.48 (Amuli rule) ✓
  - `forty_hadith` p.35 (all three quotes) ✓
  - `forty_hadith` p.375 ("possessing unoccupied time and an unoccupied heart"; "making one's heart understand the importance of worship"; "set aside a certain time..."; "in the most meritorious part of its time") ✓
  - `kernel` p.30 ("from the beginning of wayfaring...", "a big lie and slander", hypocrite clause, "Don't you want me to be God's grateful servant?", "purely for the sake of expression of thankfulness and gratitude to God Almighty") ✓
- **Duʿa Arabic:** `وَلاَ يَغْفُلُ عَنْ شُكْرِكَ وَلاَ يَسْتَخِفُّ بِأَمْرِكَ` = §126 + §127 of `duas-munajat-shabaniyah.md`, character for character. §126 of 134, so "near the end" is right.
- **Qur'an:**
  - 49:14 `words="1-14"`: Arabic words 1-14 end at قُلُوبِكُمۡ, "in your hearts", so the shown English ("...for faith has not yet entered into your hearts") matches Qarai exactly, with no verse-end mark added. Only the straight quotes differ from Qarai's curly ones.
  - 51:16-18: Qarai "virtuous... sleep a little during the night... at dawns they would plead for forgiveness" ✓
  - 48:2: Qarai "that Allah may forgive you what is past of your sin and what is to come". The chapter says only "forgiveness" and quotes none of it.
- **Citation keys:** `light`, `inner_secrets`, `forty_hadith`, `kernel`, `duas_munajat_shabaniyah` are all in `sources/bibliography.bib` and in the `irfan.lua` SHORT table.
- **Sheikh's teaching against L06:**
  - ¶7-11 (three depths; jurist ruling "both salaat are correct")
  - ¶13-15 (ship/sea/pearl; hadith)
  - ¶17-20 (Kubra; karama vs magic; "liars" is about the claim to know God)
  - ¶21-22 (Bahari's chain of introductory means; "something's wrong with this argument")
  - ¶23-25 (ʿAbd al-Samad Hamadani; shell/core/kernel; khidma/qurb/wusul)
  - ¶26-27, ¶30-32 (attention; car; vicious circle; "whole difficulty of this tariqa")
  - ¶45-48 (islam/iman/ihsan; 49:14; 51:16-18)
  - ¶66-70 (forty days; the law is harder)
  - L09 ¶72 (four journeys)
  - All supported, and no theology is changed.
- **Hamadani:** only Mulla ʿAbd al-Samad appears here (the full name is used at l.35). It is never confused with Akhund Hamadani, and Ch 7 l.67 separates them explicitly.
- **God / Prophet ﷺ:** no phrasing implies diminution. Q 48:2 is handled as in Tabatabaʾi's own words, with ʿAʾisha omitted. Fine.
- **Markers:** 2 open, both `[VERIFY]` (l.33, l.93), neither resolvable from a held extract. No `[QUERY]` or `[GAP]`. No Arabic besides the epigraph, and that is traced.
- **Glossary:** shariʿa, tariqa, haqiqa, ihsan, karamat, muʿjiza, sihr, khidma, qurb, wusul, Munajat Shaʿbaniyyah, tawhid, ʿurafaʾ all match. "Qur'an" per D32.
- **LINGO grep:** no banned words, intensifiers, wordy constructions or So/Well/Look/Now openings. Body is well under 3,600 words. No jokes (the car example is paraphrased plainly). Questions: only the approved hand-off.

## Argument (D22) against the brief

- All brief steps are present and in order: shell/core/kernel, Hamadani, salah, islam/iman/ihsan, Kubra, Bahari, Khomeini, forty days, attention, Tabatabaʾi, the Prophet's reply, four journeys.
- Omitted from the brief, harmlessly: the certainty/Paris image (L06 ¶43-44) and the Amuli p.42 footnote. Nothing later relies on them.
- Headings map to 6.1-6.3. The only forward dependency is Bahari's "chain Chapter Seven follows" (l.61), flagged above. The conclusion follows.

**Verdict: PASS WITH FIXES** (two medium items; neither is a misquotation).
