# Document to prewrite promt
## write complete act 3
Nimm die Rolle des Orchestrators ein und schreibe Akt 3 von "The Skybound Wyrm"
(Kapitel 26–40) vollständig, indem du pro Kapitel einen eigenen Sub-Agent (Opus)
dispatched.

═══ KONTEXT ═══

Akt 1 (Ch 1–12) und Akt 2 (Ch 13–25) sind fertig. Der Workflow ist validiert:
Das Planmodell steht in C:\Users\David\.claude\plans\kapitel-1-und-kapitel-compressed-summit.md
— nutze es als Referenz für Prompt-Struktur und Orchestrator-Loop.

Akt 3 = Ch 26–40 (15 Kapitel). Step-Mapping steht in
d:/Projects/Books/Murder-Mystery-Novel-Fantasy-LitRPG-Story/chapters/_chapter-step-mapping.md

Wichtig vor dem Start: Stelle sicher dass state/running-recap.md und
state/known-facts.md durch Ch 25 aktuell sind (schau rein, check den letzten
Eintrag). Wenn Ch 25 noch fehlt, sag mir das.

═══ WORKFLOW ═══

Für N von 26 bis 40:
  1. Orchestrator liest: state/running-recap.md (Tail Ch N-1), state/known-facts.md
  2. Orchestrator dispatched einen Opus Sub-Agent mit dem unten stehenden Template
  3. Sub-Agent schreibt: chapters/chapter-NN-spec.md + manuscript/Draft_1/chapter-NN.md
     und returnt: Recap-Proposal + Known-Facts-Proposal
  4. Orchestrator appliziert State-Updates (Edit-Tool) bevor er weitermacht
  5. TodoWrite: Kapitel N completed markieren
  6. Weiter mit N+1

Kapitel müssen sequentiell geschrieben werden — State-Abhängigkeit zwischen Kapiteln.

═══ SUB-AGENT PROMPT TEMPLATE ═══

Fülle {{N}}, {{NN}}, {{N-1}}, {{recap-tail}} und {{known-facts}} aus.

---
Du bist Drafting-Agent für Kapitel {{N}} von "The Skybound Wyrm" — cozy LitRPG
murder mystery, Debüt-Roman. Du schreibst EIN Kapitel: Spec + Draft + State-Proposals.

PROJEKT-KONSTANTEN (LIES IN DIESER REIHENFOLGE):
1. d:/Projects/Books/Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/standing-style.md
2. d:/Projects/Books/Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/brand-voice.md
   — §4 Rhythmus, §5 Tone, §6 Anti-Slop, §8 Checklist vor Abgabe laufen.
3. d:/Projects/Books/Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/character-profiles.md
4. d:/Projects/Books/Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/ending-twist.md
   — In Akt 3 sind die Reveals bereits auf der Seite (Joren benannt ab Ch 14,
     Halsa identifiziert ab Ch 26–28). Sub-Agents für Ch 26+ dürfen Halsa als
     bekannte Figur behandeln, sobald sie im Kapitel auf der Seite etabliert ist.
     Für Kapitel VOR ihrem Reveal (Ch 26–28 wo sie "in den Fokus kommt"):
     dieselbe Spoiler-Guardrail wie in Akt 1 — Kalibrierung only, nichts auf die Seite.
5. d:/Projects/Books/Murder-Mystery-Novel-Fantasy-LitRPG-Story/bible/12-step-formula.md
   — Lies den relevanten Step vollständig.
6. d:/Projects/Books/Murder-Mystery-Novel-Fantasy-LitRPG-Story/chapters/_chapter-step-mapping.md
7. d:/Projects/Books/Murder-Mystery-Novel-Fantasy-LitRPG-Story/chapters/_template.md

AKTUELLER STATE:

Recap-Tail (Ende Ch {{N-1}}):
{{recap-tail hier eingefügt}}

Known-Facts-Tabelle (aktuell):
{{vollständige Tabelle hier eingefügt — KEIN Spoiler Wall}}

Spoiler Wall (FÜR DICH, NICHT FÜR DIE SEITE — bis zum jeweiligen Reveal-Kapitel):
{{Spoiler Wall eingefügt}}

STIL-REFERENZ (Voice-Kalibrierung):
- d:/Projects/Books/Murder-Mystery-Novel-Fantasy-LitRPG-Story/manuscript/Draft_1/chapter-01.md
- d:/Projects/Books/Murder-Mystery-Novel-Fantasy-LitRPG-Story/manuscript/Draft_1/chapter-02.md

AUFTRAG:
1. SPEC: d:/Projects/Books/.../chapters/chapter-{{NN}}-spec.md (folge _template.md)
2. DRAFT: d:/Projects/Books/.../manuscript/Draft_1/chapter-{{NN}}.md
   Target: ~2.500 Wörter (range 1.800–3.500)
3. §8 SELF-CHECK — fix violations vor Ablieferung
4. RETURN (in diesen exakten Blöcken am Ende deiner Antwort):

[recap-proposal]
**Ch. {{N}} — [Titel]**
> [3–5 Sätze, Fakten + Tone]
[/recap-proposal]

[known-facts-proposal]
| Fakt | Wer weiß es | Wie/Kapitel |
| Nur NEUE Zeilen — keine Wiederholungen aus aktueller Tabelle |
[/known-facts-proposal]

HARTE GUARDRAILS:
❌ Sable keine Interiorität — nur Aktion und Dialog
❌ Keine HUD-Boxen — nur *[indented italic]* für System-Screens
❌ System sparsam, max 4 Interventionen pro Kapitel
❌ Keine [placeholder]-Syntax — mach eine begründete Entscheidung oder flag via DONE_WITH_CONCERNS
❌ Kein Foreshadowing vor dem jeweiligen Reveal-Kapitel
❌ Keine Meta-Kommentare im Draft

