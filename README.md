# Books Workspace

Multi-book writing workspace. Chapter-by-chapter drafting with Claude.

## Books

| Folder | Book | Status |
|---|---|---|
| [`cozy-fantasy-romance/`](cozy-fantasy-romance/) | *Kaffee, Magie und ein Drache namens Felix* — Cozy Fantasy Romance | Active (Draft 1) |
| [`Murder-Mystery-Novel-Fantasy-LitRPG-Story/`](Murder-Mystery-Novel-Fantasy-LitRPG-Story/) | *The Skybound Wyrm* — Cozy LitRPG Murder Mystery | Published (Amazon KDP, June 2026) |

## Structure (per book)

Each book folder is self-contained:

```
<book>/
├── CLAUDE.md           workspace contract (read by Claude automatically)
├── book.config.yaml    slug, title, author, default_draft
├── bible/              story bible (characters, structure, style, voice)
├── chapters/           per-chapter specs + beat/step mapping
├── state/              running recap + known-facts ledger
├── manuscript/         Draft_1/ · Draft_N/ (post-review)
├── publishing/         cover, epub metadata, KDP listing
└── review/             reviewer briefs
```

## Writing the next chapter

Open a new Claude Code chat inside the **book folder** and say: **"Schreib Kapitel N."**

Claude reads `CLAUDE.md` automatically, loads the chapter spec, running recap, and known-facts ledger, then produces the draft and proposes a recap update.

## Commands

Reusable slash commands automate the recurring work (drafting and reviewing). The book is the first argument:

| Command | What it does |
|---|---|
| `/write-chapter <book> <N>` | Draft a single chapter spec-first; propose recap + known-facts. |
| `/write-chapters <book> <from> <to>` | Orchestrate a run of chapters — one subagent per chapter, sequential. |
| `/review-chapter <book> <N> [draft]` | Blind + informed + Lektorat review in parallel → one feedback file. |

See [`framework/COMMANDS.md`](framework/COMMANDS.md) for the full suite, the backing subagents, and the roadmap of further commands.

## Starting a new book

Copy `framework/templates/book-template/` into a new folder and follow [`framework/GUIDE.md`](framework/GUIDE.md).

## Tooling

Scripts in `tools/` accept `--book <folder>` (default: The Skybound Wyrm). Example:

```
python tools/flow_audit.py --book cozy-fantasy-romance
```
