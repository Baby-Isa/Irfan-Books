# Handover to a new session (2026-10-19)

_Read this first, then `CLAUDE.md`, `docs/STATUS.md`, `docs/briefs/LESSONS.md` (1–31) and `docs/EXEMPLAR.md`. Branch: `claude/irfan-books-part-three-kh8nd2`. Commit and push after every unit._

## 1. Where we are
- **Book 2, prologue and Chapters One to Seven are done to the user's current standard.** Latest PDFs: `samples/parts-one-two-v6.pdf` (draft, red proof ladders) and `samples/parts-one-two-v6-review.pdf` (reader copy). Raw links: `https://github.com/Baby-Isa/Irfan-Books/raw/claude/irfan-books-part-three-kh8nd2/samples/<file>`.
- **D48, the proof ladder.** Every section's `::: {.point}` note is a proof: each step follows only from earlier steps and uses their words; explanations needed first are nested (2a, 2b…) and the prose tells the reader what is coming. Book-level chain approved: `docs/ladders/00-book-chain.md` (now in ARGUMENT and STORYLINE). Per-chapter ladders: `docs/ladders/NN.md`; the model is `docs/ladders/05.md`.
- **D49, punctuation.** TONE 45, amended by the user's line-by-line choices on the sweep (`reviews/punct/user-choices-2026-10-19.md`; LESSONS 32: semicolons may explain, a colon only for a reveal, echoes that add a shade stay, keep the flow, when in doubt keep his original). (colons sparingly; semicolons only between two equal full sentences or in heavy lists; no echo or long tail on a sentence's last comma; Oxford comma and "and" on every list; one vivid word welcome, echo phrases not; a fronted phrase now and then; no dashes; plain diction). `python3 build/voice.py punct FILE` and every `profile` flag sentences; writers fix or keep each flag before replying. The sweep of Ch 0–7 is done; no future sweeps.
- **Measures:** `voice.py profile` (gate); chain audit with `chainscore` splitting idle paragraphs into breathers, recaps and drag (TONE 44a; Ch 1 calibration: 73% forward, drag ≤ ~10%; a drag flag is a paragraph to look at, not a cut). Blind judge only for a new kind of chapter.
- **Stories (D47):** 25 of the Sheikh's 61 told or planned in full (`reviews/stories-audit.md`, `reviews/stories-screen.md`). Sources researched (`reviews/story-sources.md`): tell each as the Sheikh's account; cite a held or page-checked classical source where one tells the same story; differences between versions are decided by the user case by case, later.
- **Style decisions since 16 Oct:** lectures and books in the present tense ("Sheikh Bahmanpour ends his first lecture…"), events in the past; no spliced quotation fragments; pronouns for God capitalised without brackets; chapters start on the next page; chapter epigraphs evenly spaced.

## Next
0. **(2026-10-19) Part Three ladders written** (`docs/ladders/08`–`12.md`, briefs `docs/briefs/08`–`12-case.md`) and sent in chat for approval. Do not draft prose until the user approves them.
1. **Part Three briefs (Ch 8–12)** from `docs/outline/part-3.md`, written from the start as proof ladders (`docs/briefs/_TEMPLATE.md`), each with its told stories (Ch 9 now three: Fudayl, the young man told to stop, Hatim; Ch 12's Miʿraj prayer only if a held source is found). Gate A: present the chapter point, the section chain and each section's ladder in chat for approval before any prose.
2. Open with the user: Chapter One's story box (implicitly kept); the case-by-case story-source differences; the prologue names the Sheikh 5.2 times per 1,000 words (exempt, but flagged).

## 2. How the user works (beyond CLAUDE.md)
- **Newest (18–19 Oct):** he reviews in chat, line by line, and approves numbered change lists ("yes to all except …"). Show exact before → after. He wants arguments like a maths proof, plain sentences that read once, short breathers kept, colons rare, and his punctuation rules (TONE 45). Push back with reasons where a rule would add padding or grandeur; he welcomes it. Never send a paragraph you have not checked against TONE 38, 40a and 45.
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
5. **Voice gate (`docs/VOICE-TEST.md`, D44–D45; supersedes the steps below):** profile PASS → chain audit 15–28% → two blind judges, act on fair tells. Old steps:
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
| Voice rules | `docs/TONE.md` (1–44); `docs/LINGO.md`; `docs/STYLE_GUIDE.md` |
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
