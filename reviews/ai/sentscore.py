"""Rank a chapter's sentences by the features GPTZero's most-AI sentences shared (REPORT round 6):
semicolons, colons, The/This/That/It openers, abstract nouns, no quotation, scaffold labels,
"not X but Y". A pointer for the user's own-voice rephrasing list, not a detector.
Usage: python3 -I reviews/ai/sentscore.py FILE [N]"""
import re, sys
def body(s):
    s = re.sub(r"\A---\n.*?\n---\n", "", s, flags=re.S)
    s = re.sub(r"::::? \{\.point\}.*?\n::::\n", "", s, flags=re.S)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"^:::+ \{\.(ayah|quote)[^\n]*\n.*?^:::+\s*$", "", s, flags=re.S | re.M)
    s = re.sub(r"^(:::.*|#.*|\|.*)$", "", s, flags=re.M)
    return s
ABS = re.compile(r"\b\w{4,}(tion|ness|ity|ment|ance|ence|ship|ism)\b", re.I)
SCAF = re.compile(r"\b(the (first|second|third|fourth|last) (is|of)|makes the same point|agrees|reads (this|the|it)|names (two|three|four|five)|"
                  r"there are (two|three|four|five)|in short|in other words|that is why|this is (why|what|the))\b", re.I)
def score(s):
    q = '"' in s or "“" in s
    core = re.sub(r'"[^"]*"|“[^”]*”', "Q", s)
    n = len(core.split())
    f = 0.0
    f += 2 if core.count(";") == 1 else 0          # one semicolon: a mirrored "X; Y" (two or more: a list)
    f += 1 if re.search(r":\s", core) else 0
    f += 1 if re.match(r"[*_]*(The|This|That|These|It)\b", s) else 0
    f += 0.5 * len(ABS.findall(core))
    f += 0 if q else 0.5
    f += 1.5 if re.search(r"\bnot\b[^,;.]{2,60}?\b(but|rather)\b", core) else 0
    f += 1 if SCAF.search(core) else 0
    f += 0.5 if 12 <= n <= 24 else 0
    f -= 1 if n < 8 else 0
    return f
def run(path, k=15):
    t = body(open(path).read())
    out = []
    for p in t.split("\n\n"):
        p = re.sub(r"\s+", " ", p).strip()
        for s in re.split(r"(?<=[.!?])[\"”]?\s+(?=[A-Z“\"ʿ*])", p):
            if len(s.split()) >= 6:
                out.append((score(s), s))
    return sorted(out, key=lambda x: -x[0])[:k]
if __name__ == "__main__":
    for sc, s in run(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 15):
        print(f"{sc:4.1f}  {s}")
