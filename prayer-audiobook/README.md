# The Prayer, Inside and Out

A personal audio companion for long drives: about three hours on the
outward form and inner meaning of the daily prayer (salat), in its Ja'fari
form, so that the words and actions can be recited with presence of heart.

This is a side project in the Irfan-Books repository. It draws on the
source books already here (Lantern of the Path, Inner Secrets of the Path,
Forty Hadith, Spiritual Journey of the Mystics, Light Within Me), plus
Imam Khomeini's *Adab as-Salat* (The Disciplines of the Prayer), in
`sources/books/`.

## Files

| Path | What it is |
|---|---|
| `outline.md` | The 13 tracks, their length and their sources. |
| `style-guide.md` | How the scripts are written: for the ear, for a driver, sources only. |
| `script/NN-*.md` | One narration script per track. |
| `pronunciations.tsv` | Respellings so the synthetic voice says Arabic terms properly. Applied only at render time. |
| `build_audio.py` | Renders the scripts to MP3 with Kokoro (same free offline voice as the daily news briefing). |
| `build_epub.sh` | Builds an EPUB of all the scripts with pandoc. |
| `publish.py` | Builds the podcast site (feed, download page, one complete MP3, EPUB) and pushes it to `gh-pages`. |

## Building

Audio (needs Python, ffmpeg and the Kokoro model files; see the docstring
at the top of `build_audio.py`):

    python build_audio.py audio          # every track
    python build_audio.py audio 1 7      # just tracks 1 and 7

EPUB:

    ./build_epub.sh

## Publishing

    python publish.py audio _site --push

This builds the site and force-pushes it to the `gh-pages` branch as a
single fresh commit, the same way the daily news briefing podcast is
published. With GitHub Pages serving `gh-pages`, it appears at:

- Download page: https://baby-isa.github.io/Irfan-Books/
- Podcast feed (add to a podcast app by URL): https://baby-isa.github.io/Irfan-Books/feed.xml
