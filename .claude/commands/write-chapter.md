---
description: Draft a single chapter spec-first (Pattern A) — reads the book's bible+state, writes Draft_1/chapter-NN.md, proposes recap+known-facts for approval
argument-hint: <book> <N>
---

## Task: write chapter $2 of the book in `$1` (single-chapter, spec-first)

You are drafting **one** chapter interactively. `$1` is the book folder (e.g. `cozy-fantasy-romance`); `$2` is the chapter number `N`. Use the zero-padded form `chapter-NN` throughout (chapter 2 → `chapter-02`).

### Step 0 — Resolve the book (genre-neutral)
Read `$1/CLAUDE.md`. It is the authoritative index of this book's bible, state, spec, and manuscript paths. Do **not** assume bible filenames — follow the links in that file (the books differ: e.g. `romance-beat-sheet.md` vs `12-step-formula.md`, `premise-and-promise.md` vs `premise-and-twist.md`). Everything below uses paths relative to `$1/`.

### Step 1 — Get the chapter spec
- If `chapters/chapter-NN-spec.md` exists, it is **authoritative** — use it.
- If it does **not** exist, generate it from `chapters/_template.md` + `chapters/_chapter-step-mapping.md`, show it to the user, and **wait for approval before drafting** (hard gate). Do not draft against an unapproved spec.

### Step 2 — Load state + bible (read, do not summarize into prose)
- Read the **tail entry** of `state/running-recap.md` (continuity context) and all of `state/known-facts.md` (verify no knowledge leaks).
- Apply every rule from `bible/standing-style.md`.
- Apply `bible/brand-voice.md` — prose mechanics / sentence rhythm, tonal register, and the anti-slop constraints — while drafting.

### Step 3 — Draft
Write the chapter to `manuscript/Draft_1/chapter-NN.md`. Hit the spec's word-count target. No `[placeholder]` syntax — make a reasoned decision consistent with the bible. No meta/draft labels in the prose ("Ch 7", "Act 2", spec-category names). Keep any character the bible marks as opaque opaque (no unearned interiority).

### Step 4 — Self-check before proposing state
Run the brand-voice Quick-Reference checklist against the draft. **Additionally**, for each tic family the brand-voice doc names, run an independent grep over the chapter for *all* surface forms and count them — do not trust impression (a partial count leaves residuals that resurface as new findings next review round). Fix violations now.

### Step 5 — Propose state (do NOT auto-write)
Propose, for the user to accept/edit:
- a 3–5 sentence entry for `state/running-recap.md` (facts + tone only);
- any new rows for the `state/known-facts.md` table (who knows what, and in which chapter).

State files are written only after the user approves — do not edit them yourself in single-chapter mode. (The `/write-chapters` orchestrator is the one that auto-merges state; this single-chapter command keeps the author in the loop.)
