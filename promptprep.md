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

## Triage decision
1. approved
2. approved
3. all 3; with option (a) for chapter-04
4. approved
5. let it there for now

## Prepare promt for external review
As we have finished reviewing our draft 1 and incorporating the findings into our draft 2, we now have a complete manuscript I want to hand over to an external AI. Please help me design a short prompt for it so that we get a good, usable review as input - e.g. as review md file. Keep in mind: don't tell the other AI too much, as it should have the new reader experience, But tell us if it finds any continuity errors or other mistakes or anything like that. 

## plan on how to integrate the external review and write draft 3
We did an external review of our manuscript, and there were some findings. Now the question is how to use the external review to correct where our draft went wrong and integrate the findings into a new Draft_3. Can you plan that? if something is unclear, please ask? 

The promt I used to start the review with the other AI models is here: `Murder-Mystery-Novel-Fantasy-LitRPG-Story\review\feedback_Draft_2\_external-prompt-preparation.md`

Our manuscript I gave the other AI to review: `Murder-Mystery-Novel-Fantasy-LitRPG-Story\manuscript\Draft_2\_full-manuscript.md`

The review findings are here:
- `Murder-Mystery-Novel-Fantasy-LitRPG-Story\review\feedback_Draft_2\external-editor-review.md`
- `Murder-Mystery-Novel-Fantasy-LitRPG-Story\review\feedback_Draft_2\external-reader-review.md`

## plan on how to integrate the external review and write draft 4
We did an external review of our manuscript, and there is some feedback. With the first feedback already integrated however, much less real issues were found.
Now the question is how to use the external review to correct where our draft went wrong and integrate the findings into a new Draft_4. Can you plan that? if something is unclear, please ask? 

The promt I used to start the review with the other AI models is here: `Murder-Mystery-Novel-Fantasy-LitRPG-Story\review\feedback_Draft_2\_external-prompt-preparation.md`

Our manuscript I gave the other AI to review: `Murder-Mystery-Novel-Fantasy-LitRPG-Story\manuscript\Draft_3\_full-manuscript.md`

The review findings are here:
- `Murder-Mystery-Novel-Fantasy-LitRPG-Story\review\feedback_Draft_3\editorial_review_draft3.md`
- `Murder-Mystery-Novel-Fantasy-LitRPG-Story\review\feedback_Draft_3\skybound_wyrm_review_draft3.md`

## Plan until release
With draft 5 done and I already started reviewing the first chapters, it looks quite good, I want to plan what still neds to be done for publishing this book on amazon. Here is what I know:
- I need a bookcover
  - here I want to try and use nanobana and need a prompt for it - I thought the airship with the drakes and our main person theron would look good on the cover
  - In the guide I follow there is also the talk about using canva to design the title and so on
- Then I need a publishing review
  - I don't know if this should be different review than the ones I did until now
- What else needs to be inside the book before publishing?
  - chapter list
  - remark about all is fictional
  - ?
- Then I need to register at Amazon KDP

I guess this is a rought todo list for releasing this book. After that I also want to streamline this repo in the way that I want to extract the learned steps into a guide and put that into the root directory so that the framework can be used for another book as well.

But for now back to my list - can you help organize my thoughts and bring it to a better todo list: what to do now, what to prepare for, another review or going to publish - and also maybe bring that then to an orderly list which we can follow.

### Phase B
1. Pen name: Theo Weyren, no series for now
2. yes please give me examples
3. ok

yes pleae commit

## Cozy-fantasy-romance
**Goal**: Vorbereitung der benötigten outline Dokumente
**Context**: Mein 2. Buch soll ein Cozy-fantasy-romance buch werden. Ich hab das template bereits kopiert: `cozy-fantasy-romance` und ein research erstellt in bezug auf wie man so ein buch schreibt: `general-research\schreibformeln-strukturmodelle.md`. Beim mystery buch hatten wir die 12-step formula, das passt hier nicht. für unsere bible dokumente sollten wir die richtige struktur aus dem obigen research extrahieren und dann das equivalent zu premise-and-twist erstellen. das ist die vorbereitung für die characktäre und die steps.

