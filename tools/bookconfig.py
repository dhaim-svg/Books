#!/usr/bin/env python3
"""
bookconfig.py — per-book path & metadata resolution shared by the book tools.

The book tools (flow_audit, copyedit_audit, normalize_us_spelling, build_epub,
make_audiobook) used to hardcode the Skybound story directory. They now take an
additive `--book <dir>` flag and route path construction through resolve_book().

Resolution order:
    1. --book <dir>            -> that directory is the book root
    2. book.config.yaml        -> read scalar fields from <book>/book.config.yaml
    3. default                 -> the Skybound story dir (preserves old behavior)

book.config.yaml is a FLAT scalar map (no nesting), so we parse it with a tiny
stdlib reader instead of taking a PyYAML dependency — the tools stay stdlib-only.

    slug: skybound-wyrm
    title: The Skybound Wyrm
    author: Theo Weyren
    story_dir: Murder-Mystery-Novel-Fantasy-LitRPG-Story  # informational
    default_draft: Draft_6

`story_dir` in the file is informational; the directory that CONTAINS the config
(or the --book dir, or the default) is always the authoritative book root.
"""

import io
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_STORY_DIR = REPO_ROOT / "Murder-Mystery-Novel-Fantasy-LitRPG-Story"
CONFIG_NAME = "book.config.yaml"


def use_utf8_stdout() -> None:
    """Windows consoles (cp1252) crash on quoted-prose snippets — replace, don't crash."""
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


@dataclass
class Book:
    slug: str
    title: str
    author: str
    story_dir: Path
    default_draft: str

    def manuscript(self, draft: str) -> Path:
        return self.story_dir / "manuscript" / draft

    def feedback(self, draft: str) -> Path:
        return self.story_dir / "review" / f"feedback_{draft}"

    def publishing(self) -> Path:
        return self.story_dir / "publishing"


def _strip_scalar(raw: str) -> str:
    """Strip an inline '# comment', then surrounding quotes/whitespace."""
    # Drop an unquoted inline comment (leave '#' inside quotes alone).
    if not (raw.startswith('"') or raw.startswith("'")):
        hash_at = raw.find("#")
        if hash_at != -1:
            raw = raw[:hash_at]
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        raw = raw[1:-1]
    return raw


def _read_flat_yaml(path: Path) -> dict:
    """Parse a flat 'key: value' scalar map. Ignores blanks, comments, list items."""
    out: dict = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("-"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        out[key.strip()] = _strip_scalar(value)
    return out


def add_book_arg(parser) -> None:
    """Register the shared --book flag on an argparse parser."""
    parser.add_argument(
        "--book",
        metavar="DIR",
        default=None,
        help="Book root directory (default: the Skybound story dir).",
    )


def resolve_book(args) -> Book:
    book_arg = getattr(args, "book", None)
    if book_arg:
        story_dir = Path(book_arg)
        if not story_dir.is_absolute():
            story_dir = REPO_ROOT / story_dir
    else:
        story_dir = DEFAULT_STORY_DIR

    cfg_path = story_dir / CONFIG_NAME
    data = _read_flat_yaml(cfg_path) if cfg_path.is_file() else {}

    return Book(
        slug=data.get("slug", story_dir.name),
        title=data.get("title", story_dir.name),
        author=data.get("author", ""),
        story_dir=story_dir,
        default_draft=data.get("default_draft", "Draft_1"),
    )
