# Review Triage — The Skybound Wyrm, Draft 2

*Generated after Phase 1 review (2 external whole-manuscript reviews + targeted internal supplements). This document turns feedback into actionable revision priorities for Draft_3. Read this before starting Phase 3 revisions.*

---

## Phase 1 Inputs

- `review/feedback_Draft_2/external-editor-review.md` — full manuscript, external editor (Gemini)
- `review/feedback_Draft_2/external-reader-review.md` — full manuscript, external reader (ChatGPT)
- `review/feedback_Draft_2/_external-prompt-preparation.md` — prompt scaffold used for both external reviews
- `review/feedback_Draft_2/internal-ch-01.md` — pronoun, flight duration, pacing audit, Ch. 1
- `review/feedback_Draft_2/internal-ch-02.md` — pronoun, flight duration, manifest counts audit, Ch. 2
- `review/feedback_Draft_2/internal-ch-03.md` — pronoun, manifest, M. Tannin cabin class audit, Ch. 3
- `review/feedback_Draft_2/internal-ch-04.md` — locked-room mechanism audit, Ch. 4
- `review/feedback_Draft_2/internal-sable-onramp.md` — Sable scene-by-scene progression, Ch. 1–10
- `review/feedback_Draft_2/internal-vannic-arc.md` — Vannic voice registers and security logic, Ch. 1–22
- `review/feedback_Draft_2/internal-ch-23-31-block.md` — pacing and compression analysis, Ch. 23–31
- `review/feedback_Draft_2/internal-prose-tics-sweep.md` — three prose tic sweeps, full manuscript

---

## Systemic Pattern 1 — Factual Continuity (Tier 1)

These are hard errors. Each has a proposed canonical value and a state-file update required before Phase 3 begins.

---

### 1A. Wisp's Pronoun

**The contradiction:** Wisp is introduced in Ch. 1 with female pronouns throughout. Ch. 2 switches to male pronouns for six consecutive instances and reverts to female in Ch. 3 without explanation.

**Chapter-by-chapter evidence (internal audit):**

- Ch. 1: "She'd positioned herself between the brush strokes so Gravel could see every motion before it landed." / "She said it with the easy confidence of someone who'd delivered this reassurance two hundred times and found it to be consistently true." — **she/her throughout, two confirmed instances.**
- Ch. 2: "Wisp tucked the gauge under his arm." / "He said it with complete seriousness." / "He keeps it at the dining-room end in the mornings." — **he/his throughout, six confirmed instances.**
- Ch. 3: "Wisp was inside, sitting on an upended crate with a coil of harness chain in her lap..." / "She pulled the door wider with her shoulder." — **she/her throughout, four confirmed instances.**

**Proposed canonical value:** she/her. Ch. 1 and Ch. 3 agree; Ch. 2 is the outlier.

**Fix:** Change all six male-pronoun instances in Ch. 2 to female. Scan Draft_3 for any other chapter that inadvertently uses male pronouns for Wisp before treating Ch. 2 as resolved.

**State file to update:** `state/known-facts.md` — add Wisp's pronoun as a locked canonical fact.

---

### 1B. Flight Duration

**The contradiction:** Ch. 1 establishes the voyage as three days, twice. Ch. 2's System message states "11 hours to Halverstow Port" at a point in the narrative that is, at most, one morning into the flight — making the figures irreconcilable.

**Chapter-by-chapter evidence (internal audit):**

- Ch. 1: "Three days between here and his first active case assignment." / "Three days. No active case. Nothing to investigate, no inference chain to close." — **two explicit three-day confirmations.**
- Ch. 2: "*[No active queries. 11 hours to Halverstow Port.]*" — **the System message gives 11 hours remaining at a point roughly one morning in.**

**The editor's additional claim** (external editor review) references a witness saying "six days since boarding." This is not a separate contradiction: the relevant Ch. 6 passage has Esherel say she "spent the past six days drafting" the letter she intended to deliver — meaning six days since she *heard* he had booked the gondola, not six days aboard. The editor misread this. The flight-duration issue is confined to Ch. 1 vs. Ch. 2.

**Proposed canonical value:** Three-day voyage. The Ch. 2 System "11 hours" is the error. It must be reconciled — either change the hours figure to a number consistent with roughly 60–70 hours remaining (e.g., "62 hours"), or add a sentence establishing that the System is reporting time to an intermediate waypoint rather than to final port.

**State file to update:** `state/known-facts.md` — confirm three-day voyage as locked; note resolution of Ch. 2 System message.

---

### 1C. Passenger Manifest Numbers

**The contradiction:** Multiple counts appear across the manuscript referring to different populations without being labeled as such.

**Count evidence (internal audits + manuscript search):**

- Ch. 2 System message: 12 first / 16 second / 44 third = **72 total booked passengers.** One post-departure first-class amendment noted.
- Ch. 3 System message: 12 first-class entries — consistent with Ch. 2.
- Ch. 17: Captain or magistrate states "the body was sealed in a cabin with seventeen other passengers for two days" — **18 passengers in the locked first-class section**, a sub-population.
- Ch. 32 and Ch. 34: "forty-one entries" in the manifest Theron works from during the exclusivity check — this is the **investigative working manifest**, likely covering a subset of the full passenger list (e.g., excluding crew, excluding passengers who disembarked early, or accounting for the one post-departure amendment).

**Assessment:** These figures are not necessarily inconsistent — they refer to different populations (booked, locked in first class, investigation scope). The problem is they are not labeled. A reader who tracks numbers will register the gap between 72 and 41 without an explanation.