### next prep
Aus der letzten Session haben sich folgende Folgepunkte ergeben:
```
Noch zu tun (Folgeschritte, bewusst ausgeklammert):
1. bible/character-profiles.md füllen (Alexander, Daniela, Felix — leitet aus diesen zwei Docs ab, vor allem Danielas innere
Wunde und No-Way-Grund festlegen)
2. chapters/_chapter-step-mapping.md füllen (20 Beats → Kapitel-Mapping)
3. Template-Reste aufräumen — CLAUDE.md, _template.md, _chapter-step-mapping.md und review/review-brief-informed.md
referenzieren noch bible/12-step-formula.md und premise-and-twist.md → müssen auf die neuen Dateinamen umgebogen werden
```
Punkt 2 & 3 sind hauptsächlich *doing* Punkte.

Der interessante ist Punkt 1. Meine Ideen hast du aus dem `cozy-fantasy-romance\chapters\pre-draft.md` schon gelesen, jetzt bitte ich dich mir ein paar Vorschläge zu Daniela zu machen. Folgende Basis Ideen kommen mir:
- gescheiterte erste Liebe
- Zielstrebigkeit (Kaffehaus ist wichtig, kurz vor der kompletten alleinigen übernahme, keine Zeit für Romanzen)
- Eine Freundin die sich auch in Alexander verliebt und sie will nicht dazwischen stehen
aber ich bin mir sicher da gibt es noch mehr. Bitte denke meine Ideen noch etwas weiter und füge noch eigene hinzu dich ich dann durchsehen und berwerten kann.

## next preparations
**Goal:** Vorbereitung der noch abgehenden Dokumente und Buchtitel
**Context:**
Siehe als erstes die vorbereiteten Dokumente hier: `cozy-fantasy-romance\bible` wobei manche noch ein stub sind.

Als notwenige Schritte bevor wir mit dem 1. Kapitel beginnen können fehlen jetzt noch:
- `cozy-fantasy-romance\bible\standing-style.md`
- `cozy-fantasy-romance\bible\brand-voice.md`
  
Und aufbauend auf dem dann die Kapitel Planung, wenn ich mir die Struktur vom 1. Buch ansehe.
Noch ein Detail zur brand voice: Hier hatten wir im 1. Buch das Problem, dass die Stimme der Hauptperson oder generell der Textverlauf beim lesen "ruckig" oder "holprig" geklungen hat wo wir erst spät drauf gekommen sind. Das sollte hier nicht passieren.

Das andere das ich hier in die Planung einbringen wollte ist, es gibt ja den claude skill `/ghostwriter` soweit ich gehört habe - bringt uns der hierbei etwas? Jetzt vielleicht nicht unbeding beim erstellen des brand-voice 

Bezüglich Buchtitel - ich versuche mich an ein paar Vorschlägen - bitte ergänze du mit kommentaren und eigenen Vorschlägen aus denen ich dann wählen kann:
- `Hausdrache und Kaffe` mit dem Titelbild von den beiden Protagonisten und dem süßen Hausdrachen
- `Magischer Staubsauger und Drache`
- `Stadt, Land, Drache und Kaffee`


Ohje - jetz hab ich gerade gegooglet und festgestellt es gibt bereits ein buch: `The Baby Dragon Cafe` das heisst das geht nicht. Meine Handlung geht Gott sei dank in eine andere Richtung wenn ich das auf die schnelle richtig gesehen habe - aber irgendwie möchte ich den Drachen im Titel haben.

## prep für 1. kapitel
Die letzte Session hat ergeben, dass wir eigentlich bereit wären für das Schreiben des ersten Kapitels. Nur möchte ich noch eine Session dafür aufwenden, den kompletten Workspace dafür nochmal durchzusehen und vorbereiten.

Zum Beispiel ist mir aufgefallen, dass das cloud.md-File im root-Verzeichnis noch sehr strikte Punkte in Richtung des ersten Buch beinhaltet. Daher ist meine Aufgabe an dich jetzt für diese Planung oder für diese Session über den Workspace drüber zu schauen und aufzuräumen. Im root-cloud.md generelle Hinweise auf wie ein Buch zu schreiben, unabhängig davon welches Genre oder welches Buch, und nur in den Büchern selbst dann die dazugehörigen Notizen. Sodass wir beim schreiben des buches nicht durcheinander kommen.

