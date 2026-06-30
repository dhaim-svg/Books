# Book-Writing Commands & Subagents

Reusable slash commands and subagents for the recurring work of writing a book with this
framework. They live at workspace level (`.claude/commands/`, `.claude/agents/`) and are shared
across every book in the repo.

## Conventions

- **Genre-neutral via the book's `CLAUDE.md`.** No command or agent hardcodes bible filenames.
  Each one reads `<book>/CLAUDE.md` first — that file indexes the bible, state, spec, and
  manuscript paths — and follows its links. This is why the same commands work for the mystery
  book (`12-step-formula.md`, `premise-and-twist.md`) and the romance
  (`romance-beat-sheet.md`, `premise-and-promise.md`).
- **Book is the first argument**, e.g. `/write-chapter cozy-fantasy-romance 5`. Explicit, because
  more than one book is active.
- **Reviews are read-only.** The review command reports; revising prose is a separate (roadmap) step.

## Active commands

| Command | Args | What it does |
|---|---|---|
| `/write-chapter` | `<book> <N>` | Single chapter, spec-first (Pattern A). Generates the spec if missing (with approval), drafts `Draft_1/chapter-NN.md`, self-checks against brand-voice, then **proposes** recap + known-facts for the author to approve. |
| `/write-chapters` | `<book> <from> <to>` | Multi-chapter orchestrator (Pattern B). One `book-chapter-writer` subagent per chapter, **sequential**; state is **injected** into each subagent and **merged back** by the orchestrator between chapters. Autonomous (no per-chapter approval). |
| `/review-chapter` | `<book> <N> [draft]` | Dispatches three reviewers **in parallel** and assembles one `review/feedback_<draft>/chapter-NN.md` with **Blind / Informed / Lektorat** sections. |

## Active subagents

| Agent | Role |
|---|---|
| `book-chapter-writer` | The per-chapter drafting worker for `/write-chapters`. Uses injected state (never reads state files), no placeholders, spoiler-wall calibration-only, runs the brand-voice checklist, returns recap/known-facts proposals. |
| `book-blind-reviewer` | First-time-reader review. **No** bible access. |
| `book-informed-reviewer` | Continuity/technical review **with** full bible + state. |
| `book-lektor` | German stylistic line edit (grammar, repetition, rhythm/Holprigkeit, tics). Greps every tic family before counting; flags, never rewrites. |

## Hard-won lessons → where they're enforced

| Lesson | Enforced in |
|---|---|
| Inject state into subagents; don't let them self-read | `/write-chapters` + `book-chapter-writer` |
| No `[placeholder]` — decide or flag | `book-chapter-writer` |
| Spoiler-wall = calibration only | `book-chapter-writer` |
| Propose state, don't auto-write (single chapter) | `/write-chapter` |
| Parallel agents with distinct outputs | `/review-chapter` |
| Deliverable owned by the main loop (verify the path) | `/review-chapter`, `/write-chapters` |
| Full grep before a tic audit | `book-lektor` |
| Verify findings against source (quotes exist) | all three reviewers |

## Roadmap (not built yet)

Documented here so we can pick them up seamlessly. Each cites the validating memory.

- **`/review-cycle`** — the full 4-phase loop: Review → **Triage gate** (author approves) →
  copy-faithful Revise → Combine `_full-manuscript.md`. *(memory: review-revision-workflow)*
- **`/plot-audit`** — 7-pass read-only whole-manuscript structural/continuity audit, with
  adversarial per-finding verification. *(memory: plot-audit-workflow, verify-audit-findings)*
- **Tool-wrapper commands** — `/flow-audit`, `/copyedit`, `/normalize-spelling` around the
  `tools/` scripts. **Always pass `--draft` explicitly** — the tool defaults are stale for any
  non-Skybound book. *(memory: tool-draft-defaults, central-consistency-decisions)*
- **`/build-epub`** and the release steps. *(framework/GUIDE.md §7)*
- **`book-copyfaithful-reviser`** — revision worker; lead with "copy faithfully, change only
  what's listed", carry a `changed` flag + a per-item hard-preserve list, and authorize "no change
  if it's intentional craft". *(memory: revision-agent-core-rule, conservative-metric-repass)*
- **`book-finding-verifier`** — adversarial per-finding verifier; re-opens the cited source and
  defaults to refuting any finding whose quote can't be located. *(memory: verify-audit-findings)*
- **External Lektorat brief** — a `review/` template (sibling to `review-brief-blind/informed.md`)
  for handing a chapter to an outside AI/human Lektor.

After any approved fact edit, remember to **sweep the whole manuscript + state files for the OLD
value** to catch residuals the scoped brief missed. *(memory: sweep-old-value-after-fact-edit)*
