# External AI Review — Two-Prompt Plan for Draft_2

## Context

Draft_2 of *The Skybound Wyrm* is complete (~111,400 words, 40 chapters). Before any further pass, we want a fresh outside perspective from external AI(s) to flag what we can't see anymore. The constraints:

- **Fresh-reader experience.** No genre label, no character list, no twist, no bible context. The external AI(s) must encounter the book the way a real reader would.
- **Usable feedback.** Output must be a markdown review file, not a chat response.
- **Coverage without shallowness.** Asking one AI to evaluate continuity, prose, pacing, character, reader experience, and ending payoff in a single pass on a 111k-word manuscript dilutes everything. Splitting across two AIs gives each pass room to go deep.

The split: **Reader** (subjective experience) and **Editor** (analytical pass). Both receive only the manuscript and their prompt — nothing else. Two independent fresh-reader perspectives also let us cross-reference findings.

## Approach

Hand the combined manuscript file ([Murder-Mystery-Novel-Fantasy-LitRPG-Story/manuscript/Draft_2/_full-manuscript.md](Murder-Mystery-Novel-Fantasy-LitRPG-Story/manuscript/Draft_2/_full-manuscript.md)) to two different external AIs with the prompts below. Save their outputs to:

- `reviews/Draft_2/external-reader-review.md`
- `reviews/Draft_2/external-editor-review.md`

Both prompts are deliberately short, withhold all bible/spoiler context, and suggest light section structure without forcing a strict template.

---

## Prompt 1 — The Reader

```
I'm sharing a complete novel manuscript with you. Read it the way a reader would — cover to cover, in order — and then write me a review.

I don't want a literary analysis. I want to know what it was like to read this. Did you keep turning the pages or did you put it down? Where did you get hooked, where did you drift? What did you think was going to happen, and were you right? Did the ending land?

When you're done reading, write a review as a markdown file with these sections (rename them, add others, or skip ones that don't apply):

- **First impressions** — what the opening chapters felt like, what you thought you were getting into
- **What hooked me** — moments, characters, or questions that kept you reading
- **Where I drifted** — slow patches, parts you skimmed, places you wanted to skip ahead
- **Predictions** — what you thought was going on, what you expected to happen, where you were wrong
- **Characters** — who you connected with, who you didn't, who surprised you
- **The ending** — did it earn its payoff? Did it answer the questions you cared about?
- **Anything else** — odd reactions, things that stuck with you, moments you'd reread

Be honest. I don't need encouragement. If something didn't work for you, tell me what and where (chapter numbers are enough — no need to quote at length).

Aim for a review someone could read in five minutes.
```

---

## Prompt 2 — The Editor

```
I'm sharing a complete novel manuscript with you. Read the whole thing first, keeping a running list of facts as you go — names, ages, places, abilities, relationships, rules of the world, who knows what and when. Then write me an editorial review focused on errors, inconsistencies, and craft problems.

Not a summary. Not a star rating. A careful pass.

When you're done, write the review as a markdown file with these sections (rename/skip as needed):

- **Continuity errors** — contradictions in facts, timeline, geography, names, ages, abilities, who-knows-what. Cite the chapters where they conflict.
- **Plot logic** — setups without payoffs, motivations that don't hold up, clues that don't fit, coincidences doing too much work
- **Character voice & behavior** — drift in how a character speaks or acts; relationship shifts without cause
- **Prose problems** — recurring tics, repeated phrases, awkward construction, dialogue tag misuse. Give a few examples with chapter numbers — not an exhaustive list.
- **Pacing & structure** — chapters that sag, info dumps, scenes that don't earn their length, jarring transitions
- **Other** — anything else worth flagging

Cite chapter numbers for every finding. Don't summarize the plot. Don't grade the book. Skip praise — focus on what could be improved.

If something feels intentional (a deliberate ambiguity, a character lying, a planted detail), flag it as such rather than calling it an error.
```

---

## Files to Create

| Path | Contents |
|---|---|
| `reviews/Draft_2/external-reader-review.md` | The Reader AI's response, pasted as-is |
| `reviews/Draft_2/external-editor-review.md` | The Editor AI's response, pasted as-is |

No code changes. No edits to manuscript or bible.

## Verification

1. Confirm both prompts are short enough to fit comfortably above a 111k-word manuscript in the target AI's context window.
2. After pasting each prompt + manuscript into the external AI: confirm the response is a markdown review (not a chat reply or a refusal), and that it does **not** spoil the twist back at you (a sign it stayed in reader-mode).
3. Save each response to the file path above.
4. Skim both reviews for: (a) any items both AIs flag — high-priority signal; (b) Editor findings that need bible cross-checks before accepting; (c) Reader reactions that suggest a structural issue rather than a line-level one.

## Notes / Spoiler Guardrail

- Do **not** add a title, author note, or genre tag at the top of the manuscript before sending it.
- Do **not** paste any bible content, character profile, or plant-list into the external AI.
- If an external AI asks "what genre is this?" or "what should I focus on?" — answer with the prompt above only. Do not elaborate.
