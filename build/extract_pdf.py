#!/usr/bin/env python3
"""Extract a source PDF to sources/extracts/<key>.md with [p. N] page markers.
Usage: python3 build/extract_pdf.py sources/pdfs/X.pdf key"""
import subprocess, sys, pathlib
pdf, key = sys.argv[1], sys.argv[2]
txt = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True, check=True).stdout
pages = txt.split("\f")
out = [f"# {key}\n\n<!-- Extracted from {pdf} with pdftotext. [p. N] = PDF page N (not printed page). -->\n"]
for i, p in enumerate(pages, 1):
    if p.strip():
        out.append(f"\n[p. {i}]\n" + "\n".join(l.rstrip() for l in p.splitlines() if l.strip()))
dst = pathlib.Path("sources/extracts") / f"{key}.md"
dst.write_text("\n".join(out), encoding="utf-8")
print(dst, len(pages), "pages", sum(len(p.split()) for p in pages), "words")
