# Plot Audit Prompt (read-only, whole-manuscript)

Run a **read-only** structural/continuity audit across the full assembled manuscript
(`manuscript/<draft>/_full-manuscript.md`). Do **not** rewrite prose — report findings only.

For `{{BOOK_TITLE}}`, run these seven passes and report findings per pass with
`chapter:line`-style anchors:

1. **Timeline & chronology** — day/time markers, travel durations, "X days later" claims.
2. **Character knowledge** — who knows what, when; flag any knowledge that arrives before it was earned.
3. **Object & detail continuity** — items, wounds, clothing, locations; appearances vs. later references.
4. **Setup ↔ payoff** — every planted detail pays off; every payoff was planted.
5. **Cast consistency** — names, titles, relationships, physical descriptions across chapters.
6. **Stakes & motivation** — each scene's goal/conflict; flag scenes that don't move the throughline.
7. **Genre-mechanics consistency** — if your book has a System/magic/tech ruleset, verify its rules
   never contradict earlier uses. Treat in-world system lines (e.g. `*[System — ...]*`) as an
   intentional, configurable convention, not an error.

**Output:** one Markdown section per pass; each finding gets a severity (blocker / seam / nit) and an
anchor. Adversarially verify each finding against the source before reporting it — drop misreadings.
