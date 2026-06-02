# Draft 5 Revision — *The Skybound Wyrm* (Workflow-driven)

## Purpose

Produce **Draft 5** from Draft 4 by applying the consolidated triage brief, one
chapter at a time, via parallel revision agents. Every edit is authorised by the
per-chapter entry in `_triage.md`; nothing else changes.

This runs as **two workflow stages with a human approval gate between them**
(a workflow cannot pause mid-run, so the blocker checkpoint is a separate
invocation):

- **Stage A — Blocker & continuity resolution.** Resolve the 3 Blockers and the
  cross-chapter continuity seams, propose exact before/after text, and **stop for
  the user's approval.**
- **Stage B — Per-chapter revision + combine + verify.** After approval, 40
  parallel agents revise each chapter (structural fix + flow tics together),
  combine the manuscript, then re-score flow and re-check continuity.

The governing rule for every revision agent: **copy faithfully — change only what
the chapter's triage entry lists.** Do not rewrite for style beyond the named tic
fixes. Do not touch passages marked *preserve*.

---

## Read before building (load into context before Stage A)

**The triage brief (authoritative, per chapter):**
1. `Murder-Mystery-Novel-Fantasy-LitRPG-Story/review/feedback_Draft_4/_triage.md`
   — the complete per-chapter instruction set. Each chapter's entry is the only
   change-list for that chapter.

**Revision authorities (what agents fix *to*):**
2. `bible/brand-voice.md` §4.1 (sentence-level + short-chain + opener-variety
   rules), §6 (anti-slop), §8 (quick-reference checklist).
3. `review/feedback_Draft_4/_flow-audit.md` — the **Qualitative Findings** section
   only (Tic-Type A/B/C/D fix principles + the summary table). This is the tic-fix
   playbook. (The triage's Global Block 2 reproduces it in brief.)
4. `bible/standing-style.md` — POV, tense, prose rules. The voice does not change
   between drafts; agents preserve it.

**Continuity authorities (needed for Stage A blocker resolution):**
5. `bible/ending-twist.md` — twist mechanics and locked decisions (load for the
   locked-room and scry-log fixes; do not leak into prose).
6. `state/known-facts.md` — who-knows-what + the Spoiler-Wall. Note: it records
   **"Service slot used to draw the bolt,"** confirming **Ch 4 as canonical** for
   the locked-room mechanism.
7. `state/running-recap.md` — per-chapter facts/tone for continuity context.

**Source manuscript:**
8. `manuscript/Draft_4/chapter-NN.md` — the text each chapter is revised *from*.
   (Stage A reads only the blocker-affected chapters; Stage B reads each chapter
   it revises.)

---

## Output

- Revised chapters → `manuscript/Draft_5/chapter-NN.md` (NN = 01..40).
- Combined manuscript → `manuscript/Draft_5/_full-manuscript.md`.
- Stage-A brief (for approval) → `review/feedback_Draft_4/_draft5-blocker-brief.md`.
- Verification report → `review/feedback_Draft_4/_draft5-verification.md`.
- State files updated in place: `state/running-recap.md`, `state/known-facts.md`
  (only where a blocker fix changed a fact).

---

## Blockers & continuity seams to resolve in Stage A

Each seam below has a **canonical side** taken from the triage; Stage A agents
read the affected Draft_4 chapters and propose the *exact* replacement text, then
the user approves. Chapters touched: **04, 05, 06, 09, 12, 14, 21, 22, 23, 30, 33,
38, 40.**

| # | Seam (severity) | Chapters | Canonical resolution (from triage) |
|---|---|---|---|
| B1 | Locked-room mechanism (**Blocker**) | Ch 4 ↔ Ch 30 | Keep Ch 4's clean **service-slot lift-key** bolt-lift (canonical per `known-facts.md`). Rewrite Ch 30's *"no external override … the bolt had to be cut"* so the method is consistent with the service-slot override. Re-ground the Ch 30 solution beat using `ending-twist.md` + the Ch 29–32 method payoff so nothing downstream depends on a cut bolt. **Highest-risk edit — propose full before/after for the Ch 30 passage.** |
| B2 | Meta-note in System line (**Blocker**) | Ch 22 | Excise *"The surprise in Ch. 20 was real."* Rewrite the System line as in-world output (no chapter-number reference). |
| B3 | Authoring vocabulary (**Blocker** + **Should-fix**) | Ch 23 | Rewrite *"a thread for Act 3"* without act-structure vocabulary. Remove the *"case file Ch. 1–12"* chapter-number reference from the System line. |
| B4 | Voyage-length (**Should-fix**) | Ch 4, 6, 9, 12 | Canonical = **"Three days"** (Ch 1) + the hours-countdown spine. Ch 4: *"thirty hours"* → **"nineteen hours."** Ch 6 + Ch 9: *"six days drafting"* → **"two."** Ch 12: reconcile *"ten days / second / fourth / seventh day"* to fit the three-day voyage. |
| B5 | Sannholt-letter timeline (**Should-fix**) | Ch 21 | Canonical = **Tuesday's run** (Ch 19; Ch 22 "It's Wednesday"). Fix Ch 21's *"accepted Friday run"* to be consistent with a Tuesday dispatch and Wednesday-present arithmetic. |
| B6 | Book-2 device fairness (**Should-fix**) | Ch 33 (38/40) | **Plant the device on the page** at Davren's table in Ch 33 (Theron registers the sigil among Halsa's papers, sets it aside) so the Ch 38/Ch 40 "noticed earlier" claims are earned. Keep Ch 38/40 as-is once the plant exists. |
| B7 | Scry-log fairness (**Should-fix**) | Ch 4 **or** Ch 5 | Seed the scry-log / standing-detection result (one line — *"no cast magic in cabin twelve during the third night"*) into Ch 4 or Ch 5 so the reader holds it before the Ch 30 turn. Pick one site. |
| B8 | Esherel saloon/witness plan (**Should-fix**) — **AUTHORIAL CHOICE** | Ch 12 ↔ Ch 14 | Stage A must present **both** options for the user to pick: (a) add a brief line in Ch 14 acknowledging the Ch 13 floor-drop preempted the staged saloon/witness plan; **or** (b) trim Ch 12's elaborate saloon setup so nothing dangles. |
| B9 | Closing-entry date (**Should-fix**) | Ch 38 | *"Closing — Sannholt, October fifth."* → **"the seventeenth of November"** (the dated Sannholt delivery). |

