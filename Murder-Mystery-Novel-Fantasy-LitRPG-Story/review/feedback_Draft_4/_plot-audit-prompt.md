> **How to run:** Paste this into a fresh Claude Code session opened in the
> `d:\Projects\Books` workspace. No file attachments needed — the auditor reads
> everything from disk. When you are ready, say "Run the plot audit."

---

# Plot Audit — *The Skybound Wyrm*, Draft 4

## Read these files before writing anything

**Source of truth — bible (read all five):**

1. `Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/12-step-formula.md` — three-act structure and step sequence; authoritative for structural assignments
2. `Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/ending-twist.md` — full twist mechanics, locked decisions, Act 2 reveal
3. `Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/character-profiles.md` — Theron, Sable, Joren, Vannic, Halsa, supporting cast
4. `Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/standing-style.md` — POV, tense, tone, prose rules, plant rules
5. `Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/brand-voice.md` — sentence rhythm, dialogue tag economy, §5 tonal register, §6 anti-slop checklist, §8 quick-reference checklist

**State (who knows what, and when):**

6. `Murder-Mystery-Novel-Fantasy-LitRPG-Story/state/known-facts.md` — facts established on the page per chapter, plus the Spoiler Wall
7. `Murder-Mystery-Novel-Fantasy-LitRPG-Story/state/running-recap.md` — 3–5 sentence factual summary of each completed chapter

**Plant / step distribution:**

8. `Murder-Mystery-Novel-Fantasy-LitRPG-Story/chapters/_chapter-step-mapping.md` — which step each chapter belongs to and any plant-distribution notes
9. Individual chapter specs live at `Murder-Mystery-Novel-Fantasy-LitRPG-Story/chapters/chapter-NN-spec.md` — consult the relevant spec when you need to verify what a chapter was designed to do

**Draft to audit:**

10. `Murder-Mystery-Novel-Fantasy-LitRPG-Story/manuscript/Draft_4/_full-manuscript.md` — the complete 40-chapter Draft 4 manuscript; this is what gets audited

The bible is the source of truth. Where the draft contradicts the bible, that is a
finding, unless the contradiction is clearly an intentional revision (in which case
flag it as "possible intentional change — confirm"). Cite all findings by chapter
using the form `Chapter N` (or `Ch N, scene ~[scene position]` when you can narrow
it further); your location tags should be findable in the individual chapter files at
`manuscript/Draft_4/chapter-NN.md`.

---

## Audit scope and conduct

This is a structural and continuity review, not a line edit and not a rewrite. Do not
change any prose. Do not suggest stylistic improvements unless a passage is actively
broken. Your job is to find what is missing, contradictory, unfair to the reader, or
mechanically wrong — and to flag anything in the text that looks like a leftover
authoring artifact rather than finished narrative.

Work through the following passes in order. For every finding give me: the chapter/
scene location, a short quote or paraphrase so I can find it, the problem, and the
severity (**Blocker** / **Should-fix** / **Minor**). Do not pad. If a pass turns up
nothing, say so in one line and move on.

---

## Pass 1 — Causal chain

Walk the draft scene by scene. For each scene state in one clause what causes it and
what it causes. Flag any scene that connects to its neighbours with "and then" rather
than "therefore / but" — i.e. a scene that could be cut without breaking the chain.
Flag sagging stretches where nothing changes the protagonist's situation.

---

## Pass 2 — Setup / payoff inventory

Build a table of every planted detail and its payoff. The formula's step-to-chapter
assignments live in `chapters/_chapter-step-mapping.md`; the per-chapter design
intent is in the individual `chapter-NN-spec.md` files. The structural authority for
*when* each plant should appear is `bible/12-step-formula.md`. The rules governing
*how* plants must be handled (textural-not-investigative, never clustered two-per-scene)
are in `bible/standing-style.md`.

Two columns of special concern — verify each one is planted exactly where the formula
assigns it, surfaces again only after the Step-6 reveal, and is never clustered with
another plant in the same scene:

- The five Joren plants: calluses, accent slip, carved fish, the kindnesses (steward
  by name / ginger sweet / stepping aside), the niece-softness.
- Sable's "he wasn't as bad as I expected" line — planted in Step 4, must come back as
  *the* line that breaks Theron in Step 6 (not one of the five details).
- The scryproof glamour exploit — planted as dismissed exam fodder in Theron's
  backstory, paid off as the method in Step 10.
- The System quest title flip (Step 12) and the book-two thread (sigil/contract
  fragment, noticed and set aside, unresolved).

