#!/usr/bin/env python3
"""Voice test: does a new chapter read as if the exemplar's author wrote it?

Two tests, both measured against the approved exemplar (D36):

  profile  Stylometric profile. Measures paragraph and sentence length, the
           habits TONE.md names ("and" chains, "you", semicolons, colons,
           questions, dashes), banned lingo, and Burrows' Delta on function
           words, which is the standard authorship-attribution measure.
           Each figure is set against its spread across the exemplar's own
           ~200-word chunks, so "off" means "outside what the exemplar's
           author does".

  blind    Builds an anonymised packet for the voice-judge agent: a reference
           sample of the exemplar, then shuffled test passages drawn from
           (a) held-out exemplar text, (b) the new chapter and (c) a control:
           a draft the user rejected. The judge marks each passage "same
           hand" or "different hand" and quotes its tells. `score` reads
           the judge's answers against the key. The test is valid only if
           the judge catches the control; the chapter passes only if its
           passages are flagged no more often than the exemplar's own.

Usage:
  python3 build/voice.py profile FILE|REV:PATH ...   (no args: the exemplar itself)
  python3 build/voice.py blind NN book2/chapters/02-*.md [--control REV:PATH] [--round R]
  python3 build/voice.py score NN
  python3 build/voice.py openings book2/chapters/02-*.md
"""
import json, random, re, statistics as st, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXEMPLAR = ["book2/chapters/00-prologue.md", "book2/chapters/01-seeking-not-powers.md"]
EXEMPLAR_REV = "32e44c9"  # frozen exemplar (D36)
# Control drafts the user rejected (pre-D29), same topics as the exemplar.
CONTROLS = ["7225b76:book2/chapters/01-seeking-not-powers.md",
            "9d02329:book2/chapters/00-prologue.md"]
VOICE_DIR = ROOT / "reviews" / "voice"

FUNCTION_WORDS = """the of and to a in is that it as for with this not but by be are
on or from his he at which they their we our us you your what an one its was who
there all more than so if when no only even also yet because those these them
him has have can does do itself into out about up then each other such how most
were would should may must being been both any same own between through""".split()

BANNED = ["and honestly", "sit with it", "load bearing", "going down the path",
          "going against", "that's way better", "pushing back", "pushback",
          "that's on me", "the thing to hold onto", "honest take", "real caveat",
          "that's the spine", "handwave", "quiet", "quietly", "landed",
          "blast radius", "legible", "surface area", "canonical", "leverage",
          "circle back", "pull on this thread"]
INTENSIFIERS = ["very", "really", "truly", "extremely", "absolutely", "literally",
                "basically", "obviously", "clearly"]
WORDY = ["in order to", "due to the fact", "prior to", "subsequent to",
         "in terms of", "with regard to", "in the context of"]
TONE_FLAGS = ["as we should", "rarely", "lip service", "intelligent", "busy",
              "you will find", "of course", "it is worth noting", "we shall",
              "let's ask ourselves", "in his class", "fair enough"]
LONGEST = 115  # TONE 22 says 110; the exemplar's own longest is 114
BAD_OPENERS = ("So ", "Well ", "Look ", "Now ", "So, ", "Well, ", "Now, ")


# ---------------------------------------------------------------- extraction
def read_source(spec):
    """'path' reads the working tree; 'REV:path' reads git history."""
    if ":" in spec and not Path(spec).exists():
        return subprocess.run(["git", "show", spec], cwd=ROOT, check=True,
                              capture_output=True, text=True).stdout
    return (ROOT / spec).read_text() if not Path(spec).is_absolute() else Path(spec).read_text()


