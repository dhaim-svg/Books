# Review Triage — The Skybound Wyrm, Draft 3

*Generated after Phase 1 review (2 external whole-manuscript reviews + 8 targeted internal audits). This document turns feedback into actionable revision priorities for Draft_4. Read this before starting Phase 3 revisions.*

---

## Phase 1 Inputs

- `review/feedback_Draft_3/editorial_review_draft3.md` — full manuscript, external editor
- `review/feedback_Draft_3/skybound_wyrm_review_draft3.md` — full manuscript, external reader
- `review/feedback_Draft_3/internal-ch-24-arithmetic.md` — Ch.24 passenger-count arithmetic audit
- `review/feedback_Draft_3/internal-pacing-ch-18-29.md` — structural pacing audit, Ch.18–29
- `review/feedback_Draft_3/internal-alias-chain.md` — alias-chain breadcrumb audit, Ch.3/13/14/17
- `review/feedback_Draft_3/internal-supporting-cast-voice.md` — voice fingerprint analysis, Ch.2/6/8/14/17/30/35
- `review/feedback_Draft_3/internal-prose-tics-sweep-draft3.md` — four-tic sweep, full manuscript
- `review/feedback_Draft_3/internal-system-interjection-density.md` — System message density, Ch.2/3/10/12/17/28/40
- `review/feedback_Draft_3/internal-theron-wrong-footing.md` — Theron vulnerability calibration, Ch.5/17/28 + full scan
- `review/feedback_Draft_3/internal-denouement-ch-36-40.md` — denouement beat census, Ch.36–40

---

## Systemic Pattern 1 — Factual Continuity (Tier 1)

One hard factual error in Draft_3. No state-file conflicts.

---

### 1A. Ch.24 Passenger-Count Arithmetic

**The error:** The passage claims "twelve of those accounted for" but the listed examples sum to eleven: 2 (soft alibis) + 1 (textile buyer) + 1 (funeral record) + 6 (cleared on profession/reference) + 1 (Fell) = 11. The stated total is off by one.

**Structural problem underneath it:** The passage then says "that left two columns" — meaning the remainder should be 13 − 12 = 1, not 2. But the chapter addresses two open columns: Fell and Renn. Fell is in the wrong group. She belongs in the "two columns" remainder alongside Renn, not in the "accounted for" total. When Fell is excluded, the examples sum correctly to 11, and the remainder is 13 − 11 = 2, which matches "two columns."

**Evidence:** Confirmed by internal audit via direct quotation from Ch.24. See `internal-ch-24-arithmetic.md`.

**Canonical value:** "eleven of those accounted for" (not twelve); the two open columns are Fell and Renn.

**Fix:** Change "twelve" to "eleven" in the opening count sentence and the echo passage near the chapter's end. Two-word change. [Decision Gate item — see Decision 2]

**State file to update:** None required — the investigation manifest counts locked in `known-facts.md` are not affected by this intermediate count.

---

## Systemic Pattern 2 — Structural Craft (Tier 2)

---

### 2A. Mid-Book Pacing Sag (Ch.18–29)

**Both reviewers independently flag this** — the single highest-confidence issue in the entire round.

**Editor:** "The investigation feels escorted by bureaucracy. Paper trail mode — ledgers, registries, letters, case-book sorting. Feels like a plateau rather than a climb. Chapters 18–29 spend a long time in paper trail mode."

**Reader:** "Pacing dips roughly Chapters 18–22 — reading about harbor registry filings, Vantrel Secured Storage, Kolach, Marbeth slowed momentum."

**Internal audit verdict (see `internal-pacing-ch-18-29.md`):** Complaint is structurally warranted, but the two reviewers aren't pointing at the same problem. Ch.18–22 is the genuine plateau with compressible redundancy. Ch.23–29 carries more forward motion than credited, but it arrives in the same structural furniture across all twelve chapters — creating a perceptual sag even when content is advancing.

**Seven repeating patterns across Ch.18–29:**

| Pattern | Chapters present |
|---|---|
| Case-book-open or case-book-close as chapter beat | All 12 |
| Harbour-through-window atmospheric beat | All 12 |
| Document arrival at the Arms corner table | 11 of 12 |
| Letter arrives / read twice / write reply | Ch.26–29 (4 consecutive) |
| Wrong-frame self-critique | 7 chapters |
| "He read it twice" | 10 of 12 chapters |
| Document-delivery as primary information mechanism | 11 of 12 chapters |

**Load-bearing chapters (cannot compress/cut):** 18, 19, 21, 22, 23, 25, 26, 29

**Compression targets:** Ch.24 (partially redundant with 23), Ch.27 (partially redundant with 26), portions of Ch.28

**Recast candidates** (paperwork beats that could become scene-driven discovery):
- Ch.22: Open Vannic's third meeting in medias res; cut the contract-process re-walk
- Ch.24: Move Renn's Sannholt observation to a Sable-at-breakfast exchange rather than solo table meditation
- Ch.26: Move the Kolach wire to the courthouse, making the Renn discovery a witnessed scene in front of Davren rather than a solo Arms-table moment

**Preserve block for this stretch:** Norra Esherel corridor scene; fish handoff; both Pessel letters; the Roven-goes-still moment; the four working-theory lines; Davren's two questions; TL-9 confirmation; Joren's dock-side warning; the cargo-job-number pivot.

**Reduction estimate:** Compression only ~10–12% (~3,000–3,600 words). Compression + recasting 3–4 document-arrival beats ~15–18% (~4,500–5,400 words).

