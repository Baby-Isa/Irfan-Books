#!/usr/bin/env bash
# Build an EPUB of all the track scripts, for reading or for a phone's own
# text-to-speech. Needs pandoc.
#
#   ./build_epub.sh [OUT_FILE]
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
out="${1:-$here/the-prayer-inside-and-out.epub}"

pandoc \
  --metadata title="The Prayer, Inside and Out" \
  --metadata subtitle="The words and actions of the daily prayer, and what they mean" \
  --metadata lang=en-GB \
  --toc --toc-depth=1 \
  --split-level=1 \
  -o "$out" \
  "$here"/script/[0-9][0-9]-*.md

echo "Wrote $out"
