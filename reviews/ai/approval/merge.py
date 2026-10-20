"""Merge reviews/ai/approval/NN.json into one numbered approval sheet.
Checks each Before occurs exactly once in its chapter; drops overlaps (comma > variation > rephrase)."""
import json, glob, re, os
CH = {os.path.basename(f)[:2]: f for f in glob.glob("book2/chapters/[0-9][0-9]-*.md")}
ORDER = {"comma": 0, "variation": 1, "rephrase": 2}
LABEL = {"comma": "Weak final commas", "variation": "Variation edits", "rephrase": "For you to rephrase (no fix proposed)"}
def title(path):
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', open(path).read(), re.M); return m.group(1) if m else path
n, out, items_all, problems = 0, [], [], []
for j in sorted(glob.glob("reviews/ai/approval/[0-9][0-9].json")):
    nn = os.path.basename(j)[:2]; path = CH[nn]; text = open(path).read()
    items = sorted(json.load(open(j)), key=lambda x: ORDER[x["kind"]])
    spans, keep = [], []
    for it in items:
        c = text.count(it["before"])
        if c != 1:
            problems.append(f"{nn}: occurs {c}x: {it['before'][:70]}"); continue
        a = text.index(it["before"]); b = a + len(it["before"])
        if any(a < y and x < b for x, y in spans):
            problems.append(f"{nn}: overlap dropped ({it['kind']}): {it['before'][:60]}"); continue
        spans.append((a, b)); keep.append(it)
    name = "Prologue" if nn == "00" else f"Chapter {int(nn)}"
    out.append(f"\n## {name}: {title(path)}\n")
    for kind in ORDER:
        ks = [it for it in keep if it["kind"] == kind]
        if not ks: continue
        out.append(f"\n### {LABEL[kind]}\n")
        for it in ks:
            n += 1; it["n"] = n; it["ch"] = nn; items_all.append(it)
            where = f" ({it['where']})" if it.get("where") else ""
            if kind == "rephrase":
                out.append(f"**{n}.**{where} {it['before']}  \n*Why:* {it.get('note','')}\n")
            else:
                note = f"  \n*Note:* {it['note']}" if it.get("note") else ""
                out.append(f"**{n}.**{where}  \n**Before:** {it['before']}  \n**After:** {it['after']}{note}\n")
counts = {k: sum(1 for i in items_all if i["kind"] == k) for k in ORDER}
head = f"""# Approval sheet: weak commas, variation edits, and sentences for your voice (2026-10-20)

Every chapter, after today's scaffold softening (logs in `reviews/ai/scaffold-sweep-NN-2026-10-20.md`). {n} items: {counts['comma']} weak final commas, {counts['variation']} variation edits, {counts['rephrase']} sentences for you to rephrase. No sentence appears twice. Nothing here is applied yet.

**How to answer:** list the numbers you accept ("yes 1–12, 15"), the ones to keep as they are ("no 13, 14"), and your own wording for any item ("27: …"). For the rephrase items, give your wording or "keep".
"""
open("reviews/ai/approval/SHEET-2026-10-20.md", "w").write(head + "".join(out))
json.dump(items_all, open("reviews/ai/approval/sheet.json", "w"), ensure_ascii=False, indent=1)
print(n, counts); print("\n".join(problems))