def paragraphs(md, keep_boxes=True, placeholders=False):
    """Return the author's own prose as a list of (kind, text) paragraphs.

    kind is 'body' or 'box'. Point notes, word strips, headings and displayed
    quotations are removed (displayed quotes are other people's words); with
    placeholders=True a displayed quote becomes '[verse]' or '[quotation]'.
    """
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)
    out, stack, buf = [], [], []

    def flush():
        if buf:
            text = clean(" ".join(buf))
            if text:
                kind = "box" if any(c.startswith("box") for c in stack) else "body"
                out.append((kind, text))
            buf.clear()

    for line in md.splitlines():
        s = line.strip()
        m = re.match(r"^:::+\s*\{\.([\w-]+)", s)
        if m:
            flush()
            cls = m.group(1)
            stack.append(cls)
            if placeholders and cls in ("ayah", "quote"):
                out.append(("quote", "[verse]" if cls == "ayah" else "[quotation]"))
            continue
        if re.match(r"^:::+\s*$", s):
            flush()
            if stack:
                stack.pop()
            continue
        if any(c in ("point", "words", "ayah", "quote") for c in stack):
            continue
        if any(c == "box-try" for c in stack) or (stack and not keep_boxes):
            continue
        if s.startswith(">"):                               # old-style displayed quote
            flush()
            if placeholders and not (out and out[-1][0] == "quote"):
                out.append(("quote", "[quotation]"))
            continue
        if not s or s.startswith("#") or s.startswith("<!--"):
            flush()
            continue
        buf.append(s)
    flush()
    return out


def clean(t):
    t = re.sub(r"\[@[^\]]*\]", "", t)                         # citations
    t = re.sub(r"\[(VERIFY|QUERY|GAP)[^\]]*\]", "", t)       # markers
    t = re.sub(r"\[([^\]]+)\]\{[^}]*\}", r"\1", t)           # [x]{lang=ar}
    t = re.sub(r"\((Q|Nahj) [^)]*\)", "", t)                 # (Q 30:21)
    t = t.replace("*", "")
    t = re.sub(r"\s+", " ", t)
    return re.sub(r"\s+([.,;:])", r"\1", t).strip()


def strip_quoted(t):
    """Drop quoted spans of 4+ words: they are the sources' words, not ours."""
    drop = lambda m: " " if len(m.group(1).split()) >= 4 else m.group(0)
    t = re.sub(r'"([^"]*)"', drop, t)
    return re.sub(r"“([^”]*)”", drop, t)


WORD = re.compile(r"[A-Za-zʿʾ'’\-]+")


def words(t):
    return [w.lower().strip("'’") for w in WORD.findall(t) if w.strip("'’-")]


def sentences(t):
    t = re.sub(r"\b(pp?|Q|e\.g|i\.e|cf|ed|vol|ch|Ch)\.", r"\1<dot>", t)
    parts = re.split(r"(?<=[.!?])[\"”)]?\s+(?=[\"“(]?[A-Zʿ])", t)
    return [p.replace("<dot>", ".") for p in parts if words(p)]


# ---------------------------------------------------------------- features
def features(paras):
    text = " ".join(p for _, p in paras)
    own = strip_quoted(text)
    w = words(text)
    ow = words(own) or ["x"]
    sents = [s for _, p in paras for s in sentences(p)]
    k = 1000 / len(ow)
    count = lambda pat: len(re.findall(pat, own, flags=re.I))
    plen = [len(words(p)) for _, p in paras]
    slen = [len(words(s)) for s in sents]
    return {
        "words": len(w),
        "words/paragraph": st.mean(plen) if plen else 0,
        "longest paragraph": max(plen) if plen else 0,
        "words/sentence": st.mean(slen) if slen else 0,
        "sentences over 30 words %": 100 * sum(x > 30 for x in slen) / max(len(slen), 1),
        "'and' per 1k": count(r"\band\b") * k,
        "'but'/'yet' per 1k": count(r"\b(but|yet)\b") * k,
        "semicolons per 1k": own.count(";") * k,
        "colons per 1k": own.count(":") * k,
        "dashes per 1k": len(re.findall(r"\s[—–]\s|—", own)) * k,
        "brackets per 1k": own.count("(") * k,
        "questions per 1k": own.count("?") * k,
        "'you/your' per 1k": count(r"\byou(r|rs|rself)?\b") * k,
        "'we/us/our' per 1k": count(r"\b(we|us|our|ours|ourselves)\b") * k,
        "'let's' per 1k": count(r"\blet[’']s\b") * k,
        "'this/these' per 1k": count(r"\b(this|these)\b") * k,
        "commas per sentence": own.count(",") / max(len(sents), 1),
        "And/But openers per 1k": sum(bool(re.match(r"[\"“]?(And|But)\b", s)) for s in sents) * k,
        "colon-then-quote per 1k": len(re.findall(r":\s*[\"“]", text)) * k,
    }


