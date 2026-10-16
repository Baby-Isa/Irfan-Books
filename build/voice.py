#!/usr/bin/env python3
"""Voice and chain tests (docs/VOICE-TEST.md, D37, D44).

  profile     Stylometric profile against Author A (the exemplar as last
              approved). The gate.
  chain       Chain-audit packet: each section's point, then numbered
              paragraphs, for a fresh chain-auditor. chainscore counts the
              paragraphs labelled restate or aside. The edit list.
  blind       Blind authorship packets, one per judge, with held-out Author A
              passages, the chapter and rejected drafts, no near-twins; score
              reports AUC per judge. Advisory: calibration showed it cannot
              separate approved from rejected prose (reviews/voice/CALIBRATION.md).

Usage:
  python3 build/voice.py profile FILE|REV:PATH ...   (no args: the exemplar itself)
  python3 build/voice.py chain STEM book2/chapters/08-*.md
  python3 build/voice.py chainscore STEM ...
  python3 build/voice.py blind NN book2/chapters/08-*.md [--judges opus,fable,opus] [--round R]
  python3 build/voice.py score NN
  python3 build/voice.py openings book2/chapters/08-*.md
"""
import collections, json, random, re, statistics as st, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXEMPLAR = ["book2/chapters/00-prologue.md", "book2/chapters/01-seeking-not-powers.md"]
EXEMPLAR_REV = "74fea4c"  # the exemplar as the user last approved it (D36, D43), snapshotted in reviews/voice/corpus/A-*.md;
                          # the 32e44c9 freeze (Z-*.md) predates the attribution rules and fails today's profile
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
        src = CORPUS + ("A-prologue.md" if "prologue" in f else "A-ch01.md")
        paras += [p for p in paragraphs(read_source(src if rev else f))
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


# ---------------------------------------------------------------- blind test (v2, D44)
# Author A is the exemplar as the user last approved it (D43, commit 74fea4c), snapshotted
# in the corpus folder so the test needs no git history. The controls are drafts the user
# rejected, on topics outside the exemplar, so no control passage has a near-twin
# among Author A's passages: in v1, judges caught 28/30 controls that had a twin
# but only 32/46 without one, so the control check was passing on content.
CORPUS = "reviews/voice/corpus/"
A_PRO, A_CH1 = CORPUS + "A-prologue.md", CORPUS + "A-ch01.md"
CONTROL_POOL = [CORPUS + "X-ch02-v1-2d8143e.md", CORPUS + "X-ch03-v1-2d8143e.md"]
# Two folds. In fold B, Author A's held-out passages (the prologue) are on topics
# the reference (Ch 1) does not cover, as a new chapter's always are.
FOLDS = {"A": {"ref": [A_PRO, A_CH1 + "@0-3"], "pos": [A_CH1 + "@4-9"]},
         "B": {"ref": [A_CH1], "pos": [A_PRO]}}
TWIN = 0.10          # max share of a passage's word 4-grams found elsewhere in the packet
PASS_AUC, FAIL_AUC, VALID_AUC = 0.60, 0.70, 0.75   # set by calibration (VOICE-TEST.md)


def read_spec(spec):
    """'file', 'REV:file', optionally '@a-b' for sections a..b (0 = before the first ##)."""
    m = re.search(r"@(\d+)(?:-(\d+))?$", spec)
    md = read_source(spec[:m.start()] if m else spec)
    if not m:
        return md
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)
    secs = re.split(r"\n(?=## )", md)
    a, b = int(m.group(1)), int(m.group(2) or m.group(1))
    return "\n".join(secs[a:b + 1])


def pool(md, min_words, max_words):
    """Every passage of one or more adjacent body paragraphs, min..max words, in order."""
    paras = paragraphs(md, keep_boxes=False, placeholders=True)
    out, i = [], 0
    while i < len(paras):
        if paras[i][0] != "body":
            i += 1
            continue
        group, wc, j = [], 0, i
        while j < len(paras) and wc < min_words and paras[j][0] != "box":
            group.append(paras[j][1])
            wc += len(words(paras[j][1]))
            j += 1
        if min_words <= wc <= max_words:
            out.append("\n\n".join(group))
        i = max(j, i + 1)
    return out


def grams(t, n=4):
    w = words(t)
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


