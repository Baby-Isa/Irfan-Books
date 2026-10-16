# Handover to a new session (2026-10-16)

_Read this first, then `CLAUDE.md`, `docs/STATUS.md`, `docs/briefs/LESSONS.md` and `docs/EXEMPLAR.md`. All work is on branch `claude/zealous-edison-mh1dpk` (it contains everything from the older `claude/stoic-euler-p7myev`). If the new session is given a different branch, base it on `claude/zealous-edison-mh1dpk`._

## 1. Where we are
- **Book 2, Parts One and Two are drafted:** prologue and Ch 1–7. Structure v3 (D40–D41):
  - Part One, The Call: 1 More than the minimum; 2 Knowing about God is not knowing Him; 3 You already know these words.
  - Part Two, Getting Ready: 4 Know yourself, know your Lord; 5 The soul and its worlds; 6 No path outside the law; 7 Finding a guide.
  - Part Three, The Road: 8–12, with the crescendo at Ch 12.
  - Part Four, Fellow Travellers: 13–15, an analytical step back.
  - Part Five, The Destination: 16–17, the emotional homecoming. Then the epilogue, and an appendix with the full Munajat Shaʿbaniyyah.
- **Approval state:**
  - The prologue and Ch 1 are the frozen exemplar (commit `32e44c9`). The user said "keep the prologue the same"; Ch 1 has since been trimmed (the Sheikh named less often).
  - Ch 2–3 have had two rounds of user review and were then tightened by about 10% with Fable.
  - Ch 4–7 are first versions, made Opus draft → Fable edit → own read → voice gate → fact-check.
- **Sent to the user and awaiting feedback:** `samples/parts-one-two-review.pdf`, raw link https://github.com/Baby-Isa/Irfan-Books/raw/claude/zealous-edison-mh1dpk/samples/parts-one-two-review.pdf. The draft copy with point notes is `samples/parts-one-two.pdf`.
- **Next:**
  1. Apply the user's feedback on Ch 2–7. Add every repeatable lesson to `docs/briefs/LESSONS.md` and `docs/TONE.md`.
  2. Then the Part Three briefs (Ch 8–12) from `docs/outline/part-3.md`. Gate A: present them as bullets and wait for approval before any prose.

## 2. How the user works (beyond CLAUDE.md)
- **Read `docs/briefs/LESSONS.md` before drafting or reviewing anything.** It holds the 21 lessons from the user's reviews; TONE rules 23–37 hold the before/afters. The biggest are:
  - Name the Sheikh sparingly: at most 5 per 1,000 words, never twice in a paragraph, no "he says" filler. The prologue is exempt.
  - Straight prose, not "he said, she said".
  - Every paragraph earns its place in the section's chain.
  - Build the premises before "therefore".
  - No mic-drop endings.
  - Name the referent ("our physical eyes", not "those eyes").
  - Explain a puzzle or cut it.
  - State an apparent contradiction, then resolve it.
  - Theological care: nothing acts upon, diminishes or limits God.
  - Plain English, with bracketed glosses and a box for bigger ideas.
  - "whereas" for contrasts.
- **House style (D42):**
  - Oxford comma.
  - Chapter numbers in words ("Chapter Four").
  - (as) for the Imams and ﷺ for the Prophet.
  - "Qur'an"; "Abu Hamza" in our own prose.
  - One callout box per section, plus "Try this" at the end. A box must make a point.
- **No questions for the Sheikh (D39):** go around an unclear passage. Don't add `[QUERY]`.
- **Metaphysics (Ch 5 onward):** the user wants it explained step by step, logically, so that it is interesting and accessible.
- **Prose pipeline the user asked for:** Opus draft → Fable review, with Fable told each section's point → edit → give to the user. "Fable" is the Agent tool with `model: "fable"`; use it for structural and tightening reviews. When tightening, cut at most 25%.
- **The user's opinion:** the prologue and Ch 1 are still the best. Ch 2–3 felt as if they meandered. Aim new chapters at the exemplar's density.
- **Reporting:**
  - Lead with the conclusion, in short bullets.
  - Quote changed lines in full.
  - Always give the GitHub raw link for PDFs (the user reads on mobile).
  - With each PDF, give a one-line note per section on what it is meant to land.

## 3. Per-chapter pipeline (as run for Part Two)
1. **Brief:** `docs/briefs/NN-case.md` from `_TEMPLATE.md` and `docs/outline/part-N.md`. User approval (Gate A).
2. **Draft:** `chapter-writer` (Opus). It reads the exemplar, LESSONS, TONE and LINGO, and writes the point notes before the prose.
3. **Fable edit:** structure, missing steps and tightening, against the point notes.
4. **Own read-through:** against LESSONS. Recurring tics to catch:
   - "Let's start with…" openers;
   - inverted openings ("Where X stands is set out by…");
   - short closing reveal sentences;
   - impersonal "as the lecture puts it".
