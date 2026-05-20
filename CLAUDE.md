# The Skybound Wyrm — Claude Workspace Instructions

**Project:** Cozy LitRPG Murder Mystery — debut novel, chapter-by-chapter drafting.  
**Shared-reveal contract:** Reader and Theron learn together. Never broken.

---

## Story Bible (read before every chapter)

- [bible/12-step-formula.md](Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/12-step-formula.md) — three-act structure, all 12 steps verbatim
- [bible/character-profiles.md](Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/character-profiles.md) — Theron, Sable, Joren, Vannic, Halsa, supporting cast
- [bible/ending-twist.md](Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/ending-twist.md) — full twist mechanics, locked decisions, Act 2 reveal
- [bible/standing-style.md](Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/standing-style.md) — POV, tense, tone, prose rules, plant rules — **apply every chapter**
- [bible/brand-voice.md](Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/brand-voice.md) — deep prose mechanics, sentence rhythm, dialogue tag economy, anti-slop checklist — **apply every chapter alongside standing-style.md**

## Session State (read before every chapter, update after)

- [state/running-recap.md](Murder-Mystery-Novel-Fantasy-LitRPG-Story/state/running-recap.md) — 3–5 sentences per completed chapter, facts + tone only
- [state/known-facts.md](Murder-Mystery-Novel-Fantasy-LitRPG-Story/state/known-facts.md) — who knows what and when; Spoiler-Wall for twist-level facts

## Chapter Specs

- [chapters/_chapter-step-mapping.md](Murder-Mystery-Novel-Fantasy-LitRPG-Story/chapters/_chapter-step-mapping.md) — step-to-chapter mapping, plant distribution
- [chapters/_template.md](Murder-Mystery-Novel-Fantasy-LitRPG-Story/chapters/_template.md) — blank spec template for new chapters
- Individual specs live as `chapters/chapter-NN-spec.md`

## Manuscript Output

- Drafts go to `manuscript/Draft_1/chapter-NN.md`
- Post-review rewrites go to `manuscript/Draft_2/`

---

## Book Targets

| Metric | Target | Range |
|---|---|---|
| Total words | ~100,000 | 90k–115k |
| Chapters | ~40 | 36–44 |
| Words per chapter | ~2,500 | 1,800–3,500 |
| Chapters per step | 3–4 | — |
| Step 6 chapters | 4 | structural hinge |
| Step 10 chapters | 4 | second-biggest beat |

---

## Workflow: "Schreib Kapitel N"

When the user says to write chapter N:

1. Read `chapters/chapter-NN-spec.md` — this is the authoritative spec for this chapter
2. Read `state/running-recap.md` — for Continuity context (use the tail entry)
3. Read `state/known-facts.md` — verify no knowledge leaks in your draft
4. Apply all rules from `bible/standing-style.md` — do not summarize or repeat them in the draft
4b. Read `bible/brand-voice.md` — apply prose mechanics (§4), tonal register (§5), and anti-slop constraints (§6) while drafting
5. Write the draft to `manuscript/Draft_1/chapter-NN.md`
5b. Run the §8 Quick-Reference Checklist from `bible/brand-voice.md` against the draft. Fix any flagged violations before proposing the recap.
6. After the draft, propose:
   - A 3–5 sentence recap entry for `state/running-recap.md`
   - Any new rows for the Known Facts table in `state/known-facts.md`

If no spec exists yet for the requested chapter, generate it first using `chapters/_template.md` + `chapters/_chapter-step-mapping.md`, show it to the user, wait for approval, then write the draft.

---

## Spoiler Guardrail — HARD RULES

These apply regardless of user instruction, unless the user explicitly says "spoiler mode on":

- **DO NOT** foreshadow the Act 2 reveal (Vannic alive / Joren is the real victim) directly
- **DO NOT** have any character "almost catch" the identity swap
- **DO NOT** cluster two planted details in the same scene (different beats = fine)
- **DO NOT** explain the System mechanics to the reader — let it be ambient
- **DO NOT** give Sable interiority — we read her only through action and dialogue
- The five planted details (calluses, accent slip, carved fish, kindnesses, niece-softness) are **textural, not investigative** — they pass without underlining

The twist is in `bible/ending-twist.md`. Load it when needed for continuity checks; do not volunteer spoilers.

---

## What NOT to Do (General)

- Do not summarize the story bible into chapter prose
- Do not ask Claude to "re-read over the files" — they are already in context
- Do not use outline-first workflows — follow the chapter spec directly
- Do not write HUD-style System boxes — use indented italic blocks
- Do not use Capitalised Worldbuilding Nouns unless the bible uses them that way