def pick(cands, n, rng, seen):
    """n passages spread across the text, none a near-twin of anything already in `seen`."""
    order = list(range(len(cands)))
    if len(cands) > n:     # spread: one random draw per stretch, then the rest as reserves
        step = len(cands) / n
        first = [int(k * step + rng.random() * step) for k in range(n)]
        order = first + [i for i in order if i not in first]
    out = []
    for i in order:
        g = grams(cands[i])
        if g and len(g & seen) / len(g) > TWIN:
            continue
        out.append(cands[i])
        seen |= g
        if len(out) == n:
            break
    return out


NUMBER_WORDS = {str(i): w for i, w in enumerate(
    "Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen "
    "Fourteen Fifteen Sixteen Seventeen".split())}


def house_style(t):
    """Apply the current house style (D32, D42) to any passage, old or new."""
    t = re.sub(r"\bQuran", "Qur'an", t)
    t = t.replace("(ʿa)", "(as)").replace("’", "'").replace("‘", "'")
    t = t.replace("“", '"').replace("”", '"')
    t = re.sub(r"\bChapter (\d+)\b", lambda m: "Chapter " + NUMBER_WORDS.get(m.group(1), m.group(1)), t)
    # Oxford comma: strip every comma before "and"/"or" in every passage alike.
    # (Adding commas heuristically created a false "comma before a pair" habit.)
    t = re.sub(r", (and|or) ", r" \1 ", t)
    return t


JUDGE_NOTE = ("_Each passage below is either by Author A or by a different hand writing on "
              "the same broad subject. Any number, including none or all, may be by a different "
              "hand. Topic varies within one author's work: judge the voice, not the subject. "
              "House style (spelling, honorifics, commas before 'and') has been made uniform, "
              "and quotations show as [verse] or [quotation], so neither is evidence._\n")


def blind(nn, cand, judges=("opus", "fable", "opus"), n=6, rnd="1", ctrl=None,
          ref=None, pos=None, folds=None, min_words=120, max_words=260):
    """One packet per judge, each with its own fold, sample and order."""
    VOICE_DIR.mkdir(parents=True, exist_ok=True)
    folds = folds or ["A", "B"]
    for k, model in enumerate(judges, 1):
        rng = random.Random(f"{nn}-{rnd}-{k}")
        fold = folds[(k - 1) % len(folds)]
        refs = ref or FOLDS[fold]["ref"]
        poss = pos or FOLDS[fold]["pos"]
        ctrls = ctrl or CONTROL_POOL
        reference = "\n\n".join(p for kind, p in paragraphs(
            "\n\n".join(read_spec(s) for s in refs), keep_boxes=False, placeholders=True)
            if kind != "box")
        seen = grams(reference)
        items = []
        for src, specs in (("chapter", cand), ("exemplar", poss), ("control", ctrls)):
            cands = []
            for s in specs:
                cands += pool(read_spec(s), min_words, max_words)
            got = pick(cands, n, rng, seen)
            if len(got) < n:
                print(f"  note: judge {k} has {len(got)}/{n} {src} passages (pool too small)")
            items += [(src, p) for p in got]
        rng.shuffle(items)
        reference = house_style(reference)
        items = [(s, house_style(p)) for s, p in items]
        labels = [chr(65 + i) for i in range(len(items))]
        key = {lab: s for lab, (s, _) in zip(labels, items)}
        key["_meta"] = {"candidate": cand, "reference": refs, "exemplar": poss,
                        "control": ctrls, "fold": fold, "judge_model": model, "round": rnd}
        stem = f"{nn}-j{k}"
        (VOICE_DIR / f"{stem}-key.json").write_text(json.dumps(key, indent=1))
        lines = [f"# Voice packet {stem}\n",
                 "## Reference: Author A (all of this is by Author A)\n", reference,
                 "\n## Test passages\n", JUDGE_NOTE]
        for lab, (_, p) in zip(labels, items):
            lines += [f"### Passage {lab}\n", p, ""]
        (VOICE_DIR / f"{stem}-packet.md").write_text("\n".join(lines))
        print(f"Judge {k} ({model}, fold {fold}): reviews/voice/{stem}-packet.md, "
              f"{len(items)} passages, reference {len(words(reference))} words")
    print(f"Run one fresh voice-judge per packet (Agent model as listed), then: "
          f"python3 build/voice.py score {nn}")


def auc(hi, lo):
    """P(a random 'hi' score beats a random 'lo' score), ties count half."""
    if not hi or not lo:
        return float("nan")
    return sum((h > l) + 0.5 * (h == l) for h in hi for l in lo) / (len(hi) * len(lo))


