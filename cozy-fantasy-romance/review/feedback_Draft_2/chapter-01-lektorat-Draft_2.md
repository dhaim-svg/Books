# Lektorat Draft_2 / Kapitel 1 — *Kaffee, Magie und ein Drache namens Felix*

**Geprüft:** `manuscript/Draft_2/chapter-01.md` (2.211 Wörter, ~90 Kommas, 12 Semikolons)  
**Befund in einem Satz:** Grammatik und Kommasetzung sind im Kapitel durchgehend korrekt — das wahrgenommene „Zuviel an Beistrichen" ist **Kommadichte** (Einschub-/Appositionsstapelung in einzelnen Sätzen), kein Fehler; harte Fehler gibt es nur zwei plus einen Typografiefund.

---

## A — Echte Fehler (Pflicht-Korrekturen)

### A1 — Z. 31: Fehlende Zeitangabe / faulty pronominalization

**Original:**
> Die Fahrt hatte lang gedauert, und Felix hatte **die meiste davon** damit verbracht, Alexander über den Rand der Kiste hinweg zuzusehen …

**Problem:** „die meiste" kann im Deutschen nicht ohne Substantiv auf ein Zeitkonzept zeigen. Das Pronomen „davon" verweist auf „die Fahrt", aber „die meiste [Fahrt]" ist kein idiomatisches Deutsch — gemeint ist „die meiste **Zeit** [der Fahrt]". Das fehlende „Zeit" macht den Satz grammatisch unvollständig.

**Korrektur (zwei Varianten):**

Option A (minimal): `die meiste Zeit davon` → „Felix hatte die meiste **Zeit** davon damit verbracht, …"

Option B (Umformulierung): „Felix hatte **den größten Teil der Fahrt** damit verbracht, …"

→ **Option A** ist der kürzeste Fix und ändert nichts am Rhythmus.

---

### A2 — Z. 35, 47, 95: Falsche schließende Anführungszeichen (Typografie)

**Diagnose:** Die drei Dialog-Zeilen verwenden:
- Öffnendes Anführungszeichen: `„` (U+201E, korrekt) ✓
- Schließendes Anführungszeichen: `"` (**U+0022, ASCII-gerade**) ✗

Das schließende Zeichen muss `"` (U+201C, typografisch korrekt für Deutsch) sein, nicht das ASCII-Gänsefüßchen.

Bestätigt per Zeichenzählung: 3 × `„` (U+201E) / 0 × `"` (U+201C) / 3 × `"` (U+0022).

**Betroffene Zeilen:**

| Z. | Aktuell | Korrekt |
|---|---|---|
| 35 | `„Wir sind da"` | `„Wir sind da"` |
| 47 | `„Es ist keine schlechte Werkstatt"` | `„Es ist keine schlechte Werkstatt"` |
| 95 | `„Fertig"` | `„Fertig"` |

**Korrektur:** Alle drei schließenden `"` (U+0022) durch `"` (U+201C) ersetzen.

> **Hinweis für den Build:** Pandoc mit `--smart` normalisiert gerade zu typografisch korrekten Anführungszeichen automatisch — aber nur konsistent, wenn das Öffnen-Zeichen ebenfalls gerade war. Da hier gemischt wird (`„` öffnet, `"` schließt), muss manuell korrigiert werden.

---

### A3 — Z. 61: Syntaxambiguität (niedrig priorisiert)

**Original:**
> In die zweite Schublade kamen die Messinstrumente, **das Messgerät an den Gürtelhalter**.

**Problem:** Unklar, ob (a) Messinstrumente → Schublade UND Messgerät → Gürtelhalter (gemeinte Lesart) oder (b) Messinstrumente + Messgerät → Schublade, wobei Messgerät am Gürtelhalter hängt. Die koordinierte Ellipse (fehlendes Verb im zweiten Teil) ist zulässig, erzeugt aber Ambiguität.

**Korrektur:** Verb explizit machen:
- „In die zweite Schublade kamen die Messinstrumente; das Messgerät hängte er an den Gürtelhalter."
- Oder: „In die zweite Schublade kamen die Messinstrumente; das Messgerät an den Gürtelhalter."  
  (Semikolon trennt die beiden Destinationen klarer als Komma)

Schweregrad: **niedrig** — die Bedeutung ist aus dem Kontext erschließbar. Trotzdem auflösenswert.

---

## B — Kommadichte-Hotspots (Vorschläge, keine Pflicht)