**Proposed fix:** Add a brief in-text label at each count's first use establishing what population it covers. Do not force the numbers to be identical — they refer to different things. The goal is unambiguity, not uniformity.

**State file to update:** `state/known-facts.md` — record each figure with its labeled category.

---

### 1D. M. Tannin Cabin Class

**The contradiction:** The Ch. 3 System booking record places M. Tannin in first class, cabin three. Ch. 13 has Theron recall the manifest as "cabin three-T, one male passenger, economy."

**Evidence (internal audit + manuscript search):**

- Ch. 3 System message: "*[Booking amended post-departure: M. Tannin, first class, cabin three. Original booking name on record under sealed administrative note. Steward's discretion.]*" — **first class, cabin 3.**
- Ch. 13: "Theron had the manifest page in his head: cabin three-T, one male passenger, economy." — **third-class economy, cabin 3-T.**

**Assessment:** These are two different cabins. First class, cabin 3 is the amended booking (the cover identity's listed berth). Cabin 3-T is Vannic's actual third-class cabin where Theron finds him. Theron's Ch. 13 recall is probably meant to be of the Petor Vann third-class booking — but M. Tannin and Petor Vann are two different manifest entries. The confusion is that Ch. 13 calls it "the manifest page" in a way that implies it is the same entry as Ch. 3's M. Tannin line.

**Proposed canonical value:** First class, cabin 3 = M. Tannin's manifest entry (the post-departure amendment). Third class, cabin 3-T = Petor Vann's actual berth. Ch. 13's recall ("manifest page: cabin three-T, one male passenger, economy") must be rewritten to make clear Theron is recalling the Petor Vann third-class booking line, not the M. Tannin first-class entry.

**State file to update:** `state/known-facts.md` — record both entries with their classes and cabin numbers as distinct manifest rows.

---

## Systemic Pattern 2 — Structural Craft (Tier 2)

---

### 2A. Pacing Asymmetry

**External editor (pacing):** Ch. 1–3 too slow; "slice-of-life" delays the hook. The middle and late investigation sections are "extremely compressed" and "staccato." The book is front-heavy.

**External reader (pacing):** "The middle stretch slowed for me, especially once the case moved off the Wyrm and into the harbor offices and records work in Chapters 23–31... a few of the procedural chapters begin to rhyme with one another: table, coffee, list, clerk, coach, repeat."

**Internal audit verdict on Ch. 1:** The cozy texture earns most of its runtime — the Wisp scene, the cabin-settling, and the boarding-queue dynamics do character and world work efficiently. The first mystery-adjacent beat (the Vannic handshake observation) arrives roughly at the chapter's second third. The one genuine gap: "the chapter does not land a single forward-pulling question by its close; the sole dangling note (the woman in the brown coat going still at Vannic's thank-you) is suggestive but very quiet." The editor's "front-heavy" complaint overstates the problem at the opening; the opening texture is earning its place.

**Internal audit verdict on Ch. 23–31:** The complaint is structural, not impressionistic. Seven specific patterns repeat across all nine chapters (Arms corner table in every chapter; clerk/courier arriving at the table in five chapters; case-book-open as the final beat in seven of nine chapters; letter-arrives-read-twice-write-reply in four consecutive chapters; harbour-through-window in every chapter; wrong-frame self-critique in Ch. 23 and 24 consecutively; System annotation at chapter close in eight of nine). Load-bearing chapters that cannot be cut: Ch. 23, 25, 26, 29, 30, 31. Compression budget: Ch. 24, Ch. 27, and the flanking sequences in Ch. 28. The emotional high of the block is Ch. 23's Norra Esherel corridor delivery; the intellectual high is Ch. 29–31. The worst sag is Ch. 27 in full and the first half of Ch. 28.

**Synthesis:** Both complaints are real. The opening pacing issue is milder than the editor suggests. The middle-block sag is a genuine structural problem. The recommended approach is independent for each end.

**Recommended call:** Add a single forward-pulling beat at the close of Ch. 1 (not a new scene — one additional observation or a question that does not resolve). For Ch. 23–31: compress Ch. 24 by removing the second wrong-frame reflection (redundant with Ch. 23); compress Ch. 27 by cutting the profile-drafting sequence and opening on the Pessel letter arriving; trim Ch. 28 to one flanking sequence around the Davren meeting rather than two; reduce the harbour-through-window punctuation to three or four appearances across the nine chapters by substituting alternate atmospheric registers. Target: ~15–20% reduction in block length. [Decision Gate item — see Decision 5]

---

### 2B. Sable On-Ramp

**External editor:** "The pivotal scene in which Theron gains her trust, learns her background, and brings a civilian into a highly regulated legal investigation is completely absent."

**Internal audit verdict:** The pivot in Ch. 7's working lunch is present and internally logical. What is missing is not the pivot itself but the ground prepared before it. Specifically: (a) no scene in Ch. 1–6 shows Theron building provisional trust before it crystallizes in Ch. 7; (b) the reader has no frame for why Sable can do what she does in Ch. 8 onward (interrogation strategy, behavioral profiling) before she demonstrates it; (c) the Ch. 1 detail of Sable going still at the Vannic boarding moment is the most individuating early beat she gets, and it is not followed up.

The audit establishes her scene-by-scene background appearances in Ch. 1–6 as coherent internally. The Ch. 5 manifest delivery is the first unsolicited action, and the "now is when I would have rather you came" line signals she has something. The Ch. 7 pantry scene and working lunch are the clear inauguration of the partnership:

> "She waited. Theron registered that he was meant to say the next thing, and that he did not yet have it. ... 'I'd like to compare,' he said. 'If you've an hour.' 'I've an hour.'"

