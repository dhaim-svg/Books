# The Skybound Wyrm

Cozy LitRPG Murder Mystery — debut novel. Chapter-by-chapter drafting with Claude.

## Structure

```
Murder-Mystery-Novel-Fantasy-LitRPG-Story/
├── bible/          story bible (permanent — characters, formula, twist, style rules)
├── chapters/       per-chapter specs + step-to-chapter mapping
├── state/          running recap + known-facts ledger (updated after each chapter)
├── manuscript/     Draft_1/ (first drafts) · Draft_2/ (post-review rewrites)
├── review/         reviewer-KI briefs + feedback/
└── research/       background research docs
```

See [CLAUDE.md](CLAUDE.md) for the full workflow and book targets.

## How to write the next chapter

Open a new Claude Code chat in this workspace and say: **"Schreib Kapitel N."**

Claude reads `CLAUDE.md` automatically, loads the chapter spec, running recap, and known-facts ledger, then produces the draft and proposes a recap update.