def load_run(nn):
    runs = []
    for kf in sorted(VOICE_DIR.glob(f"{nn}-j*-key.json")):
        af = Path(str(kf).replace("-key.json", "-answers.json"))
        if not af.exists():
            print(f"  missing {af.name}")
            continue
        key, ans = json.loads(kf.read_text()), json.loads(af.read_text())
        ans = ans.get("passages", ans)
        meta = key.pop("_meta")
        rows = []
        for lab, src in key.items():
            a = ans.get(lab, {})
            p = a.get("p", a.get("probability"))
            if p is None:     # v1 answers: verdict and confidence only
                c = a.get("confidence", 3)
                p = 50 + 10 * c if a.get("verdict") == "same" else 50 - 10 * c
            rows.append((src, float(p), lab, a))
        runs.append((kf.name[:-9], meta, rows))
    return runs


def score(nn, quiet=False):
    runs = load_run(nn)
    if not runs:
        sys.exit(f"No answers for {nn}")
    per = []
    print(f"Blind voice test {nn}: {runs[0][1]['candidate']}")
    print(f"  {'judge':10} {'model':6} fold  mean p: A-held  chapter control   "
          f"AUC A>control  A>chapter  chapter>control")
    for stem, meta, rows in runs:
        g = {s: [p for src, p, _, _ in rows if src == s] for s in ("exemplar", "chapter", "control")}
        m = {s: st.mean(v) if v else float("nan") for s, v in g.items()}
        r = (auc(g["exemplar"], g["control"]), auc(g["exemplar"], g["chapter"]),
             auc(g["chapter"], g["control"]))
        per.append((g, r))
        print(f"  {stem:10} {meta['judge_model']:6} {meta['fold']:4} "
              f"{m['exemplar']:13.0f} {m['chapter']:8.0f} {m['control']:7.0f}   "
              f"{r[0]:13.2f} {r[1]:10.2f} {r[2]:16.2f}")
    valid = st.mean(r[0] for _, r in per)
    gap = st.mean(r[1] for _, r in per)
    better = st.mean(r[2] for _, r in per)
    # Bootstrap over passages within each judge: how sure is the A>chapter figure?
    rng = random.Random(0)
    boots = []
    for _ in range(2000):
        vals = []
        for g, _ in per:
            ex = [rng.choice(g["exemplar"]) for _ in g["exemplar"]]
            ch = [rng.choice(g["chapter"]) for _ in g["chapter"]]
            vals.append(auc(ex, ch))
        boots.append(st.mean(vals))
    boots.sort()
    lo, hi = boots[int(0.05 * len(boots))], boots[int(0.95 * len(boots)) - 1]
    if valid < VALID_AUC:
        verdict = "INVALID (the panel could not tell Author A from the rejected drafts)"
    elif gap <= PASS_AUC:
        verdict = "PASS"
    elif gap <= FAIL_AUC:
        verdict = "BORDERLINE (act on the tells, then re-run)"
    else:
        verdict = "REWRITE"
    print(f"  panel: validity AUC {valid:.2f} (need {VALID_AUC}); "
          f"A-over-chapter AUC {gap:.2f} (90% {lo:.2f}-{hi:.2f}; pass <= {PASS_AUC}, "
          f"rewrite > {FAIL_AUC}); chapter-over-control {better:.2f}")
    print(f"  verdict: {verdict}")
    out = {"validity_auc": valid, "a_over_chapter_auc": gap, "ci90": [lo, hi],
           "chapter_over_control_auc": better, "verdict": verdict,
           "judges": [{"stem": s, "model": m["judge_model"], "fold": m["fold"],
                       "auc": dict(zip(("a_over_control", "a_over_chapter", "chapter_over_control"), r))}
                      for (s, m, _), (_, r) in zip(runs, per)]}
    (VOICE_DIR / f"{nn}-score.json").write_text(json.dumps(out, indent=1))
    if quiet:
        return verdict
    # Tells: chapter passages rated below the median of Author A's own passages
    for (stem, meta, rows), (g, _) in zip(runs, per):
        bar = st.median(g["exemplar"]) if g["exemplar"] else 50
        low = [(lab, p, a) for src, p, lab, a in rows if src == "chapter" and p < bar]
        fa = [(lab, p, a) for src, p, lab, a in rows if src == "exemplar" and p < 50]
        for lab, p, a in sorted(low, key=lambda x: x[1]):
            print(f"  {stem} {lab} (chapter, p={p:.0f}; Author A median {bar:.0f}): act on these")
            for t in a.get("tells", []):
                print(f"     - {t}")
        for lab, p, a in fa:
            print(f"  {stem} {lab} (Author A false alarm, p={p:.0f}): discount chapter tells like these")
            for t in a.get("tells", []):
                print(f"     - {t}")
    return verdict


