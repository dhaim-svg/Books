# Internal Audit — Ch.24 Passenger-Count Arithmetic

## The Issue

The chapter's opening paragraph states that thirteen passengers (fourteen minus Vannic) have been reviewed, with "twelve of those accounted for." The named examples that constitute those twelve sum to eleven. The same paragraph then identifies "two columns" (Fell and Renn) as the remaining open work — but Fell is listed among the twelve, which means she is simultaneously counted as closed and treated narratively as an open column. The "two columns" framing is only arithmetically consistent if Fell is not in the "accounted for" group, making the correct count eleven, not twelve.

---

## Evidence (quoted from Ch.24)

**Paragraph 2 (lines 5–6):**

> Fourteen passengers, minus Vannic. Twelve of those accounted for, at least in outline: the two with soft alibis from the steward's briefing, the textile buyer, the woman with the funeral record, the six who had cleared on profession and reference, and Fell, who had not cleared so much as complicated. That left two columns that, until yesterday, he had considered closed. He turned to the first.

**Echo passage, paragraph near end of chapter (line 147):**

> He had fourteen passengers, minus one. Twelve of those with some kind of accounting. Two columns still working. One of them waiting on a warrant. The other flagged for revisit with an uncertain steward's note and a wrong-frame correction and a journey to Sannholt that was already in progress.

---

## Count breakdown

Working from the "twelve accounted for" list as written:

| # | Example as written | Count |
|---|---|---|
| 1–2 | "the two with soft alibis from the steward's briefing" | 2 |
| 3 | "the textile buyer" | 1 |
| 4 | "the woman with the funeral record" | 1 |
| 5–10 | "the six who had cleared on profession and reference" | 6 |
| 11 | "Fell, who had not cleared so much as complicated" | 1 |
| **Total** | | **11** |

The list as written names eleven passengers, not twelve.

---

## Discrepancy

**Claimed:** twelve accounted for.  
**Counted:** eleven named examples sum to eleven.  
**Off by:** 1 (one passenger is either unnamed or miscounted).

There is a second, structural discrepancy: the paragraph closes with "that left two columns" — meaning 13 − 12 = 1 remaining, not 2. The "two columns" are Fell (first column, addressed on the following page) and Renn (second column). For "two columns" to be correct, the arithmetic must read 13 − 11 = 2. This is internally consistent only if the "accounted for" total is eleven, not twelve — which is also what the examples actually sum to.

Fell is therefore listed in the wrong group. She belongs in the "two columns" remainder, not in the "accounted for" total.

---

## Does this conflict with any locked canonical value?

Cross-checked against `state/known-facts.md`:

- **Manifest — booked total:** 72 passengers (12 first / 16 second / 44 third). No conflict — Ch.24 is working from the third-class subset only.
- **Manifest — investigation scope:** 41 entries. No conflict — Ch.24's "fourteen passengers, minus Vannic" refers to the third-class passengers beyond Vannic's cover identity, consistent with the row at Ch.14: "Third-class manifest has fourteen passengers beyond Vannic."
- **Known-facts row, Ch.14:** "four with no profession or reference on record" and the two soft alibis from Ch.15 briefing are all consistent with the passage's sub-groupings.
- **Known-facts row, Ch.15:** Halsa Renn filed as fourth-tier; Maret Fell as the Mirren east harbour connection — both established as open/complicated, not closed.

No locked canonical value is contradicted by correcting the total to eleven. The fix removes the internal inconsistency without altering any value in the known-facts table.

---

## Proposed canonical value

The correct "accounted for" count at this point in Ch.24's narrative is **eleven**.

This is consistent with: (a) the examples as written summing to eleven; (b) "two columns" (Fell + Renn) equalling the correct remainder (13 − 11 = 2); (c) the echo passage's "two columns still working" — one waiting on a warrant (Fell), the other flagged for revisit (Renn).

---

## Fix options

**A. Minimum-change fix: change the stated total from "twelve" to "eleven."**

Paragraph 2 becomes:

> Fourteen passengers, minus Vannic. Eleven of those accounted for, at least in outline: the two with soft alibis from the steward's briefing, the textile buyer, the woman with the funeral record, the six who had cleared on profession and reference, and Fell, who had not cleared so much as complicated. That left two columns that, until yesterday, he had considered closed.

Echo passage (line 147) becomes:

> He had fourteen passengers, minus one. Eleven of those with some kind of accounting. Two columns still working.

This is a two-word change across the chapter (both instances of "twelve" → "eleven"). The list itself is unchanged; the remainder arithmetic resolves cleanly to 2.

**B. Add one more named passenger to the "accounted for" list to reach twelve — then remove Fell from it.**

This would require naming a twelfth passenger who is cleanly closed, keeping Fell out of the list, so that "twelve accounted for" plus "two columns" (Fell + Renn) = 14 − 1 = 13. Example insertion: "...the six who had cleared on profession and reference, and the cabin-one-T couple traveling together on the family transfer paperwork, and Fell, who..." — but this introduces a new name with no prior establishment, requires a known-facts update, and creates worldbuilding that needs to be seeded retroactively. The prose gain is nil.

**C. Restructure the passage to enumerate the two columns separately from the "accounted for" list.**

This would mean rewriting the paragraph so Fell and Renn are explicitly set aside at the top ("two columns I'm re-examining"), and the count of "accounted for" applies only to the cleanly-closed remainder. This is accurate but over-engineers a one-word error. Not warranted.

---

## Recommendation

**Fix A.** Change "twelve" to "eleven" in both the opening paragraph and the echo passage near the chapter's end. This is the minimum-change correction: it makes the stated total match the examples as written, resolves the "two columns" remainder to 2, and requires no new material, no known-facts update, and no prose restructuring. The sentence rhythm is unaffected.

Both instances to change:

1. Paragraph 2, opening block: `Twelve of those accounted for` → `Eleven of those accounted for`
2. Echo passage, final section: `Twelve of those with some kind of accounting` → `Eleven of those with some kind of accounting`

---

## State-file update required?

**No.** The known-facts table does not record the intermediate "accounted for" count as a locked canonical value. The manifest totals (72 booked / 41 investigation-scope / 14 third-class beyond Vannic) are locked and are not affected by this fix. No row in `state/known-facts.md` requires amendment.
