#!/usr/bin/env python3
"""Build a book PDF (or check markers).

  python3 build/build.py pdf book1 [--final] [chapter-glob]   → build/out/book1.pdf
  python3 build/build.py check [book1|book2]                   → list VERIFY/QUERY/GAP markers
  python3 build/build.py epub book1                            → build/out/book1.epub

Needs: pandoc ≥3.1, `pip install typst` (fonts are in build/fonts/).
--final fails if any [VERIFY]/[QUERY]/[GAP] marker remains and hides draft styling.
"""
import glob, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
OUT = BUILD / "out"
MARK = re.compile(r"\[(VERIFY|QUERY|GAP):[^\]]*\]")
BOOKS = {
    "book1": ("ʿIrfan: Lectures on Islamic Mysticism", "The Lecture Series", "Book One · Faithful edition"),
    "book2": ("ʿIrfan: A Journey into Islamic Mysticism", "An Introduction for Seekers", "Book Two · Expanded edition"),
    "sample": ("ʿIrfan: Design Sample", "Typography and ornament test", "Not a real chapter"),
}


def chapters(book, pattern="*"):
    base = BUILD / "sample" if book == "sample" else ROOT / book / "chapters"
    return sorted(base.glob(f"{pattern}.md"))


def check(books):
    total = 0
    for b in books:
        for f in chapters(b):
            for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
                for m in MARK.finditer(line):
                    total += 1
                    print(f"{f.relative_to(ROOT)}:{n}: {m.group(0)[:110]}")
    print(f"{total} open marker(s)")
    return total


def pdf(book, final=False, pattern="*"):
    if final and check([book]):
        sys.exit("release build refused: open markers remain")
    OUT.mkdir(exist_ok=True)
    work = OUT / book
    work.mkdir(exist_ok=True)
    env = dict(os.environ, IRFAN_ROOT=str(ROOT))
    includes = []
    for f in chapters(book, pattern):
        typ = work / (f.stem + ".typ")
        subprocess.run(["pandoc", str(f), "-f", "markdown", "-t", "typst",
                        "--lua-filter", str(BUILD / "irfan.lua"),
                        "--template", str(BUILD / "chapter.typst-template"),
                        "-o", str(typ)], check=True, env=env)
        includes.append(f'#include "{typ.name}"')
    title, sub, ed = BOOKS[book]
    main = work / "main.typ"
    main.write_text(
        f'#import "../../template.typ": *\n'
        f'#show: book.with(title: "{title}", subtitle: "{sub}", edition: "{ed}", draft: {str(not final).lower()})\n'
        + "\n".join(includes) + "\n", encoding="utf-8")
    import typst
    target = OUT / f"{book}.pdf"
    typst.compile(str(main), output=str(target), root=str(BUILD),
                  font_paths=[str(BUILD / "fonts")], ignore_system_fonts=True)
    print(f"wrote {target.relative_to(ROOT)}")


def epub(book):
    OUT.mkdir(exist_ok=True)
    target = OUT / f"{book}.epub"
    title = BOOKS[book][0]
    subprocess.run(["pandoc", *map(str, chapters(book)), "-o", str(target),
                    "--metadata", f"title={title}", "--toc", "--split-level=1"], check=True)
    print(f"wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    cmd = a[0]
    if cmd == "check":
        sys.exit(1 if check(a[1:] or ["book1", "book2"]) else 0)
    book = a[1]
    if cmd == "pdf":
        rest = [x for x in a[2:] if x != "--final"]
        pdf(book, final="--final" in a, pattern=rest[0] if rest else "*")
    elif cmd == "epub":
        epub(book)
