# Books Workspace — Claude Instructions

This is a **multi-book writing workspace**. Each book lives in its own folder with a self-contained `CLAUDE.md` — that file is the authoritative contract for drafting that book.

**When working on a specific book: read that book's `CLAUDE.md` first.** The instructions here are workspace-wide only — no book-specific rules, no drafting workflows.

---

## Books

| Folder | Book | Status |
|---|---|---|
| `cozy-fantasy-romance/` | *Kaffee, Magie und ein Drache namens Felix* — Cozy Fantasy Romance | **Aktiv (Draft_1)** |
| `Murder-Mystery-Novel-Fantasy-LitRPG-Story/` | *The Skybound Wyrm* — Cozy LitRPG Murder Mystery | **Veröffentlicht** (Amazon KDP, 2026-06-04) |

Each book folder has its own `CLAUDE.md` with the full drafting workflow, story guardrails, and book targets.

---

## Starting a New Book

1. Copy `framework/templates/book-template/` into a new folder
2. Fill in `book.config.yaml` (slug, title, author)
3. Localise `CLAUDE.md` — replace `{{BOOK_TITLE}}`, `{{GENRE}}`, and the guardrail block
4. Fill the bible files; follow [`framework/GUIDE.md`](framework/GUIDE.md) for the end-to-end process

---

## General Craft References

Genre-agnostic craft resources live in `general-research/`:
- [`12-step-formula.md`](general-research/12-step-formula.md) — three-act / 12-step structure
- [`schreibformeln-strukturmodelle.md`](general-research/schreibformeln-strukturmodelle.md) — writing formulas & structure models

---

## Tooling

Scripts in `tools/` accept `--book <folder>` to select a book:

```
python tools/flow_audit.py --book cozy-fantasy-romance
python tools/build_epub.py --book cozy-fantasy-romance
```

**Default (when `--book` is omitted):** The Skybound Wyrm. Always pass `--book` explicitly when working on other books.

---

## Workspace-Wide Principles

These apply regardless of which book is being drafted:

- Do not summarize the story bible into chapter prose
- Do not ask Claude to "re-read over the files" — they are already in context
- Do not use outline-first workflows — follow the chapter spec directly
- Do not use Capitalised Worldbuilding Nouns unless the book's bible uses them that way
