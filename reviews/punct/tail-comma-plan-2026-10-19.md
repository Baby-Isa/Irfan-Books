# Plan: weak final commas (user, 2026-10-19)

**The problem.** A sentence that ends on a comma and a phrase with no verb of its own: "…as if asleep, heedless of a God who is near"; "…ask God's forgiveness with the word astaghfirullah, often by habit"; "…feels abandoned by their own soul, unable to carry it further". The user: "they read horridly; we really need to cut those."

**Size.** A first detector (`reviews/punct/tailcomma.py`) finds 241 candidate sentences in Ch 0–12 (roughly 70% real on a spot check): prologue 13, Ch 1 17, Ch 2 20, Ch 3 19, Ch 4 9, Ch 5 28, Ch 6 20, Ch 7 30, Ch 8 8, Ch 9 21, Ch 10 18, Ch 11 26, Ch 12 12.

**Steps.**
1. **Rule (TONE 45, amended):** no sentence ends on a comma followed by a verbless phrase (an appositive, a participle phrase, or a tag like "often by habit"). Allowed: the last item of a list; a quotation's attribution; a full clause with its own verb ("as Chapter Twelve explains"; "which the lectures call…").
2. **Fix menu, in the user's order of preference:** (1) join with "and" ("as if asleep and heedless of a God who is near"); (2) a "which/who/whose" clause; (3) move the phrase to the front or middle of the sentence; (4) give it its own short sentence; (5) cut it if it only repeats.
3. **Tool:** build the detector into `voice.py punct` as a TAIL-COMMA flag, so every new draft and edit is checked; tighten it against the false positives before the sweep.
4. **Sweep:** one numbered before → after list per Part (Part Three first, then Parts One and Two), the user approving line by line as with the punctuation sweep; fixes then applied, profile re-run, PDFs rebuilt.
5. **Prevention:** add the rule to LESSONS and to the chapter-writer and editor prompts.