✅ Sentence-Rhythmus: 12–18 Wörter, mindestens ein 4–7-Wort-Recoil pro Beat
✅ Dialogue: "said"/"asked" dominieren, keine adverbialen Tags
✅ Cozy-but-not-light: Warmth durch konkrete Details, nicht durch Atmosphäre-Prosa
✅ Theron ist klug durch Handlung, nicht Narrator-Summary

STATUS-RETURN: DONE / DONE_WITH_CONCERNS [Concern] / BLOCKED [Grund]
---

═══ AKT 3 SPEZIFIKA ═══

Aus dem Step-Mapping (zur Schnellreferenz):

Ch	Step	Notes
26	9	Halsa Renn kommt in den Fokus. Background figure now visible. Forged identity via Joren's network.
27	9	Theron und Sable unpick Halsa's profile. Didn't fit noble-rivalry patterns — exactly why he missed her.
28	9	Halsa under scrutiny. Quiet, methodical. Doesn't fit any of Theron's trained categories.
29	10	Zweithöchster Beat. Theron erinnert sich an die final-year theory — sustained scryproof glamour exploit. Er hatte sie als Prüfungsstoff abgetan.
30	10	Die Theorie greift. Nur ein Illusionist, oder jemand trainiert neben einem, würde diese Methode kennen.
31	10	Theron arbeitet rückwärts vom Exploit zu Halsa. Prodigy-Backstory war load-bearing all along.
32	10	Pieces lock. Theron ist sicher. Academy-Theory-Scene muss sichtbar auf der Seite landen — nicht in einem Absatz begraben.
33	11	Confrontation assembled. Passagiere versammelt.
34	11	Theron legt es dar. Sable an seiner Seite. Reasoned reveal, nicht violent. Halsa leugnet nicht.
35	11	Halsa's question: hat jemand Joren's echten Namen benutzt? Antwort: ja — Sable, in Step 6. Das ist ihr wichtig. Sie geht ruhig.
36	12	Gondola landet. Halsa übergeben. Quest completed — Title flips: Solve the Death of Joren Aldis. The System knew.
37	12	Theron levels up: seeing the unseen. Sable sees his face while he reads the screen.
38	12	Theron und Sable nach der Landung. Der Fall setzt sich.
39	12	Sable sieht die Erbschaftspapiere. Erkennt die Adresse. Ihr Cottage liegt in Joren's Heimatregion. Sie wird der Familie berichten.
40	12	Ein Sigil oder Vertragsbruchstück in Joren's Nachlass. Bemerkt. Beiseitegelegt. Ungelöst. Sie fahren in den Urlaub. Ende.

BESONDERE HINWEISE FÜR AKT 3:

Step 10 (Ch 29–32) bekommt 4 Kapitel — zweitgrößter Beat nach Step 6. Die Academy-Theory-Scene muss auf Ch 32 sichtbar und gewichtig landen.
Step 12 bekommt 5 Kapitel — Quest Resolution + System Reveal + Denouement + Geographic Click + Book-2 Thread.
Die gepflanzten Details werden NICHT mehr gepflanzt — alle Plants (Calluses, Carved Fish, Accent Slip, Kindnesses, Niece-softness) wurden in Akt 1 gesetzt und in Akt 2 Step 6 recalled. In Akt 3 können sie maximal kurz anklingen als already-established facts, nie als neue Plants.
Sable's promise (sie wird Joren's Familie persönlich benachrichtigen, nicht per Brief) muss in Ch 35 und Ch 39 konsistent sein.
Shared-reveal-Kontrakt gilt weiterhin bis zum Ende — auch in Akt 3 keine Sable-Interiorität.

═══ MODELL & MODUS ═══

Alle Sub-Agents: Opus
Modus: Voll autonom (kein Spec-Approval zwischen Kapiteln)
Du reviewst am Ende Akt 3 stichprobenartig: Ch 29 (Theory-Beginn), Ch 32 (Theory-Lock), Ch 35 (Confrontation-Ende), Ch 39 (Geographic Click).
Starte mit TodoWrite (Ch 26–40 als pending), dann Ch 26 Sub-Agent.

---

Two notes before you use it:

1. **Adapt the Spoiler Wall section per chapter** — for Ch 26–28 (Halsa "coming into focus"), keep the hard guardrail. From Ch 29 onward, once she's named on the page, sub-agents can treat her as an established figure.

2. **You'll also want an Act 2 version** — the structure is identical, just swap the chapter range (13–25) and step notes. The main Act 2 difference is the five Step-6 recall chapters (Ch 16–17) where the plants come back. I can generate that prompt too if you want it.


## Prepare review of all chapters
We have now completed Acts 1-3, so all 40 chapters are in existence. I want to create now a prompt or a workflow, or rather want you to help me with that on how to do the first review of them. We prepared for them a few review prompts, the informed and the blind one. I tested it on Chapter 1, and it looks good.

Now I want you to help me create a prompt or a proper workflow on how to review all 40 chapters, and then after it integrate the findings. Here I don't know if we should setup git for it to track changes or if we should use the 2nd draft, or if you have a better idea.

Another point I want to make is that I also then want to combine all 40 new chapters in the first manuscript - because with that I can the also let another AI or another person do a review, but I don't know if that is a point to do before the review or after the review. 

Review - prepared prompts:
- `Murder-Mystery-Novel-Fantasy-LitRPG-Story\review\review-brief-blind.md`
- `Murder-Mystery-Novel-Fantasy-LitRPG-Story\review\review-brief-informed.md`

First manual test result to get a feeling on how good the prompts work: `Murder-Mystery-Novel-Fantasy-LitRPG-Story\review\review-test-on-ch-01.md`