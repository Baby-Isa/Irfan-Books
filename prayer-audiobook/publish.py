#!/usr/bin/env python3
"""
Build the podcast site for the rendered tracks, and optionally publish it.

    python publish.py AUDIO_DIR SITE_DIR [--push]

AUDIO_DIR holds the NN-*.mp3 files made by build_audio.py. SITE_DIR gets:

    audio/NN-*.mp3                      one episode per track
    audio/the-prayer-inside-and-out.mp3 every track in one file, to download
    feed.xml                            podcast RSS feed (serial, in order)
    index.html                          a plain page with download links
    the-prayer-inside-and-out.epub      the scripts as an ebook

With --push, SITE_DIR is committed as a fresh orphan commit and
force-pushed to the gh-pages branch, the same way the daily-news-briefing
podcast is published, so the branch only ever holds the current site.
GitHub Pages must be set to serve the gh-pages branch (repository
Settings, Pages, "Deploy from a branch", gh-pages, root).

The feed is marked serial and each episode gets an episode number and a
publication time one minute after the previous track's, so podcast apps
list and play the tracks in order rather than newest first.
"""

import datetime
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))

TITLE = "The Prayer, Inside and Out"
DESCRIPTION = (
    "A companion for long drives: the words and actions of the daily prayer, "
    "what they mean outwardly and inwardly, so they can be recited with "
    "presence of heart. Drawn from Imam Khomeini's Adab as-Salat, the Lantern "
    "of the Path, Sayyid Haydar Amuli's Inner Secrets of the Path and others."
)
AUTHOR = "Irfan Books"
LANGUAGE = "en-gb"
BASE_URL = os.environ.get("PAGES_BASE_URL", "https://baby-isa.github.io/Irfan-Books").rstrip("/")
COMPLETE_NAME = "the-prayer-inside-and-out.mp3"
EPUB_NAME = "the-prayer-inside-and-out.epub"
# Fixed so re-publishing does not reshuffle episodes in podcast apps.
FIRST_PUBLISHED = datetime.datetime(2026, 10, 20, 12, 0, tzinfo=datetime.timezone.utc)
ITUNES = "http://www.itunes.com/dtds/podcast-1.0.dtd"


def duration_seconds(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", path],
        check=True, capture_output=True, text=True,
    )
    return float(out.stdout.strip())


def hms(seconds):
    seconds = int(round(seconds))
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def track_info(mp3_name):
    """Title and a short description for a track, from its script."""
    slug = os.path.splitext(mp3_name)[0]
    number = int(slug.split("-")[0])
    with open(os.path.join(HERE, "script", f"{slug}.md"), encoding="utf-8") as f:
        blocks = [b.strip() for b in re.split(r"\n\s*\n", f.read()) if b.strip()]
    title = blocks[0].lstrip("#").strip().split(": ", 1)[-1]
    body = " ".join(b for b in blocks[1:] if b != "---").replace("*", "")
    body = " ".join(body.split())
    summary = body[:300].rsplit(" ", 1)[0] + "…"
    return number, title, summary


def build_site(audio_dir, site_dir):
    audio_out = os.path.join(site_dir, "audio")
    os.makedirs(audio_out, exist_ok=True)
    tracks = sorted(f for f in os.listdir(audio_dir) if re.match(r"\d\d-.*\.mp3$", f))
    if not tracks:
        sys.exit(f"No NN-*.mp3 files in {audio_dir}")

    episodes = []
    for name in tracks:
        src = os.path.join(audio_dir, name)
        shutil.copy2(src, os.path.join(audio_out, name))
        number, title, summary = track_info(name)
        episodes.append({
            "number": number, "title": title, "summary": summary, "file": name,
            "bytes": os.path.getsize(src), "seconds": duration_seconds(src),
        })

    # Every track in one file. Same encoder settings throughout, so the
    # concat demuxer can join them without re-encoding.
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as lst:
        for name in tracks:
            lst.write(f"file '{os.path.abspath(os.path.join(audio_dir, name))}'\n")
    complete = os.path.join(audio_out, COMPLETE_NAME)
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst.name,
         "-c", "copy", "-metadata", f"title={TITLE}", "-metadata", f"artist={AUTHOR}", complete],
        check=True,
    )
    os.remove(lst.name)
    complete_seconds = duration_seconds(complete)

    subprocess.run([os.path.join(HERE, "build_epub.sh"), os.path.join(site_dir, EPUB_NAME)], check=True)
    write_feed(episodes, os.path.join(site_dir, "feed.xml"))
    write_index(episodes, complete_seconds, os.path.getsize(complete), os.path.join(site_dir, "index.html"))
    print(f"Site built in {site_dir}: {len(episodes)} tracks, {hms(complete_seconds)} in total")


