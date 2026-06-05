# Reusable Novel-Writing Framework Guide — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extract the repo's reusable novel-writing spine into a root-level `framework/` template kit and make the five book tools config-driven (a `--book` flag), without changing any published *Skybound Wyrm* content.

**Architecture:** A new `tools/bookconfig.py` module resolves a `Book` (paths + metadata) from a `--book <dir>` flag, a discovered `book.config.yaml`, or a default that is the current Skybound story dir — so every existing command behaves identically. The five tools gain an additive `--book` flag that routes path construction through that resolver. A `framework/templates/book-template/` tree holds genre-neutral, genericized copies of the bible/chapter/review/publishing scaffolding plus a `GUIDE.md` walkthrough; the untouched Skybound folder is the worked example the guide points to.

**Tech Stack:** Python 3 (stdlib only — no PyYAML; a tiny flat-scalar YAML reader lives in `bookconfig.py`), `unittest` for tests, Markdown for the framework content, Pandoc for the EPUB build (unchanged).

**Reference spec:** `docs/superpowers/specs/2026-06-04-framework-guide-design.md`

---

## File Structure

**New code:**
- `tools/bookconfig.py` — `Book` dataclass + `resolve_book(args)` + flat-YAML reader + shared stdout-UTF-8 helper. One responsibility: turn CLI args into resolved per-book paths/metadata.
- `tests/test_bookconfig.py` — `unittest` coverage for the resolution order and path helpers.

**Modified code (additive `--book` only — default behavior preserved):**
- `tools/flow_audit.py`, `tools/copyedit_audit.py`, `tools/normalize_us_spelling.py`, `tools/build_epub.py`, `tools/make_audiobook.py`.

**New config (round-trips Skybound through the resolver):**
- `Murder-Mystery-Novel-Fantasy-LitRPG-Story/book.config.yaml`.

**New framework tree (all new files, no existing files touched):**
- `framework/GUIDE.md`
- `framework/templates/book-template/` — `book.config.yaml`, `CLAUDE.md`, `bible/*`, `chapters/*`, `state/*`, `review/*`, `publishing/*`, `manuscript/Draft_1/.gitkeep`.

---

## Conventions used in every task

- Run all commands from the repo root `D:\Projects\Books` (the working dir). Use forward slashes in Python paths; the tools already use `pathlib`.
- Tests are dependency-free: `python -m unittest tests.test_bookconfig -v`.
- Commit after each task. Commit messages end with the required trailer:
  ```
  Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
  ```

---

### Task 1: `tools/bookconfig.py` resolver + tests

**Files:**
- Create: `tools/bookconfig.py`
- Create: `tests/test_bookconfig.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_bookconfig.py`:

```python
import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import bookconfig  # noqa: E402


def _ns(**kw):
    base = {"book": None}
    base.update(kw)
    return Namespace(**base)


class ResolveBookTests(unittest.TestCase):
    def test_default_is_skybound(self):
        book = bookconfig.resolve_book(_ns())
        self.assertEqual(book.story_dir, bookconfig.DEFAULT_STORY_DIR)
        # Skybound config supplies these once Task 7 lands; resolver must not crash
        # if the file is missing, so only assert the path shape here.
        self.assertTrue(str(book.story_dir).endswith("Murder-Mystery-Novel-Fantasy-LitRPG-Story"))

    def test_book_flag_overrides_dir(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "book.config.yaml").write_text(
                'slug: dummy\ntitle: Dummy Book\nauthor: A. N. Other\n'
                'story_dir: ignored\ndefault_draft: Draft_2\n',
                encoding="utf-8",
            )
            book = bookconfig.resolve_book(_ns(book=str(d)))
            self.assertEqual(book.story_dir, d)
            self.assertEqual(book.slug, "dummy")
            self.assertEqual(book.title, "Dummy Book")
            self.assertEqual(book.author, "A. N. Other")
            self.assertEqual(book.default_draft, "Draft_2")

    def test_missing_config_falls_back_to_dir_name(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            book = bookconfig.resolve_book(_ns(book=str(d)))
            self.assertEqual(book.slug, d.name)
            self.assertEqual(book.default_draft, "Draft_1")

    def test_path_helpers(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            book = bookconfig.resolve_book(_ns(book=str(d)))
            self.assertEqual(book.manuscript("Draft_3"), d / "manuscript" / "Draft_3")
            self.assertEqual(book.feedback("Draft_3"), d / "review" / "feedback_Draft_3")
            self.assertEqual(book.publishing(), d / "publishing")

    def test_inline_comment_and_quotes_stripped(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "book.config.yaml").write_text(
                'slug: "q"   # trailing comment\ntitle: \'Quoted Title\'\n',
                encoding="utf-8",
            )
            book = bookconfig.resolve_book(_ns(book=str(d)))
            self.assertEqual(book.slug, "q")
            self.assertEqual(book.title, "Quoted Title")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python -m unittest tests.test_bookconfig -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'bookconfig'` (file not created yet).

- [ ] **Step 3: Write `tools/bookconfig.py`**

```python
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
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `python -m unittest tests.test_bookconfig -v`
Expected: PASS — all 5 tests OK.

- [ ] **Step 5: Commit**

```bash
git add tools/bookconfig.py tests/test_bookconfig.py
git commit -m "Add bookconfig resolver for config-driven book tools"
```

---

### Task 2: Route `flow_audit.py` through the resolver

**Files:**
- Modify: `tools/flow_audit.py` (constants at `:45-47`, `parse_args` at `:427`, `main` at `:447-503`)

- [ ] **Step 1: Add the import and `--book` flag**

At the top of `tools/flow_audit.py`, after the existing stdout wrapper block (around line 38), add:

```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bookconfig  # noqa: E402
```

In `parse_args()` (before `return p.parse_args()`), add:

```python
    bookconfig.add_book_arg(p)
