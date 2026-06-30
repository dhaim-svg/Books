# Voice & Style — Anpassungsvorschlag
**Projekt:** *Kaffee, Magie und ein Drache namens Felix*
**Datum:** 2026-06-25
**Status:** Eingearbeitet (2026-06-28)
- D1 → `bible/brand-voice.md` §7.1 Anti-Tic-Tabelle (alle 4 Varianten + Budget-Regel)
- D2 → `bible/brand-voice.md` §9 Checkliste (Negations-Tic, alle 4 Varianten)
- D3 → `bible/brand-voice.md` §4.2 Fragment-Disziplin (Fragment-Paar-Kreuzreferenz)
- D4b → `cozy-fantasy-romance/CLAUDE.md` Schritt 5b (§8 → §9 korrigiert)

---

Dieser Vorschlag entstand aus dem Vergleich des KI-generierten Kapitels 1 (`manuscript/Draft_1/chapter-01.md`) mit der autorisierten Nachbearbeitung (`chapter-01-reworked.md`). Die Autorin hat in der Überarbeitung insgesamt 6 Instanzen einer Negations-Betonung-Familie entfernt (ca. eine Instanz alle 285 Wörter bei 1712 Wörtern Gesamtlänge). Die zugrunde liegende Regel existiert bereits in `bible/brand-voice.md` — sie war jedoch zu eng formuliert und hat die Verstöße nicht erfasst.

Jeder Punkt (D1–D4) ist unabhängig freizugeben. **Keine BibelDatei wird ohne explizite Freigabe geändert.**

---

## D1 — `brand-voice.md` §7.1: Negations-Tic-Eintrag erweitern

### Erläuterung

Der aktuelle Eintrag in der Anti-Tic-Tabelle (§7.1) nennt nur die affirmative Kernform. Die Autorin hat in Kapitel 1 jedoch 4 Varianten der gleichen Konstruktionsfamilie entfernt: die affirmative Form, die kausale Form, die vergleichende Form und das Fragment-Paar. Alle vier klingen mechanisch, weil sie Negation als rhetorisches Gerüst einsetzen statt den präziseren Begriff direkt zu wählen. Der neue Eintrag benennt alle vier Varianten explizit, erklärt kurz das Warum und fügt eine Budget-Regel hinzu.

### Vorher

```
| „Es ist nicht nur X, es ist Y." „Nicht bloß X, sondern Y." | Den Punkt einmal machen, mit dem präziseren Wort. Wenn beide nötig: zwei Sätze. |
```

### Nachher

```
| **Negations-Tic-Familie** (alle 4 Varianten — Budget: 0 pro Kapitel; max. 1 wenn wirklich unersetzbar, nie 2 im selben Kapitel) | Den präziseren Begriff wählen. Wenn beide Aspekte wichtig sind: zwei eigenständige Sätze — keiner negiert den anderen. |
| *Affirmativ:* „Es ist nicht nur X, es ist Y." / „Nicht bloß X, sondern Y." | |
| *Kausal:* „nicht weil X, sondern weil Y" | |
| *Vergleichend:* „Nicht die X von jemandem der … — sondern/als wäre das Y." | |
| *Fragment-Paar:* „Nicht X. Y, dass …" / „Nicht X. Aber Y." (erster Satz negiert, zweiter spiegelt affirmativ) | |
| **Warum schädlich:** Alle vier Varianten bauen Negation als rhetorisches Gerüst auf — sie klingen konstruiert, wiederholen ein Muster und verzögern den eigentlichen Punkt. Die Stimme dieser Geschichte macht den Punkt einmal, mit dem richtigen Wort. | |
```

### Rationale

Ohne die Benennung aller 4 Varianten kann ein LLM (oder ein menschlicher Schreiber im Flow) die Konstruktion variieren und die Regel trotzdem unterlaufen. Mit expliziten Beispielen aus dem echten Kapitel ist der Eintrag im §9-Self-Check direkt anwendbar.

---

## D2 — `brand-voice.md` §9-Checkliste: Prüfpunkt aktualisieren

### Erläuterung

Der aktuelle Checklisten-Eintrag nennt nur eine Form der Negations-Konstruktion. Für einen schnellen mechanischen Self-Check muss er alle 4 Varianten der Familie benennen — kompakt, ohne die Vollbegründung (die gehört in §7.1).

### Vorher

```
- [ ] Keine „Es ist nicht X, es ist Y"-Konstruktionen. Null.
```

### Nachher

```
- [ ] Keine Negations-Tic-Konstruktionen (Budget: 0 — max. 1 wenn wirklich unersetzbar):
  affirmativ („nicht X, sondern Y"), kausal („nicht weil X, sondern weil Y"),
  vergleichend („Nicht die X von … — als wäre das Y"),
  Fragment-Paar („Nicht X. Y, dass …"). Jede Instanz im Klartext benennen.
```

### Rationale

Vier Wörter in der alten Regel; vier Varianten in der neuen. Der Reviewer kann die Formulierung direkt als Such-Pattern verwenden. „Jede Instanz im Klartext benennen" verhindert, dass eine Instanz als Einzelfall durchgeht.

---

## D3 — `brand-voice.md` §4.2: Fragment-Disziplin — Hinweis auf Negations-Fragment-Paare

