# Copyedit Triage — *The Skybound Wyrm* Draft_5 → Draft_6

Final language pass (Phase A). Combines three layers:
1. **Mechanical proofread** (`tools/copyedit_audit.py`) — punctuation, doubled words, spacing, style consistency.
2. **Agent copyedit sweep** — 40 chapters, each finding adversarially verified against the source (73 agents).
3. **Deterministic spelling normalization** (`tools/normalize_us_spelling.py`) — UK → US, the locked house style.

**Outcome:** the prose is mechanically clean. The real work is (a) one systemic spelling normalization
and (b) six genuine prose corrections. Everything else the sweep "found" was UK/US spelling, which is
handled deterministically below — **not** from the agents' per-chapter verdicts, which were unreliable
(see note).

---

## A. Decisions already locked
- **US English** house spelling.
- **Em-dashes: unchanged.** The 11 "unspaced" em-dashes are all intentional interrupted dialogue
  (`"Madam Esherel—"`, `"when did he—"`, `—Second-class corridor`). Not errors.

## B. Spelling normalization (deterministic, pre-approved by the US-English decision)

`normalize_us_spelling.py` makes **194 replacements** across 38 chapters (ch 16 & 26 already clean).
Top items:

| Replacement | Count | | Replacement | Count |
|---|---|---|---|---|
| harbour → harbor | 70 | | parlour → parlor | 3 |
| grey → gray | 15 | | behaviour → behavior | 3 |
| travelling → traveling | 13 | | favourite → favorite | 3 |
| colour → color | 12 | | recognise → recognize | 3 |
| defence → defense | 10 | | labourers/labour → labor | 6 |
| centre → center | 8 | | + ~25 long-tail words | — |
| acknowledgement → acknowledgment | 7 | | | |
| harbourmaster → harbormaster | 5 | | | |
| flavour → flavor | 5 | | | |

Curated map only — always-`-ise` words (surprise, promise, advise, exercise, disguise…) are **not**
touched; only `recognise` is genuinely UK here. "Gray Quay" (proper noun) is already US and unaffected.

**⚠ One item flagged for your confirmation:** `draught → draft` (×7). Five are **"sleeping draught"**
(a medicinal dose) and one is "the draught from the door." US spells both `draft`, so the conversion is
correct — but "sleeping draught" is an evocative phrase some authors keep on purpose. **Convert, or keep
"draught"?**

## C. Prose corrections (need your approval — these change words, not just spelling)

All six were flagged by the sweep and verified against the source. All are genuine errors.

| # | Ch | Type | Current text | → Fix |
|---|---|---|---|---|
| 1 | 16 | missing article | "Because he was **working mage**, not a noble who dabbled" | "…he was **a** working mage…" |
| 2 | 28 | dropped "not" (inverts meaning) | "tonight without going past what he had **yet earned**" | "…what he had **not** yet earned" (cf. line 89) |
| 3 | 19 | redundant reflexive | "Fell was **self-identifying herself** as a Toll subcontractor" | "Fell was **self-identifying** as…" (cf. lines 19, 23) |
| 4 | 19 | wrong preposition | "looked at the time **of** the gooseneck lamp" | "…the time **on** the gooseneck lamp" (he reads its oil scale) |
| 5 | 33 | usage | "It came in **dryer** than usual" | "**drier**" (comparative adj.; book uses US "dryly") |
| 6 | 04 | US convention | "addressed to **no-one** yet" | "no one" (handled in B) |

## D. Why the agents' spelling verdicts were discarded

Each chapter was copyedited by an isolated agent that could only see its own chapter, so they guessed the
house spelling differently: some assumed US and "kept" `colour→color`; ch 12/14/22/24/25/27/31/33 saw a
local UK majority and *dropped* real UK spellings as "no standard." Net: the agent spelling verdicts are
inconsistent and incomplete. The deterministic normalizer (Section B) supersedes them entirely and catches
every instance. The agents' **non-spelling** findings (Section C) are reliable and verified.

## E. Mechanical audit residue (`_copyedit-mechanical.md`)
7 flagged "doubled words" — all legitimate (`her her` = "gave her her name"; six `had had`
past-perfects). No action.

---

## Apply plan → Draft_6
1. `python tools/normalize_us_spelling.py` (Draft_5 → Draft_6) — Section B.
2. Apply the six Section-C prose edits to the Draft_6 chapter files.
3. Verify: `normalize_us_spelling.py --src Draft_6 --dry-run --audit` shows **no residual UK forms**;
   re-run `flow_audit.py --draft Draft_6` (regression) and `copyedit_audit.py --draft Draft_6`.
4. Reassemble `Draft_6/_full-manuscript.md` (front-matter + 40 chapters + back-matter).