```

- [ ] **Step 2: Make `main()` resolve paths from the book**

In `main()`, replace the manuscript/report path construction. Change:

```python
    args = parse_args()
    manuscript_dir = STORY_DIR / "manuscript" / args.draft
```

to:

```python
    args = parse_args()
    book = bookconfig.resolve_book(args)
    manuscript_dir = book.manuscript(args.draft)
```

And replace the report-writing block (currently using module-level `REPORT_PATH`):

```python
    report = build_report(results, args.draft)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(f"\nReport written → {REPORT_PATH.relative_to(REPO_ROOT)}")
```

with:

```python
    report = build_report(results, args.draft)
    report_path = book.feedback(args.draft) / "_flow-audit.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport written → {report_path.relative_to(REPO_ROOT)}")
```

Delete the now-unused module-level `REPORT_PATH = ...` line (`:47`). Leave `REPO_ROOT` and `STORY_DIR` defined (still referenced by `relative_to`/imports and harmless).

> Note: this changes the flow-audit report destination from the hardcoded `feedback_Draft_5/` to `feedback_<draft>/`, matching the per-draft convention the other tools already use. That is the intended fix, not a regression.

- [ ] **Step 3: Smoke-test default behavior**

Run: `python tools/flow_audit.py --chapter 02 --draft Draft_6`
Expected: prints the chapter-02 flow stats with no path error (default book = Skybound).

- [ ] **Step 4: Smoke-test the `--book` flag resolves**

Run: `python tools/flow_audit.py --book Murder-Mystery-Novel-Fantasy-LitRPG-Story --chapter 02 --draft Draft_6`
Expected: identical output to Step 3.

- [ ] **Step 5: Commit**

```bash
git add tools/flow_audit.py
git commit -m "flow_audit: resolve paths via bookconfig --book"
```

---

### Task 3: Route `copyedit_audit.py` through the resolver

**Files:**
- Modify: `tools/copyedit_audit.py` (constants `:50-56`, `parse_args` `:392`, `main` `:400-440`)

- [ ] **Step 1: Add the import and `--book` flag**

After the stdout wrapper block (around line 47), add:

```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bookconfig  # noqa: E402
```

In `parse_args()` (before `return p.parse_args()`), add:

```python
    bookconfig.add_book_arg(p)
```

- [ ] **Step 2: Make `main()` resolve paths from the book**

Replace:

```python
    args = parse_args()
    manuscript_dir = STORY_DIR / "manuscript" / args.draft
```

with:

```python
    args = parse_args()
    book = bookconfig.resolve_book(args)
    manuscript_dir = book.manuscript(args.draft)
```

Replace the report path resolution:

```python
    report = build_report(results, args.draft)
    rp = report_path_for(args.draft)
```

with:

```python
    report = build_report(results, args.draft)
    rp = book.feedback(args.draft) / "_copyedit-mechanical.md"
```

Delete the now-unused `report_path_for()` helper (`:55-56`).

- [ ] **Step 3: Smoke-test default behavior**

Run: `python tools/copyedit_audit.py --chapter 01 --draft Draft_6`
Expected: prints chapter-01 mechanical findings, no path error.

- [ ] **Step 4: Regression — full report matches prior behavior**

Run: `python tools/copyedit_audit.py --draft Draft_6`
Expected: writes `Murder-Mystery-Novel-Fantasy-LitRPG-Story/review/feedback_Draft_6/_copyedit-mechanical.md` and prints `Report written → ...feedback_Draft_6/_copyedit-mechanical.md`.

- [ ] **Step 5: Commit**

```bash
git add tools/copyedit_audit.py
git commit -m "copyedit_audit: resolve paths via bookconfig --book"
```

---

### Task 4: Route `normalize_us_spelling.py` through the resolver

**Files:**
- Modify: `tools/normalize_us_spelling.py` (constants `:43-44`, `parse_args` `:223`, `main` `:232-235`)

- [ ] **Step 1: Add the import and `--book` flag**

After the stdout wrapper block (around line 41), add:

```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bookconfig  # noqa: E402
```

In `parse_args()` (before `return p.parse_args()`), add:

```python
    bookconfig.add_book_arg(p)
```

- [ ] **Step 2: Make `main()` resolve src/dst from the book**

Replace:

```python
    args = parse_args()
    src_dir = STORY_DIR / "manuscript" / args.src
    dst_dir = STORY_DIR / "manuscript" / args.dst
```

with:

```python
    args = parse_args()
    book = bookconfig.resolve_book(args)
    src_dir = book.manuscript(args.src)
    dst_dir = book.manuscript(args.dst)
```

- [ ] **Step 3: Smoke-test a no-write audit on the published draft**

Run: `python tools/normalize_us_spelling.py --src Draft_6 --dry-run --audit`
Expected: reports `0` residual UK forms (Draft_6 is already normalized), writes nothing.

- [ ] **Step 4: Verify `--book` resolves the same dir**

Run: `python tools/normalize_us_spelling.py --book Murder-Mystery-Novel-Fantasy-LitRPG-Story --src Draft_6 --dry-run --audit`
Expected: identical to Step 3.

- [ ] **Step 5: Commit**

```bash
git add tools/normalize_us_spelling.py
git commit -m "normalize_us_spelling: resolve paths via bookconfig --book"
```

---

### Task 5: Route `build_epub.py` through the resolver

**Files:**
- Modify: `tools/build_epub.py` (constants `:24-29`, `main` `:32-81`)

- [ ] **Step 1: Add the import and `--book` flag**

After the imports (around line 22), add:

```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bookconfig  # noqa: E402
```

In `main()`, in the argparse block, after the `--draft` argument, add:

```python
    bookconfig.add_book_arg(ap)
