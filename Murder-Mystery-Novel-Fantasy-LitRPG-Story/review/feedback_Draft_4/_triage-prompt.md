# Triage Builder — *The Skybound Wyrm*, Draft 4

## Purpose

Build a consolidated revision brief (`_triage.md`) for Draft 4 by combining two
completed audits:

- **Flow audit:** `review/feedback_Draft_4/_flow-audit.md`  
  Prose rhythm, sentence structure, opener variety — all 40 chapters measured and
  hotspot-listed. Tic types A/B/C/D are defined in the qualitative findings section.

- **Plot audit:** `review/feedback_Draft_4/_plot-audit-findings.md`  
  Structural, continuity, fairness, motivation, tonal, and AI-artifact findings across
  7 passes.

The output is a per-chapter brief. Each entry in `_triage.md` is a complete,
self-contained revision instruction for one chapter — ready to be handed to a revision
agent without that agent needing to read both source audits.

---

## Read before building

**Both source audits — read in full, do not summarize from memory:**

1. `Murder-Mystery-Novel-Fantasy-LitRPG-Story/review/feedback_Draft_4/_flow-audit.md`  
   All sections: the Überblick, heatmap, per-chapter hotspot list, and the full
   Qualitative Findings section (tic types A/B/C/D including the Type D entry).

2. `Murder-Mystery-Novel-Fantasy-LitRPG-Story/review/feedback_Draft_4/_plot-audit-findings.md`  
   All sections: verdict, passes 1–7 findings, setup/payoff table, AI-artifact
   hit-list.

**Reference for tic-type context:**

3. `Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/brand-voice.md`  
   §4.1 (sentence-level rules, including the short-chain and opener-variety rules
   added after the flow audit), §6 (anti-slop checklist), §8 (quick-reference
   checklist). Read to understand what revision agents will use as their authority —
   do not re-derive findings from it.

---

## Output

Write to:
`Murder-Mystery-Novel-Fantasy-LitRPG-Story/review/feedback_Draft_4/_triage.md`

---

## Output format

### File header

Begin the file with exactly:

```
# Draft 4 Triage — The Skybound Wyrm
_Sources: `_flow-audit.md` (flow/rhythm) · `_plot-audit-findings.md` (structural/continuity)_
_Revision rule for all agents: copy faithfully — change only what is listed below._
_Do not fix findings not listed here. Do not rewrite for style beyond the tic fixes._
```

---

### Global section

Immediately after the header, before the per-chapter entries, write two blocks:

**Block 1 — Blockers (address before any chapter revision begins):**

List the three Blocker-severity findings from the plot audit as a numbered list.
For each: chapter, exact quote from the audit, one-clause problem statement.
Do not propose fixes. Do not explain — just locate and name the problem.

**Block 2 — Flow tic-type quick reference:**

Four entries, one per tic type (A, B, C, D) drawn directly from the Qualitative
Findings section of `_flow-audit.md`. One to two sentences per type:
- What the tic is (structural definition)
- The fix principle (one clause — not a rewrite)
- For Type C: the exemption note (intentional anaphora — do NOT revise)
- For Type D: the three affected chapters

This reference is for revision agents reading individual chapter entries; it saves
them from having to open `_flow-audit.md` themselves.

---

### Per-chapter entries

One entry per chapter, in order (01 to 40). Heading format:

```
## Chapter NN [flow score: X.X | plot: <highest severity or "none">]
```

The `plot:` tag uses the **highest** severity of any plot finding in that chapter
(Blocker / Should-fix / Minor / none). If only AI-artifact list items apply, use
their severity.

Each entry has up to four subsections. **Omit a subsection entirely** if that chapter
has nothing in it.

#### Subsection: Blocker

Only if the chapter has a Blocker-level plot finding. One line per finding:

> *"exact quote from the audit"* → problem in one clause

#### Subsection: Should-fix

One line per finding using the same format. Include:
- Plot-audit Should-fix findings for this chapter
- AI-artifact hit-list items at Should-fix severity for this chapter

#### Subsection: Flow

Copy the hotspot entries for this chapter from `_flow-audit.md` **verbatim** —
do not paraphrase or regenerate them. Label each hotspot with its tic type in
square brackets: `[Type A]`, `[Type B]`, `[Type D]`. Hotspots that are Type C
(intentional anaphora, must not be revised) must be labeled `[Type C — preserve]`.

After the hotspots, append one line per slop-tic / AI-artifact item from the
plot audit's Pass 7 list that falls in this chapter and has Should-fix or Minor
severity (use the same one-line format as above).

#### Subsection: Minor / Polish

One line per Minor-severity plot finding and per Minor-severity AI-artifact entry
for this chapter. Same one-line format.

---

### Cross-reference tag

When a plot finding and a flow hotspot point to the **same passage**, add a `⟳`
tag to both lines with a one-word label identifying the issue (e.g., `⟳ meta-note`,
`⟳ countdown`, `⟳ act3`). This tells the revision agent that one edit addresses two
findings simultaneously.

---

## Conduct rules

- **Consolidate, do not re-diagnose.** Take all findings as given from the two source
  audits. Do not invent new findings, change severities, or dispute the audits.
- **List problems, not solutions.** Each entry names what is wrong and where. It does
  not say what to write instead. Revision agents will derive their fixes from the
  tic-type reference block and `bible/brand-voice.md`.
- **Every chapter gets an entry**, even if it has no plot findings. A chapter with
  only a flow score and hotspot list is a complete and valid entry.
- **Exact quotes must be copied verbatim** from the source audits — do not paraphrase.
- **Hotspot entries from `_flow-audit.md` must be copied verbatim**, including the
  sentence indices and quoted snippets.
- Do not produce running commentary, explanatory paragraphs, or transitions between
  entries. Entries only.

---

## DO NOT

- Do not rewrite or improve any prose.
- Do not propose fixes inline with findings.
- Do not merge or skip chapters.
- Do not add findings that are not in the two source audits.
- Do not read the manuscript (`_full-manuscript.md` or individual `chapter-NN.md`
  files) — the triage is built entirely from the two audit reports.
- Do not summarize the audits back in the preamble — the header and global blocks
  are functional, not descriptive.
