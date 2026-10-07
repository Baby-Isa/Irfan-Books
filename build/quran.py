#!/usr/bin/env python3
"""Print verified Quranic Arabic plus Qaraʾi English. Usage: python3 build/quran.py 30:21 [2:255-257 ...]
Copy Arabic into chapters ONLY from this output (golden rule 1)."""
import sys, pathlib
P = pathlib.Path(__file__).resolve().parent.parent / "sources/quran/quran-uthmani.tsv"
Q = {}
for line in P.read_text(encoding="utf-8").splitlines():
    if line.startswith("#"): continue
    s, a, t = line.split("\t"); Q[(int(s), int(a))] = t
T = {}
tp = P.parent / "en.qarai.txt"
if tp.exists():
    for line in tp.read_text(encoding="utf-8").splitlines():
        parts = line.split("|", 2)
        if len(parts) == 3 and parts[0].isdigit():
            T[(int(parts[0]), int(parts[1]))] = parts[2]
for ref in sys.argv[1:]:
    s, a = ref.split(":"); lo, _, hi = a.partition("-")
    for i in range(int(lo), int(hi or lo) + 1):
        print(f"{s}:{i}\t{Q[(int(s), i)]}")
        if T: print(f"  Qaraʾi: {T.get((int(s), i), '?')}")