Minor copyedits that live in blocker chapters (Ch 30 *"third watch"* → *"third
night"*; Ch 30 *"We measured"* porthole) are folded into that chapter's Stage-B
revision per its triage entry — they do not need separate Stage-A treatment.

---

## Stage A — Blocker & continuity resolution (run first, then STOP)

Author and run a workflow that:

1. Reads `_triage.md` (Global Block 1 + the entries for the 13 affected chapters),
   the continuity authorities (`ending-twist.md`, `known-facts.md`,
   `running-recap.md`), and each affected `manuscript/Draft_4/chapter-NN.md`.
2. Resolves the seams above. Run one agent per seam (B1–B9) — they are
   independent, so dispatch in parallel. Each agent returns, **per affected
   chapter**: the exact **before** snippet (verbatim from Draft_4) and the
   proposed **after** snippet, plus a one-line rationale tying it to the canonical
   resolution. For **B1** (locked-room) and **B6** (Book-2 plant), require the full
   passage, not just a line. For **B8**, return *both* options (a) and (b) as
   alternatives.
3. The main loop writes the consolidated proposals to
   `review/feedback_Draft_4/_draft5-blocker-brief.md` and **presents them to the
   user for approval** — explicitly asking the user to choose the B8 option and to
   confirm/adjust the B1 locked-room rewrite.

**Stop here.** Do not start Stage B until the user approves the brief.

Continuity guardrail for Stage A: the locked-room and scry-log rewrites must not
break the **shared-reveal contract** or foreshadow the Act-2 reveal (Vannic alive
/ Joren the real victim). Honour the Spoiler Guardrail in `CLAUDE.md`.

---

## Stage B — Per-chapter revision + combine + verify (run after approval)

Author and run a workflow with three phases:

### Phase 1 — Revise all 40 chapters (parallel)

One agent per chapter (NN = 01..40), dispatched in parallel — distinct output
files, no shared state, no conflicts. Each agent receives:

- The chapter's **`_triage.md` entry, verbatim** (its complete change-list).
- The source `manuscript/Draft_4/chapter-NN.md`.
- The tic-fix authorities: brand-voice §4.1/§6/§8 and the flow-audit Qualitative
  Findings fix principles (Global Block 2 of the triage).
- For the 13 blocker chapters: the **approved Stage-A before/after edit(s)** for
  that chapter.

Each agent:

- **Copies the chapter faithfully and changes only what its triage entry lists**
  (plus the approved blocker edit, if any). Applies the named tic fixes:
  - **Type A** — merge two stage-direction beats into one compound, or give the
    second an adverbial/object-first lead.
  - **Type B** — consolidate the "did not" negations into a single adverbial unit;
    replace a final pronoun with the name.
  - **Type C — preserve** — do **not** revise (Ch 30 theory/Halsa anaphora; Ch 09
    discovery staccato). Exception: the Ch 33 accidental "it's warm" echo — cut one
    instance.
  - **Type D** — replace *"A beat."* with a small grounding action or remove it
    (Ch 02, 06, 16).
  - Slop-tics — thin/vary across the span as the entry states (working, half-inch,
    nod, on-inspection, not-smiling, cup-turn, shape-of-it, right-name,
    Sable-nothing, X-was-X, gloss-closer). Excise the structural meta-notes.
- **Honours every *preserve* note** in the entry: the §5.4 "he had a name" pivot
  weight (Ch 16), the Ch 37 nod-inversion, the intentional enumerated lists.
- Targets the brand-voice §4.1 thresholds (opener variety, ≤2 consecutive ≤6-word
  sentences outside an exempt beat) **without flattening intentional rhythm.**
- **Writes the result to `manuscript/Draft_5/chapter-NN.md`** and returns a short
  structured summary: `{chapter, editsApplied[], slopTicsThinned[],
  blockerApplied, preservedNotes[], notes}`.

A chapter whose triage entry contains *only* flow hotspots still gets a flow
revision — all 40 chapters are flagged, so **none are copied unchanged** this
round.

### Phase 2 — Combine + state update

- Concatenate `manuscript/Draft_5/chapter-01.md … chapter-40.md` (in order, with
  the project's chapter-separator convention) into
  `manuscript/Draft_5/_full-manuscript.md`.
- Update `state/running-recap.md` and `state/known-facts.md` **only** where a
  blocker fix changed a recorded fact (e.g. the scry-log now seeded in Ch 4/5; the
  Ch 30 mechanism wording; the Book-2 plant now on-page in Ch 33).

### Phase 3 — Verification (flow re-score + continuity recheck)

- **Flow re-score:** an agent runs `python tools/flow_audit.py --draft Draft_5`
  and reports the new composite score per chapter **beside the Draft_4 score**
  (before → after). Flag any chapter that did not improve or that regressed.
- **Continuity recheck:** an agent confirms, against `manuscript/Draft_5/`, that
  **each Blocker/seam (B1–B9) is actually resolved**, that no **shared-reveal
  leak** or Act-2 foreshadow was introduced, and that the eight canonical plants
  and the glamour-exploit / quest-title payoffs still land. Adversarially verify
  before reporting (drop misreadings).
- Write both to `review/feedback_Draft_4/_draft5-verification.md` and summarise
  for the user.

The main loop then **verifies all 40 `manuscript/Draft_5/chapter-NN.md` files
exist** with correct names before declaring Draft 5 complete.

---

## Conduct rules

- **Copy faithfully — change only what is listed.** Lead every revision agent with
  this. The triage entry + approved blocker edit are the *entire* mandate.
- **Do not re-diagnose.** Take the triage as given. Do not invent new findings, do
  not "improve" prose that wasn't flagged, do not re-score severities.
- **Preserve intentional craft.** Type-C passages, the §5.4 pivot, the Ch 37
  inversion, enumerated lists — these are marked preserve and must survive intact.
- **Verify before claiming done.** Re-score with `flow_audit.py`; confirm blockers
  resolved; confirm all 40 output files written.
- **Parallel where independent.** 40 distinct chapter files and 9 independent
  seams fan out cleanly; combine and verify are barriers.

## DO NOT

- Do not start Stage B before the user approves the Stage-A blocker brief.
- Do not rewrite for style beyond the named tic fixes.
- Do not touch passages marked *preserve*.
- Do not foreshadow the Act-2 reveal or break the shared-reveal contract
  (Spoiler Guardrail in `CLAUDE.md` applies).
- Do not alter Ch 4's canonical service-slot bolt-lift (fix the Ch 30 side).
- Do not write HUD-style System boxes; keep System notes as indented italic lines.
- Do not skip or merge chapters; produce exactly 40 output files.