[Decision Gate item — see Decision 3]

---

### 2B. Denouement Length (Ch.36–40) — Editor/Reader Split

**Editor:** "The denouement extends past peak tension. Chapters 36–40 carry less new information than their length warrants."

**Reader:** "The ending landed perfectly. The quiet desk confrontation and the epilogue Book-2 hook worked."

**Internal audit verdict (see `internal-denouement-ch-36-40.md`):** Both reviewers are correct about different things. The five chapters (12,574 words, 18 information-bearing beats) are surrounded by atmospheric framing beats that the Reader valued and the Editor targets.

**The genuine conflict:** The Editor objects to the prose envelope (fewer words for the same content); the Reader valued the texture the extra words produce. No single beat the Editor wants cut is a beat the Reader explicitly praised — except the general register of the block.

**Compression options available (if authorized):**
1. Trim atmospheric framing across Ch.36–40 (no beats cut, prose shorter)
2. Merge Ch.36/37 geography
3. Compress Ch.38's temporal span
4. Cut one redundant confirmation exchange in Ch.40

Combined yield: ~10–13% reduction (~1,200–1,600 words) without touching any Reader-praised beat. Book-2 hook survives all four options intact.

**Key question for decision gate:** Is the Editor's objection about block length relative to information load (satisfiable by targeted atmospheric compression), or a structural objection to five denouement chapters rather than three (not satisfiable by line-level trimming)? [Decision Gate item — see Decision 4]

---

### 2C. Alias-Chain Breadcrumb Clarity (Ch.3/13/14/17)

**Editor:** "The alias chain (M. Tannin / Petor Vann / Lord Petric Vannic / Joren Aldis) risks reading as a bookkeeping error."

**Internal audit verdict (see `internal-alias-chain.md`):** The complaint is partially warranted, but the problem is narrower than stated. The Vannic/Joren/Petric chain is handled well — Ch.13 is dramatized cleanly, Ch.14 states the full structure in one plain paragraph, Ch.17 gives a crisp magistrate briefing. None of these read as bookkeeping error.

**The actual problem:** M. Tannin only. The name appears once in Ch.3 (sealed first-class manifest amendment), ranks second on Theron's suspect list in Ch.5, and is never mentioned again in any of the four audited chapters. A reader who registered it will carry it as an unresolved thread. M. Tannin is *not* an alias in the Vannic-swap chain — it is a separate passenger. The prose never clarifies this.

**Draft_3 canonical consistency:** The Ch.13 confusion between M. Tannin's Cabin 3 and Petor Vann's Cabin 3-T (the Draft_2 error) has been correctly resolved. No regression.

**Proposed minimal fixes (guardrail-safe):**
1. **Ch.3:** Add one sentence — Theron picks a mundane explanation for the amendment and files it, reducing the sense the narrative is holding M. Tannin in reserve. Proposed: *He picked one at random — the merchant — and filed it there.*
2. **Ch.13:** In the aft-stairwell recalibration passage, add one sentence noting the Tannin amendment is unconnected to anything uncovered. Proposed: *The Tannin amendment was still in the first-class manifest and still none of his business — a sealed change made before boarding, tied to nothing he had uncovered. He moved it to the back of the column.*

Both fixes repair bookkeeping legibility without adding information that helps a reader anticipate the swap. [Decision Gate item — see Decision 9]

---

### 2D. False-Identity Exposition Delivery (Ch.14/17)

**Editor:** "The false-identity/forced-betrothal layer arrives as a big explanatory block and becomes a 'second premise' competing with the murder plot."

**Internal audit verdict:** The alias-chain audit found Ch.14 and Ch.17 are legible and not structurally broken. The two-layer structure (murder investigation + identity swap + forced-betrothal politics) is by design in the bible.

**Assessment:** The concern is about delivery mode (info-dump vs. dramatized), not about the premise existing. Worth checking whether the Ch.14 exposition block could be fragmented across the scene rather than front-loaded. Light touch only. [Decision Gate item — see Decision 10]

---

### 2E. Theron/Sable Intimacy Bridge (Ch.31–35)

**Editor:** "The Theron/Sable shift to 'functionally intimate' happens between scenes; partnership-to-finishing-each-other's-moves feels compressed."

**Assessment:** This complaint is not directly validated or refuted by the internal audits (no dedicated audit). The internal-supporting-cast-voice audit identified Ch.30 and Ch.35 as relevant chapters but focused on dialogue differentiation. Two options:
- Add 1–2 on-page beats in Ch.31–34 showing the intimacy developing
- Accept the current compressed presentation (Reader did not flag this)

[Decision Gate item — see Decision 11]

---

## Systemic Pattern 3 — Character Coherence (Tier 3)

---

### 3A. Supporting-Cast Voice Differentiation

**Editor:** "Supporting cast (Calden, Vellaine, Esherel, Sable, Davren) speak in the same compressed register. Only Wisp differs."

**Internal audit verdict (see `internal-supporting-cast-voice.md`):** Partially warranted. Homogeneity is real for Calden and Vellaine specifically — in adjacent chapters (Ch.5/6) their cadence is nearly identical. Complaint is overstated for Esherel (already the most developed voice architecture) and Halsa (most distinctive voice in the book).

**Priority ranking (from audit):**

