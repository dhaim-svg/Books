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

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bookconfig  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    ap = argparse.ArgumentParser(description="Build KDP-ready EPUB — The Skybound Wyrm")
    ap.add_argument("--draft", default=None, help="Manuscript draft (default: config default_draft)")
    bookconfig.add_book_arg(ap)
    args = ap.parse_args()

    book = bookconfig.resolve_book(args)
    draft = args.draft or book.default_draft
    pub_dir = book.publishing()
    metadata = pub_dir / "epub-metadata.yaml"
    covers = sorted(pub_dir.glob("*cover*.jpg")) + sorted(pub_dir.glob("*cover*.jpeg"))
    if not covers:
        print(f"ERROR: no '*cover*.jpg' found in {pub_dir}", file=sys.stderr)
        sys.exit(1)
    cover = covers[0]
    out = REPO_ROOT / "dist" / f"{book.slug}.epub"

    if not shutil.which("pandoc"):
        print(
            "ERROR: pandoc not found on PATH.\n"
            "  Install it, then re-run:\n"
            "    winget install --id JohnMacFarlane.Pandoc    (Windows)\n"
            "    https://pandoc.org/installing.html",
            file=sys.stderr,
        )
        sys.exit(1)

    src = book.manuscript(draft)
    front = src / "_front-matter.md"
    back = src / "_back-matter.md"
    chapters = sorted(src.glob("chapter-*.md"))

    missing = [p for p in (metadata, cover, front, back) if not p.exists()]
    if missing or len(chapters) != 40:
        for p in missing:
            print(f"ERROR: missing {p}", file=sys.stderr)
        if len(chapters) != 40:
            print(f"ERROR: expected 40 chapters, found {len(chapters)}", file=sys.stderr)
        sys.exit(1)

    inputs = [front, *chapters, back]
    out.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "pandoc",
        "--from=markdown+smart",          # curl straight quotes, en/em dashes
        f"--metadata-file={metadata}",
        f"--epub-cover-image={cover}",
        "--toc", "--toc-depth=1",
        "--split-level=1",                # split into one EPUB section per H1
        "-o", str(out),
        *[str(p) for p in inputs],
    ]
    print("Running:\n  " + " ".join(cmd) + "\n")
    result = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if result.returncode != 0:
        print(f"\npandoc exited {result.returncode}", file=sys.stderr)
        sys.exit(result.returncode)

    size = out.stat().st_size
    print(f"\nBuilt {out.relative_to(REPO_ROOT)} ({size/1e6:.1f} MB)")
    print("Next: validate in Kindle Previewer (or epubcheck) before uploading to KDP.")


if __name__ == "__main__":
    main()