**Was hier steht und was nicht:** Die folgenden Kommas sind alle grammatisch **korrekt** — sie müssen stehen. Was als „übermäßig" empfunden wird, ist die Stapelung mehrerer Einschübe/Appositionen **im selben Satz**. Die Lösung ist **Umstellen** (Satz teilen, Einschub zum eigenen Satz machen), nicht Kommas-Streichen.

Alle Vorschläge sind gegen §4 brand-voice geprüft: kein Stakkato, keine Kurzsatz-Kette (≤8 Wörter) von mehr als zwei aufeinanderfolgenden Sätzen, keine Hauptsatzreihung ohne Nebensatz-Einbettung, kein neuer Gedankenstrich über Budget (aktuell 4/~9).

---

### B1 — Z. 3: Appositionskette am Satzende

**Original:**
> … trug ihn durch die Tür, schräg, den einzigen Winkel, in dem er hindurchpasste.

Komma-Cluster: `, schräg, den einzigen Winkel, in dem er hindurchpasste` — 3 Kommas auf engem Raum.

**Vorschlag:** „schräg" in die Verbalphrase integrieren:
> … trug ihn schräg durch die Tür, den einzigen Winkel, in dem er hindurchpasste.

→ Ein Komma weniger; der Rhythmus des Satzes bleibt erhalten.

---

### B2 — Z. 5: Dreifach-Einschub in einem langen Satz

**Original:**
> Seine Arme meldeten den Tag, von den Schultern bis in die Finger, diese gleichmäßige Müdigkeit nach Stunden Heben, die er gern hatte, weil sie nichts von ihm verlangte, als getan zu sein.

Sechs Kommas, drei Einschübe: (1) räumliche Spezifikation, (2) Apposition zu „den Tag", (3) Relativsatz mit Kausalnebensatz.

**Vorschlag:** In zwei Sätze aufteilen — physische Empfindung und seine Beziehung dazu trennen:
> Seine Arme meldeten den Tag, von den Schultern bis in die Finger. Diese gleichmäßige Müdigkeit nach Stunden Heben mochte er, weil sie nichts von ihm verlangte, als getan zu sein.

→ 6 → 2+2 Kommas. Beides §4-konform: erster Satz mit Adverbial-Einschub, zweiter mit Relativsatz. Der zweiteilige Rhythmus (Empfindung / Wertung) trägt den Charakter gut.

---

### B3 — Z. 7: Appositions-Kettensatz nach Doppelpunkt

**Original:**
> ein langer Schlauch, knapp vier Meter breit, Risse im Putz an zwei Stellen, ein Fußboden, der nachgab, wenn man nicht aufpasste.

Dies ist der Inhalt nach dem Doppelpunkt: eine Liste statischer Raumeigenschaften. Die letzten beiden Kommas — „, ein Fußboden, der nachgab, wenn man nicht aufpasste" — stehen innerhalb des Relativsatzes und erzeugen Verschachtelung.

**Vorschlag:** Den Fußboden als eigenen Satz abtrennen; die Liste bleibt sauber:
> Der Raum lag vor ihm, so wie er ihn seit dem Mittag im Kopf hatte: ein langer Schlauch, knapp vier Meter breit, Risse im Putz an zwei Stellen. Der Fußboden gab nach, wenn man nicht aufpasste.

→ Die Listensätze beschreiben statische Fakten; der Fußboden-Satz beschreibt ein aktives Verhalten — das ist eine sinnvolle rhythmische Zäsur.

---

### B4 — Z. 9: Doppel-Komma um „dort"

**Original:**
> An einer Stelle wischte er mit dem Stiefel über den Boden, dort, wo der Staub am dicksten lag, und das Brett darunter war heller, als er erwartet hatte.

„dort, wo" erzeugt zwei aufeinanderfolgende Kommas um „dort". Das „dort" ist redundant — „wo" allein lokalisiert ausreichend.

**Vorschlag:** „dort" streichen:
> An einer Stelle wischte er mit dem Stiefel über den Boden, wo der Staub am dicksten lag, und das Brett darunter war heller, als er erwartet hatte.

→ Ein Komma weniger. Der Satz verliert nichts; „wo" allein ist idiomatisch sauberer als „dort, wo".

---

### B5 — Z. 21: Stapel aus Einschub + doppeltem Hauptsatz

**Original:**
> Erspartes hatte er für drei Monate, falls nichts käme, mehr als genug, das wusste er, er wusste es bis auf die Münze, und trotzdem ging sein Blick jedes Mal zuerst zu dieser einen Zeile.