5. **Voice gate (`docs/VOICE-TEST.md`):**
   - Run `python3 build/voice.py profile <chapter>`; it must PASS.
   - Build the blind packet with `python3 build/voice.py blind NN <chapter> [--round R]`. It writes `reviews/voice/NN-packet.md`; rename it to `NNrR-…` for later rounds, as was done for 02r7 and 02r8.
   - Run a fresh `voice-judge` agent on the packet, then score it with `python3 build/voice.py score NN`.
   - Act on fair tells.
6. **Fact-check:** `fidelity-checker` writes `reviews/book2-NN.md`. Fix every High and Medium item.
7. **Build:** `python3 build/build.py pdf book2 "0[0-7]*" [--review]`, copy the output to `samples/`, commit, push, and send the raw link.

## 4. Voice test (rebuilt 2026-10-16, D44)
The v1 caveat is resolved. Read `docs/VOICE-TEST.md`: profile = gate; chain audit (`chain-auditor`, Fable) = edit list with a 28% ceiling; blind judge = advisory only. Score `reviews/voice/PREDICTIONS-ch02-07.md` against the user's feedback when it arrives. Step 5 of the pipeline above now reads: profile PASS, then the chain audit, then (optional) the blind judge.

## 5. Open items
- **Unconfirmed Arabic (`[VERIFY]`; needs printed editions):**
  - Ch 6, the Prophet's reply "Don't you want me to be God's grateful servant?" (Kernel p. 30);
  - Ch 7, ʿIsa's saying (Misbah al-Shariʿa / Lantern p. 13);
  - Part One: Nahj 1.1.1, the light hadith, the Whispered Prayer of the Lovers, and Nahj 3.403 (Qutbuddin p. 810).
  - Run `python3 build/build.py check` for the full list.
- **Ch 7** names six teachers in prose, against a guideline of five. The user was told and can decide.
- **The Ch 2 hunger lines** ("They may be wrong… They cannot be wrong…") were kept, although a judge flagged them as staccato, because they follow the user's own instruction. The user was asked about this.
- **Bahari (Ch 6):** the lecture calls "Ayatullah Muhammad Bahari" a contemporary who "recently passed away", so he is not tied to the Shaykh Muhammad Bahari in Akhund Hamadani's line (Ch 7).
- **Carried over from the earlier handover:**
  - permissions for quoted translations;
  - the Sheikh's preferred title;
  - the paragraph-spacing trial (D35);
  - whether Book 1 (Faithful) is still wanted;
  - checking the Munajat lines against Mafatih p. 244.

## 6. Key files
| Purpose | File |
|---|---|
| Lessons from the user's reviews | `docs/briefs/LESSONS.md` |
| Model to imitate | `docs/EXEMPLAR.md`; `book2/chapters/00-prologue.md`; `01-seeking-not-powers.md` |
| Voice rules | `docs/TONE.md` (1–37); `docs/LINGO.md`; `docs/STYLE_GUIDE.md` |
| Structure | `docs/ARGUMENT.md` v3; `docs/STORYLINE.md` v3; `docs/outline/` (FRAMEWORK §1–9, part-1 to part-5) |
| Part dividers | `book2/parts/N-*.md` (front matter `before: N`); `build/part.typst-template` |
| Munajat lines used (each once) | `docs/outline/FRAMEWORK.md` §4; Arabic in `sources/extracts/duas-munajat-shabaniyah.md` by § |
| Decisions | `docs/DECISIONS.md` (D1–D43) |
| Voice gate | `build/voice.py`; `docs/VOICE-TEST.md`; `reviews/voice/` |
| Fact-check reports | `reviews/book2-NN.md`, `reviews/book2-02-03-tighten.md` |

## 7. Working notes
- **Setup:** run `pip install typst pymupdf`; pandoc is preinstalled.
- **Voice notes (.m4a):** Hugging Face is blocked. Install `sherpa-onnx` and `soundfile`, then download the Whisper small.en model and `silero_vad.onnx` from the k2-fsa GitHub releases. Convert the audio with `ffmpeg -ar 16000 -ac 1` and use VAD segmentation.
- **Commits:**
  - Commit and push after each unit.
  - End each message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and the session's own `Claude-Session:` line.
  - No PR unless asked.