> "'Why you, and not me.' She looked at him. The look was kind without being soft. 'Because you're going to write down what he says, sir, and I'm not.'"

**Two seed-point options from the audit:**

- **Option A: End of Ch. 2, passenger lounge.** The lounge scene already exists; Sable is at her corner table with property papers. One paragraph inserted before Theron moves to the reading alcove — she asks him something about the second-class manifest process (she is a first-class passenger asking about second-class records, which is odd), or she makes a remark demonstrating she has already clocked the lounge's other occupants with a precision that surprises him. He files it without understanding it. Cost: one paragraph in an existing scene.

- **Option B: Ch. 3, corridor close.** Ch. 3 ends with Theron walking back via the empty lounge and corridor. A seed beat in which he passes Sable's cabin door — hears something, or glimpses through an open door something inconsistent with the property-papers persona — and files it as unresolved. One paragraph. Quieter than Option A; preserves more mystery around who she is.

**Spoiler constraint (hard rule):** Any seed scene must not reveal Sable's professional identity. The beat must read as texture — something slightly unusual that Theron notices and cannot place — not as disclosure. Nothing in the seed may function as a clue to who she is; it may only seed the idea that she notices things he does not expect her to notice.

[Decision Gate item — see Decision 4]

---

### 2C. Locked-Room Mechanism

**External editor:** "If any passenger or steward with a simple piece of metal can use a service slot to manipulate the bolt, the room was never truly locked."

**Internal audit verdict: Partially supported.**

The text establishes that the service slot requires a specific instrument:

> "The service slot was the only access, and the service slot was three feet to the left of the bolt and required a steward's lift-key."

> "It was a thin, flat thing, dull steel, the sort of object that did not appear in any guidebook to gondola travel."

The "did not appear in any guidebook" line gestures at obscurity but does not state that only one key exists, that Calden is the sole holder, or that the slot's location is non-obvious. The constraint on knowledge and tool access is implied but not stated.

However, the audit also notes that the editor slightly misframes what the locked-room achieves narratively: "The puzzle the sealed cabin creates is not 'who could have opened the door'... The puzzle is 'why was the bolt drawn at all.' Theron's working interpretation is that the bolt-drawn cabin is evidence the occupant drew it himself — and therefore that no one entered." The locked room is deployed as evidence of no intrusion, not as an impossible-entry puzzle. This distinction is never made explicit in the text, which means a reader expecting a classical locked-room setup will register the editor's objection.

**Three options (from audit):**

- **Option (i):** Redesign mechanism — replace the service-slot approach with something that genuinely restricts access (two-key control, sealed slot, wax pellet indicator). Closes the objection structurally; moderate cost in rewriting the discovery scene.
- **Option (ii):** Leave as-is. Reader-level readers did not notice (confirmed by Reader review). The tool is described densely enough to read as proprietary. The locked-room is not the novel's genre promise.
- **Option (iii):** One-line patch — add a sentence establishing the lift-key as a single controlled item: *"The lift-key was Calden's alone — there was one per gondola, held by the head steward, and it had not left his person since boarding."* Closes the editor's specific objection with the lowest disruption. Insert in Ch. 4 discovery scene or Theron's interior survey.

**Recommended call:** Option (iii). [Decision Gate item — see Decision 2]

---

## Systemic Pattern 3 — Character Coherence (Tier 3)

---

### 3A. Vannic Voice Drift

**External editor:** "The abrupt transformation from the disciplined mage to the pitiful, disorganized debtor is not plausibly derived psychologically."

**External reader:** "Lord Vannic/Joren Aldis is effective because he never becomes a monster. He stays human, which makes the eventual reckoning harder and better." — The destination is right; the Reader did not register the gap as a problem.

**Internal audit verdict: Fully supported.**

The Ch. 1 register (dock arrival and corridor handshake):

> "He walked at the front of the convoy with the settled certainty of someone who had never been required to hurry and had developed opinions about people who were."
> "His gaze moved across the dock once and efficiently. The scholars — dismissed. The family — beneath notation. Theron — assessed as young and not immediately consequential, set aside."
> "the raised ridge, built up by years of sustained casting hold, where prolonged contact with a spellwork frame wears the skin to something harder and more specific than ordinary callus... You didn't get that from an occasional hobby. You got it from ten hours a day, reliably, across years."

The Ch. 13–22 register (confrontation through final interview):

> "The man who opened it was thirty years old at the outside, with the wrinkled look of someone who hadn't slept well in three days and was still wearing yesterday's waistcoat."
> "The man who was not Petor Vann made a sound that was not quite a word and stepped backward. He did not shut the door."
> "He told her about Berric Toll. He did it in the agonized, digressive fashion of a man who had been rehearsing a story and kept catching himself adding disclaimers..."
> "'I — this is entirely my —' 'Sit down,' the magistrate said."

The gap between these registers is significant and never bridged on the page. The audit confirms: "The fear of discovery is implicit in the premise, but the text offers no internal thought, no narrator observation, and no contextual framing to explain the behavioral magnitude of the shift." The closest the text comes is "the wrinkled look of someone who hadn't slept well in three days" — a physical notation, not a psychological bridge.

**Proposed fix:** Add 1–2 internal-thought beats or a short narrator observation in Ch. 13 or the Ch. 17 scenes, bridging the registers. For example: Vannic consciously suppressing his composed register in the confrontation moment, or a brief Theron observation that the three days in third class with nothing to do except wait for a knock he dreaded have materially deteriorated the man who scanned the boarding dock in a second. The bridge must not require a new scene — it should be a sentence or two inserted into the existing confrontation or interview passages.

