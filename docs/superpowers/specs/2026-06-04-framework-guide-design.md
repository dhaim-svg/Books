# Design: Reusable Novel-Writing Framework Guide

**Date:** 2026-06-04
**Status:** Approved (design) — pending spec review → implementation plan

## Context

*The Skybound Wyrm* was written, reviewed, copyedited, and published to Amazon KDP using a
spec-first, AI-assisted workflow that grew organically across six drafts: a story bible, per-chapter
specs, a one-chat-per-chapter drafting loop, multi-pass reviews (blind/informed, plot audit, flow
audit), a copyedit + US-spelling normalization pass, and a release pipeline (front/back matter, cover,
KDP listing, Pandoc EPUB build). All of that knowledge currently lives entangled with one specific
book and with hardcoded paths in the tools.

**Goal:** extract the reusable spine into a `framework/` folder at the repo root so a second book can
start from a clean, genre-neutral template kit instead of from this story — without disturbing the
published Skybound book.

## Decisions (locked with user)

1. **Form:** copy-a-template-folder kit — `framework/` with a GUIDE + book-agnostic templates + generic
   tools. (Not a doc-only guide; not an automated scaffold script.)
2. **Genre scope:** **genre-neutral skeletons.** Process, structure, and tools carry over; cozy/LitRPG-
   specific style becomes generic prompts. Skybound is the worked example, pointed to — not embedded.
3. **Tools:** **genericize via a per-book config**, with the Skybound path as the default so nothing
   breaks.

## Architecture

```
framework/
  GUIDE.md                         # master walkthrough (setup → draft → review → finalize → release)
  templates/
    book-template/                 # COPY this whole folder to start a new book
      book.config.yaml             # per-book config consumed by the tools
      CLAUDE.md                    # genericized workspace/workflow instructions
      bible/
        12-step-formula.md         # reusable 3-act / 12-step structure (genre-neutral)
        standing-style.md          # POV/tense/prose-discipline skeleton
        brand-voice.md             # sentence-rhythm / dialogue-economy / anti-slop skeleton
        character-profiles.md      # BLANK template (headers + prompts)
        premise-and-twist.md       # BLANK template (renamed from ending-twist, genre-neutral)
      chapters/
        _template.md               # chapter-spec template
        _chapter-step-mapping.md   # BLANK template
      state/
        running-recap.md           # empty
        known-facts.md             # empty
      review/
        review-brief-blind.md      # genericized prompt
        review-brief-informed.md   # genericized prompt
        plot-audit-prompt.md       # genericized plot-audit prompt
      publishing/
        kdp-listing-template.md
        cover-brief-template.md
        epub-metadata-template.yaml
      manuscript/Draft_1/.gitkeep
```

The existing `Murder-Mystery-Novel-Fantasy-LitRPG-Story/` book is **left untouched** and serves as the
worked example. Generic tools stay shared in the repo's `tools/`.

### Genericization buckets (explicit source → template mapping)

**Reusable defaults** — copy, strip Skybound-specific names/plot, keep the craft:
- `bible/12-step-formula.md` → keep step definitions, act structure, chapters-per-step guidance; remove
  Skybound plot content.
- `bible/standing-style.md` → keep POV/tense/prose rules; remove Sable/Theron/plant specifics.
- `bible/brand-voice.md` → keep §4 prose mechanics, §5 register, §6 anti-slop, §8 checklist; neutralize
  examples.
- `chapters/_template.md` → copy as-is (already generic).
- `review/review-brief-blind.md`, `review-brief-informed.md` → neutralize book title/character names →
  placeholders.
- `review/plot-audit-prompt.md` → genericized from the plot-audit workflow (the 7-pass recipe; treat
  `*[Investigator —]*`-style system lines as an intentional, configurable convention).
- `CLAUDE.md` → genericized workflow (project name, paths via `{{placeholders}}`; keep the "Schreib
  Kapitel N" loop, spoiler-guardrail pattern as an optional section, the bible/state read-before-write
  discipline).

**Blank skeletons** — section headers + fill-in prompts only:
- `bible/character-profiles.md`, `bible/premise-and-twist.md`, `chapters/_chapter-step-mapping.md`,
  `state/running-recap.md`, `state/known-facts.md`, all three `publishing/*` templates.