```

- [ ] **Step 2: Resolve book-relative paths inside `main()`**

Change the `--draft` default so the config can drive it:

```python
    ap.add_argument("--draft", default=None, help="Manuscript draft (default: config default_draft)")
```

After `args = ap.parse_args()`, replace the hardcoded module constants by resolving from the book. Insert:

```python
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
```

Then update the rest of `main()` to use these locals instead of the module constants:
- `src = STORY_DIR / "manuscript" / args.draft` → `src = book.manuscript(draft)`
- `missing = [p for p in (METADATA, COVER, front, back) ...]` → `missing = [p for p in (metadata, cover, front, back) ...]`
- `OUT.parent.mkdir(...)` → `out.parent.mkdir(parents=True, exist_ok=True)`
- in the pandoc `cmd`: `f"--metadata-file={METADATA}"` → `f"--metadata-file={metadata}"`; `f"--epub-cover-image={COVER}"` → `f"--epub-cover-image={cover}"`; `"-o", str(OUT)` → `"-o", str(out)`
- the closing report lines using `OUT` → `out`

Delete the module-level `STORY_DIR`, `PUB_DIR`, `METADATA`, `COVER`, `OUT` constants (`:25-29`); keep `REPO_ROOT`.

- [ ] **Step 3: Regression build (only if Pandoc is on PATH)**

Run: `python tools/build_epub.py`
Expected: `Built dist/skybound-wyrm.epub (X.X MB)`. (Filename is now slug-based — `skybound-wyrm.epub` — which is fine; the KDP upload already happened from the prior `The-Skybound-Wyrm.epub`. If Pandoc is not installed, the tool prints the install hint and exits 1 — acceptable; note it in the task report and move on.)

- [ ] **Step 4: Commit**

```bash
git add tools/build_epub.py
git commit -m "build_epub: resolve paths/metadata via bookconfig --book"
```

---

### Task 6: Add `--book` to `make_audiobook.py`

**Files:**
- Modify: `tools/make_audiobook.py` (argparse + `main` `:127-158`)

`make_audiobook.py` already takes `--input-dir`/`--output-dir` and has no `STORY_DIR`. The `--book` flag here just supplies smarter defaults when the explicit dirs aren't given, keeping it consistent with the other four tools.

- [ ] **Step 1: Add the import and `--book` flag**

After the imports (around line 33), add:

```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bookconfig  # noqa: E402
```

In `main()`, change the `--input-dir` / `--output-dir` defaults to sentinels and register `--book`:

```python
    parser.add_argument('--book', metavar='DIR', default=None,
                        help='Book root (default: Skybound). Sets --input-dir default.')
    parser.add_argument('--input-dir', default=None,
                        help='Chapter source dir (default: <book>/manuscript/<default_draft>)')
    parser.add_argument('--output-dir', default=None,
                        help='Output dir for WAV files (default: audiobook/<default_draft>)')
```

(Replace the existing `--input-dir`/`--output-dir` definitions; keep the other arguments unchanged.)

- [ ] **Step 2: Resolve defaults from the book in `main()`**

After `args = parser.parse_args()`, before `input_dir = Path(args.input_dir)`, insert:

```python
    book = bookconfig.resolve_book(args)
    input_dir = Path(args.input_dir) if args.input_dir else book.manuscript(book.default_draft)
    output_dir = Path(args.output_dir) if args.output_dir else (
        bookconfig.REPO_ROOT / "audiobook" / book.default_draft)
```

and delete the now-duplicate `input_dir = Path(args.input_dir)` / `output_dir = Path(args.output_dir)` lines.

- [ ] **Step 3: Verify argument parsing (no TTS deps needed)**

Run: `python tools/make_audiobook.py --help`
Expected: help text lists `--book`, `--input-dir`, `--output-dir`; exits 0. (A full run needs the audiobook venv — out of scope here.)

- [ ] **Step 4: Commit**

```bash
git add tools/make_audiobook.py
git commit -m "make_audiobook: add --book flag for default I/O dirs"
```

---

### Task 7: Add `book.config.yaml` to Skybound + regression-verify all tools

**Files:**
- Create: `Murder-Mystery-Novel-Fantasy-LitRPG-Story/book.config.yaml`

- [ ] **Step 1: Write the Skybound config**

Create `Murder-Mystery-Novel-Fantasy-LitRPG-Story/book.config.yaml`:

```yaml
# Per-book config consumed by the tools in tools/ via bookconfig.resolve_book().
slug: skybound-wyrm
title: The Skybound Wyrm
author: Theo Weyren
story_dir: Murder-Mystery-Novel-Fantasy-LitRPG-Story   # informational; folder is authoritative
default_draft: Draft_6
```

- [ ] **Step 2: Re-run the resolver tests (now with the real Skybound config present)**

Run: `python -m unittest tests.test_bookconfig -v`
Expected: PASS (all tests still green; `test_default_is_skybound` now also reads real metadata).

- [ ] **Step 3: Add an assertion that the default book reads Skybound metadata**

Append a test method to `tests/test_bookconfig.py` inside `ResolveBookTests`:

```python
    def test_default_reads_skybound_config(self):
        book = bookconfig.resolve_book(_ns())
        self.assertEqual(book.slug, "skybound-wyrm")
        self.assertEqual(book.title, "The Skybound Wyrm")
        self.assertEqual(book.author, "Theo Weyren")
        self.assertEqual(book.default_draft, "Draft_6")