def lingo_hits(paras):
    hits = []
    for _, p in paras:
        low = re.sub(r'"[^"]*"|“[^”]*”', " ", p).lower()   # sources' words are exempt
        for lst, label in ((BANNED, "banned"), (INTENSIFIERS, "intensifier"),
                           (WORDY, "wordy"), (TONE_FLAGS, "TONE check")):
            for term in lst:
                if re.search(r"\b" + re.escape(term) + r"\b", low):
                    hits.append(f"{label}: '{term}' in \"{p[:70]}…\"")
        for s in sentences(p):
            if s.startswith(BAD_OPENERS):
                hits.append(f"opener: \"{s[:60]}…\"")
    return hits


def chunks(paras, size=180):
    out, cur, n = [], [], 0
    for kp in paras:
        cur.append(kp)
        n += len(words(kp[1]))
        if n >= size:
            out.append(cur)
            cur, n = [], 0
    if cur and n >= size / 2:
        out.append(cur)
    return out


def fw_profile(paras):
    ws = words(strip_quoted(" ".join(p for _, p in paras)))
    n = max(len(ws), 1)
    return [ws.count(f) / n for f in FUNCTION_WORDS]


def delta(vec, refs):
    """Burrows' Delta of vec against the centroid of refs."""
    cols = list(zip(*refs))
    zs = []
    for v, col in zip(vec, cols):
        mu, sd = st.mean(col), st.pstdev(col)
        if sd > 0:
            zs.append(abs(v - mu) / sd)
    return st.mean(zs)


def exemplar_paras(rev=True):
    paras = []
    for f in EXEMPLAR:
        paras += [p for p in paragraphs(read_source(f"{EXEMPLAR_REV}:{f}" if rev else f))
                  if p[0] == "body"]
    return paras


# ---------------------------------------------------------------- profile
def profile(specs):
    ex = exemplar_paras()
    ex_chunks = chunks(ex)
    ex_feats = [features(c) for c in ex_chunks]
    keys = [k for k in features(ex) if k not in ("words", "longest paragraph")]
    spread = {k: (st.mean(f[k] for f in ex_feats), st.pstdev(f[k] for f in ex_feats))
              for k in keys}
    ex_whole = features(ex)

    ex_fw = [fw_profile(c) for c in ex_chunks]
    loo = sorted(delta(ex_fw[i], ex_fw[:i] + ex_fw[i + 1:]) for i in range(len(ex_fw)))
    d90 = loo[int(0.9 * (len(loo) - 1))]

    print(f"Exemplar ({EXEMPLAR_REV}): {ex_whole['words']} words of body prose, "
          f"{len(ex_chunks)} chunks. Delta of its own chunks (leave-one-out): "
          f"median {st.median(loo):.2f}, 90th percentile {d90:.2f}.\n")
    report = {}
    for spec in specs:
        paras = [p for p in paragraphs(read_source(spec)) if p[0] == "body"]
        f = features(paras)
        cks = chunks(paras)
        ds = [delta(fw_profile(c), ex_fw) for c in cks]
        over = sum(d > d90 for d in ds)
        off = []
        print(f"== {spec}  ({f['words']} words, {len(paras)} paragraphs)")
        print(f"   {'measure':28} {'chapter':>8} {'exemplar':>9}   z")
        for k in keys:
            mu, sd = spread[k]
            z = (f[k] - mu) / sd if sd else 0.0
            mark = "  OFF" if abs(z) >= 2 else ("  drift" if abs(z) >= 1 else "")
            if abs(z) >= 2:
                off.append(k)
            print(f"   {k:28} {f[k]:8.1f} {ex_whole[k]:9.1f} {z:+5.1f}{mark}")
        lp = f["longest paragraph"]
        mark = "  OFF" if lp > LONGEST else ("  long" if lp > 110 else "")
        print(f"   {'longest paragraph':28} {lp:8.0f} {'≤110':>9}{mark}")
        print(f"   Function-word Delta: median {st.median(ds):.2f} over {len(ds)} chunks; "
              f"{over}/{len(ds)} chunks beyond the exemplar's 90th percentile ({d90:.2f}).")
        hits = lingo_hits(paras)
        body = " ".join(t for _, t in paras)
        sheikh = len(re.findall(r"\bSheikh\b|\bBahmanpour\b(?<!Sheikh Bahmanpour)", body))
        says = len(re.findall(r"\b(?:he|she) (?:says|adds|notes|remarks|grants|points out)\b", body))
        rate = 1000 * sheikh / max(f["words"], 1)
        print(f"   Sheikh named {sheikh} times ({rate:.1f} per 1k; cap 5, TONE 23); 'he says'-type verbs: {says}")
        if rate > 5:
            hits.append(f"attribution: Sheikh named {rate:.1f} times per 1,000 words (cap 5, TONE 23)")
        for h in hits:
            print(f"   LINGO {h}")
        # Delta is reported, not gated: calibration showed it does not separate
        # drafts from the exemplar with a ~3,300-word reference (VOICE-TEST.md).
        verdict = "PASS" if (not off and lp <= LONGEST and not hits) else "REWRITE"
        print(f"   Profile verdict: {verdict}\n")
        report[spec] = {"verdict": verdict, "off": off, "delta_median": st.median(ds),
                        "delta_over": f"{over}/{len(ds)}", "lingo": hits}
    return report


