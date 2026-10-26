"""Print each sheet item with the sentence before and after it (verses and quotes shown in brackets).
Usage: python3 reviews/ai/approval/context.py LO HI"""
import json, glob, os, re, sys
items = json.load(open("reviews/ai/approval/sheet.json"))
CH = {os.path.basename(f)[:2]: f for f in glob.glob("book2/chapters/[0-9][0-9]-*.md")}
def clean(t):
    t = re.sub(r"::::? \{\.point\}.*?\n::::?\n", "\n", t, flags=re.S)
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"\[@[^\]]*\]", "", t)
    t = re.sub(r"^:::+ \{\.ayah ref=\"([^\"]+)\"[^\n]*\n(.*?)\n:::+\s*$", lambda m: f"[Verse, Q {m.group(1)}: {m.group(2).strip()}]", t, flags=re.S | re.M)
    t = re.sub(r"^:::+ \{\.quote[^\n]*source=\"([^\"]+)\"[^\n]*\n(.*?)\n:::+\s*$", lambda m: f"[Quoted, {m.group(1)}: {m.group(2).strip()}]", t, flags=re.S | re.M)
    t = re.sub(r"^:::+.*$", "", t, flags=re.M)
    t = re.sub(r"^#+\s*(.*)$", r"[Heading: \1]", t, flags=re.M)
    return t
def sents(t):
    t = re.sub(r"\s+", " ", t).strip()
    return [s for s in re.split(r"(?<=[.!?\]])[\"”]?\s+(?=[A-Z“\"ʿ*\[])", t) if s.strip()]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for it in items:
    if not lo <= it["n"] <= hi: continue
    raw = open(CH[it["ch"]]).read(); b = it["before"]
    i = raw.find(b); pre, post = clean(raw[:i]), clean(raw[i + len(b):])
    ps, ns = sents(pre[-1500:]), sents(post[:1500])
    print(f"### {it['n']} [{it['kind']}]")
    print("PREV:", ps[-1] if ps else "(start)")
    print("ITEM:", re.sub(r"\s+", " ", clean(b)).strip())
    if it.get("after"): print("AFTER:", re.sub(r"\s+", " ", re.sub(r"\[@[^\]]*\]", "", it["after"])).strip())
    print("NEXT:", ns[0] if ns else "(end)")
    print()