def write_feed(episodes, path):
    ET.register_namespace("itunes", ITUNES)
    ET.register_namespace("atom", "http://www.w3.org/2005/Atom")
    it = "{%s}" % ITUNES
    rss = ET.Element("rss", {"version": "2.0"})
    ch = ET.SubElement(rss, "channel")
    ET.SubElement(ch, "title").text = TITLE
    ET.SubElement(ch, "link").text = BASE_URL + "/"
    ET.SubElement(ch, "description").text = DESCRIPTION
    ET.SubElement(ch, "language").text = LANGUAGE
    ET.SubElement(ch, it + "author").text = AUTHOR
    ET.SubElement(ch, it + "explicit").text = "false"
    ET.SubElement(ch, it + "type").text = "serial"
    ET.SubElement(ch, it + "category", {"text": "Religion & Spirituality"})
    ET.SubElement(ch, "{http://www.w3.org/2005/Atom}link", {
        "href": BASE_URL + "/feed.xml", "rel": "self", "type": "application/rss+xml"})

    for ep in episodes:
        published = FIRST_PUBLISHED + datetime.timedelta(minutes=ep["number"])
        item = ET.SubElement(ch, "item")
        ET.SubElement(item, "title").text = f"{ep['number']}. {ep['title']}"
        ET.SubElement(item, "description").text = ep["summary"]
        ET.SubElement(item, "pubDate").text = published.strftime("%a, %d %b %Y %H:%M:%S +0000")
        ET.SubElement(item, "guid", {"isPermaLink": "false"}).text = f"prayer-inside-and-out-{ep['number']:02d}"
        ET.SubElement(item, "enclosure", {
            "url": f"{BASE_URL}/audio/{ep['file']}", "length": str(ep["bytes"]), "type": "audio/mpeg"})
        ET.SubElement(item, it + "episode").text = str(ep["number"])
        ET.SubElement(item, it + "episodeType").text = "full"
        ET.SubElement(item, it + "duration").text = hms(ep["seconds"])

    ET.ElementTree(rss).write(path, encoding="utf-8", xml_declaration=True)


def write_index(episodes, complete_seconds, complete_bytes, path):
    rows = "\n".join(
        f'<li><a href="audio/{html.escape(ep["file"])}" download>{ep["number"]}. '
        f'{html.escape(ep["title"])}</a> <span>{hms(ep["seconds"])}</span></li>'
        for ep in episodes
    )
    page = f"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<style>
:root {{ --bg:#faf8f3; --fg:#222; --muted:#6b6457; --accent:#1f5f4a; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#16181a; --fg:#e8e6e1; --muted:#a39d91; --accent:#7cc4a8; }} }}
body {{ background:var(--bg); color:var(--fg); font:17px/1.55 Georgia, serif; max-width:40rem; margin:0 auto; padding:2rem 16px; }}
h1 {{ font-weight:normal; margin-bottom:.2rem; }}
p {{ color:var(--muted); }}
a {{ color:var(--accent); }}
ol {{ list-style:none; padding:0; }}
li {{ display:flex; justify-content:space-between; gap:1rem; padding:.45rem 0; border-bottom:1px solid color-mix(in srgb, var(--muted) 30%, transparent); }}
li span {{ color:var(--muted); font-variant-numeric:tabular-nums; }}
.big {{ display:inline-block; margin:1rem 0; padding:.7rem 1.1rem; border:1px solid var(--accent); border-radius:6px; text-decoration:none; }}
</style></head><body>
<h1>{TITLE}</h1>
<p>{html.escape(DESCRIPTION)}</p>
<a class="big" href="audio/{COMPLETE_NAME}" download>Download everything as one MP3 ({hms(complete_seconds)}, {complete_bytes / 1_000_000:.0f} MB)</a>
<p>The full text as an ebook: <a href="{EPUB_NAME}" download>{EPUB_NAME}</a></p>
<p>Or add this feed to a podcast app: <a href="feed.xml">{BASE_URL}/feed.xml</a></p>
<ol>
{rows}
</ol>
</body></html>
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)


def push(site_dir):
    """Force-push site_dir to gh-pages as a single orphan commit."""
    repo = subprocess.run(["git", "-C", HERE, "rev-parse", "--show-toplevel"],
                          check=True, capture_output=True, text=True).stdout.strip()
    remote = subprocess.run(["git", "-C", repo, "remote", "get-url", "origin"],
                            check=True, capture_output=True, text=True).stdout.strip()
    with tempfile.TemporaryDirectory() as tmp:
        def git(*args):
            subprocess.run(["git", "-C", tmp, *args], check=True)
        git("init", "-q", "-b", "gh-pages")
        shutil.copytree(site_dir, tmp, dirs_exist_ok=True)
        open(os.path.join(tmp, ".nojekyll"), "w").close()
        git("add", "-A")
        git("-c", "user.name=podcast-bot", "-c", "user.email=podcast-bot@users.noreply.github.com",
            "commit", "-q", "-m", f"Publish {TITLE} {datetime.date.today().isoformat()}")
        git("push", "--force", remote, "gh-pages")
    print(f"Pushed to gh-pages. Feed: {BASE_URL}/feed.xml")


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    audio_dir, site_dir = sys.argv[1], sys.argv[2]
    build_site(audio_dir, site_dir)
    if "--push" in sys.argv[3:]:
        push(site_dir)


if __name__ == "__main__":
    main()
