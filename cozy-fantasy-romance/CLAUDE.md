# Kaffee, Magie und ein Drache namens Felix — Claude Workspace Instructions

**Project:** Cozy Fantasy Romance — chapter-by-chapter drafting.  
**Shared-reveal contract:** Leserin und Daniela entdecken Alexanders wahres Talent gemeinsam — die gepflanzten Details deuten es an; kein Charakter benennt es explizit, bis er es selbst zeigt. Never broken.

---

## Story Bible (read before every chapter)

- [bible/romance-beat-sheet.md](bible/romance-beat-sheet.md) — 20-Beat-Struktur (Romancing the Beat), alle Beats verbatim
- [bible/character-profiles.md](bible/character-profiles.md) — Alexander, Daniela, Felix, Nebencast (Lena, Hanna, Eltern)
- [bible/premise-and-promise.md](bible/premise-and-promise.md) — Prämisse, sanfte Wendung (Talent-Reveal), gepflanzte Details, locked decisions
- [bible/standing-style.md](bible/standing-style.md) — POV, tense, tone, prose rules, plant rules — **apply every chapter**
- [bible/brand-voice.md](bible/brand-voice.md) — deep prose mechanics, sentence rhythm, dialogue tag economy, anti-slop checklist — **apply every chapter alongside standing-style.md**

## Session State (read before every chapter, update after)

- [state/running-recap.md](state/running-recap.md) — 3–5 sentences per completed chapter, facts + tone only
- [state/known-facts.md](state/known-facts.md) — who knows what and when; Spoiler-Wall for talent-reveal facts

## Chapter Specs

- [chapters/_chapter-step-mapping.md](chapters/_chapter-step-mapping.md) — Beat-to-chapter mapping, plant distribution, Daniela-Kapitel markiert
- [chapters/_template.md](chapters/_template.md) — blank spec template for new chapters
- Individual specs live as `chapters/chapter-NN-spec.md`

## Manuscript Output

- Drafts go to `manuscript/Draft_1/chapter-NN.md`
- Post-review rewrites go to the next `manuscript/Draft_N/` (bump the number each review pass)

---

## Book Targets

| Metric | Target | Range |
|---|---|---|
| Total words | ~90,000 | 80k–100k |
| Chapters | ~36 | 32–40 |
| Words per chapter | ~2,500 | 1,800–3,200 |
| Kapitel pro Beat | 1–2 | — |
| Beat 10 (Midpoint / Hinge) | 1 Kapitel | volles Kapitel, kein Szenenende |
| Beat 15 & 18 (Break-up / Grand Gesture) | 1–2 Kapitel je | leise / bescheiden, kein Spektakel |

---

## Workflow: "Schreib Kapitel N" (write chapter N)

When the user says to write chapter N:

1. Read `chapters/chapter-NN-spec.md` — this is the authoritative spec for this chapter
2. Read `state/running-recap.md` — for Continuity context (use the tail entry)
3. Read `state/known-facts.md` — verify no knowledge leaks in your draft
4. Apply all rules from `bible/standing-style.md` — do not summarize or repeat them in the draft
4b. Read `bible/brand-voice.md` — apply prose mechanics (§4), tonal register (§5), and anti-slop constraints (§6) while drafting
5. Write the draft to `manuscript/Draft_1/chapter-NN.md`
5b. Run the §9 Quick-Reference Checklist from `bible/brand-voice.md` against the draft. Fix any flagged violations before proposing the recap.
6. After the draft, propose:
   - A 3–5 sentence recap entry for `state/running-recap.md`
   - Any new rows for the Known Facts table in `state/known-facts.md`

If no spec exists yet for the requested chapter, generate it first using `chapters/_template.md` + `chapters/_chapter-step-mapping.md`, show it to the user, wait for approval, then write the draft.

---

## Talent-Reveal Guardrail — HARD RULES

These apply regardless of user instruction, unless the user explicitly says "spoiler mode on":

- **DO NOT** foreshadow Alexanders außergewöhnliches Talent direkt — kein Charakter benennt es explizit, bis er es in Beat 18 selbst zeigt
- **DO NOT** lass irgendeinen Charakter Alexanders Talent explizit kommentieren (kein: „du bist viel zu gut für einen normalen Arkanisten")
- **DO NOT** cluster two planted details in the same scene (different beats = fine)
- **DO NOT** erklär die Magiemechanik der Welt dem Leser — sie ist Atmosphäre, nicht System
- **DO NOT** gib Daniela Introspektion in Alexander-Kapiteln — sie bleibt opak, gelesen nur durch Aktion und Dialog
- Die fünf gepflanzten Details (Hände, Geräte, Felix, Notizbuch, Funken) sind textural, nicht ermittelnd — sie passieren ohne Unterstreichung

Die sanfte Wendung (Alexanders Talent) und Danielas No-Way-Gründe sind in `bible/premise-and-promise.md` dokumentiert. Bei Kontinuitätsprüfungen laden; keine Spoiler von dir aus.

---

## What NOT to Do (General)

- Do not summarize the story bible into chapter prose
- Do not ask Claude to "re-read over the files" — they are already in context
- Do not use outline-first workflows — follow the chapter spec directly
- Do not write HUD-style status boxes — use indented italic blocks (if your genre uses system/UI text at all)
- Do not use Capitalised Worldbuilding Nouns unless the bible uses them that way
