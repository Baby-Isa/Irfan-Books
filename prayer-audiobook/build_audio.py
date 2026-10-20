#!/usr/bin/env python3
"""
Render the track scripts in script/ to MP3s with Kokoro.

Uses the same engine and voice as the daily-news-briefing podcast
(kokoro-onnx, voice bf_isabella, British English), so it runs offline
with no account or key once the ~350MB model files are downloaded:

    pip install kokoro-onnx soundfile
    base=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
    curl -sSL -o models/kokoro-v1.0.onnx  $base/kokoro-v1.0.onnx
    curl -sSL -o models/voices-v1.0.bin   $base/voices-v1.0.bin

Usage:
    python build_audio.py [OUT_DIR] [TRACK_NUMBER ...]

With no track numbers, every script/NN-*.md is rendered. Needs ffmpeg.

Unlike the news brief, each paragraph is synthesized separately so the
narration can breathe: a short silence between paragraphs, a longer one
at each "---" section break and after the title. That pacing matters
more for a three-hour listen than for a ten-minute bulletin.
"""

import glob
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

VOICE = os.environ.get("KOKORO_VOICE", "bf_isabella")
LANG = os.environ.get("KOKORO_LANG", "en-gb")
SPEED = float(os.environ.get("KOKORO_SPEED", "0.95"))
MODEL_PATH = os.environ.get("KOKORO_MODEL_PATH", os.path.join(HERE, "models/kokoro-v1.0.onnx"))
VOICES_PATH = os.environ.get("KOKORO_VOICES_PATH", os.path.join(HERE, "models/voices-v1.0.bin"))

ALBUM = "The Prayer, Inside and Out"
ARTIST = "Irfan Books"

PAUSE_PARAGRAPH = 0.7
PAUSE_SECTION = 1.8
PAUSE_TITLE = 1.5


def load_pronunciations():
    fixes = []
    with open(os.path.join(HERE, "pronunciations.tsv"), encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            written, spoken = line.rstrip("\n").split("\t")
            fixes.append((written, spoken))
    # Longest first, so "al-Fatiha" is respelled before "Fatiha" can match.
    fixes.sort(key=lambda p: len(p[0]), reverse=True)
    return fixes


def apply_pronunciations(text, fixes):
    for written, spoken in fixes:
        # \b fails next to an apostrophe at the end of "ruku'", so use
        # explicit "not a letter" lookarounds instead.
        text = re.sub(rf"(?<![\w']){re.escape(written)}(?![\w'])", spoken, text, flags=re.IGNORECASE)
    return text


def parse_script(path):
    """Return (title, [segments]) where a segment is a paragraph or None for a section break."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    title = blocks[0].lstrip("#").strip()
    segments = []
    for b in blocks[1:]:
        if b == "---":
            segments.append(None)
        else:
            segments.append(" ".join(b.split()))
    return title, segments


def strip_markdown(text):
    return text.replace("*", "").replace("_", " ")


def render_track(kokoro, path, out_dir, fixes):
    import soundfile as sf

    title, segments = parse_script(path)
    number = int(os.path.basename(path).split("-")[0])
    print(f"Track {number}: {title}")

    chunks = []
    sample_rate = 24000

    def silence(seconds):
        return np.zeros(int(seconds * sample_rate), dtype=np.float32)

    def speak(text):
        nonlocal sample_rate
        spoken = apply_pronunciations(strip_markdown(text), fixes)
        samples, sample_rate = kokoro.create(spoken, voice=VOICE, speed=SPEED, lang=LANG)
        return samples.astype(np.float32)

    chunks += [silence(0.5), speak(title), silence(PAUSE_TITLE)]
    for seg in segments:
        if seg is None:
            chunks.append(silence(PAUSE_SECTION - PAUSE_PARAGRAPH))
            continue
        chunks += [speak(seg), silence(PAUSE_PARAGRAPH)]
    chunks.append(silence(1.5))

    os.makedirs(out_dir, exist_ok=True)
    slug = os.path.splitext(os.path.basename(path))[0]
    wav_path = os.path.join(out_dir, f"{slug}.wav")
    mp3_path = os.path.join(out_dir, f"{slug}.mp3")
    sf.write(wav_path, np.concatenate(chunks), sample_rate)
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error", "-i", wav_path,
            "-ac", "1", "-c:a", "libmp3lame", "-b:a", "64k",
            "-metadata", f"title={number:02d}. {title.split(': ', 1)[-1]}",
            "-metadata", f"album={ALBUM}",
            "-metadata", f"artist={ARTIST}",
            "-metadata", f"track={number}",
            mp3_path,
        ],
        check=True,
    )
    os.remove(wav_path)
    seconds = sum(len(c) for c in chunks) / sample_rate
    print(f"  -> {mp3_path} ({int(seconds // 60)}:{int(seconds % 60):02d})")


def main():
    from kokoro_onnx import Kokoro

    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "audio")
    wanted = {int(n) for n in sys.argv[2:]}
    paths = sorted(glob.glob(os.path.join(HERE, "script", "[0-9][0-9]-*.md")))
    if wanted:
        paths = [p for p in paths if int(os.path.basename(p).split("-")[0]) in wanted]

    fixes = load_pronunciations()
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)
    for path in paths:
        render_track(kokoro, path, out_dir, fixes)


if __name__ == "__main__":
    main()