```

Run: `python -m unittest tests.test_bookconfig -v`
Expected: PASS, including the new `test_default_reads_skybound_config`.

- [ ] **Step 4: Full backward-compat regression sweep**

Run each and confirm no path errors and the expected report destinations:

```bash
python tools/flow_audit.py --draft Draft_6 --no-report
python tools/copyedit_audit.py --draft Draft_6 --no-report
python tools/normalize_us_spelling.py --src Draft_6 --dry-run --audit
```

Expected: flow audit prints per-chapter stats; copyedit prints findings; normalizer reports 0 residual UK forms. None write outside `Murder-Mystery-Novel-Fantasy-LitRPG-Story/`.

- [ ] **Step 5: Confirm Skybound prose is untouched**

Run: `git status --porcelain Murder-Mystery-Novel-Fantasy-LitRPG-Story/manuscript Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible`
Expected: empty output (only the new `book.config.yaml` is added, which is outside those paths).

- [ ] **Step 6: Commit**

```bash
git add Murder-Mystery-Novel-Fantasy-LitRPG-Story/book.config.yaml tests/test_bookconfig.py
git commit -m "Add Skybound book.config.yaml; verify tool backward-compat"
```

---

### Task 8: Scaffold the `framework/` tree

**Files:**
- Create: `framework/templates/book-template/book.config.yaml`
- Create: `framework/templates/book-template/manuscript/Draft_1/.gitkeep`

- [ ] **Step 1: Create the directory skeleton**

```bash
mkdir -p framework/templates/book-template/bible
mkdir -p framework/templates/book-template/chapters
mkdir -p framework/templates/book-template/state
mkdir -p framework/templates/book-template/review
mkdir -p framework/templates/book-template/publishing
mkdir -p framework/templates/book-template/manuscript/Draft_1
```

(On Windows PowerShell, use `New-Item -ItemType Directory -Force <path>` for each, or run the above via the Bash tool.)

- [ ] **Step 2: Add the template config**

Create `framework/templates/book-template/book.config.yaml`:

```yaml
# Copy this whole folder to start a new book, then fill these in.
# The tools in tools/ read this via `--book <this-folder>`.
slug: my-book-slug              # kebab-case; used for the EPUB filename
title: My Book Title
author: Pen Name
story_dir: my-book-folder       # informational; the folder itself is authoritative
default_draft: Draft_1
```

- [ ] **Step 3: Keep the empty manuscript dir in git**

Create `framework/templates/book-template/manuscript/Draft_1/.gitkeep` with content:

```
# Drafts land here: chapter-01.md … chapter-NN.md, plus _front-matter.md / _back-matter.md.
```

- [ ] **Step 4: Commit**

```bash
git add framework/templates/book-template/book.config.yaml framework/templates/book-template/manuscript/Draft_1/.gitkeep
git commit -m "Scaffold framework/book-template directory tree"
```

---

### Task 9: Genericize the reusable-default bible files

**Files:**
- Create: `framework/templates/book-template/bible/12-step-formula.md`
- Create: `framework/templates/book-template/bible/standing-style.md`
- Create: `framework/templates/book-template/bible/brand-voice.md`

These are **transform-from-source** files: copy the Skybound original, then strip story-specific content per the checklist. The craft (structure, prose rules, rhythm guidance) stays; the plot/character specifics become genre-neutral placeholders.

- [ ] **Step 1: Copy the three sources into the template**

```bash
cp Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/12-step-formula.md framework/templates/book-template/bible/12-step-formula.md
cp Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/standing-style.md   framework/templates/book-template/bible/standing-style.md
cp Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/brand-voice.md      framework/templates/book-template/bible/brand-voice.md
```

- [ ] **Step 2: Genericize `12-step-formula.md`**

Read the copied file. Apply these transformations (use Edit per occurrence):
- Keep verbatim: the three-act framing, all 12 step **definitions**, the chapters-per-step guidance, the structural-hinge notes (e.g. "Step 6 = 4 chapters").
- Replace every Skybound plot instantiation of a step with a neutral prompt. Pattern: where a step says what happens *in Skybound* (names like Theron/Sable/Joren/Vannic/Halsa, the murder/airship/System specifics), replace that sentence with `> _For your book: <one-line prompt describing what this step needs>._`
- Remove the "ending twist"/reveal specifics entirely; replace with `> _For your book: define your Act-2 reveal in premise-and-twist.md._`

Verification grep (must return nothing):
`grep -niE "Theron|Sable|Joren|Vannic|Halsa|Skybound|airship|drake" framework/templates/book-template/bible/12-step-formula.md`

- [ ] **Step 3: Genericize `standing-style.md`**

- Keep verbatim: POV rules, tense rules, prose-discipline rules, plant/foreshadow *mechanics* phrased generically, the System-rendering rule ("indented italic block, not HUD box") since LitRPG-neutral phrasing is fine — but reword as `> _If your book has a game/System layer:_` so non-LitRPG books can ignore it.
- Replace Sable/Theron/named-character examples with `the protagonist` / `a supporting character` / `[CHARACTER]`.
- Replace the five Skybound "planted details" list with a generic instruction: `> _List your book's planted details here — textural, not investigative._`

Verification grep (must return nothing):
`grep -niE "Theron|Sable|Joren|Vannic|Halsa|Skybound|calluses|carved fish|niece" framework/templates/book-template/bible/standing-style.md`

- [ ] **Step 4: Genericize `brand-voice.md`**