Sechs Kommas, vier Einschübe: konditionaler Einschub / Apposition / parenthetischer Einschub / Amplifikation durch Wiederholung / Adversativsatz. Dies ist der dichteste Satz im Kapitel.

**Vorschlag:** In drei Sätze aufteilen — das angespannte Gedankenloop Alexanders wird dadurch sogar deutlicher spürbar:
> Erspartes hatte er für drei Monate, falls nichts käme. Mehr als genug, das wusste er, er wusste es bis auf die Münze. Und trotzdem ging sein Blick jedes Mal zuerst zu dieser einen Zeile.

→ Die Wiederholung „das wusste er / er wusste es bis auf die Münze" (der innere Loop) bleibt erhalten. „Und trotzdem" als Satzanfang ist zulässig (nicht in der Anti-Move-Tabelle; §3.1 verbietet nur „Und somit", „Und daher", „Und folglich"). Rhythmus: Fakt / Selbstversicherung / konträres Verhalten — drei Schläge.

---

### B6 — Z. 43: Doppelter Relativsatz auf „die Stelle"

**Original:**
> Er fand die Stelle, an der der Fußboden nachgab, die in der Mitte, die Alexander selbst noch nicht entdeckt hatte, und trat zweimal darauf.

Fünf Kommas; „die Stelle" trägt drei modifizierende Strukturen: `[an der der Fußboden nachgab]` + `[die in der Mitte]` + `[die Alexander selbst noch nicht entdeckt hatte]`.

**Vorschlag A** (Apposition integrieren, Relativsatz kürzen):
> Er fand die Stelle in der Mitte, an der der Fußboden nachgab — eine, die Alexander selbst noch nicht entdeckt hatte —, und trat zweimal darauf.

→ Zwei Gedankenstriche klammern den Parenthetical; der Satz wird klar lesbar. Bringt den Gedankenstrich-Count auf 6 (Budget ~9, ok).

**Vorschlag B** (ohne Gedankenstrich, falls Budget geschont werden soll):
> Er fand die Stelle in der Mitte, an der der Fußboden nachgab. Alexander selbst hatte sie noch nicht entdeckt. Er trat zweimal darauf.

→ Drei Sätze: Entdeckung / neue Information / Aktion. Zweiter und dritter Satz je ≤8 Wörter — zwei kurze in Folge, noch innerhalb des Limits. Prüfen ob Kontext davor (direkt nach einem langen Felix-Absatz) ausreichend Puffer gibt.

---

## C — Stil-Watchlist (kein Fehler, zur zukünftigen Politur)

Diese Punkte sind **keine Korrekturen** — sie sind quantifizierte Beobachtungen von Mustern, die bei Häufung rhythmisch erschöpft wirken können. Alle waren in `project_cozy_fantasy_romance.md` als Residuals dokumentiert; hier mit exakten Zählungen.

### C1 — Semikolon-Rhythmus: 12 Semikolons

Semikolon-Zeilen (Grep `; `): Z. 5, 7, 39, 43 (×2), 57, 69, 71, 81, 103, 111, 113.  
**→ Empfehlung:** 2–3 Semikolons aufbrechen, bevorzugt dort, wo ein einfacher Punkt oder ein Nebensatz natürlicher wäre. Kandidaten: Z. 71 (`Fremd war das alles noch, der Raum und die Straße davor; die Bank war es nicht.` → Punkt), Z. 113 (`nach Abwesenheit geklungen; jetzt lag…` → `, jetzt aber lag…`).

### C2 — „klein"-Stamm: 12 Vorkommen

Kein Nullbudget; aber 12 im selben Kapitel ist viel. Trefferliste:
Z. 17 (`kleine nützliche Dinge`) · Z. 51 (`kleines Stück`) · Z. 57 (`kleine arkane Lampe` / `kleinen magischen Stein` / `kleiner heller Kreis`) · Z. 61 (`kleinen Verbindungen`) · Z. 65 (`kleinen Federn`) · Z. 73 (`kleines Wärmemodul`) · Z. 75 (`kleinen Schrauben`) · Z. 79 (`kleinen Lötkolben` / `kleine helle Fläche`) · Z. 87 (`kleines Fließen`).  
Die Häufung ist teilweise inhärent (Werkzeug- und Gerätenamen), aber in Z. 57 stehen drei Instanzen innerhalb eines Absatzes.  
**→ Empfehlung:** In Z. 57 mindestens eine ersetzen — „eine kleine arkane Lampe" → „eine arkane Lampe" (das Adjektiv ist dort redundant, der Satz erklärt die Lampe im nächsten Halbsatz).

### C3 — „als" + Konjunktiv: 4–5 Vergleichskonstruktionen

Instanzen:
- Z. 17: `als bestätige er sich damit selbst`
- Z. 19: `als wäre der Gruß eine Frage gewesen`
- Z. 19: `als gäbe es dort noch etwas zu prüfen`
- Z. 39: `als prüfe er, ob es ihn auch hielt`
- Z. 49: `wie jemand, der eine Aussage gegenprüft` (Präsens-Analogon)

Kein Nullbudget; der Konjunktiv II nach „als" ist stilistisch legitim. Bei 5 Vorkommen in ~2.200 Wörtern wird das Muster jedoch spürbar.  
**→ Empfehlung:** Einen entfernen; Kandidat Z. 19 zweite Instanz (`als gäbe es dort noch etwas zu prüfen` → `und wandte sich der leeren Ladefläche zu, als wäre dort noch etwas zu prüfen` — schon besser, aber ähnliche Konstruktion; oder einfach: `und wandte sich wieder der leeren Ladefläche zu, ohne zu wissen warum`).

### C4 — „ohne … zu": 4 Vorkommen

Instanzen: Z. 15 (`ohne hinauszusehen`) · Z. 31 (`ohne je den Eindruck zu erwecken`) · Z. 73 (`ohne noch einmal nachzusehen`) · Z. 93 (`ohne etwas zu fordern`).  
**→ Kein Handlungsbedarf** bei 4/~2.200 Wörtern; gleichmäßig verteilt, kein Cluster.

### C5 — „die meiste Zeit": gelöstes Problem nach Fix A1

Nach Korrektur Z. 31 entsteht kein neues Muster.

---

## Typografie-Quickcheck

| Check | Befund | Status |
|---|---|---|
| Öffnende Anführungszeichen `„` (U+201E) | 3 × (Z. 35, 47, 95) | ✓ korrekt |
| Schließende Anführungszeichen `"` (U+201C) | 0 × | ✗ → **Fix A2** |
| ASCII-gerade `"` (U+0022) | 3 × (Z. 35, 47, 95) | ✗ → **Fix A2** |
| Gedankenstrich `—` (spaced) | 4 × (Z. 81 ×2, Z. 107 ×2) | ✓ konsistent, Budget ok |
| Gedankenstrich unspaced | 0 × | ✓ |
| Bindestrich `" - "` als Pseudo-Dash | 0 × | ✓ |
| Doppelte Leerzeichen | 0 × | ✓ |
| Verdoppelte Wörter (echter Fehler) | 0 × (tool-Flag Z. 43 „der der" = false positive¹) | ✓ |
| Semikolon (Konsistenz) | 12 × (alle korrekt gesetzt) | ✓ / C1 |

¹ „Er fand die Stelle, an **der der** Fußboden nachgab" — beide „der" sind grammatisch verschiedene Wörter: „an der" = Relativpronomen fem. auf „Stelle"; „der Fußboden" = Artikel mask. Nom. Korrekt.

---

## Zusammenfassung: Was ist zu tun?

| Priorität | Punkt | Zeile(n) |
|---|---|---|
| **Muss** | A2 — schließende `"` → `"` (U+201C) | 35, 47, 95 |
| **Muss** | A1 — „die meiste Zeit davon" | 31 |
| **Sollte** | A3 — Syntaxambiguität Messgerät-Satz | 61 |
| **Kann** | B1–B6 — Kommadichte-Hotspots (Vorschläge) | 3, 5, 7, 9, 21, 43 |
| **Kann** | C1 — 2–3 Semikolons aufbrechen | verteilt |
| **Kann** | C2 — `klein` in Z. 57 ausdünnen | 57 |
| **Kann** | C3 — einen `als`-Konjunktiv entfernen | 19 (Kandidat) |

Die Muss-Punkte (A1, A2) sind minimale Eingriffe, die das Manuskript nicht berühren. Die Sollte/Kann-Punkte sind Vorschläge für Draft_3 — nach Freigabe durch den Autor.

---

*Generiert: 2026-06-29. Basis: manueller Lektorats-Read + Python-Zeichenanalyse + `tools/copyedit_audit.py --book cozy-fantasy-romance --draft Draft_2 --chapter 01 --no-report`. Kein Eingriff in `manuscript/Draft_2/chapter-01.md` in diesem Durchgang.*
