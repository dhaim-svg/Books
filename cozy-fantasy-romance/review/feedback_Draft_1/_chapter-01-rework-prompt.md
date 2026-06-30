# Goal — Kapitel 1 (Draft_2): Dokumente abschließen, neu schreiben, verifizieren, bis sauber

Modell: Opus für Schreiben und Voice-Beurteilung. Nur rein mechanische Schritte
(Audit-Skripte ausführen, Tippfehler abarbeiten) dürfen an Sub-Agents delegiert werden.

Arbeitsverzeichnis: D:\Projects\Books  (Buch: cozy-fantasy-romance/)
Lies zuerst cozy-fantasy-romance/CLAUDE.md — das ist der autoritative Vertrag.

Lege zu Beginn eine Todo-Liste (TodoWrite) mit den Phasen 1–4 an und halte sie aktuell.

## Kontext-Dateien (alle lesen, bevor du editierst)
- bible/brand-voice.md  (§4.2 Fragment-Disziplin, §7.1 Negations-Tic, §9 Checkliste)
- bible/standing-style.md  (POV/Tempus/Plant-Regeln)
- chapters/chapter-01-spec.md  (autoritative Spec; Plant #1 landet in Szene 3; Ziel ~2.500 Wörter)
- state/running-recap.md, state/known-facts.md
- manuscript/Draft_1/chapter-01.md           (KI-Draft = BASIS für den Rewrite)
- manuscript/Draft_1/chapter-01-reworked.md   (Autoren-Rework: gute Ideen UND die 7 Flags)
- review/chapter-01-informed.md      (mechanische Befunde: 26 Gedankenstriche, 5 Negationen, Plant-Zeile, Wortzahl …)
- review/chapter-01-blind.md         (Leser-Befunde inkl. Tic #2)
- review/chapter-01-comparison-analysis.md  (7 Autoren-Changes + 7 Flags F1–F7 + Negations-Katalog)

## Querschnitt-Guardrails (gelten in ALLEN Phasen)
- Zentrale Konsistenz-Entscheidungen EINMAL treffen, dann deterministisch überall anwenden
  (z.B. „arkane Lampe" vs. „Kerze" — eine Variante wählen und durchziehen; keine Drift).
- Keine Capitalised Worldbuilding Nouns, außer die Bible nutzt sie so → „arkane Lampe" klein.
- Findings adversarisch gegen den Quelltext prüfen, BEVOR du danach revidierst
  (Review-Agents können fehllesen; nicht blind jedem Befund folgen).
- Nach jeder Fakt-/Wort-Änderung den ALTEN Wert im ganzen Kapitel gegenprüfen (Residuen).

---

## Phase 1 — Dokument-Baustellen schließen

D-A. review/voice-style-adjustment-proposal.md: Status-Header (Z.4 „noch nicht eingearbeitet")
     auf „eingearbeitet" aktualisieren und je D1/D2/D3/D4b kurz mit Fundort markieren
     (sie stehen bereits in brand-voice.md / CLAUDE.md — nur den veralteten Header korrigieren).

D-B. bible/brand-voice.md: Tic #2 als LEICHTE Watchlist-Notiz ergänzen — KEIN Null-Budget.
     Im §7-Tic-Bereich eine Beobachtungslisten-Zeile: Muster „[Subjekt] kannte [es] (auswendig)"
     bei Häufung (≥3 im Kapitel) prüfen und ausdünnen; in §9 als weicher „Watchlist, kein Budget"-
     Prüfpunkt vermerken. Bewusst klein halten, Checkliste nicht aufblähen.
     (≤~5 Zeilen, eine Datei → direkt umsetzen, kein writing-plan.)

---

## Phase 2 — Kapitel 1 neu schreiben → manuscript/Draft_2/chapter-01.md

Basis = manuscript/Draft_1/chapter-01.md. Schreibe eine neue Fassung nach manuscript/Draft_2/chapter-01.md.

Anforderungen:
- Gedankenstriche: ≤1 pro 250 Wörter (bei ~2.500 Wörtern also ≤~10; Ziel klar darunter, ~5–7).
  Ausgangswert war 26.
- Negations-Tic-Familie (alle 4 Varianten, §7.1): Ziel 0 (max. 1 wenn wirklich unersetzbar, nie 2).
  Ausgangswert war 5.
- Plant #1: muss in Szene 3 landen (Spec). Die Hand-Ruhe als ANGEBOREN/natürlichen Zustand rahmen
  (nicht als „erlernt/von langem Üben" — das war Flag F7). ABER subtil: NICHT unterstreichen,
  KEIN Spoiler-Graubereich auf Alexanders Talent (kein „als wäre das ihr natürlicher Zustand"-
  Konstrukt, das zugleich Negations-Variante 3 war). Plant zeigen, nicht erklären.
- Gute Autoren-Changes aus chapter-01-reworked.md einarbeiten, ABER die 7 Flags vermeiden/fixen:
  F1 Kerzenflammen-Kontinuität (Licht-Quelle im ganzen Kapitel konsistent — Schlussbild abgleichen),
  F2 „selsbt"→„selbst", F3 „präzisionsbereich"→„Präzisionsbereich", F4 „ein kleine magischer"→„ein kleiner",
  F5 „Arkane Lampe" klein, F6 Spaced Hyphens → echte Em-Dashes, F7 Plant innen (siehe oben).
- Tic #2 entschärfen: die 4× „kannte er/es auswendig"-Konstruktionen auf max. 1 reduzieren.
- Weitere Informed-Fails: ≤2 aufeinanderfolgende Sätze mit „Er"-Anfang; max. 1 Trikolon;
  keine unschönen Hauptsatzreihungen.
- Wortzahl: ~2.500 (Bereich 1.800–3.200). Von 1712 aus durch ECHTE Szenen-Erweiterung wachsen
  (sinnliche/atmosphärische Beats, Beat-1-Material aus der Spec) — kein Fülltext, keine Wiederholung.
- Schritt 5b: §9 Quick-Reference-Checkliste aus brand-voice.md gegen den Draft laufen, Verstöße fixen.

---

## Phase 3 — Verifizieren (4 Checks, Reviews parallel)

Mechanische Audits (stdout lesen):
  python tools/flow_audit.py --book cozy-fantasy-romance --draft Draft_2 --chapter 01
  python tools/copyedit_audit.py --book cozy-fantasy-romance --draft Draft_2 --chapter 01

  Caveat flow_audit: Opener-/Subjekt-Metrik ist englisch-kalibriert → %subject und opener-chain
  IGNORIEREN; nur Satzlänge, %short, short-chain, One-Liner ernst nehmen.

  Caveat copyedit: US/UK-Spelling- und Quote-Checks sind englisch-orientiert → geflaggte Items
  gegen deutsche Norm gegenprüfen; Whitespace/Doppelwort/Satzzeichen/Em-Dash-Spacing voll gültig.

Reviews (zwei Sub-Agents PARALLEL, unterschiedliche Output-Dateien):
  - Informed-Review-Agent: liest review/review-brief-informed.md und folgt ihm; prüft
    manuscript/Draft_2/chapter-01.md mit VOLLEM Bible-/Spec-/State-Zugang;
    Output → review/chapter-01-informed-r{N}.md.
  - Blind-Review-Agent: liest review/review-brief-blind.md und folgt ihm; prüft NUR
    manuscript/Draft_2/chapter-01.md; liest KEINE Bible/Spec/State-Datei (Blindheit wahren);
    Output → review/chapter-01-blind-r{N}.md.
  ({N} = aktuelle Runde, beginnend bei 2.)

---

## Phase 4 — Loop / Stopp

STOPP-Kriterium (alles muss gelten):
  - Informed-Review: 0 High-Severity-Fails (Gedankenstriche im Budget; 0 Negations-Tic-Instanzen;
    Plant-Zeile korrekt & ohne Spoiler; Style-Compliance Pass; Wortzahl im Zielbereich).
  - Blind-Review: kein wiederkehrender Tic geflaggt (weder Negation noch „kannte"); Cozy-Register ok;
    kein kritischer Leser-Befund.
  - flow_audit: sprachunabhängige Metriken nicht geflaggt.
  - copyedit_audit: 0 echte mechanische Fehler.

Wenn NICHT erfüllt und Runde < 3:
  - Befunde adversarisch gegen den Text prüfen (Fehllesungen verwerfen).
  - GEZIELT nur die bestätigten Fails revidieren — copy-faithful: nur das Geflaggte ändern,
    intakte Prosa wortgetreu lassen. Kein Wert ist zu ändern, wenn er bewusstes Handwerk ist.
  - Zurück zu Phase 3 (nächste Runde {N+1}).

Wenn erfüllt ODER Runde == 3:
  - STOPP. Schreibe einen kompakten Übergabe-Bericht:
    * Pfad der finalen Fassung (manuscript/Draft_2/chapter-01.md) + Wortzahl.
    * Vorher/Nachher: Gedankenstriche, Negationen, Tic-#2-Vorkommen, Wortzahl.
    * Welche Dokument-Edits (Phase 1) gemacht wurden.
    * Restliche Urteilsfragen / bewusst offen gelassene Punkte für den Autor.
    * Vorschlag für state/running-recap.md + state/known-facts.md (Workflow-Schritt 6),
      NICHT automatisch schreiben — zur Freigabe vorlegen.
