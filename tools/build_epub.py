#!/usr/bin/env python3
"""
build_epub.py — Assemble Draft_6 into a KDP-ready EPUB via Pandoc (Phase D).

Order: copyright front matter -> chapter-01..40 -> back matter. Pandoc generates
the title page from publishing/epub-metadata.yaml (title + subtitle + author) and
the navigation TOC automatically; front-matter headings tagged {.unlisted} are
kept out of the reader's TOC so it starts at Chapter 1.

Requires Pandoc on PATH (https://pandoc.org/installing.html — Windows:
`winget install --id JohnMacFarlane.Pandoc`).

USAGE:
    python tools/build_epub.py                 # build dist/The-Skybound-Wyrm.epub
    python tools/build_epub.py --draft Draft_6  # choose draft
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STORY_DIR = REPO_ROOT / "Murder-Mystery-Novel-Fantasy-LitRPG-Story"
PUB_DIR = STORY_DIR / "publishing"
METADATA = PUB_DIR / "epub-metadata.yaml"
COVER = PUB_DIR / "skybound-wyrm-cover-1600x2560.jpg"
OUT = REPO_ROOT / "dist" / "The-Skybound-Wyrm.epub"


def main() -> None:
    ap = argparse.ArgumentParser(description="Build KDP-ready EPUB — The Skybound Wyrm")
    ap.add_argument("--draft", default="Draft_6", help="Manuscript draft (default Draft_6)")
    args = ap.parse_args()

    if not shutil.which("pandoc"):
        print(
            "ERROR: pandoc not found on PATH.\n"
            "  Install it, then re-run:\n"
            "    winget install --id JohnMacFarlane.Pandoc    (Windows)\n"
            "    https://pandoc.org/installing.html",
            file=sys.stderr,
        )
        sys.exit(1)

    src = STORY_DIR / "manuscript" / args.draft
    front = src / "_front-matter.md"
    back = src / "_back-matter.md"
    chapters = sorted(src.glob("chapter-*.md"))

    missing = [p for p in (METADATA, COVER, front, back) if not p.exists()]
    if missing or len(chapters) != 40:
        for p in missing:
            print(f"ERROR: missing {p}", file=sys.stderr)
        if len(chapters) != 40:
            print(f"ERROR: expected 40 chapters, found {len(chapters)}", file=sys.stderr)
        sys.exit(1)

    inputs = [front, *chapters, back]
    OUT.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "pandoc",
        "--from=markdown+smart",          # curl straight quotes, en/em dashes
        f"--metadata-file={METADATA}",
        f"--epub-cover-image={COVER}",
        "--toc", "--toc-depth=1",
        "--split-level=1",                # split into one EPUB section per H1
        "-o", str(OUT),
        *[str(p) for p in inputs],
    ]
    print("Running:\n  " + " ".join(cmd) + "\n")
    result = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if result.returncode != 0:
        print(f"\npandoc exited {result.returncode}", file=sys.stderr)
        sys.exit(result.returncode)

    size = OUT.stat().st_size
    print(f"\nBuilt {OUT.relative_to(REPO_ROOT)} ({size/1e6:.1f} MB)")
    print("Next: validate in Kindle Previewer (or epubcheck) before uploading to KDP.")


if __name__ == "__main__":
    main()