- Keep verbatim: §4 prose mechanics, §5 tonal register, §6 anti-slop checklist, §8 quick-reference checklist — these are craft, not story.
- Neutralize any worked example that quotes Skybound prose: replace the quoted snippet with a short invented-neutral example or `> _Example (replace with your own voice):_`.
- Replace cozy-LitRPG-specific register notes with `> _Set your book's register here (this template's example was cozy LitRPG)._` while keeping the *structure* of the register section.

Verification grep (must return nothing):
`grep -niE "Theron|Sable|Joren|Vannic|Halsa|Skybound|airship|drake" framework/templates/book-template/bible/brand-voice.md`

- [ ] **Step 5: Run all three greps together**

```bash
grep -rniE "Theron|Sable|Joren|Vannic|Halsa|Skybound|airship|drake|calluses|carved fish" framework/templates/book-template/bible/12-step-formula.md framework/templates/book-template/bible/standing-style.md framework/templates/book-template/bible/brand-voice.md
```
Expected: no output (zero leakage).

- [ ] **Step 6: Commit**

```bash
git add framework/templates/book-template/bible/12-step-formula.md framework/templates/book-template/bible/standing-style.md framework/templates/book-template/bible/brand-voice.md
git commit -m "Add genericized reusable bible templates (structure/style/voice)"
```

---

### Task 10: Genericize the workspace `CLAUDE.md` template

**Files:**
- Create: `framework/templates/book-template/CLAUDE.md`

- [ ] **Step 1: Copy the source**

```bash
cp CLAUDE.md framework/templates/book-template/CLAUDE.md
```

- [ ] **Step 2: Genericize it**

Edit the copy:
- Replace the project header/title and the "Cozy LitRPG Murder Mystery" tagline with `# {{BOOK_TITLE}} — Claude Workspace Instructions` and `**Project:** {{GENRE}} — chapter-by-chapter drafting.`
- Replace the `Murder-Mystery-Novel-Fantasy-LitRPG-Story/...` path prefixes in the bible/state/chapter links with relative `bible/…`, `state/…`, `chapters/…` (the template IS the book root, so paths are relative).
- Keep verbatim, as the reusable spine: the "Story Bible (read before every chapter)" list, the "Session State" list, the "Chapter Specs" list, the **Workflow: "Schreib Kapitel N"** numbered loop, the **Book Targets** table (mark the numbers as `> _tune to your book_`), and the "What NOT to Do (General)" list.
- Convert the **Spoiler Guardrail — HARD RULES** section into an **optional, clearly-labeled pattern**: retitle it `## Optional Pattern — Spoiler / Reveal Guardrail` with a lead line: `> _Keep this section only if your book has a twist/reveal to protect. Replace the Skybound-specific rules below with your own._` Replace the Vannic/Joren/identity-swap specifics with `[describe your reveal]` / `[your planted details]` placeholders.
- Rename the `ending-twist.md` reference to `premise-and-twist.md` to match the template's bible file.

- [ ] **Step 3: Verify no Skybound leakage and no absolute story paths remain**

```bash
grep -niE "Theron|Sable|Joren|Vannic|Halsa|Skybound|Murder-Mystery-Novel-Fantasy-LitRPG-Story|ending-twist" framework/templates/book-template/CLAUDE.md
```
Expected: no output.

- [ ] **Step 4: Commit**

```bash
git add framework/templates/book-template/CLAUDE.md
git commit -m "Add genericized CLAUDE.md workspace template"
```

---

### Task 11: Genericize the review briefs + plot-audit prompt

**Files:**
- Create: `framework/templates/book-template/review/review-brief-blind.md`
- Create: `framework/templates/book-template/review/review-brief-informed.md`
- Create: `framework/templates/book-template/review/plot-audit-prompt.md`

- [ ] **Step 1: Copy the two review briefs**

```bash
cp Murder-Mystery-Novel-Fantasy-LitRPG-Story/review/review-brief-blind.md    framework/templates/book-template/review/review-brief-blind.md
cp Murder-Mystery-Novel-Fantasy-LitRPG-Story/review/review-brief-informed.md framework/templates/book-template/review/review-brief-informed.md
```

- [ ] **Step 2: Genericize both briefs**

In each copy, replace book/character specifics with placeholders, keeping the review *structure and questions*:
- Book title → `{{BOOK_TITLE}}`; protagonist/named characters → `the protagonist` / `[CHARACTER]`.
- Any cozy-LitRPG-mystery genre framing → `{{GENRE}}` (keep the genre-shaped questions but make the noun a placeholder).
- Keep verbatim: the blind-vs-informed distinction, the rubric/dimensions, the output-format instructions, the "treat `*[Investigator —]*` system lines as intentional convention" note (reword to `*[System —]*`-style, configurable).

- [ ] **Step 3: Author the genericized plot-audit prompt**

The plot-audit prompt lives in the workflow memory, not a repo file. Create `framework/templates/book-template/review/plot-audit-prompt.md` capturing the genericized 7-pass recipe:

