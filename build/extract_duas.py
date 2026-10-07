#!/usr/bin/env python3
"""Convert a duas.org data_v2 JSON file to sources/extracts/duas-<slug>.md.
Segments are numbered [§N]; each has Arabic, transliteration and English.
Usage: python3 build/extract_duas.py file.json slug"""
import json, sys, pathlib
src, slug = sys.argv[1], sys.argv[2]
d = json.load(open(src, encoding="utf-8"))
out = [f"# duas.org: {d.get('title', slug)}\n",
       f"<!-- Source: https://www.duas.org/data_v2/{slug}.json (duas.org: 'No Copyright - Extend credit if using the content'). Cite as [@duas_{slug.replace('-', '_')}, §N]. -->\n"]
n = 0
for du in d.get("duas", []):
    out.append(f"\n## {du.get('title','')}\n")
    if du.get("description"): out.append(f"_Description:_ {du['description']}\n")
    if du.get("reference"): out.append(f"_Reference:_ {du['reference']}\n")
    for sg in du.get("segments", []):
        n += 1
        out.append(f"[§{n}]\nAR: {sg.get('arabic','').strip()}\nEN: {sg.get('translation','').strip()}\n")
dst = pathlib.Path("sources/extracts") / f"duas-{slug}.md"
dst.write_text("\n".join(out), encoding="utf-8")
print(dst, n, "segments")