# ---------------------------------------------------------------- blind test
def passages(md, n, rng, min_words=110, max_words=190):
    """n passages of one or two adjacent body paragraphs, spread across the text."""
    paras = paragraphs(md, keep_boxes=False, placeholders=True)
    cands, i = [], 0
    while i < len(paras):
        if paras[i][0] != "body":
            i += 1
            continue
        group, wc, j = [], 0, i
        while j < len(paras) and wc < min_words:
            group.append(paras[j][1])
            wc += len(words(paras[j][1]))
            j += 1
        if min_words <= wc <= max_words + 60:
            cands.append("\n\n".join(group))
        i = j
    if len(cands) <= n:
        return cands
    step = len(cands) / n
    return [cands[int(k * step + rng.random() * step)] for k in range(n)]


NUMBER_WORDS = {str(i): w for i, w in enumerate(
    "Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen "
    "Fourteen Fifteen Sixteen Seventeen".split())}


def house_style(t):
    """Apply the current house style (D32, D42) to any passage, old or new."""
    t = re.sub(r"\bQuran", "Qur'an", t)
    t = t.replace("(ʿa)", "(as)")
    t = re.sub(r"\bChapter (\d+)\b", lambda m: "Chapter " + NUMBER_WORDS.get(m.group(1), m.group(1)), t)
    # Oxford comma: strip every comma before "and"/"or" in every passage alike.
    # (Adding commas heuristically created a false "comma before a pair" habit.)
    t = re.sub(r", (and|or) ", r" \1 ", t)
    return t