# ---------------------------------------------------------------- chain audit (D44)
# The blind authorship judge cannot separate the user's approved prose from the
# drafts he rejected (calibration 2026-10-16), because what he rejected is
# section-level: paragraphs that do not move the section towards its point.
# The chain audit asks a fresh judge to label each paragraph against the
# section's point note and counts the paragraphs that do not advance it.
def chain(stem, spec):
    md = re.sub(r"\A---\n.*?\n---\n", "", read_spec(spec), flags=re.S)
    out, n, sec = [f"# Chain packet {stem}\n"], 0, 0
    for block in re.split(r"\n(?=## )", md):
        head = block.split("\n", 1)[0]
        if not head.startswith("## "):
            continue
        sec += 1
        pt = re.search(r":::+\s*\{\.point\}\s*\n(.*?)\n:::+", block, re.S)
        out += [f"## Section {sec}: {head[3:].strip()}\n",
                f"**Point:** {clean(pt.group(1)) if pt else '(none given)'}\n"]
        for kind, text in paragraphs(block, keep_boxes=True, placeholders=True):
            if kind == "quote":
                out.append(text + "\n")
            elif kind == "box":
                out.append(f"[box] {text}\n")
            else:
                n += 1
                out.append(f"¶{n}. {house_style(text)}\n")
    (VOICE_DIR / f"{stem}-chain-packet.md").write_text("\n".join(out))
    (VOICE_DIR / f"{stem}-chain-key.json").write_text(json.dumps({"source": spec}))
    print(f"reviews/voice/{stem}-chain-packet.md: {sec} sections, {n} paragraphs")


CHAIN_BAD = ("restate", "aside")


def chain_score(stems):
    print(f"  {'packet':14} {'source':52} paras  restate aside  idle%  idle words%")
    rows = []
    for stem in stems:
        src = json.loads((VOICE_DIR / f"{stem}-chain-key.json").read_text())["source"]
        ans = json.loads((VOICE_DIR / f"{stem}-chain-answers.json").read_text())
        labs = ans["paragraphs"]
        pk = (VOICE_DIR / f"{stem}-chain-packet.md").read_text()
        wc = {m.group(1): len(words(m.group(2))) for m in re.finditer(r"¶(\d+)\. (.*)", pk)}
        bad = [k for k, v in labs.items() if v["label"] in CHAIN_BAD]
        idle = len(bad) / max(len(labs), 1)
        idle_w = sum(wc.get(k.lstrip("¶"), 0) for k in bad) / max(sum(wc.values()), 1)
        c = collections.Counter(v["label"] for v in labs.values())
        rows.append((stem, src, idle, idle_w))
        print(f"  {stem:14} {src[-52:]:52} {len(labs):5} {c['restate']:8} {c['aside']:5} "
              f"{100 * idle:5.0f} {100 * idle_w:11.0f}")
    return rows


def openings(spec):
    """First sentence of every body paragraph, for the TONE rule 1 read-through."""
    for i, (_, p) in enumerate(p for p in paragraphs(read_source(spec)) if p[0] == "body"):
        print(f"{i + 1:3}. {sentences(p)[0]}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    opt = lambda name, default=None: a[a.index(name) + 1] if name in a else default
    lst = lambda name: opt(name).split(",") if opt(name) else None
    if a[0] == "profile":
        profile(a[1:] or EXEMPLAR)
    elif a[0] == "blind":
        blind(a[1], [a[2]], judges=tuple(lst("--judges") or ("opus", "fable", "opus")),
              n=int(opt("--n", 6)), rnd=opt("--round", "1"), ctrl=lst("--control"),
              ref=lst("--ref"), pos=lst("--pos"), folds=lst("--folds"))
    elif a[0] == "score":
        v = score(a[1])
        sys.exit(0 if v == "PASS" else 1)
    elif a[0] == "chain":
        chain(a[1], a[2])
    elif a[0] == "chainscore":
        chain_score(a[1:])
    elif a[0] == "openings":
        openings(a[1])
    else:
        sys.exit(__doc__)
