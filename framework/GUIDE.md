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

The `/write-chapter <book> <N>` command automates one chapter; `/write-chapters <book> <from> <to>`
orchestrates a whole run (one subagent per chapter, sequential). See [`COMMANDS.md`](COMMANDS.md).

## 5. Phase 2 — Review & revise

Blind review (`review/review-brief-blind.md`) and informed review
(`review-brief-informed.md`); whole-manuscript plot audit (`review/plot-audit-prompt.md`);
flow audit (`tools/flow_audit.py --book My-Book`). Triage findings into a `_triage.md`,
then run parallel **copy-faithful** revision agents ("copy faithfully, change only what's
listed") into the next `Draft_N`.

The `/review-chapter <book> <N> [draft]` command runs the blind + informed + **Lektorat**
(German line-edit) reviews together in parallel and assembles one feedback file. See
[`COMMANDS.md`](COMMANDS.md).

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
| Publishing | `…/publishing/` |

---

**Fresh repo?** Copy `framework/` **and** `tools/` together. Paperback and audiobook are
"next steps" beyond this guide (`make_audiobook.py` exists; paperback is not yet automated).