1. **Vellaine** — Highest priority. Ch.5 testimony matches Calden's cadence. The Ch.2 System notification (she has read Theron's reconstruction paper) has never been activated in dialogue — one oblique reference to the paper's argument would be more differentiating than any rhythm change.
2. **Calden** — Second priority. Has a good structural marker (paired-negative pattern) but it collapses in short exchanges. The profile's "opens up to Sable differently" has never been rendered in dialogue.
3. **Davren** — Low-cost fix. Interchangeable with the Halverstow magistrate in Ch.17. One warm-under-procedure line or one direct quoted sentence from his writ in Ch.35 would suffice.

**Leave as-is:** Esherel, Halsa (most distinctive), Wisp (editor's own reference point), Sable (voice differentiation via dialogue/action only — POV lock maintained).

[Decision Gate item — see Decision 8]

---

### 3B. Theron's Vulnerability Calibration

**Editor:** "Theron is almost never visibly wrong-footed — he reads past the learning curve."
**Reader:** *Praised* the Esherel red herring — "I let myself get dragged right along with his 'clean page.'"

**Internal audit verdict (see `internal-theron-wrong-footing.md`):** The Editor and Reader are not contradicting each other — they are responding to different mechanisms. The Reader praised *structural* wrong-footedness (the entire Esherel arc collapses at Ch.13). The Editor objects to a *texture* problem — few moment-to-moment visible stumbles.

**Close analysis:**
- **Ch.5:** Editor's complaint is not well-aimed here. Ch.5's confident tone is load-bearing setup for Ch.13's collapse.
- **Ch.17:** Editor's complaint has most warrant here. The magistrate scene gives Theron professional validation with no friction, no challenge, no stumble.
- **Ch.28:** Editor's complaint not well-aimed. Chapter is titled *The Wrong Kind of Certainty*; Theron admits "I don't have the method" to a magistrate; System explicitly names the problem.

**The genuine gap:** Ch.17–22 (six chapters of administrative grinding post-Halverstow landing). Theron makes only correct incremental progress with no wrong inferences and no structural wrong-footedness building toward a collapse.

**Seeding opportunities (if authorized):**
- **Opportunity A:** Brief Roven misread in Ch.19–20 — lowest disruption
- **Opportunity B:** Fell-before-Renn misread in Ch.24 — supports Ch.24 recast
- **Opportunity C:** Fell-hypothesis misfire in Ch.29 — highest visibility

**Preserve block:** Ch.13 Vannic reveal prose; Ch.16 "small talk" recognition; Ch.28 "I don't have the method" admission; Ch.23 self-critique page.

[Decision Gate item — see Decision 5]

---

## Systemic Pattern 4 — Prose Tics (Tier 4)

**Internal audit verdict (see `internal-prose-tics-sweep-draft3.md`):**

**Prior-round tic status:**
- "Someone who" formula: reduced 37→27; no longer a priority
- Filing-verb crutches: mixed — `catalogued` removed but `filed`/`registered` remain elevated; `noted` has joined them
- Passive landscape: fully resolved ✓

**This round's four tics — actual counts and priority ranking:**

---

### Tic 1 — Cognitive Verbs (Priority 3 of 4)

**Total metaphorical instances:** ~118–122 (`filed` 49, `noted` 50, `registered` 52, `categorized` 2 = 153 raw)

**Top-density chapters:** Ch.5, 1, 4, 6, 7 (8–10 each)

**Worst-offender sentences (immediate fix regardless of Decision):**
- Ch.6: "He filed the lounge. He filed the chin..." — the Draft_2 violation survived unchanged
- Ch.4: Triple-`noted` with self-referential nesting

**Recommendation:** Fix the two surviving worst-offender sentences immediately. Light pass on Chs.1, 4, 5, 6, 7, 10 for density reduction. Do not strip uniformly.

---

### Tic 2 — "The Kind of…" Formula (Priority 4 of 4)

**Total count:** 65 instances (~1.6/chapter)

**Top-density chapters:** Ch.5, 15, 29

**Assessment:** This is both a tic and a voice marker. The device is valid when applied to character behavior; it is deflective when applied to soup, sentences, and sleep (Ch.29 has two consecutive uses of the latter type).

Both reviewers disagreed on this — the Reader praised the rhythm. Light sweep of Ch.5, 15, 29 only.

---

### Tic 3 — "Said" Tag Monotony (Priority 1 of 4 — HIGHEST)

**Total "said" tags:** 746 (72% of all tracked attribution)

**Chapters with 80%+ "said" rate:** 16 chapters

| Priority Chapter | Said-rate | Notes |
|---|---|---|
| Ch.22 | ~80% | 41 said tags; testimony-heavy with auditory flatness |
| Ch.13 | ~80% | Major confrontation scene — most visible impact |
| Ch.14 | ~80% | Exposition-heavy; tag monotony reinforces info-dump feel |
| Ch.20 | ~80% | Registry-filing interviews |
| Ch.31 | ~80% | Partnership scenes |
| Ch.33 | ~80% | |

**Fix method:** Beat substitution (action beats replacing tags in dialogue), NOT synonym replacement (whispered/declared/intoned = purple prose). A speech followed by the speaker picking up a coffee cup is better than "said" replaced by "admitted."

---

### Tic 4 — Tonal Modifier Overuse (Priority 2 of 4)

**Total counts:** `small` 314, `quiet` 67, `careful` 60, `slight` 18 = 459 combined

**Concentration problem in Ch.11–12:**
- Ch.11: 26× `small` (~1 per 96 words); "small clean X" formula repeats 4× within 400 words
- Ch.12: 24× `small`; similar density
- Ch.32: 7× `quiet` (highest per-chapter `quiet` count)

**Register problem Ch.7–12:** ~25,000 words sustaining the same tonal band without modulation.

**Recommendation:** Reduce `small` in Ch.11–12 to ~14–15 each; audit `quiet` and `careful` in Ch.7–10 and Ch.32. The goal is tonal variation within a chapter, not eliminating the modifiers globally.

---

## Systemic Pattern 5 — System Device (Tier 5)

**Internal audit verdict (see `internal-system-interjection-density.md`):**

The convention (sparse, earned, no interpretation) confirmed from `bible/standing-style.md`. The Ch.35 climax payoff message ("The question has been asked...") is the calibration standard — its power depends on contrast with sparser mid-book usage.

**Net recommendation: cut 4, trim 2, preserve 5.**

| Chapter | Message | Action | Reason |
|---|---|---|---|
| Ch.2 | Manifest amendment | **Preserve** | Essential mystery seed, correct System use |
| Ch.2 | No active queries + countdown | **Trim** countdown figure only | Dry irony earns the message; countdown is gratuitous |
| Ch.3 | Off duty. Sleep well. | **Preserve** | Model use — confirms decision, earns Theron's smile |
| Ch.10 | The cleanest page… (aphorism) | **Cut** | Doubles a beat Vellaine and Sable named more memorably |
| Ch.10 | Countdown | **Cut** | First of a repetitive pair; Ch.12's serves the same function better |
| Ch.12 | A column closes when… (aphorism) | **Cut** | Captions what the prose image "The underline took the slate seriously" already delivered |
| Ch.12 | Countdown | **Preserve** (trim to *Quest active*, no figures) | Keep as the sole countdown beat |
| Ch.17 | "The case is not tidier than it was. It is more accurate." | **Cut** | Announces the chapter's thematic arc; this is the worst offender |
| Ch.28 | Column update | **Trim** — cut final editorial clause only | Column-update function is legitimate at structural hinge; the final "uniquely positioned" commentary is Theron repeating himself |
| Ch.40 | Note: the corner of the slip. | **Preserve** | Five words, pure confirmation — the calibration standard |

[Decision Gate item — see Decision 7]

---

## Preserve Block

**These items surfaced in the Phase 1 inputs but must not be altered in Draft_4 regardless of other decisions.**

- **The Ch.13 swap reveal** — the moment Theron names Vannic aloud and Vannic names Joren; the prose sequence of this revelation is load-bearing and correctly calibrated
- **The Esherel arc** (Ch.5–13) — the Reader explicitly praised this as the structural wrong-footedness working; do not flatten Theron's Ch.5 confidence in service of moment-to-moment stumbles
- **Ch.16 "small talk" recognition** — load-bearing wrong-footing moment (from internal-theron-wrong-footing.md)
- **Ch.23 self-critique page** — load-bearing wrong-footing moment
- **Ch.28 "I don't have the method" admission** — the Editor's complaint about Ch.28 is not warranted; this is a strong wrong-footing chapter
- **Halsa Ch.35 speech** — the most distinctive supporting voice; do not touch
- **The final desk confrontation** — Reader praised it; bible specifies restrained aftermath
- **Ch.35 System message** ("The question has been asked...") — the climax payoff; never altered
- **Book-2 hook in Pessel's bundle** — Reader praised; survives all compression options
- **Wooden-fish motif** — planted detail; bible-locked
- **Sable's interiority** — NEVER accessed; all voice fixes come through dialogue and action only
- **The five planted details** (calluses, accent slip, carved fish, kindnesses, niece-softness) — textural, not investigative; pass without underlining

---

## Continuity Issues Sub-Table

| Chapter | Issue | Old value (Draft_3) | Canonical value (Draft_4) | Fix action |
|---|---|---|---|---|
| Ch.24 | Passenger-count arithmetic | "twelve of those accounted for" | "eleven of those accounted for"; Fell belongs in remainder | Change "twelve" to "eleven" in count sentence and echo; move Fell to remainder column |
| Ch.3 | M. Tannin loose thread | No resolution after suspect-list appearance | Theron files a mundane explanation; thread closed | Add one sentence [Conditional: Decision 9] |
| Ch.13 | M. Tannin loose thread (Part 2) | Amendment never revisited post-reveal | One sentence noting it is unconnected | Add one sentence [Conditional: Decision 9] |

---

## Per-Chapter Must-Fix List

*[Conditional] items require the corresponding Decision Gate authorization before execution.*

| Chapter | Fix items |
|---|---|
| **Ch.1** | ① Tic 1 density reduction — Chs. 1/4/5/6/7/10 light pass on cognitive verbs [Conditional: Decision 12] |
| **Ch.3** | ① M. Tannin closure sentence [Conditional: Decision 9] |
| **Ch.4** | ① Fix triple-`noted` worst-offender sentence (immediate; no Decision required) |
| **Ch.5** | ① Tic 1 density reduction [Conditional: Decision 12] ② Tic 2 light pass ("the kind of…") [Conditional: Decision 12] |
| **Ch.6** | ① Fix surviving "He filed the lounge…" sentence (immediate; no Decision required) ② Tic 1 density reduction [Conditional: Decision 12] |
| **Ch.7** | ① Tic 1 density reduction [Conditional: Decision 12] ② Tic 4 tonal modifier audit (`small`/`quiet`) [Conditional: Decision 12] |
| **Ch.8** | ① Tic 3 said-tag pass (low priority) [Conditional: Decision 12] |
| **Ch.10** | ① Tic 1 density reduction [Conditional: Decision 12] ② Cut System aphorism message + countdown [Conditional: Decision 7] |
| **Ch.11** | ① Tic 4 — reduce `small` to ~14–15 instances [Conditional: Decision 12] |
| **Ch.12** | ① Tic 4 — reduce `small` to ~14–15 instances [Conditional: Decision 12] ② Cut System aphorism; trim countdown to *Quest active* [Conditional: Decision 7] |
| **Ch.13** | ① Tic 3 said-tag pass (highest-impact scene) [Conditional: Decision 12] ② M. Tannin note in recalibration passage [Conditional: Decision 9] |
| **Ch.14** | ① Tic 3 said-tag pass [Conditional: Decision 12] ② False-identity exposition re-dramatize option [Conditional: Decision 10] ③ Vellaine voice — thesis-reference line [Conditional: Decision 8] |
| **Ch.15** | ① Tic 2 light pass [Conditional: Decision 12] |
| **Ch.17** | ① Cut System thematic-caption message ("The case is not tidier…") [Conditional: Decision 7] ② Theron wrong-footing: is this the chapter to seed friction? [Conditional: Decision 5] |
| **Ch.18** | ① [Conditional: Decision 3] Pacing sag structural authorization |
| **Ch.19** | ① [Conditional: Decision 3] Pacing sag / Theron Roven-misread seed opportunity A [Conditional: Decision 5] |
| **Ch.20** | ① Tic 3 said-tag pass (registry-filing interviews) [Conditional: Decision 12] ② [Conditional: Decision 3] Pacing sag |
| **Ch.21** | ① [Conditional: Decision 3] Pacing sag (load-bearing; likely compression only) |
| **Ch.22** | ① Tic 3 said-tag pass (highest-density chapter; 41 instances) [Conditional: Decision 12] ② [Conditional: Decision 3] Pacing sag — open Vannic meeting in medias res recast |
| **Ch.23** | ① [Conditional: Decision 3] Pacing sag — reduce harbour-window and document-delivery density; Esherel corridor scene preserved |
| **Ch.24** | ① **Ch.24 arithmetic fix — change "twelve" to "eleven" in two places** (Tier 1; no Decision required) ② [Conditional: Decision 3] Pacing sag — compression (redundant with Ch.23) ③ Fell-before-Renn misread seed opportunity B [Conditional: Decision 5] |
| **Ch.25** | ① [Conditional: Decision 3] Pacing sag (load-bearing; likely compression only) |
| **Ch.26** | ① [Conditional: Decision 3] Pacing sag — Kolach wire to courthouse recast |
| **Ch.27** | ① [Conditional: Decision 3] Pacing sag — compression (partially redundant with Ch.26) |
| **Ch.28** | ① Trim System column-update: cut final "uniquely positioned" clause [Conditional: Decision 7] ② [Conditional: Decision 3] Pacing sag — flanking sequence compression |
| **Ch.29** | ① [Conditional: Decision 3] Pacing sag — letter-arrives-read-twice-write-reply pattern break ② Fell-hypothesis misfire seed opportunity C [Conditional: Decision 5] ③ Tic 2 light pass [Conditional: Decision 12] |
| **Ch.30** | ① Calden voice — rendered Sable-Calden exchange [Conditional: Decision 8] |
| **Ch.31** | ① Tic 3 said-tag pass [Conditional: Decision 12] ② Sable/Theron intimacy bridge — on-page beat option [Conditional: Decision 11] |
| **Ch.32** | ① Tic 4 — audit `quiet` (7 instances, highest per-chapter count) [Conditional: Decision 12] ② Sable/Theron intimacy bridge [Conditional: Decision 11] |
| **Ch.33** | ① Tic 3 said-tag pass [Conditional: Decision 12] ③ Sable/Theron intimacy bridge [Conditional: Decision 11] |
| **Ch.34** | ① Sable/Theron intimacy bridge [Conditional: Decision 11] |
| **Ch.35** | ① Davren voice — warm-under-procedure line or direct quote from his writ [Conditional: Decision 8] |
| **Ch.36–40** | ① [Conditional: Decision 4] Denouement atmospheric compression options |

---

## What Does Not Need Fixing

**These items surfaced in Phase 1 inputs but are NOT revision targets for Draft_4.**

- **The Vannic/Petric/Joren alias chain** (Ch.13/14/17): the chain is legible and dramatized correctly. Only M. Tannin needs addressing (see 2C above). Do not add breadcrumbs to the main swap chain.
- **Theron's confidence in Ch.5**: his smooth tone in Ch.5 is the setup for Ch.13's collapse. Do not add visible stumbles here — it would spoil the structural wrong-footedness the Reader praised.
- **Ch.28 wrong-footing**: the Editor's complaint is not aimed at Ch.28. The chapter already has "I don't have the method" and a System message naming the problem. Do not treat this as a vulnerability-gap chapter.
- **Esherel's voice** (any chapter): Esherel already has the most developed voice architecture in the supporting cast. The Editor's "same register" complaint does not apply to her. No action.
- **Halsa's voice** (any chapter): the most distinctive voice in the book. The repetition-with-variation structure achieves its effect precisely. No action.
- **Wisp's voice**: the Editor's own reference point for what differentiated voice looks like. No action.
- **Sable's interiority**: the Editor's "same compressed register" complaint about Sable can only be addressed through her dialogue and actions — not through POV access. The POV lock is a bible-level decision.
- **Stylistic repetition as a voice-strip**: the Editor flagged "The page was the page" / "He inclined his half-inch" patterns; the Reader called it a signature that "works incredibly well to establish tone." This is a Decision Gate item — but even if a light sweep is authorized, it cannot be a refactor.
- **The existing System device climax payoff** (Ch.35): Reader praised it explicitly. The thin-out of mid-book messages (Tier 5) strengthens the contrast; it does not alter the payoff chapter.
- **The Book-2 hook**: Reader praised; survives all compression scenarios in the denouement.
- **Vannic as comic-relief figure**: Do not recast him as a villain or add meaningful punishment to his arc. His humbling is proportionate per the bible.
- **The Act 2 reveal location**: Do not move it. The social-plot inversion in Act 3 is by design.
- **Any addition of action-climax beats**: The bible specifies a reasoned reveal. Reader confirms the quiet desk confrontation landed. This is not a solvable complaint in Draft_4.

---

## Triage Decision Gate

*Complete all decisions before Phase 3 revision begins. Structural changes and spec amendments cannot be executed until these are confirmed.*

---

**Decision 1: Restructuring scope**

Which chapters are authorized for structural changes (scene insertions, scene type recasts, merges, not just line edits)?

Recommendation: Authorize structural change in (a) any pacing-sag chapter per Decision 3 — likely Ch.22, 24, 26, 27, 28; (b) Ch.14/17 if Decision 10 authorizes false-identity re-dramatization; (c) Ch.31–34 if Decision 11 authorizes Sable/Theron intimacy bridge beats; (d) Ch.19 or Ch.24 or Ch.29 if Decision 5 authorizes wrong-footing seeds. All other chapters: line-edit only.

Spec amendments required before Phase 3 begins for any chapter authorized for structural change.

**Author's decision:** I'll go with your recommendation

---

**Decision 2: Ch.24 arithmetic fix**

Canonical fix: change "twelve" to "eleven" in the count sentence and the echo passage near the chapter's end. Move Fell to the "two columns" remainder. Two-word change in two places.

Option A: Change "twelve" to "eleven" in both locations (minimum change; no material added)
Option B: Rewrite the paragraph to make the count explicit by listing Fell separately from the start

Recommendation: Option A. No new prose; closes the error cleanly.

**Author's decision:** Option A

---

**Decision 3: Pacing sag Ch.18–29 — scope and method**

Both reviewers converge on this. Compression and scene recasting are both authorized in the plan.

(a) Full authorization: compress AND recast the three identified candidate chapters (Ch.22, Ch.24, Ch.26). Target ~15–18% block reduction.
(b) Compression only: cut the most repetitive beats in Ch.24, 27, 28. Target ~10–12% block reduction. No scene-type changes.
(c) Targeted authorization: authorize specific chapters only from (a)'s list.
(d) No structural action: line-edit the block only.

Recommendation: (a) full authorization. The joint reviewer confirmation makes this the highest-confidence fix in the round; the recast candidates have clear in-narrative paths for dramatization (characters are present who can credibly deliver the information in person).

**Author's decision:** Option A

---

**Decision 4: Denouement length (Ch.36–40)** *(Editor/Reader split)*

Editor: wants cuts. Reader: praised the ending as-is.

(a) Targeted atmospheric compression — trim prose envelope across Ch.36–40 (~10–13% reduction, ~1,200–1,600 words) without cutting any information-bearing beats. Book-2 hook survives. No Reader-praised beats removed.
(b) No action — accept the Reader's reading; Editor's objection is taste-level against the tonal register that makes the ending work.

The core question: is the Editor's complaint about the block's length relative to information load (satisfiable by option a), or a structural objection to five chapters of denouement (not satisfiable by any line-level change)?

Recommendation: If the Editor's objection is about information density, option (a) satisfies it. If it is structural, (b) is more honest — forced compression of the atmospheric framing would remove precisely what the Reader praised.

**Author's decision:** Option B

---

**Decision 5: Theron wrong-footing** *(Editor/Reader split)*

Editor: Theron too smooth overall. Reader: praised Esherel arc (structural wrong-footedness). Internal audit: the genuine gap is Ch.17–22.

(a) Seed 1–2 visible misreads: authorize Opportunity A (Roven misread, Ch.19–20) and/or Opportunity B (Fell-before-Renn misread, Ch.24). These are the lowest-disruption options.
(b) Seed Opportunity C also (Fell-hypothesis, Ch.29) — higher visibility, more risk.
(c) No new misreads — the Esherel arc is sufficient; accept the Reader's reading. The Ch.17 magistrate scene could have friction added without a full misread (one line of institutional resistance).
(d) Add minor friction to Ch.17 magistrate scene only, without full misread.

Recommendation: (a) or (d). The gap in Ch.17–22 is real, but seeding too many misreads risks undermining the systematic-deduction competence that gives Theron's eventual solve its weight. A single short-lived misread in Ch.19–20 plus one friction beat in Ch.17 would address the Editor's core objection without the Reader noticing a change.

**Author's decision:** Option A

---

**Decision 6: Stylistic repetition** *(Editor/Reader split)*

Editor: "The page was the page," "He inclined his half-inch" — tic liability. Reader: "Works incredibly well to establish tone."

(a) Light sweep of highest-frequency instances only — not a refactor, just capping any single chapter where the pattern appears 3+ times in proximity.
(b) Preserve as-is — Reader endorsed it; this is a signature, not a flaw.

Recommendation: (b). The Reader's endorsement is specific and the Editor's complaint is a taste-level preference. Touching this risks stripping a voice element that is working.

**Author's decision:** Option B

---

**Decision 7: System interjection density** *(Editor/Reader split on overall device; clear audit findings on specific messages)*

Recommendation: Authorize cuts as per Tier 5 table — cut Ch.10 aphorism + countdown, Ch.12 aphorism, Ch.17 thematic-caption; trim Ch.2 countdown figure and Ch.28 editorial clause; preserve all others. This is supported by internal audit evidence (each cut is justified individually) and by the structural logic that the thin-out strengthens the Ch.35 climax contrast.

(a) Authorize all 4 cuts + 2 trims as per table
(b) Authorize cuts only (Ch.10/12/17 aphorism removal), leave countdowns untouched
(c) No action

Recommendation: (a).

**Author's decision:** Option A

---

**Decision 8: Supporting-cast voice differentiation**

(a) Priority three only: Vellaine (one thesis-reference line + embedded-evaluation habit), Calden (one rendered Sable-Calden exchange), Davren (one warm-under-procedure line). Leave Esherel, Halsa, Wisp, Sable unchanged.
(b) Full per-character pass across all flagged chapters.
(c) No action — Editor's complaint was overstated; Reader did not flag this.

Recommendation: (a). The three priority fixes are low-intervention and high-leverage. A full pass risks introducing inconsistencies across the manuscript.

**Author's decision:** Option A

---

**Decision 9: Alias-chain breadcrumbs (M. Tannin only)**

Recommendation: Authorize the two specific minimal fixes (one sentence in Ch.3 closing the Tannin thread, one sentence in Ch.13 noting the amendment is unconnected). Both are guardrail-verified — they cannot help a reader anticipate the swap.

(a) Authorize both sentences as proposed
(b) Ch.3 only
(c) Ch.13 only
(d) No action — the M. Tannin thread may read as ambient world-texture, not an unresolved loose end

Recommendation: (a). The internal audit confirms the Vannic chain is fine; only M. Tannin needs addressing.

**Author's decision:** Option A

---

**Decision 10: False-identity exposition delivery (Ch.14/17)**

(a) Re-dramatize the Ch.14 exposition block — fragment it across the scene so information arrives through action rather than front-loaded block
(b) Accept as-is — the alias-chain audit did not identify a structural problem with these chapters

Recommendation: (b). The alias-chain audit found Ch.14/17 legible. This is a "nice to have" polish, not a structural fix. If Phase 3 capacity is limited, skip it.

**Author's decision:** Option B

---

**Decision 11: Sable/Theron intimacy bridge (Ch.31–35)**

(a) Add 1–2 on-page beats across Ch.31–34 showing the working-intimacy developing (dialogue-only; Sable POV lock maintained)
(b) Accept as-is — Reader did not flag this; Editor's observation is about craft density between scenes

Recommendation: (b) unless the author feels the intimacy transition reads as jarring on re-read. This is not validated by either audit or Reader feedback.

**Author's decision:** Option B

---

**Decision 12: Prose tic scope**

Recommendation per tic:
- **Tic 1 (cognitive verbs):** Fix the two worst-offender sentences immediately (Ch.4, Ch.6) regardless of decision. Light pass on Chs.1, 4, 5, 6, 7, 10 for density reduction.
- **Tic 2 ("the kind of…"):** Light sweep of Ch.5, 15, 29 only.
- **Tic 3 (said-tag monotony):** Priority pass on Chs.13, 14, 20, 22, 31, 33 via beat substitution.
- **Tic 4 (tonal modifiers):** Reduce `small` in Ch.11–12 to ~14–15 each; audit `quiet`/`careful` in Ch.7–10 and Ch.32.

(a) Authorize all four tic passes at recommended scope
(b) Tics 1 and 3 only (the two most objectively grounded complaints)
(c) Tic 3 only (said-tag monotony is the highest priority)
(d) No tic action

Recommendation: (a) — all four tics at recommended scope. The scopes are conservative; none require systematic stripping.

**Author's decision:** Option A

---

**Decision 13: State-file updates before Phase 3**

`state/known-facts.md` should be updated with any new canonical values before chapter revision begins.

Proposed additions:
- Ch.24 canonical passenger count: "eleven of those accounted for, two columns (Fell and Renn) remaining" (from Decision 2)
- M. Tannin closed thread (from Decision 9, if authorized)

**Author confirms:** yes

---

**Decision 14: Bible updates before Phase 3**

No bible updates required for Draft_4. The swap mechanics, reveal structure, and all locked decisions remain unchanged. The CLAUDE.md line 30 stale reference ("Post-review rewrites go to `manuscript/Draft_2/`") should be updated to reflect the current draft convention, but this is a housekeeping item, not a bible change.

**Author confirms:** yes

---

**Decision 15: Chapter spec amendments before Phase 3**

Required before Phase 3 begins for each chapter authorized for structural change in Decision 1.

Likely spec amendments needed (final list set by Decision 1):
- Any Ch.18–29 chapter authorized for pacing recast (Ch.22, 24, 26 likely)
- Ch.19 or Ch.24 if wrong-footing seed authorized (Decision 5)
- Ch.14/17 if false-identity re-dramatization authorized (Decision 10)
- Ch.31–34 if intimacy bridge beats authorized (Decision 11)

Constrained edits (no spec amendment required): Ch.4/6 worst-offender tic fixes; Ch.24 arithmetic fix; Ch.3/13 M. Tannin sentences; all tic-reduction passes in line-edit-only chapters.

**Author confirms:** yes

---

## Decisions Appendix

Decisions recorded: 2026-05-24 after author walk-through of all 15 gate items.

**Decision 1 — Restructuring scope:**
Structural changes authorized in: Ch.19 (Roven misread seed, per Decision 5); Ch.22 (pacing recast — open Vannic meeting in medias res); Ch.24 (pacing compression + arithmetic fix + Fell misread seed); Ch.26 (pacing recast — Kolach wire to courthouse); Ch.27 (pacing compression — reduce Scene 1 framing further per Draft_3 amendment); Ch.28 (flanking sequence compression — per Draft_3 amendment + System trim per Decision 7).
All other chapters: line-edit only.
Spec amendments required before Phase 3 for: Ch.19, Ch.22, Ch.24, Ch.26. Ch.27 and Ch.28 already have Draft_3 amendments; Draft_4 amendments will be appended.

**Decision 2 — Ch.24 arithmetic fix:**
Option A — change "twelve" to "eleven" in count sentence and echo passage. Two-word change. No new prose.

**Decision 3 — Pacing sag Ch.18–29:**
Option A — full authorization: compress AND recast. Authorized chapters and methods:
- Ch.22: open Vannic meeting in medias res; cut contract-process re-walk
- Ch.24: additional compression (no harbour-window or case-book ritual in Scene 1 opener) + arithmetic fix + misread seed
- Ch.26: Kolach wire delivered at magistrate's office (Davren present), not at the Arms
- Ch.27: further framing reduction beyond Draft_3 amendment (target: reduce "He read it twice" pattern; no case-book open/close ritual except once at chapter end)
- Ch.28: per existing Draft_3 amendment (flanking compression) + System trim

**Decision 4 — Denouement length (Ch.36–40):**
Option B — no action. Accept the Reader's reading. The ending stays as-is.

**Decision 5 — Theron wrong-footing:**
Option A — seed Opportunity A (Roven misread, Ch.19) and Opportunity B (Fell-before-Renn misread, Ch.24).
- Ch.19: Theron briefly interprets Vannic's "Roven will be aware of the passage" as Roven being present on the gondola; Vannic corrects him (Roven knew of the run but wasn't a passenger). Short-lived, self-correcting.
- Ch.24: In Scene 1 re-examination, Theron ranks Fell above Renn as the more likely re-entry candidate (Fell has the cleaner Toll connection); Renn is noted as the "quieter name" that keeps sliding back in the column. He's in the right pool, wrong person ranked first. The misread resolves over Ch.24–26 as the Kolach result arrives.