```markdown
# Plot Audit Prompt (read-only, whole-manuscript)

Run a **read-only** structural/continuity audit across the full assembled manuscript
(`manuscript/<draft>/_full-manuscript.md`). Do **not** rewrite prose — report findings only.

For `{{BOOK_TITLE}}`, run these seven passes and report findings per pass with
`chapter:line`-style anchors:

1. **Timeline & chronology** — day/time markers, travel durations, "X days later" claims.
2. **Character knowledge** — who knows what, when; flag any knowledge that arrives before it was earned.
3. **Object & detail continuity** — items, wounds, clothing, locations; appearances vs. later references.
4. **Setup ↔ payoff** — every planted detail pays off; every payoff was planted.
5. **Cast consistency** — names, titles, relationships, physical descriptions across chapters.
6. **Stakes & motivation** — each scene's goal/conflict; flag scenes that don't move the throughline.
7. **Genre-mechanics consistency** — if your book has a System/magic/tech ruleset, verify its rules
   never contradict earlier uses. Treat in-world system lines (e.g. `*[System — ...]*`) as an
   intentional, configurable convention, not an error.

**Output:** one Markdown section per pass; each finding gets a severity (blocker / seam / nit) and an
anchor. Adversarially verify each finding against the source before reporting it — drop misreadings.
```

- [ ] **Step 4: Verify no leakage**

```bash
grep -rniE "Theron|Sable|Joren|Vannic|Halsa|Skybound|Investigator" framework/templates/book-template/review/
```
Expected: no output.

- [ ] **Step 5: Commit**

```bash
git add framework/templates/book-template/review/
git commit -m "Add genericized review briefs + plot-audit prompt templates"
```

---

### Task 12: Blank skeletons + copy the chapter-spec template

**Files:**
- Create: `framework/templates/book-template/bible/character-profiles.md`
- Create: `framework/templates/book-template/bible/premise-and-twist.md`
- Create: `framework/templates/book-template/chapters/_template.md`
- Create: `framework/templates/book-template/chapters/_chapter-step-mapping.md`
- Create: `framework/templates/book-template/state/running-recap.md`
- Create: `framework/templates/book-template/state/known-facts.md`
- Create: `framework/templates/book-template/publishing/kdp-listing-template.md`
- Create: `framework/templates/book-template/publishing/cover-brief-template.md`
- Create: `framework/templates/book-template/publishing/epub-metadata-template.yaml`

- [ ] **Step 1: Copy the already-generic chapter-spec template verbatim**

```bash
cp Murder-Mystery-Novel-Fantasy-LitRPG-Story/chapters/_template.md framework/templates/book-template/chapters/_template.md
```

Then open it and replace any Skybound example values with `[…]` placeholders if present (grep check in Step 11).

- [ ] **Step 2: `bible/character-profiles.md` (blank skeleton)**

```markdown
# Character Profiles

> One block per named character. Keep it to what the prose needs — voice, want, secret, tells.

## [Protagonist Name]
- **Role:**
- **Want (external) / Need (internal):**
- **Voice & speech tells:**
- **Physical anchors (1–2 repeatable details):**
- **Secret / blind spot:**
- **Arc across the book:**

## [Character Name]
- **Role:**
- **Want / Need:**
- **Voice & speech tells:**
- **Physical anchors:**
- **Secret / blind spot:**
- **Relationship to protagonist:**

<!-- Duplicate the block above per character. -->
```

- [ ] **Step 3: `bible/premise-and-twist.md` (blank skeleton, renamed from ending-twist)**

```markdown
# Premise & Twist

> The spine the whole book is built to support. Load this for continuity checks; keep it out of the prose.

## One-line premise

[Logline: protagonist + situation + central question.]

## The central question / mystery

[What the reader is trying to figure out, if anything.]

## The Act-2 reveal (locked)

[State the reveal plainly. What is true that the reader doesn't yet know?]

## Mechanics of the twist

[How it works; what must be true earlier for it to land fairly.]

## Planted details (textural, not investigative)

1. [detail] — pays off in [chapter]
2. [detail] — pays off in [chapter]

## Locked decisions

- [decisions that must not drift across drafts]
```

- [ ] **Step 4: `chapters/_chapter-step-mapping.md` (blank skeleton)**

```markdown
# Chapter ↔ Step Mapping

> Map the 12 structural steps to chapters, and distribute planted details. Fill as you outline.

| Step | Beat (from 12-step-formula.md) | Chapters | Plants introduced |
|------|--------------------------------|----------|-------------------|
| 1    |                                |          |                   |
| 2    |                                |          |                   |
| …    |                                |          |                   |
| 12   |                                |          |                   |

**Plant distribution:** [list each planted detail and the chapter it first appears.]
```

- [ ] **Step 5: `state/running-recap.md` (empty)**

```markdown
# Running Recap

> 3–5 sentences per completed chapter: facts + tone only, no commentary. Append after each chapter.
```

- [ ] **Step 6: `state/known-facts.md` (empty)**

```markdown
# Known Facts

> Who knows what, and when. Add a row when a fact becomes known to a character or the reader.

| Fact | Known to | Since chapter | Reader knows? |
|------|----------|---------------|---------------|
|      |          |               |               |

## Spoiler-Wall (twist-level facts — keep below the line)

<!-- facts that must not leak into prose before the reveal -->
```

- [ ] **Step 7: `publishing/kdp-listing-template.md` (blank skeleton)**

```markdown
# KDP Listing Worksheet — {{BOOK_TITLE}}

## Blurb (≤4000 chars, light HTML allowed)

[Back-cover sales copy. Lead with the strongest hook for your genre.]

## Subtitle

[e.g. "A Cozy LitRPG Mystery" — optional but helps discovery.]

## 7 Keywords (long-tail search phrases)

1.
2.
3.
4.
5.
6.
7.

## Categories (BISAC paths)

1.
2.
3.

## Pricing

- List price: [$2.99–$9.99 for the 70% royalty band]
- KDP Select / Kindle Unlimited: [on / off]

## AI-content disclosure

[Answer KDP's AI question honestly: AI-generated vs AI-assisted; list the tools used.]
```

- [ ] **Step 8: `publishing/cover-brief-template.md` (blank skeleton)**

