"""Apply the user's answers (answers.json) to the chapters, by the exact befores in sheet.json.
Usage: python3 reviews/ai/approval/apply.py LO HI   (item numbers; skips items already applied)"""
import json, glob, os, sys
items = {str(i["n"]): i for i in json.load(open("reviews/ai/approval/sheet.json"))}
ans = json.load(open("reviews/ai/approval/answers.json"))
done_p = "reviews/ai/approval/applied.json"
done = set(json.load(open(done_p))) if os.path.exists(done_p) else set()
CH = {os.path.basename(f)[:2]: f for f in glob.glob("book2/chapters/[0-9][0-9]-*.md")}
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for k, v in sorted(ans.items(), key=lambda x: int(x[0])):
    if not lo <= int(k) <= hi or k in done: continue
    it = items[k]; path = CH[it["ch"]]; text = open(path).read()
    before = v.get("before_override", it["before"])
    if v["d"] == "before":
        done.add(k); continue
    new = it["after"] if v["d"] == "after" else v["text"]
    if before.startswith("\n") and not new.startswith("\n"): new = "\n" + new
    if text.count(before) != 1:
        print(f"SKIP {k}: before occurs {text.count(before)}x in {path}"); continue
    open(path, "w").write(text.replace(before, new)); done.add(k); print(f"applied {k} ({v['d']})")
json.dump(sorted(done, key=int), open(done_p, "w"))