**Decision 6 — Stylistic repetition:**
Option B — preserve as-is. Reader endorsed the signature; no sweep.

**Decision 7 — System interjection density:**
Option A — all 4 cuts + 2 trims as per Tier 5 table:
- Ch.10: cut both messages (aphorism + countdown)
- Ch.12: cut aphorism; trim countdown to *Quest active* (no figures)
- Ch.17: cut thematic-caption message ("The case is not tidier than it was. It is more accurate.")
- Ch.2: trim countdown figure only (keep dry irony line)
- Ch.28: trim column-update — cut final "uniquely positioned" editorial clause only

**Decision 8 — Supporting-cast voice:**
Option A — priority three only: Vellaine (Ch.14 — one thesis-reference line + embedded-evaluation habit); Calden (Ch.30 — one rendered Sable-Calden exchange); Davren (Ch.35 — one warm-under-procedure line or direct quote from his writ).

**Decision 9 — Alias-chain breadcrumbs:**
Option A — both M. Tannin sentences:
- Ch.3: add one sentence where Theron picks a mundane explanation for the amendment and files it there (proposed: *He picked one at random — the merchant — and filed it there.*)
- Ch.13: add one sentence in aft-stairwell recalibration passage noting the Tannin amendment is unconnected (proposed: *The Tannin amendment was still in the first-class manifest and still none of his business — a sealed change made before boarding, tied to nothing he had uncovered. He moved it to the back of the column.*)

