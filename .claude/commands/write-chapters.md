---
description: Orchestrate a run of chapters (Pattern B) — one book-chapter-writer subagent per chapter, sequential, state injected and merged between dispatches
argument-hint: <book> <from> <to>
---

## Task: orchestrate chapters $2 through $3 of the book in `$1`

You are the **orchestrator**. `$1` = book folder; `$2` = first chapter; `$3` = last chapter. You dispatch **one `book-chapter-writer` subagent per chapter, sequentially**, because each chapter depends on the previous chapter's updated state. Do **not** wrap this in a Workflow — you must merge each chapter's state proposals into the state files (via Edit) between dispatches, and that human-readable merge belongs in the orchestrator loop. Use the zero-padded `chapter-NN` form.

### Preflight
1. Read `$1/CLAUDE.md` to resolve the bible / state / spec / manuscript paths (genre-neutral — follow its links, don't assume filenames). Note the structure doc (12-step / beat sheet) and `chapters/_chapter-step-mapping.md`.
2. Confirm `state/running-recap.md` is current **through chapter ($2 − 1)** (check the tail entry) and `state/known-facts.md` looks consistent. If state is **not** current up to the start point, **stop and tell the user** — do not guess or backfill silently.
3. Create one task per chapter $2..$3 to track progress.

### Loop — for N from $2 to $3, in order
1. Read the **current** `state/running-recap.md` tail + the full `state/known-facts.md` table (they change every iteration).
2. **Dispatch one `book-chapter-writer` subagent** (Opus). Inject directly into its prompt — the subagent must NOT read state files itself:
   - the resolved book paths (bible files, premise doc, structure doc, `chapters/_template.md`, `_chapter-step-mapping.md`, manuscript dir) named explicitly;
   - chapter number N and the relevant step/beat note from the mapping;
   - the **recap tail** (verbatim);
   - the **full known-facts table** (verbatim) — but **without** any Spoiler-Wall rows;
   - the **Spoiler-Wall** separately, clearly labelled *FOR CALIBRATION ONLY — NOTHING ON THE PAGE* (only if this book has one).
3. The subagent writes `chapters/chapter-NN-spec.md` + `manuscript/Draft_1/chapter-NN.md` and returns `[recap-proposal]` / `[known-facts-proposal]` blocks + a status line (`DONE` / `DONE_WITH_CONCERNS` / `BLOCKED`).
4. **You** (the orchestrator) merge the state updates into the files via Edit: append the recap entry to `state/running-recap.md`; add only the *new* rows to `state/known-facts.md`. You own the state writes — do not delegate them.
5. If the subagent returned `BLOCKED`, or a concern that affects continuity, stop and surface it before continuing.
6. Mark the task done; continue with N+1.

### After the run
Spot-check a sample (e.g. the first chapter, a structural hinge, the last chapter) for voice drift, placeholder leaks, and that planted details landed. Report the run summary.

### Autonomy & model
This is a delegated multi-chapter run: do not pause for per-chapter spec approval between chapters. All chapter-writer subagents run on **Opus** (debut-prose quality).