Mach auch einen check ob ich sonst noch was übersehen habe in richtung: root=generel gültig; buch-eben=für dieses buch/genre gültig.

## kleine anpassung für felix den Hausdrachen
Ich habe mir gerade im Charakter-Sheet die Charaktere durchgelesen, und großteils passt sie, aber für Felix brauchen wir noch eine kleine Anpassung. Gerade durch sein leicht katzenhaftes Wesen soll er bis zu einem gewissen Grad auch ein Gegenpol zu Alexanders Schüchternheit sein. Also eher der kleine Schlingel, der ihm vielleicht so Sachen bringt, die er sonst nicht macht, und so dieses ab und zu kleine pointierte Wesen, das beim Leser für ein Schmunzeln sorgt.

Wie könnten wir das am besten noch hinbringen? 

## Review chapter 01
**Goal:** Review und Analyse des Chapter1 in Kombination mit meinen Anpassungen - Ableitungen dazu für unsere Dokumente erstellen
**Context:**
Auf Basis unsere erstellten Dokumente in `cozy-fantasy-romance\bible` und der spec wurde ein erstes Dokument erstellt. Dieses dient uns als Prüfung zur adaptierung und korrektur etwaiger probleme dienen. Dazu soll folgendes passieren:
1. Reviews ähnlich wie im 1. Buch nur adaptiert auf dieses, siehe als Vorlage
   - `Murder-Mystery-Novel-Fantasy-LitRPG-Story\review\review-brief-blind.md`
   - `Murder-Mystery-Novel-Fantasy-LitRPG-Story\review\review-brief-informed.md`
2. Vergleich zwischen deinem geschrieben Kapitel und meinem adaptierten Kapitel 1: `cozy-fantasy-romance\manuscript\Draft_1\chapter-01-reworked.md`
   - mir sind vorallem so konstellation wie so verneinungen um bestimmte dinge hervorzuheben wie zb `...als er es kannte — nicht weil die Sonne früher unterging, sondern weil...`, `...roch raus — nicht weil jemand ihn gerufen hatte, sondern weil...` aufgefallen die meiner meinung nach seltener eingesetzt werden sollten.

Wenn wir diese Reviews und die Analyse haben soll darauf ein Vorschlag erstellt werden wie wir die branding voice oder den schreibstil noch anpassen müssen, bevor wir weiter machen.

Frage nach wenn ich mich wo unklar ausgedrück habe und es klärung bedarf.

## Goal für Einarbeitung des reviews und neuschreibung chapter 1
**Goal**: Erstellung eines optimierten Prompts der unter verwendung des `/Goal` Befehls folgende Aufgaben erledigt:
1. alle restlichen Baustellen in unsere Dokumente einarbeitet
2. danach basierend auf den überarbeiteten Dokumenten Chapter 1 neu schreibt
3. Dann diese mit unseren reviewing tools verifiziert
4. punkt 2 und punkt 3 wiederholt bis es passt und es sinn macht das ich wieder drauf schaue