[Decision Gate item — see Decision 3]

---

### 3B. Vannic Security Logic

**External editor:** Claimed that the manifest booking-change is a plain-text "administrative note" readable by anyone, and that Vannic's cover is undermined by his conspicuous dock behavior.

**Internal audit verdict: Partially supported, with a correction.**

The editor's specific claim about the manifest is **not accurate.** The Ch. 3 System entry reads:

> "*[Booking amended post-departure: M. Tannin, first class, cabin three. Original booking name on record under sealed administrative note. Steward's discretion.]*"

And Theron's interpretation confirms the seal: "Sealed administrative note meant a clerk on the ground had recorded the original entry and locked it under Calden's office, not the System's." The original name is not visible to manifest readers. No fix needed for this specific claim.

However, the editor's underlying concern about security logic has one valid sub-point: the dock exposure. Vannic boards as himself — conspicuously — with a personal steward, a luggage cart stacked three high, and his name murmured through the queue. No scene or narrator observation accounts for when or how he transitioned to the Petor Vann cover identity. The manifest note establishes that the M. Tannin amendment was "paid on the dock after boarding but before lift," which implies the transition happened on board — but no passage shows or narrates it.

**Proposed fix:** One line or brief narrator summary in Ch. 1 or Ch. 2 (or as Theron's later inference in Ch. 13 or Ch. 14) acknowledging the transition: the real lord was seen boarding conspicuously, went below, and established his cover identity with crew before passengers had cause to go looking for him. The fix does not require a new scene — a single retrospective sentence closes the gap.

[Decision Gate item — simpler fix than the editor implied; confirm wording in Decision 1]

---

## Systemic Pattern 4 — Prose Tics (Tier 4)

**Note:** The external Reader praised the prose overall ("exact, patient, and quietly funny without making a show of being funny"). Only the editor flagged these tics. Phase 3 target is top-density reduction, not elimination. These are voice elements that work in moderation and irritate only in accumulation.

---

### Tic 1: "Someone who" Formula

**Pattern:** `[noun] of someone who [verb-phrase]` — indirect characterization through behavioral history.

**Total count:** 37 instances across 20 chapters.

**High-density chapters (from sweep):**

| Chapter | Count |
|---------|-------|
| Ch. 1 | 7 |
| Ch. 23 | 4 |
| Ch. 15 | 3 |
| Ch. 20 | 3 |
| Ch. 2, 4, 13, 17, 33 | 2 each |

**Worst offenders (from sweep):**
- Ch. 1: "she angled herself and the bag around him with the efficiency of someone who had already spent too much of this morning navigating around people."
- Ch. 33: "Her cabin was the cabin of someone who had unpacked the way a person unpacked who meant to be in a room for one night." *(self-referential nesting — formula folds into itself)*
- Ch. 23: "A second clerk at the back of the room was copying from one register into another with the serene patience of someone who had long ago made her peace with the world."

**Phase 3 target:** Reduce the highest-density chapters (Ch. 1, Ch. 23) by varying at least half the instances with concrete action or physical notation. Chapters with 1–2 instances: no action required.

---

### Tic 2: Filing-Verb Crutches

**Pattern:** Metaphorical use of `filed`, `registered`, `catalogued`, `logged` for Theron's cognitive processing.

**Total count:** ~95 metaphorical instances. Breakdown: `filed` ~58, `registered` ~32, `catalogued` 1, `logged` 3–4.

**High-density chapters (from sweep):**

| Chapter | Count | Notes |
|---------|-------|-------|
| Ch. 10 | ~10 | Chapter is literally about case-page review; verb over-concentrated |
| Ch. 7 | ~9 | |
| Ch. 16 | ~7 | |
| Ch. 24 | ~7 | |
| Ch. 12 | ~5 | |

**Worst offenders (from sweep):**
- Ch. 7: "He filed the lounge. He filed the chin in the right hand. He filed *Verrin, S., still at corner table, still in property papers* in the part of the notebook that was the verify column..." — three consecutive `filed` uses in one sentence.
- Ch. 29: "Theron looked up, registered the soup, registered the spoon, registered the host's mild expression, and thanked him." — triple `registered` in sequence.
- Ch. 34: "Theron registered the un-opened note in the part of his head that registered such things and did not, for the moment, do anything with the registration." — `registered` × 2 + `registration` in one sentence.

**Phase 3 target:** Replace approximately half the instances in the highest-density chapters (Ch. 7, Ch. 10, Ch. 16, Ch. 24) with varied alternatives: noted, held, marked, let sit, stored away, kept. The triple-stacked instances (Ch. 7 and Ch. 29) are first-priority fixes regardless of density threshold.

---

### Tic 3: Passive Landscape Constructions

**Total count:** 2 instances, both in a single sentence, Ch. 2.

**Both instances (from sweep):**
> "A river was occurring below. Hills were present in a general direction."

**Assessment:** Both in Ch. 2, para ~235. A two-word fix resolves each ("A river ran below. Hills rose in a general direction."). The following sentence in the paragraph redeems the passage stylistically — the issue is confined to these two lines. Not a systemic problem.

**Phase 3 target:** Two-word fix in Ch. 2. No other instances found in manuscript.

[Decision Gate item for Tics 1 and 2 — see Decision 6]

---

## Systemic Pattern 5 — Preserve Block

These items are **not revision targets.** Phase 3 revisers must diff against this list. Any change touching the items below requires explicit Decision Gate authorization.

- **The System-message device** — both reviews praised it. The editor called it "an excellent, innovative foundation." The reader: "They could have been a gimmick, but here they add a useful second layer." Do not alter the format, tone, or frequency of System messages.
- **The drakes, Wisp's warmth, Theron's classifying habit** — Reader: "The drakes... are vivid immediately, not decorative." These are the cozy register's load-bearing elements. Do not cut or flatten them in any compression pass.
- **Halsa's Ch. 35 speech** — Reader: "Her Chapter 35 speech is the point where the novel's emotional intent becomes clear." This is the moral center of the book. Do not alter.
- **Ch. 36–40 restrained aftermath** — Reader: "Chapters 36–40 are the aftermath: the case is settled, the human costs are named, and the novel chooses restraint over spectacle. That worked for me." Do not add resolution, explanation, or emotional amplification.
- **The final coach scene** — Reader: "The final coach sequence is quiet in a way that feels earned rather than deflated. It ends on motion rather than explanation." Do not add a closing flourish or wrap-up beat.

---

## Continuity Issues Sub-Table

| Chapter | Issue | Old value (in text) | Proposed canonical value | Fix action |
|---------|-------|---------------------|--------------------------|------------|
| Ch. 2 | Wisp pronoun | he/him/his (6 instances) | she/her | Change all six instances; scan full Draft_3 for any other chapter with wrong pronoun |
| Ch. 2 | Flight duration | "11 hours to Halverstow Port" (System message) | Three-day voyage | Change hours figure to ~60–70 hours, or add narrative context for a different reference point |
| Ch. 2 | Manifest label | 72 passengers listed without population label | "72 passengers, booked manifest" | Add inline label clarifying this is the booked count |
| Ch. 3 | Manifest label | "12 first-class entries" without population label | "12 first-class entries, booked manifest" | Add inline label |
| Ch. 13 | M. Tannin cabin class | "cabin three-T, one male passenger, economy" (Theron's recall) | First class, cabin 3 = M. Tannin entry; third class, cabin 3-T = Petor Vann entry | Rewrite Ch. 13 recall to make clear Theron is recalling the Petor Vann third-class booking, not the M. Tannin first-class entry |
| Ch. 17 | Manifest label | "seventeen other passengers for two days" without population label | 18 passengers locked in first-class section | Add inline label clarifying this is the first-class sub-population |
| Ch. 32, 34 | Manifest label | "forty-one entries" without population label | Investigation working manifest (sub-population, distinct from 72 booked) | Add inline label at first use (Ch. 32) explaining this is the investigation-scope manifest; Ch. 34 label follows from Ch. 32 |

---

## Standing Style / POV Edge Cases

No additional style edge cases surfaced in Phase 1 audits. Specifically:

- No Sable-interiority leaks were identified in any of the audit files.
- No double System pings or System formatting inconsistencies were flagged in the internal audits (the Ch. 39 double-ping flag from the Draft_1 triage was resolved in Draft_2).
- No POV drift instances were identified.

The editor's comment about System message consistency ("ensure the rules about who can see these messages and how the board auto-updates remain transparent once the action reaches the ground") is a general caution, not a specific flagged instance. No violation was identified in the audits.

---

## Per-Chapter Must-Fix List

Chapters not listed have no flagged must-fix items and are clean for Draft_3 revision.

| Chapter | Must-Fix Items |
|---------|----------------|
| **Ch. 1** | ① Add one forward-pulling beat at the chapter close — a question or observation that does not resolve, giving the reader a reason to turn the page beyond atmosphere. One paragraph or less; do not add a new scene. [Conditional: Decision 5] ② Reduce "someone who" formula from 7 instances: vary at least 4 of the 7, targeting the most formulaic (the fish-worker, the efficiency-around-people, the Esherel-through-gaps, the Vannic-never-hurried). [Conditional: Decision 6] |
| **Ch. 2** | ① Change all six Wisp male pronouns to she/her. ② Change System "11 hours to Halverstow Port" to a figure consistent with a three-day voyage (~60–70 hours remaining), or add narrative context establishing a different reference point. ③ Add inline population label to the 72-passenger manifest count ("booked manifest"). ④ Fix two passive landscape constructions: "A river was occurring below" → "A river ran below"; "Hills were present in a general direction" → "Hills rose in a general direction." ⑤ [Conditional: Decision 4, Option A] If Option A is selected: insert 1–2 paragraph seed beat in the lounge scene before Theron moves to the reading alcove. |
| **Ch. 3** | ① Add inline population label to the first-class manifest count ("12 first-class entries, booked manifest"). ② [Conditional: Decision 4, Option B] If Option B is selected: insert one-paragraph seed beat in the corridor close — Theron passes Sable's door and notices something inconsistent with the property-papers persona; files without resolving. |
| **Ch. 4** | ① [Conditional: Decision 2] If Option (iii) is selected: add one sentence in the discovery scene or Theron's interior survey establishing the lift-key as a single controlled item — "there was one per gondola, held by the head steward, and it had not left his person since boarding." If Option (i): redesign mechanism per revised spec. If Option (ii): no action. |
| **Ch. 7** | ① Reduce filing-verb density from ~9 instances: fix the triple-`filed` sentence ("He filed the lounge. He filed the chin in the right hand. He filed...") — vary at minimum two of the three into "noted," "held," or "marked." Also address the `registered` × 5 cluster. [Conditional: Decision 6] |
| **Ch. 10** | ① Reduce filing-verb density from ~10 instances — highest chapter count. Replace approximately half with varied alternatives; prioritize the consecutive `filed` + `catalogued` sequence and the dialogue exchange in which Theron performs the same tic aloud twice. [Conditional: Decision 6] |
| **Ch. 13** | ① Rewrite Theron's manifest recall: "cabin three-T, one male passenger, economy" must be rephrased to make clear this is the Petor Vann third-class booking line, not the M. Tannin first-class entry. ② [Conditional: Decision 3] If bridge beats are authorized: add 1–2 sentences or a short narrator observation bridging the Ch. 1 composed register and the Ch. 13 collapse — three days of claustrophobic concealment as context; Vannic consciously suppressing his trained composure, or a physical notation of deterioration that goes beyond the wrinkled waistcoat. |
| **Ch. 16** | ① Reduce filing-verb density from ~7 instances. [Conditional: Decision 6] |
| **Ch. 17** | ① Add inline population label to "seventeen other passengers for two days" — clarify this is the first-class sub-population of 18. ② [Conditional: Decision 3] If bridge beats are authorized: the magistrate interview is a secondary candidate for a bridge sentence, showing Vannic's composition cracking deliberately rather than failing entirely. |
| **Ch. 23** | ① Reduce "someone who" formula from 4 instances: vary at least 2. [Conditional: Decision 6] |
| **Ch. 24** | ① [Conditional: Decision 5] If block compression is authorized: cut the second wrong-frame reflection on Renn (the meta-commentary repeats Ch. 23's frame-shift beat without adding new emotional register). Retain the Calden-notebook handoff and Sable-departure material. Target: reduce to ~65% of current length. ② Reduce filing-verb density from ~7 instances. [Conditional: Decision 6] |
| **Ch. 27** | ① [Conditional: Decision 5] If block compression is authorized: cut the profile-drafting sequence entirely — its content is redundant with Ch. 26's column. Open the chapter on the Pessel letter arriving. Target: reduce to ~60% of current length. |
| **Ch. 28** | ① [Conditional: Decision 5] If block compression is authorized: merge the two flanking sequences around the Davren meeting into one. One scene before the meeting, one scene after — not three case-book-open moments. Target: reduce to ~75% of current length. |
| **Ch. 29** | ① Fix triple-`registered` sentence: "Theron looked up, registered the soup, registered the spoon, registered the host's mild expression, and thanked him." Replace at minimum two of the three instances. [Conditional: Decision 6] |
| **Ch. 32** | ① Add inline population label at first use of "forty-one entries" — clarify this is the investigation working manifest, distinct from the 72-passenger booked manifest. |
| **Ch. 34** | ① Fix self-referential `registered` sentence: "Theron registered the un-opened note in the part of his head that registered such things and did not, for the moment, do anything with the registration." Replace at minimum one `registered` and the `registration` noun. [Conditional: Decision 6] |

---

## What Does Not Need Fixing

**These items surfaced in the Phase 1 inputs but are not revision targets for Draft_3.**

- **Manifest numbers that refer to different populations (72 booked vs. 18 first-class vs. 41 investigation-scope vs. 40 flatlines):** These are NOT inconsistencies if each is labeled with its category in text. The labeling is the fix; the numbers themselves are correct for their respective populations. Do not force them to be the same number.
- **Esherel's "six days" (Ch. 6):** The editor paraphrased this as "six days since boarding," but the actual passage has Esherel say she spent the past six days drafting the letter she intended to deliver — meaning six days since she heard Vannic had booked the gondola, not time aboard. This is characterization, not a continuity error. **Do not correct.**
- **The editor's claim that the manifest booking-change is "plain-text readable by anyone":** Not accurate. The Ch. 3 System entry describes a "sealed administrative note at the steward's discretion" with the original name not visible. No fix needed for this specific claim. The only real security-logic fix is the boarding-scene transition (covered in 3B above).
- **Reader-praised elements:** Halsa Ch. 35 speech, final coach scene, restrained Ch. 36–40 aftermath, System-message device, drakes, Wisp's warmth, Theron's classifying habit — all in the Preserve Block. No action.
- **Low-frequency "someone who" instances:** Any chapter with 1 instance of the formula (Ch. 3, 5, 7, 8, 18, 21, 22, 24, 25, 26, 29). Not a pattern at that density. No action.
- **All Tic 3 instances outside Ch. 2:** No other passive landscape constructions were found in the manuscript. The two instances in Ch. 2 are the entire issue.
- **Ch. 32 word count (minor ceiling overage from Draft_1):** Not re-flagged in Draft_2 reviews. No action.
- **The editor's "overloaded exposition blocks" flag:** The audit did not identify specific info-dump passages beyond what is covered in the pacing section (2A). The world-building is doing character and atmosphere work. The Ch. 1 texture issue is addressed in 2A and Decision 5.

---

## Triage Decision Gate

Complete these decisions before Phase 3 revision begins. Structural changes and spec amendments cannot be executed until these are confirmed.

---

**Decision 1: Restructuring scope**

Which chapters are authorized for structural changes (new scenes, scene merges, insertions, not just line edits)?

Recommendation: Authorize structural change in (a) the Sable seed chapter — Ch. 2 if Option A, Ch. 3 if Option B — one paragraph insertion in an existing scene; (b) Ch. 1 close — one additional beat, no new scene; (c) Ch. 24 and Ch. 27 — compression by cutting specified passages; (d) Ch. 28 — compression by merging flanking sequences; (e) the Vannic confrontation chapter (Ch. 13) and optionally Ch. 17 — insertion of 1–2 bridge sentences. All other chapters: line-edit only.

Spec amendments required before Phase 3 begins for any authorized structural chapter.

**Author's decision:** Authorize structural changes in Ch. 2 (Sable seed, Option A — one paragraph insertion at end of existing lounge scene), Ch. 13 (Vannic bridge beats — 1-2 sentences in confrontation narration), Ch. 24 (compression — cut wrong-frame reflection), Ch. 27 (compression — cut profile-drafting opening sequence), Ch. 28 (flanking sequence compression). Ch. 4 (one-line patch to locked-room passage) and Ch. 1 (one forward-pulling beat at chapter close) are constrained edits — no spec amendments required. All other chapters: constrained edit only.

---

**Decision 2: Locked-room mechanism**

Option (i) redesign mechanism, (ii) leave as-is, or (iii) one-line patch establishing the lift-key as a single controlled item held by the head steward?

Recommendation: Option (iii). Least disruption; closes the editor's specific objection; preserves the forensic reading of the bolt as evidence of no intrusion.

**Author's decision:** Option (iii) — one-line patch.

---

**Decision 3: Vannic voice arc**

Add 1–2 bridge beats in Ch. 13 (and optionally Ch. 17) connecting the Ch. 1 composed-mage register to the confrontation-scene collapse, or accept the Reader's reading that the humanization works as-is and leave unchanged?

Recommendation: Add bridge beats. The Reader's enjoyment confirms the destination is right; the bridge makes the journey readable to editor-type readers without altering the destination. Target: 1–2 sentences inserted into existing passages in Ch. 13.

**Author's decision:** Add 1-2 bridge beats in Ch. 13 confrontation narration.

---

**Decision 4: Sable on-ramp**

Add seed scene Option A (Ch. 2 end, lounge — one paragraph showing Sable attending to something slightly beyond her papers), Option B (Ch. 3 corridor — one paragraph of Theron noticing something through her door), or leave as-is?

Recommendation: Option A. The lounge scene already exists; one paragraph insertion is lower disruption than a corridor pause. The beat: Sable asks Theron something about the second-class manifest process — she is a first-class passenger asking about second-class records, which is odd — or makes a remark that shows she has already clocked the lounge's occupants with a precision that surprises him. He files it without understanding it.

Spoiler constraint reminder: the seed must not reveal her professional identity. It must function as texture, not disclosure.

**Author's decision:** Option A — Ch. 2 lounge end, one paragraph.

---

**Decision 5: Pacing asymmetry**

(a) Address both the Ch. 1 close and the Ch. 23–31 block compression, (b) address only one, or (c) neither?

Recommendation: (a) both. The Ch. 1 close fix is minimal — one paragraph, no new scene. The Ch. 23–31 compression is real work but addresses a genuine structural problem confirmed by both external reviews. Specific authorized compressions: Ch. 24 (remove second wrong-frame reflection), Ch. 27 (cut profile-drafting, open on Pessel letter), Ch. 28 (merge two flanking sequences into one). The harbour-through-window punctuation should appear no more than three or four times across the nine chapters.

**Author's decision:** Both: add forward-pulling beat at Ch. 1 close + compress Ch. 24, Ch. 27, and Ch. 28 flanking sequences.

---

**Decision 6: Prose tics**

(a) Address top-density chapters only — Ch. 1 and Ch. 23 for Tic 1; Ch. 7, Ch. 10, Ch. 16, Ch. 24 for Tic 2; plus the triple-stacked instances in Ch. 29 and Ch. 34 regardless of chapter density — (b) address all instances throughout the manuscript, or (c) no action?

Recommendation: (a) top-density and triple-stacked instances only. The Reader did not register the tics; the editor complained about accumulation. Reducing the highest-density clusters and fixing the most naked mechanical repetitions eliminates the cumulative weight without stripping a voice element that works in moderation.

**Author's decision:** (a) Top-density chapters only (Ch. 7, 10, 16, 24 for Tic 2; Ch. 1 and Ch. 23 for Tic 1; triple-stacked instances in Ch. 29 and Ch. 34 regardless of density; Ch. 2 two-word fix for Tic 3).

---

**Decision 7: Tier 1 canonical values — confirm each**

- **Wisp's pronoun:** she/her throughout the manuscript? **Author confirms:** Yes — she/her is canonical; Ch. 2's six he/him instances are the errors to fix.
- **Flight duration:** Three-day voyage is canonical; resolve Ch. 2 System "11 hours" by: (a) changing the hours figure, or (b) adding narrative context for a different reference point? **Author's choice:** (a) Change the hours figure to a value consistent with a three-day voyage and the narrative point at which Ch. 2 occurs; Phase 3 reviser to verify elapsed time from context.
- **Manifest numbers:** Confirm labeling approach — each count labeled with its category (booked / first-class locked section / investigation-scope) rather than forcing one number? **Author confirms:** Yes — labeling approach confirmed; counts need not be the same number, only unambiguous.
- **M. Tannin / Petor Vann cabin entries:** First class, cabin 3 = M. Tannin entry; third class, cabin 3-T = Petor Vann entry; Ch. 13 recall to be rewritten to name the Petor Vann line specifically? **Author confirms:** Yes — Ch. 13 recall to be rewritten.
- **Esherel's "six days" (Ch. 6):** Confirmed as not a continuity error — she is counting days before boarding; do not alter? **Author confirms:** Yes — do not alter.

---

**Decision 8: State file updates before Phase 3**

`state/known-facts.md` will be updated with canonical Tier 1 values (Wisp pronoun, flight duration, manifest population labels, M. Tannin / Petor Vann cabin entries) before any chapter revision begins.

**Author confirms:** Confirmed — state files updated before Phase 3 begins.

---

**Decision 9: Bible updates before Phase 3**

Required only if Decision 2 selects Option (i) redesign. If Option (iii) one-line patch or Option (ii) leave as-is, no bible update is needed.

**Author confirms:** Not required — Decision 2 = Option (iii). No bible files need updating.

---

**Decision 10: Chapter spec amendments**

Required before Phase 3 begins for each chapter authorized for structural change in Decision 1. Spec amendments must be written and approved before the corresponding revision session opens.

**Author confirms:** Confirmed — spec amendments to be written for Ch. 2, Ch. 13, Ch. 24, Ch. 27, Ch. 28 before Phase 3 begins. Ch. 4 and Ch. 1 close are constrained edits; no spec amendments required.

---

## Decisions Appendix

Decisions recorded 2026-05-22 after author walk-through of all 10 gate items.

**Decision 1 — Restructuring scope:**
Structural changes (new scenes, scene insertions, compression cuts) authorized in:
- Ch. 2: insert one Sable seed paragraph at the end of the existing lounge scene (see Decision 4).
- Ch. 13: add 1–2 bridge-beat sentences to Vannic confrontation narration (see Decision 3).
- Ch. 24: cut the wrong-frame self-critique reflection (repeats Ch. 23 material).
- Ch. 27: cut the profile-drafting sequence opening (repeats Ch. 26 content; Pessel letter remains).
- Ch. 28: trim flanking sequences (harbour-window, case-book close, transition beats) by ~20%.
- Ch. 4: one-line addition to locked-room passage — constrained edit, **no spec amendment required**.
- Ch. 1: add one forward-pulling beat at chapter close — constrained edit, **no spec amendment required**.
All other chapters: constrained edit only.
Spec amendments required before Phase 3 for: Ch. 2, Ch. 13, Ch. 24, Ch. 27, Ch. 28.

**Decision 2 — Locked-room mechanism:**
Option (iii) — one-line patch. Add a sentence establishing the steward's lift-key as a single controlled item held by the head steward: e.g., "there was one per gondola, held by the head steward, and it had not left his person since boarding." No mechanism redesign. No spec amendment required.

**Decision 3 — Vannic voice arc:**
Add 1–2 bridge beats in Ch. 13 confrontation narration. Target: a sentence or two acknowledging three days in third class without sleep, his composed register consciously suppressed, or physical deterioration. The Reader's "humanized" reading is the destination — the bridge makes the journey legible to analytical readers too.

**Decision 4 — Sable on-ramp:**
Option A — insert one paragraph at the end of the existing Ch. 2 lounge scene. Beat: Sable reading the second-class manifest in a way that is slightly too attentive to be curious. Theron notices and files it. No disclosure of her identity or profession. Spec amendment required for Ch. 2.

**Decision 5 — Pacing asymmetry:**
Both sides addressed:
- Ch. 1 close: add one forward-pulling beat (a question, a detail, a foreboding observation) so the chapter ends with narrative momentum rather than ambient close.
- Ch. 23–31: compress Ch. 24, 27, and Ch. 28 flanking sequences (~15–20% block-length reduction). Load-bearing chapters (23, 25, 26, 29, 30, 31) untouched.

**Decision 6 — Prose tics:**
Top-quartile density chapters only — do not strip uniformly.
- Tic 2 (filing verbs, ~95 instances): reduce density in Ch. 7, 10, 16, 24. Target: replace ~half the instances in those chapters with varied alternatives (noted, held, marked, stored away). Lower-density chapters: leave as-is.
- Tic 1 ("someone who" formula, ~37 instances): cap at 2 per chapter in Ch. 1 (currently 7) and Ch. 23 (currently 4). Lower-density chapters: leave as-is.
- Tic 3 (passive landscape, 2 instances in Ch. 2): two-word fix. Not a systemic issue.

**Decision 7 — Tier 1 canonical values:**
- Wisp's pronoun: **she/her** throughout. Ch. 2's six he/him instances are the errors.
- Flight duration: **three-day voyage** is canonical. Ch. 2 System message "11 hours to Halverstow Port" must be reconciled — Phase 3 reviser to choose between (a) changing the hours to a figure consistent with three days remaining at that narrative point or (b) adding brief narrative context explaining the figure. Either approach is acceptable; record the chosen approach in the Ch. 2 revision commit message.
- Manifest numbers: **labeling approach** — each count to be labeled with its category in text (booked / boarded / under investigation / flatlined). Not required to be the same number; required to be unambiguous.
- M. Tannin cabin: **First Class, Cabin 3** is canonical. The error is in Ch. 13: Theron's recall conflates the Petor Vann third-class berth (3-T) with the M. Tannin first-class entry (Cabin 3). Fix: rewrite Ch. 13 recall to specify which booking line Theron is thinking of.
- Witness "six days since boarding" (Esherel, Ch. 6): **do not correct.** Editor's reading was a misparse — Esherel was counting from before boarding, not from departure. This is not a timeline error.

**Decision 8 — State file updates:**
Confirmed. `state/known-facts.md` and `state/running-recap.md` to be updated with canonical Tier 1 values **before any Phase 3 chapter revision begins**.

**Decision 9 — Bible updates:**
Not required. Decision 2 chose option (iii) — one-line patch — so no mechanism redesign. No bible file needs updating.

**Decision 10 — Spec amendments:**
Required for Ch. 2, Ch. 13, Ch. 24, Ch. 27, Ch. 28. To be written as a batch before Phase 3 begins. Ch. 4 (one-line addition) and Ch. 1 (forward-pulling close beat) are constrained edits — no spec amendment needed.
