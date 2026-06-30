# Design: Reusable Book-Writing Commands + Subagents

**Date:** 2026-06-30
**Status:** Approved (design) — pending spec review → implementation plan

## Context

Across both books in this workspace (*The Skybound Wyrm*, published; *Kaffee, Magie und ein
Drache namens Felix*, in Draft_2) the same handful of tasks recur every draft and every chapter:
write a chapter, write a whole run of chapters, review a chapter from several perspectives. Until
now the prompts for these were hand-rewritten each session (see the accreted drafts in
`promptprep.md`). The validated procedures already live in memory — they just have no reusable
home.

**Goal:** turn the recurring book work into reusable, genre-neutral **slash commands** backed by
**subagents**, so future chapters and drafts (this book and the next) start from a stable contract
instead of a re-improvised prompt. The hard-won lessons from six Skybound drafts are baked into the
command/agent definitions rather than re-remembered each time.

## Decisions (locked with user)

1. **Form:** **Commands + Subagents.** Slash commands are the user-typed entry points; subagents are
   the reusable workers (reviewer roles, chapter-writer). *(Not skills-only; not a hybrid skill
   layer.)*
2. **Scope:** build the **Kern-Set now** (the three must-have commands + four agents). Everything
   else (the full revise cycle, plot-audit, tool/publishing wrappers) is **documented as a roadmap**
   in a suitable doc, not built yet.
3. **Lektorat arm:** **sprachlich-stilistisch** (German line editor) — grammar, expression, word
   repetition, sentence rhythm / "Holprigkeit", filler words, style tics. Mechanical proofreading
   stays with the existing tools.
4. **Defaults (taken from the design Q&A):** English command names; book passed as the **first
   argument**; `/review-chapter` writes **one feedback file with three sections**; the Lektor is a
   read-only agent with **no external brief template** in the Kern (that goes on the roadmap).

## Leitprinzip — genre-neutral via the book's own `CLAUDE.md`

The two books deliberately use **different bible filenames** (`premise-and-twist.md` +
`12-step-formula.md` for the mystery; `premise-and-promise.md` + `romance-beat-sheet.md` for the
romance). Commands and agents therefore **never hardcode bible filenames**. They read
`<book>/CLAUDE.md` first — that file already indexes the bible, state, spec, and manuscript paths —
and follow those links. This keeps the whole suite genre-neutral and valid for any future book that
follows the framework template. The book is selected by argument, mirroring the existing `--book`
convention of the `tools/`.

## Architecture

```
D:\Projects\Books\
  .claude\
    commands\
      write-chapter.md       # Pattern A — single chapter, spec-first, propose state
      write-chapters.md      # Pattern B — multi-chapter orchestrator (one subagent per chapter)
      review-chapter.md      # 3-arm review (blind + informed + Lektorat), parallel
    agents\
      book-chapter-writer.md     # the Pattern-B per-chapter drafting worker
      book-blind-reviewer.md     # reader perspective, NO bible
      book-informed-reviewer.md  # continuity, FULL bible
      book-lektor.md             # German stylistic line editor (NEW)
  framework\
    COMMANDS.md              # suite reference + hard-won-lessons matrix + deferred roadmap
```

Both existing books are untouched; they are the worked examples the commands operate on. The suite
lives at workspace level (checked into the Books repo) so it is shared across both books and every
future one.

### Command: `/write-chapter` — single chapter (Pattern A)

