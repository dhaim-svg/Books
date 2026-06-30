---
description: Review one chapter from three perspectives in parallel (blind reader + informed continuity + German Lektorat) and assemble one feedback file
argument-hint: <book> <N> [draft]
---

## Task: review chapter $2 of the book in `$1` (draft: `$3`, default = current)

`$1` = book folder; `$2` = chapter number N; `$3` = optional draft folder name (e.g. `Draft_2`). Use the zero-padded `chapter-NN` form.

### Step 0 — Resolve
Read `$1/CLAUDE.md` for the bible/state/spec paths and the genre string. Determine the draft:
- if `$3` is given, use it;
- else read `book.config.yaml` `default_draft`, or fall back to the highest existing `manuscript/Draft_N/` that contains chapter N.

Locate the chapter file `$1/manuscript/<draft>/chapter-NN.md` and confirm it exists.

### Step 1 — Dispatch three reviewers IN PARALLEL (single message)
They are independent roles with no shared output, so fire all three at once (each writes its findings in the book's language):
- **`book-blind-reviewer`** — give it **only** the chapter file path and the genre string. Tell it explicitly NOT to open the bible/spec/state.
- **`book-informed-reviewer`** — give it the chapter file, its `chapters/chapter-NN-spec.md`, and the bible + state files resolved from `$1/CLAUDE.md`.
- **`book-lektor`** — give it the chapter file plus `bible/brand-voice.md` and `bible/standing-style.md`.

Each returns its findings as Markdown (none of them writes files).

### Step 2 — Assemble the deliverable (you own the write)
Write `$1/review/feedback_<draft>/chapter-NN.md` **yourself** from the three returned bodies — do not have the agents write it. Structure:

```
# Chapter NN — Review (<draft>)

## Blind Review
<blind body>

## Informed Review
<informed body>

## Lektorat (Sprachlich-stilistisch)
<lektor body>
```

After writing, list the `feedback_<draft>` directory and confirm the exact filename landed (correct zero-padding, correct folder).

### Step 3 — Light verify + summarize
Spot-check that quoted lines in the findings actually exist in the chapter (the Lektor already counted tics by grep). Present a short triage-style summary to the user — must-fix items first, then style/polish. Do **not** edit the chapter; this command only reviews.