```markdown
# Cover Brief — {{BOOK_TITLE}}

**Spec:** 1600 × 2560 px (1.6:1), RGB, JPEG, ≥72 dpi. Title legible at ~200 px thumbnail.

## Art prompt (image model)

> [Describe the scene: subject, setting, mood, palette, composition. Leave the top third
> uncluttered for the title. End with: "No text, no lettering, no logos."]

## Typography (Canva or similar)

- Title: {{BOOK_TITLE}}
- Author: [pen name]
- Optional tagline / series line:

## Checklist

- [ ] Exactly 1600×2560
- [ ] Title readable at thumbnail size
- [ ] Protagonist/key art matches the bible
```

- [ ] **Step 9: `publishing/epub-metadata-template.yaml` (blank skeleton)**

```yaml
# Pandoc metadata for build_epub.py. Fill in per book.
---
title: My Book Title
subtitle: A Subtitle Here
author: Pen Name
lang: en-US
rights: © 2026 Pen Name. All rights reserved.
description: |
  Back-cover blurb here. Pandoc embeds this as the EPUB description.
...
```

- [ ] **Step 10: Verify the blank skeletons carry no Skybound content**

```bash
grep -rniE "Theron|Sable|Joren|Vannic|Halsa|Skybound|Weyren|airship|drake" framework/templates/book-template/bible/character-profiles.md framework/templates/book-template/bible/premise-and-twist.md framework/templates/book-template/chapters/ framework/templates/book-template/state/ framework/templates/book-template/publishing/
```
Expected: no output.

- [ ] **Step 11: Commit**

```bash
git add framework/templates/book-template/bible/character-profiles.md framework/templates/book-template/bible/premise-and-twist.md framework/templates/book-template/chapters/ framework/templates/book-template/state/ framework/templates/book-template/publishing/
git commit -m "Add blank book-template skeletons (bible, chapters, state, publishing)"
```

---

### Task 13: Write `framework/GUIDE.md`

**Files:**
- Create: `framework/GUIDE.md`

- [ ] **Step 1: Write the full guide**

Create `framework/GUIDE.md` with the 10-section walkthrough below. Fill each section with real prose (no "TBD"); reference the worked example by path.

```markdown
# The Novel-Writing Framework — End-to-End Guide

A reusable, spec-first, AI-assisted process for writing and self-publishing a novel.
It is the generalized spine of *The Skybound Wyrm* (the worked example throughout —
`Murder-Mystery-Novel-Fantasy-LitRPG-Story/`).

## 1. Overview & philosophy

- **Spec-first:** every chapter is drafted from a written spec, never improvised.
- **Shared-reveal discipline:** decide what the reader learns when, and never break it.
- **One chat per chapter:** each chapter is a fresh drafting session (bible + state in context).
- **Draft → review → revise loop:** structure, then prose, then line-level — separate passes.
- **AI-assisted with human gates:** the author approves specs, triage, and every reveal.

## 2. Repo & book layout

How `framework/templates/book-template/` maps to a working book: bible (the rules),
chapters (the specs), manuscript (the prose), state (recap + known-facts), review
(the briefs + audits), publishing (cover/listing/metadata). The tools in `tools/`
operate on any book via `--book <book-dir>`.

## 3. Phase 0 — Start a new book

1. Copy `framework/templates/book-template/` to a new top-level folder, e.g. `My-Book/`.
2. Fill `My-Book/book.config.yaml` (slug, title, author, default_draft).
3. Fill the bible: `12-step-formula.md` (tune the beats), `standing-style.md`,
   `brand-voice.md`, `character-profiles.md`, `premise-and-twist.md`.
4. Map structure in `chapters/_chapter-step-mapping.md`.

## 4. Phase 1 — Drafting loop ("Schreib Kapitel N")

Per chapter: write `chapters/chapter-NN-spec.md` from the template → in a fresh chat,
say "Schreib Kapitel N" → the model reads the spec + bible + state, drafts to
`manuscript/Draft_1/chapter-NN.md` → update `state/running-recap.md` and
`state/known-facts.md`. Repeat to the end.

## 5. Phase 2 — Review & revise

Blind review (`review/review-brief-blind.md`) and informed review
(`review-brief-informed.md`); whole-manuscript plot audit (`review/plot-audit-prompt.md`);
flow audit (`tools/flow_audit.py --book My-Book`). Triage findings into a `_triage.md`,
then run parallel **copy-faithful** revision agents ("copy faithfully, change only what's
listed") into the next `Draft_N`.

## 6. Phase 3 — Copyedit & finalize

`tools/copyedit_audit.py --book My-Book` (mechanical proofread) →
`tools/normalize_us_spelling.py --book My-Book` (deterministic US/UK pass) → reassemble
`_full-manuscript.md`. Decide manuscript-wide consistency centrally (see §9).

## 7. Phase 4 — Release

Author `_front-matter.md` (copyright) and `_back-matter.md` (thank-you + review request);
write the cover brief (`publishing/cover-brief-template.md`) and generate art; fill
`publishing/kdp-listing-template.md` and `epub-metadata.yaml`; build with
`tools/build_epub.py --book My-Book`; validate in Kindle Previewer; upload to KDP and
answer the AI-content disclosure honestly.

## 8. Tools reference

| Tool | Purpose | Book selection |
|------|---------|----------------|
| `flow_audit.py` | Per-chapter prose-flow diagnostic | `--book <dir>` (default: Skybound) |
| `copyedit_audit.py` | Mechanical proofread/copyedit | `--book <dir>` |
| `normalize_us_spelling.py` | Deterministic UK→US spelling | `--book <dir>` |
| `build_epub.py` | Assemble KDP-ready EPUB via Pandoc | `--book <dir>` |
| `make_audiobook.py` | Chapters → audio via Kokoro TTS | `--book <dir>` |

All default to the Skybound book when `--book` is omitted, so existing commands are unchanged.

## 9. Hard-won lessons

- **Verify audit findings adversarially** before acting — AI audits misread ~⅓ of the time.
- **"Copy faithfully, change only what's listed"** — lead every revision agent with this.
- **Conservative metric re-pass** — tell metric-driven agents "no change if it's intentional craft."
- **Decide manuscript-wide consistency centrally** — per-chapter agents each guess differently.
- **Sweep the old value after a fact edit** — grep the whole manuscript + state files.
- **Pandoc gotcha** — leading HTML comments inject a duplicate title `<h1>`; use `--split-level=1`.

## 10. Worked-example index

| Phase | Skybound reference |
|-------|--------------------|
| Bible | `Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/` |
| Specs | `…/chapters/chapter-01-spec.md` … |
| Drafts | `…/manuscript/Draft_1/` … `Draft_6/` |
| Reviews | `…/review/feedback_Draft_*/` |
| Publishing | `…/publishing/` + `publishing/` (repo root) |

---

**Fresh repo?** Copy `framework/` **and** `tools/` together. Paperback and audiobook are
"next steps" beyond this guide (`make_audiobook.py` exists; paperback is not yet automated).
```