### Erläuterung

§4.2 definiert bereits Fragment-Disziplin (Fragmente sparsam als Präzisionswerkzeug) und die Kurzsatz-Ketten-Regel. Keine dieser Regeln benennt explizit das Negations-Fragment-Paar-Muster als eigene Risikoklasse. Damit kann die Variante „Nicht X. Y, dass …" formal als erlaubtes Fragment durchgehen — obwohl sie zur Negations-Tic-Familie gehört und dem gleichen Null-Budget unterliegt. Ein ergänzender Satz schließt diese Lücke.

### Vorher

```
**Fragment-Disziplin:** Fragmente (Sätze ohne finites Verb) sind erlaubt — sparsam. Ihr Einsatz ist Präzisionswerkzeug: ein Erkenntnismoment, ein harter Stopp, ein emotionaler Beat der sich selbst abschneidet. Drei Fragmente in Folge in einem Übergangskontext: Stakkato-Fehler, korrigieren.
```

### Nachher

```
**Fragment-Disziplin:** Fragmente (Sätze ohne finites Verb) sind erlaubt — sparsam. Ihr Einsatz ist Präzisionswerkzeug: ein Erkenntnismoment, ein harter Stopp, ein emotionaler Beat der sich selbst abschneidet. Drei Fragmente in Folge in einem Übergangskontext: Stakkato-Fehler, korrigieren. Fragment-Paare, bei denen der erste Satz negiert und der zweite affirmativ spiegelt („Nicht X. Y, dass …" / „Nicht X. Aber Y."), zählen zur Negations-Tic-Familie (→ §7.1) und unterliegen dem gleichen Null-Budget — auch wenn beide Sätze formal als Fragmente qualifizieren.
```

### Rationale

Ohne diesen Zusatz existiert eine Hintertür: ein LLM, das die §7.1-Regel kennt, könnte die Fragment-Pair-Variante als „das ist doch ein Fragment, kein Nicht-X-sondern-Y" rechtfertigen. Der ergänzende Satz schließt diese Interpretation explizit aus.

---

## D4 — Durchsetzung & Nummerierungsdrift (keine Bibel-Textänderung)

Diese Empfehlungen betreffen den Workflow und eine Referenz in `CLAUDE.md`, nicht den Bibeltext selbst. Es gibt daher kein Vorher/Nachher für eine Bibeldatei.

---

### D4a — Durchsetzung: Review-Brief als letzte Verteidigungslinie

#### Empfehlung

Der eigentliche Fehler in Kapitel 1 war kein fehlendes Regelwerk, sondern ein fehlender Durchsetzungsschritt: Der §9-Checklisten-Check (Workflow-Schritt 5b) hat die Verstöße entweder nicht erfasst oder die enge Formulierung der alten Regel hat sie durchgelassen.

Für dieses Buch: Der adaptierte Review-Brief (`review/review-brief-informed.md`) listet in Check #4 (Brand-Voice §9-Check) bereits alle 4 Negations-Varianten und verlangt, jede Instanz im Klartext zu zitieren. Dieser Stand ist ausreichend.

Für künftige Bücher: Das Template `framework/templates/book-template/review/review-brief-informed.md` sollte die vollständige Negations-Familie-Definition in Check #4 aufnehmen, damit neue Projekte nicht den gleichen blinden Fleck erben. Dies ist eine Empfehlung für den nächsten Framework-Pflegeschritt — kein dringender Handlungsbedarf für das laufende Buch.

---

### D4b — Nummerierungsdrift: CLAUDE.md Schritt 5b

#### Empfehlung

`cozy-fantasy-romance/CLAUDE.md` Schritt 5b lautet aktuell:

> „5b. Run the **§8** Quick-Reference Checklist from `bible/brand-voice.md` against the draft."

Die Quick-Reference Checklist ist jedoch **§9** in `brand-voice.md` (§8 ist der Vergleichsautoren-Abschnitt). Die Referenz ist um einen Abschnitt verschoben.

Zu korrigieren: `§8` → `§9` in Schritt 5b von `cozy-fantasy-romance/CLAUDE.md`.

Dies ist eine triviale Änderung, aber eine irreführende Unstimmigkeit — insbesondere wenn ein neuer Kontext (oder ein LLM ohne Vorkenntnisse) Schritt 5b mechanisch ausführt und §8 nachschlägt.

**Diese Korrektur kann direkt in `CLAUDE.md` vorgenommen werden — kein Bibelfile betroffen.**

---

## Freigabe

Um einen Punkt einzuarbeiten, genügt eine der folgenden Antworten:

- „Punkt D1 freigeben" — §7.1 Anti-Tic-Tabelle wird aktualisiert
- „Punkt D2 freigeben" — §9-Checklisten-Eintrag wird aktualisiert
- „Punkt D3 freigeben" — §4.2 Fragment-Disziplin wird ergänzt
- „Punkt D4b freigeben" — CLAUDE.md Schritt 5b wird korrigiert (§8 → §9)
- „D4a zur Kenntnis genommen" — keine Aktion erforderlich, nur Bestätigung

Mehrere Punkte können gleichzeitig freigegeben werden, z. B. „D1, D2 und D4b freigeben".