- **File:** `.claude/commands/write-chapter.md`
- **Args:** `$1` = book folder, `$2` = chapter number `N`. Argument-hint: `<book> <N>`.
- **Procedure (in the command body):**
  1. Read `<book>/CLAUDE.md` to resolve the bible / state / spec / manuscript paths (genre-neutral
     index).
  2. Locate `chapters/chapter-NN-spec.md`. **If it does not exist:** generate it from
     `chapters/_template.md` + `chapters/_chapter-step-mapping.md`, show it to the user, and **wait
     for approval** before drafting (hard gate). If it exists, use it as authoritative.
  3. Read the **tail entry** of `state/running-recap.md` and all of `state/known-facts.md`.
  4. Apply `bible/standing-style.md` + `bible/brand-voice.md` (rhythm/tone/anti-slop) — do **not**
     summarize the bible into prose.
  5. Write the draft to `manuscript/Draft_1/chapter-NN.md`.
  6. Run the brand-voice quick-reference checklist against the draft **and** an independent grep of
     the project's tic families; fix violations **before** proposing state.
  7. **Propose** (do not auto-write) a 3–5 sentence `running-recap` entry and any new
     `known-facts` rows; the user accepts/edits, then the chapter is locked.
- **Why propose-don't-write here:** single-chapter mode is interactive; the cozy workflow explicitly
  keeps state edits behind author approval. (Contrast the orchestrator below, which auto-applies.)

### Command: `/write-chapters` — multi-chapter orchestrator (Pattern B)

- **File:** `.claude/commands/write-chapters.md`
- **Args:** `$1` = book, `$2` = from, `$3` = to. Argument-hint: `<book> <from> <to>`.
- **Execution model:** **main-loop orchestration** (the command instructs the model to act as
  orchestrator and dispatch subagents via the Agent tool), **not** a Workflow script. Rationale: the
  orchestrator must merge each chapter's returned recap/known-facts **into existing state files via
  Edit** between dispatches, and chapters are strictly sequential on that state. The validated
  Pattern B is exactly this loop; a rigid JS Workflow handles the human-readable state-merge less
  robustly. *(A Workflow variant is possible later for the parallel review fan-out — see roadmap.)*
- **Procedure:**
  1. **Preflight:** read `<book>/CLAUDE.md`; confirm `state/` is current through chapter `from-1`
     (read the recap tail). If it is not, **stop and tell the user** — do not guess.
  2. **Loop** N from `from` to `to`, sequentially:
     a. Read the current `state/running-recap.md` tail + `state/known-facts.md`.
     b. Dispatch **one `book-chapter-writer` subagent** (Opus) with the state **injected directly**
        into the prompt: recap tail + full known-facts table + spoiler-wall (calibration-only) +
        the resolved book paths + chapter N + the relevant step/beat note from the mapping. The
        subagent **does not read state files itself**.
     c. The subagent writes `chapters/chapter-NN-spec.md` + `manuscript/Draft_1/chapter-NN.md` and
        returns `[recap-proposal]` / `[known-facts-proposal]` blocks plus a status
        (`DONE` / `DONE_WITH_CONCERNS` / `BLOCKED`).
     d. The **orchestrator** applies the state updates itself (append recap entry; add new
        known-facts rows) via Edit — the orchestrator owns the state writes.
     e. Track progress (one task per chapter).
  3. After the run, **spot-check** a sample of chapters (e.g. first, a hinge, last).
- **Autonomy:** no per-chapter spec approval during a delegated run (validated autonomous mode);
  the user delegated the whole range up front.

### Command: `/review-chapter` — 3-arm review