- [ ] **Step 2: Verify the guide references real paths**

```bash
ls framework/templates/book-template/bible/12-step-formula.md framework/templates/book-template/review/plot-audit-prompt.md Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible
```
Expected: all paths exist (no "No such file").

- [ ] **Step 3: Commit**

```bash
git add framework/GUIDE.md
git commit -m "Add framework GUIDE.md end-to-end walkthrough"
```

---

### Task 14: Final verification & wrap-up

**Files:** none (verification + memory update only).

- [ ] **Step 1: Whole-template leakage scan**

```bash
grep -rniE "Theron|Sable|Joren|Vannic|Halsa|Weyren|Skybound|airship|drake|calluses|Investigator" framework/templates/book-template/
```
Expected: no output. (The GUIDE.md and the worked-example index intentionally name Skybound — they are outside `templates/book-template/`, so this scan excludes them.)

- [ ] **Step 2: Full test suite green**

Run: `python -m unittest tests.test_bookconfig -v`
Expected: PASS (all tests).

- [ ] **Step 3: Backward-compat regression (no `--book`)**

```bash
python tools/flow_audit.py --draft Draft_6 --no-report
python tools/copyedit_audit.py --draft Draft_6 --no-report
python tools/normalize_us_spelling.py --src Draft_6 --dry-run --audit
```
Expected: all run clean; normalizer reports 0 residual UK forms.

- [ ] **Step 4: `--book` works on a freshly-copied dummy**

```bash
cp -r framework/templates/book-template /tmp/dummy-book
mkdir -p /tmp/dummy-book/manuscript/Draft_1
printf '# Chapter 1 — Test\n\nA short test sentence. Another one here.\n' > /tmp/dummy-book/manuscript/Draft_1/chapter-01.md
python tools/flow_audit.py --book /tmp/dummy-book --chapter 01 --draft Draft_1 --no-report
```
Expected: prints chapter-01 flow stats for the dummy book with no path error. (On Windows, substitute a temp path like `$env:TEMP\dummy-book` and use the Bash tool or `Copy-Item -Recurse`.)

- [ ] **Step 5: Confirm Skybound content is unchanged**

```bash
git log --oneline -1
git status --porcelain Murder-Mystery-Novel-Fantasy-LitRPG-Story/manuscript Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible Murder-Mystery-Novel-Fantasy-LitRPG-Story/chapters
```
Expected: empty porcelain output (only additive `book.config.yaml` + tool edits + new `framework/` tree exist across the branch).

- [ ] **Step 6: Update memory**

Update `C:\Users\David\.claude\projects\D--Projects-Books\memory\project_skybound_wyrm.md` to note the framework guide is built (`framework/GUIDE.md` + `framework/templates/book-template/`, tools now `--book`-aware), and add the one-line pointer to `MEMORY.md` if not already covered. (No new memory file needed — fold into the existing project memory.)

- [ ] **Step 7: Final commit**

```bash
git add -A
git commit -m "Verify framework extraction; mark guide complete"
```

---

## Self-Review notes (author's check against the spec)

- **Spec coverage:** Architecture tree → Tasks 8–13; tool genericization + `bookconfig.py` + resolution order → Tasks 1–6; Skybound `book.config.yaml` → Task 7; GUIDE 10-section outline → Task 13; success criteria (no leakage, backward compat, `--book` works, Skybound untouched) → Task 14. Out-of-scope items (no `new_book.py`, no Skybound content changes, no separate-repo packaging) are respected.
- **Open considerations resolved:** (a) `book.config.yaml` field set kept minimal (slug/title/author/story_dir/default_draft); (b) `bookconfig.py` centralizes the shared `use_utf8_stdout()` helper (the tools may adopt it opportunistically; not forced here); (c) spoiler-guardrail demoted to an optional labeled pattern in the template `CLAUDE.md` (Task 10).
- **Type consistency:** `Book` fields (`slug`, `title`, `author`, `story_dir`, `default_draft`) and methods (`manuscript`, `feedback`, `publishing`) are used identically across Tasks 2–6; `add_book_arg`/`resolve_book` signatures match between definition (Task 1) and all callers.
```