Flag: any plant with no payoff, any payoff with no plant, any plant that lands too
early or gives the swap away before Act 2, and any scene carrying two plants at once.

---

## Pass 3 — Fairness check (mystery contract)

The reveal model is *reader and Theron solve simultaneously*. Verify every clue needed
to reach the solution is on the page before the reveal, nothing critical happens only
off-page, and the reader is never behind or ahead of Theron on the load-bearing beats.
Flag any solution step that relies on information the reader was never given.

Cross-reference `state/known-facts.md` (the who-knows-what record and its Spoiler
Wall) to verify no information reaches the reader before it reaches Theron, and no
information is withheld from Theron that the reader already has. Use
`state/running-recap.md` for sequence sanity on what was established when.

---

## Pass 4 — Timeline & locked-room continuity

This is a sealed cabin on a moving gondola. Track where every named character is in
every scene, who knows what at each point, and whether the murder method is physically
consistent with the established layout and timing. Flag any character who knows
something before they could have learned it, any spatial impossibility, and any
contradiction in the sequence of the death.

Use `state/known-facts.md` as your who-knows-what-and-when ledger and
`state/running-recap.md` for chronological sequencing across chapters.

---

## Pass 5 — Motivation

For each major character (Theron, Sable, Halsa, Vannic, Joren in backstory) confirm
every significant action has a motive consistent with `bible/character-profiles.md`.
Specifically check Theron does not drift away from his "slightly insufferable, sees
roles before people" baseline into being warm too early, and that Halsa reads as
sympathetic-but-not-exonerated rather than as a cackling villain.

---

## Pass 6 — Stakes / tonal curve

Map the emotional curve: where it's buoyant beach-read, where the one real death
carries weight. Flag tonal slips — grimdark creep, jokes that undercut the Step-6
recall passage, or stretches where the cozy texture (Wisp, the drakes, banter) drops
out entirely.

The cozy-texture and tonal register rules are in `bible/standing-style.md` and
`bible/brand-voice.md` §5. Confirm Steps 6 and 10 have the page space the pacing
notes in `bible/12-step-formula.md` demand and aren't compressed into a paragraph.

---

## Pass 7 — AI-artifact / leftover-note sweep

Much of this draft was AI-assisted. Scan for text that is authoring scaffolding rather
than finished narrative and should never reach a reader. Report each with location and
exact quote.

The project's own slop definitions are in `bible/brand-voice.md` §6 (anti-slop
checklist) and §8 (quick-reference checklist). Use those as the primary reference for
what counts as a tic or stock gesture in *this* manuscript's voice. Look for:

- Bracketed or placeholder text: `[like this]`, `[TODO]`, `[NAME]`, `[insert X]`,
  `<...>`, `TKTK`, "TBD", unresolved placeholder names from the bible (e.g. "Lord
  Vannic" used as a literal placeholder where a final name was meant to go).
- Meta-commentary that leaked into prose: instructions to the writer, craft notes,
  "this is where X happens", "Note:", "Remember to", parenthetical authoring asides.
- AI tells / slop: hedging filler ("it's worth noting", "a testament to", "navigate
  the complexities of"), repeated stock gestures (characters constantly "nodding",
  "letting out a breath they didn't know they were holding"), over-frequent em-dashes,
  three-part lists used reflexively, and emotionally over-explained beats that tell the
  reader how to feel. Cross-check the full tic-list in brand-voice.md §6.
- Continuity seams from multi-session drafting: a character or object named two
  different ways, recap sentences that repeat information the reader already has, a
  scene that re-establishes something already established.
- LitRPG-specific: System screens / status dashboards appearing more often than the
  restrained cadence the bible calls for, or stat blocks dumped where a single line
  would do.

For this pass only, do not soften. A leftover bracket is a Blocker regardless of how
small it looks.

---

## Output format

Write findings to:
`Murder-Mystery-Novel-Fantasy-LitRPG-Story/review/feedback_Draft_4/_plot-audit-findings.md`

Structure that file as follows:

1. A one-paragraph verdict: is the draft structurally sound, and what are the top
   three things to fix first.
2. Findings grouped by pass, each as: `[Severity] Location — problem (quote)`.
3. The setup/payoff table from Pass 2.
4. A flat list of every AI-artifact / leftover-note hit from Pass 7, so I can
   search-and-destroy them in one go.

---

## Do NOT

- Do not rewrite, restructure, or "improve" any prose.
- Do not invent findings to seem thorough — an empty pass is a valid result.
- Do not summarise the plot back to me; I wrote it.
- Do not propose fixes inside the findings; list problems. I'll ask for fixes
  separately on the ones I choose.