**Decision 10 — False-identity exposition (Ch.14/17):**
Option B — accept as-is. Alias-chain audit confirmed these chapters are legible.

**Decision 11 — Sable/Theron intimacy bridge:**
Option B — accept as-is. Not validated by audits or Reader feedback.

**Decision 12 — Prose tic scope:**
Option A — all four tics at recommended scope:
- Tic 1 (cognitive verbs): fix Ch.4 triple-noted and Ch.6 "filed the lounge" immediately; light pass Chs.1, 4, 5, 6, 7, 10
- Tic 2 ("the kind of…"): light sweep Chs.5, 15, 29 only
- Tic 3 (said-tag monotony): priority pass Chs.13, 14, 20, 22, 31, 33 via beat substitution
- Tic 4 (tonal modifiers): reduce `small` in Chs.11–12 to ~14–15 each; audit `quiet`/`careful` in Chs.7–10 and Ch.32

**Decision 13 — State-file updates:**
Confirmed. `state/known-facts.md` updated with Ch.24 canonical count and M. Tannin closed-thread row before Phase 3 begins. Done 2026-05-24.

**Decision 14 — Bible updates:**
Confirmed. No bible file changes. `CLAUDE.md` line 30 stale reference updated to reflect `manuscript/Draft_4/`. Done 2026-05-24.

**Decision 15 — Spec amendments:**
Confirmed. Spec amendments to be written for Ch.19, Ch.22, Ch.24, Ch.26 before Phase 3 begins. Ch.27 and Ch.28 receive appended Draft_4 sections to their existing Draft_3 amendments. Constrained edits (no spec required): all tic-reduction chapters, Ch.3/13 M. Tannin sentences, Ch.24 arithmetic fix.