- **File:** `.claude/commands/review-chapter.md`
- **Args:** `$1` = book, `$2` = N, `$3` = draft (optional; default = the book's current draft).
  Argument-hint: `<book> <N> [draft]`.
- **Procedure:**
  1. Resolve the chapter file `manuscript/<draft>/chapter-NN.md` and the genre string (from
     `<book>/CLAUDE.md` / `book.config.yaml`).
  2. **Dispatch three subagents in parallel** (single message; each returns its findings — distinct
     roles, no file conflicts):
     - `book-blind-reviewer` — given **only** the chapter text + genre; instructed not to open the
       bible/spec/state.
     - `book-informed-reviewer` — given the chapter + its spec + the bible + state files.
     - `book-lektor` — given the chapter + the book's `brand-voice.md` / `standing-style.md`.
  3. The **main loop** assembles the deliverable `review/feedback_<draft>/chapter-NN.md` from the
     three returned bodies (it owns the write; it verifies the exact path/name afterward), with
     sections `## Blind Review`, `## Informed Review`, `## Lektorat (Sprachlich-stilistisch)`.
  4. **Light verify:** confirm each reviewer's quoted lines actually exist in the chapter; the
     Lektor's tic counts already come from a full grep (below). Present a short summary.
- **Read-only:** all three arms **report**; none edit. Revising is the deferred `/review-cycle`.

### Subagent: `book-chapter-writer`

- **Frontmatter:** `name`, `description`, `tools: Read, Write, Edit, Glob, Grep`, `model: opus`.
- **System prompt (genericized from the validated `promptprep.md` sub-agent template):**
  drafts ONE chapter = spec + draft + state proposals. Reads the book constants in order
  (standing-style → brand-voice §rhythm/tone/anti-slop/checklist → character-profiles → premise doc
  → structure/step doc → chapter-step-mapping → `_template`). **Hard rules:** use the injected state,
  do **not** read state files; spoiler-wall is calibration-only (nothing on the page); **no
  `[placeholder]` syntax** — make a reasoned decision or return `DONE_WITH_CONCERNS`; keep opaque
  characters opaque (no unearned interiority); run the brand-voice checklist before delivering.
  **Return** the spec + draft paths and the `[recap-proposal]` / `[known-facts-proposal]` blocks +
  status line.

### Subagent: `book-blind-reviewer`

- **Frontmatter:** `tools: Read, Grep`, `model: opus`.
- **System prompt (genericized from `review-brief-blind.md`):** developmental editor who has NOT
  read the rest of the book; reads the chapter exactly as a first-time reader. Genre injected. Five
  reader-perspective questions (first-page test, planted-detail naturalness, POV character landing,
  tone calibration, one line to cut / one to keep). No plot summary; flag immersion breaks.

### Subagent: `book-informed-reviewer`

- **Frontmatter:** `tools: Read, Grep`, `model: opus`.
- **System prompt (genericized from `review-brief-informed.md`):** continuity editor with full bible
  access; technical verification, not style. Five checks (plant discipline vs the chapter spec,
  standing-style compliance, spoiler/foreshadow discipline, known-facts consistency, word count vs
  target). **Verify each cited line exists**; report Pass/Fail first, then the note, with
  `chapter:line` anchors. Treats in-world system lines (`*[System — …]*`) as an intentional
  convention, not an error.

### Subagent: `book-lektor` (NEW)

- **Frontmatter:** `tools: Read, Grep`, `model: opus`.
- **Lens:** German stylistic line editor. Focus: grammar, expression/word choice, **word
  repetition, sentence rhythm / "Holprigkeit"** (the late-caught problem from Book 1), filler words,
  project style tics. **Read-only — flags, never rewrites.**
- **Procedure (bakes in the tic-audit lessons):**
  1. Read the chapter and the book's `brand-voice.md` to learn the project's tic families and rhythm
     rules (e.g. Negations-Tic, Komparativ-„als", Gedankenstrich frequency, „ohne … zu", als +
     Konjunktiv).
  2. For **each** tic family, run an **independent grep over all surface forms** of the family and
     count — do not rely on impression or a partial enumeration (full-grep-before-tic-audit lesson).
  3. Flag rhythm/Holprigkeit: Vorfeld-variation, subject-opener repetition, sentence-length
     monotony, semicolon-rhythm sameness.
  4. Flag filler words and local redundancy; flag grammar/Ausdruck slips.
  5. **Verify every quote exists** in the chapter; report each finding with a `chapter:line` anchor,
     the quote, a severity, and a **suggested direction** (not a finished rewrite).

### `framework/COMMANDS.md` — suite reference + roadmap

A single doc that:
- documents the active commands (3) and agents (4) with one-line purposes and usage;
- states the genre-neutral principle (reads `<book>/CLAUDE.md`) and the book-as-first-arg convention;
- carries the **hard-won-lessons enforcement matrix** (below);
- lists the **deferred roadmap** so we can pick it up seamlessly, each with the validating memory:
  - `/review-cycle` — Review → **Triage gate** → copy-faithful Revise → Combine (the 4-phase loop).
  - `/plot-audit` — 7-pass read-only whole-manuscript structural/continuity audit.
  - tool-wrapper commands — `/flow-audit`, `/copyedit`, `/normalize-spelling` (always pass `--draft`
    explicitly — the tool defaults are stale for non-Skybound books).
  - publishing — `/build-epub` and the release steps.
  - agents — `book-copyfaithful-reviser` (lead with "copy faithfully, change only what's listed";
    `changed` flag + per-item hard-preserve list) and `book-finding-verifier` (adversarial
    per-finding verification; default to refuting unlocatable quotes).
  - an **external Lektorat brief** template (sibling to `review-brief-blind/informed.md`) for
    hand-off to an outside AI/human.

`framework/COMMANDS.md` is referenced from `README.md` and from `framework/GUIDE.md` §5.

### Hard-won-lessons → enforcement (traceability)

| Lesson (memory) | Enforced in (Kern) |
|---|---|
| Inject state into subagents; don't let them self-read state | `/write-chapters` + `book-chapter-writer` |
| No `[placeholder]` — decide or flag | `book-chapter-writer` |
| Spoiler-wall = calibration only | `book-chapter-writer` |
| Propose state, don't auto-write (single chapter) | `/write-chapter` |
| Parallel agents with distinct outputs | `/review-chapter` |
| Workflow/deliverable path owned by the main loop | `/review-chapter` + `/write-chapters` |
| Full grep before tic audit | `book-lektor` |
| Verify findings against source (quotes exist) | all three reviewer agents |
| Copy faithfully, change only what's listed | *roadmap* (`book-copyfaithful-reviser`) |
| Adversarial per-finding verifier | *roadmap* (`book-finding-verifier`) |
| Conservative metric re-pass | *roadmap* (revise cycle) |
| Central consistency decisions; sweep old value | *roadmap* (revise cycle / normalize wrapper) |
| Tool `--draft` defaults are stale | *roadmap* (tool wrappers) — noted explicitly |

## Out of scope (YAGNI)

- The deferred commands/agents above are **documented, not built**.
- No external Lektorat brief template in the Kern (roadmap).
- No German command aliases (English names; trivial to alias later).
- No default-book inference (book is always an explicit argument while two books are active).
- No changes to either book's manuscript/bible content.

## Success criteria / verification

- All seven files exist; the three commands are invokable via `/`.
- **Genre-neutral check:** the commands resolve the cozy book's bible (`romance-beat-sheet.md`,
  `premise-and-promise.md`) and the mystery book's bible (`12-step-formula.md`,
  `premise-and-twist.md`) purely through each book's `CLAUDE.md` — no bible filename is hardcoded in
  any command/agent (grep proves it).
- **Live smoke test:** `/review-chapter cozy-fantasy-romance 1 Draft_2` (an existing finished
  chapter) produces `review/feedback_Draft_2/chapter-01.md` with three populated sections; the
  Lektor's tic counts come from grep; cited quotes verify against the chapter.
- No `Skybound`/`Theron`/`Sable`/`Alexander`/`Daniela`/book-title leakage in the command or agent
  definitions (grep).
- `framework/COMMANDS.md` exists and is linked from `README.md` and `GUIDE.md`.

## Open considerations (resolve during planning)

- Exact frontmatter per command/agent (`allowed-tools`, `argument-hint`, `model`); whether reviewer
  agents stay Opus or drop to a cheaper tier for the blind/lektor passes.
- How `/review-chapter` resolves the **default draft** when `$3` is omitted: from
  `book.config.yaml` `default_draft`, or the highest existing `Draft_N` folder.
- Whether `/write-chapter`'s draft target should ever be a draft other than `Draft_1` (Kern keeps it
  first-draft authoring; revising is the roadmap cycle).
- Whether to add minimal German aliases now or defer.