**Worked example** — unchanged: the whole Skybound folder, referenced by the GUIDE per phase.

### Tool genericization (config-driven, backward-compatible)

- New shared module `tools/bookconfig.py` with a `resolve_book(args)` helper.
- Each of the five tools (`flow_audit.py`, `copyedit_audit.py`, `normalize_us_spelling.py`,
  `build_epub.py`, `make_audiobook.py`) gains a `--book <dir>` flag.
- **Resolution order:** `--book <dir>` → a discovered `book.config.yaml` → **default = the current
  Skybound story dir** (preserves every existing command and committed behavior).
- `book.config.yaml` schema (minimal):
  ```yaml
  slug: skybound-wyrm
  title: The Skybound Wyrm
  author: Theo Weyren
  story_dir: Murder-Mystery-Novel-Fantasy-LitRPG-Story   # relative to repo root
  default_draft: Draft_6
  ```
- Tools read `story_dir` (book root) and resolve `manuscript/Draft_N`, `review/feedback_Draft_N`, etc.
  relative to it — exactly as today, just no longer hardcoded. `build_epub.py` reads `title`/`author`/
  `default_draft` from the config; the per-book `publishing/epub-metadata.yaml` still supplies the
  blurb/subtitle for Pandoc.
- A `book.config.yaml` is added to the Skybound folder so it round-trips through the new resolver.

### `GUIDE.md` outline

1. Overview & philosophy — spec-first, shared-reveal/contract discipline, one-chat-per-chapter, the
   draft→review→revise loop, AI-assisted with human gates.
2. Repo & book layout; how the template kit maps to a working book.
3. **Phase 0 — Start a new book:** copy `book-template/`, fill `book.config.yaml`, fill the bible.
4. **Phase 1 — Drafting loop:** chapter specs, "Schreib Kapitel N", recap + known-facts updates.
5. **Phase 2 — Review & revise:** blind/informed reviews, plot audit, flow audit, triage, parallel
   copy-faithful revision agents → next draft.
6. **Phase 3 — Copyedit & finalize:** `copyedit_audit`, `normalize_us_spelling`, the central-consistency
   rule, reassemble full manuscript.
7. **Phase 4 — Release:** front/back matter, cover brief + AI image prompt, KDP listing worksheet,
   `build_epub`, KDP upload + AI-content disclosure.
8. **Tools reference:** each tool's purpose + `--book` usage.
9. **Hard-won lessons:** verify audit findings adversarially; "copy faithfully, change only what's
   listed"; conservative metric re-pass; decide manuscript-wide consistency centrally; sweep old values
   after fact edits; the Pandoc title-in-body / `--split-level` gotcha.
10. Worked-example index: per-phase links into the Skybound book.

## Out of scope (YAGNI)

- No `new_book.py` scaffold script (copy-folder model chosen; revisit later if desired).
- No changes to any Skybound manuscript/bible content; tools only gain an additive `--book` flag and a
  default-preserving resolver.
- No separate-repo packaging; the GUIDE notes "copy `tools/` + `framework/` too" for a fresh repo.
- Paperback/audiobook get a brief "next steps" note, not full chapters.

## Success criteria / verification

- `framework/templates/book-template/` exists with every file above; no `[BRACKETED]`/Skybound leakage
  in the genericized files (grep for character names / book title).
- Backward compatibility: every tool run **without** `--book` behaves exactly as before (default Skybound
  path); `flow_audit.py` / `copyedit_audit.py` produce identical reports for Draft_6.
- `--book` works: pointing a tool at a freshly-copied dummy book (with a filled `book.config.yaml` and a
  stub chapter) runs without path errors.
- `build_epub.py --book <skybound>` still produces a clean EPUB (regression).
- Skybound files unchanged (git shows only additive `--book`/config edits to tools, plus the new
  `framework/` tree and a Skybound `book.config.yaml`).

## Open considerations (resolve during planning)

- Exact `book.config.yaml` field set vs. what each tool truly needs (keep minimal).
- Whether `bookconfig.py` should also centralize the Windows stdout-UTF-8 wrapper the tools share.
- How much of the spoiler-guardrail section in `CLAUDE.md` is generic (keep as an optional, clearly-
  labeled pattern rather than mandatory).