**Context**:
Die letzte Session schloss mit folgendem Abschlussbericht:  
```
Alle 4 Punkte eingearbeitet:

- D1 bible/brand-voice.md §7.1 — Negations-Tic-Zeile auf alle 4 Varianten (Affirmativ / Kausal / Vergleichend / Fragment-Paar) mit Budget-Regel und kurzem Warum erweitert.
- D2 bible/brand-voice.md §9-Checkliste — Prüfpunkt nennt jetzt alle 4 Varianten der Familie mit der Anweisung, jede Instanz im Klartext zu benennen.
- D3 bible/brand-voice.md §4.2 Fragment-Disziplin — Satz am Ende ergänzt: Fragment-Paare die negieren+affirmativ spiegeln zählen zur Negations-Tic-Familie und unterliegen dem Null-Budget.
- D4b CLAUDE.md Schritt 5b — §8 → §9 korrigiert.

---
Nächste Schritte — drei unabhängige Baustellen, du entscheidest die Reihenfolge:

1. Rework-Flags bereinigen — die 7 Begleit-Flags aus der Analyse (chapter-01-reworked.md): Kerzenflammen-Kontinuität, 3 Tippfehler, „Arkane Lampe" capitalization, Spaced Hyphens, Plant #1 semantische Verschiebung. Falls du willst, erledige ich das in einem Schritt.
2. Blind-Review-Tic #2 adressieren — der Reviewer hat unabhängig ein zweites Muster gefunden: „er kannte es / kannte er auswendig" 4× in einem Kapitel. Kein Regelverstoß, aber rhythmisch erschöpft. Meinungsfrage: reicht ein Hinweis in brand-voice.md, oder klärst du das beim Revidieren von Kapitel 1?
3. Kapitel 1 überarbeiten (Draft_2) — mit den jetzt geklärten Regeln das KI-Kapitel nach dem informed-Review-Befund revidieren: Gedankenstrich-Frequenz (26→max 7), 5 Negations-Instanzen, Plant #1-Zeile, Wortzahl Richtung 2.500 Wörter.
```

Ich möchte mir die Funktionen von Claude im Sinne von `/Goal` und/oder `/Workflows` zu nutze machen um die offenen Dokumente einzuarbeiten und basierend darauf ein eine neue version von chapter 1 zu schreiben und das dann zu verifizieren. 

Hilf mir dabei einen optimierten prompt für diese Aufgabe zu erstellen.

Noch eine Anmerkung: Beim schreiben des 1. Buches hat es sich bewährt zum schreiben auf Opus zu setzen - ich habe derzeit den Opusplan Modus - kann man den nur für dieses Projekt deaktivieren oder können wir das in dem prompt so vermerken, bzw. siehst du das immer noch als sinnvoll an?

## Bewertung Draft_2
**Goal:** Überprüfung von Draft_2 aus Rechtschreibungs und Grammatik Sicht

**Context:**
Unser Review und überarbeitung der bible Dokumente hatte als Produkt draft2 chapter 1: `cozy-fantasy-romance\manuscript\Draft_2\chapter-01.md` bevor ich dich als reviewer wieder drüber schauen lasse habe ich es selbst gelesen. Insgesamt ist es inhaltlich deutlich besser als Draft 1, aber mir ist die häufige Verwenung (fast übermäßg nach meinem Gefühl) von Beistrichen aufgefallen. Als Beispiel nenne ich dir die Sätze in Zeile 7 und 9 und dann noch viele weitere. Füre ein Lektorat auf das draft durch und schau was du findest.

## Define skilss or commands für wiederkehrende arbeiten
**Goal:** Definierung von nützlichen skills/commands für wiederkehrede arbeiten an einem buch

**Context:**
Wenn wir uns die vergangenen Arbeiten an diesem oder dem ersten Buch ansehen, gibt es bestimmte Tätigkeiten, die immer wieder gemacht werden, wie zum Beispiel:
- schreibe ein Kapitel
- führe das Review auf ein bestimmtes Kapitel oder ein bestimmten Draft aus
Bis jetzt haben wir die Kommandos dafür immer wieder neu geschrieben. Eigentlich gäbe es genau für solche wiederkehrenden Tätigkeiten Kommandos.
Das Ziel in dieser Session ist es, die alten Memories zu durchforsten und allgemeingültige Skills oder Agents oder Kommandos oder eine Kombination derselben zu kreieren, die uns die Arbeiten am Buch für die kommenden Drafts und Chapters erleichtern.
Dabei sollen folgende Funktionen auf jeden Fall vorkommen:
- schreiben eines Chapters
- den Workflow, den wir beim ersten Buch erarbeitet haben, wo wir ein Chapter Probe geschrieben haben und dann in einem einzigen Rutsch das restliche Buch mit einem Sub-Agent pro Chapter
- natürlich die Reviews, die dann die verschiedenen Sichtweisen dokumentieren
Dieses Mal könnten wir zusätzlich zu unseren beiden Review-Armten (Blind und Brief informed) auch noch gleich das Lektorat dazufügen.