def blind(nn, chapter, control=None, n=4, seed=None):
    rng = random.Random(seed if seed is not None else nn)
    pro = read_source(f"{EXEMPLAR_REV}:{EXEMPLAR[0]}")
    ch1 = read_source(f"{EXEMPLAR_REV}:{EXEMPLAR[1]}")
    cut = ch1.index("## Some do see")          # reference: prologue + Ch 1 §1–3
    reference = "\n\n".join(p for k, p in paragraphs(pro + "\n\n" + ch1[:cut],
                                                      keep_boxes=False, placeholders=True)
                            if k != "box")
    items = [("exemplar", p) for p in passages(ch1[cut:], n, rng)]
    items += [("chapter", p) for p in passages(read_source(chapter), n, rng)]
    ctrl = control or CONTROLS[0]
    cmd = read_source(ctrl)
    if "## Some do see" in cmd:
        cmd = cmd[cmd.index("## Some do see"):]
    items += [("control", p) for p in passages(cmd, n, rng)]
    rng.shuffle(items)
    # House style is a giveaway, not voice: normalise it in every passage, so the
    # judge cannot tell old text from new by conventions adopted later (D32, D42).
    norm = house_style
    reference, items = norm(reference), [(src, norm(p)) for src, p in items]

    VOICE_DIR.mkdir(parents=True, exist_ok=True)
    labels = [chr(65 + i) for i in range(len(items))]
    key = {lab: src for lab, (src, _) in zip(labels, items)}
    key["_meta"] = {"chapter": chapter, "control": ctrl, "exemplar": EXEMPLAR_REV}
    (VOICE_DIR / f"{nn}-key.json").write_text(json.dumps(key, indent=1))
    lines = [f"# Voice packet {nn}\n",
             "## Reference: Author A (all of this is by Author A)\n", reference,
             "\n## Test passages\n",
             "_Each passage below is either by Author A or by a different hand. "
             "Any number, including none or all, may be by a different hand. "
             "Topic varies within one author's work: judge the voice, not the subject._\n"]
    for lab, (_, p) in zip(labels, items):
        lines += [f"### Passage {lab}\n", p, ""]
    out = VOICE_DIR / f"{nn}-packet.md"
    out.write_text("\n".join(lines))
    print(f"Packet: {out.relative_to(ROOT)} ({len(items)} passages). "
          f"Key: {(VOICE_DIR / f'{nn}-key.json').relative_to(ROOT)} (do not show the judge).")
    print(f"The judge writes reviews/voice/{nn}-answers.json, then run: "
          f"python3 build/voice.py score {nn}")


def score(nn):
    key = json.loads((VOICE_DIR / f"{nn}-key.json").read_text())
    ans = json.loads((VOICE_DIR / f"{nn}-answers.json").read_text())
    meta = key.pop("_meta")
    flagged = {src: [] for src in ("exemplar", "chapter", "control")}
    total = {src: 0 for src in flagged}
    for lab, src in key.items():
        total[src] += 1
        a = ans.get(lab, {})
        if a.get("verdict") == "different":
            flagged[src].append((lab, a.get("confidence"), a.get("tells", [])))
    fx, fc, fk = (len(flagged[s]) for s in ("exemplar", "chapter", "control"))
    print(f"Blind voice test {nn}: {meta['chapter']} (control {meta['control']})")
    print(f"  control flagged  {fk}/{total['control']}   (the judge must catch these)")
    print(f"  exemplar flagged {fx}/{total['exemplar']}   (false alarms)")
    print(f"  chapter flagged  {fc}/{total['chapter']}")
    valid = fk >= (total["control"] + 1) // 2 + 1 if total["control"] > 2 else fk >= 1
    passed = fc <= fx      # no more often than the real author in the same run
    verdict = ("INVALID (judge missed the control; rerun with a fresh judge)" if not valid
               else "PASS" if passed else "REWRITE")
    print(f"  verdict: {verdict}")
    for lab, conf, tells in flagged["chapter"]:
        print(f"  Passage {lab} (chapter, confidence {conf}): act on these")
        for t in tells:
            print(f"     - {t}")
    if flagged["exemplar"]:
        print("  False alarms on the real author: discount any chapter tell of the same kind")
        for lab, conf, tells in flagged["exemplar"]:
            for t in tells:
                print(f"     - [{lab}] {t}")
    return verdict


def openings(spec):
    """First sentence of every body paragraph, for the TONE rule 1 read-through."""
    for i, (_, p) in enumerate(p for p in paragraphs(read_source(spec)) if p[0] == "body"):
        print(f"{i + 1:3}. {sentences(p)[0]}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == "profile":
        specs = a[1:]
        profile(specs or EXEMPLAR)
    elif a[0] == "blind":
        ctrl = a[a.index("--control") + 1] if "--control" in a else None
        rnd = a[a.index("--round") + 1] if "--round" in a else "1"
        blind(a[1], a[2], ctrl, seed=f"{a[1]}-{rnd}")
    elif a[0] == "score":
        v = score(a[1])
        sys.exit(0 if v == "PASS" else 1)
    elif a[0] == "openings":
        openings(a[1])
    else:
        sys.exit(__doc__)
