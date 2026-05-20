# Skybound Wyrm — Chapter Writing Prompt Guide

Anleitung und Vorlagen, um die Story Kapitel für Kapitel mit Claude zu schreiben.

---

## Was am ursprünglichen Entwurf schiefging

- **"Re-read over the files"** — überflüssig. Project Files sind in jeder neuen Konversation automatisch im Kontext. Diese Anweisung kostet nur Tokens und signalisiert Unsicherheit.
- **Der Step-Recap ist von der Bibel abgedriftet.** Der Entwurf liest sich wärmer als das, was tatsächlich geplant ist. Die Bibel sagt, Theron ist "slightly insufferable" und zupft an seiner Graduation Pin (er hat sich sein Selbstvertrauen noch nicht verdient). Wenn man Claude sagt "the reader needs to love him", bekommt man einen weichgespülten Theron, der den Charakterbogen kaputtmacht — seine Lektion (Menschen als Menschen sehen) landet nur, wenn er anfangs etwas verschlossen ist. Lieber die Bibel-Sprache wörtlich zitieren statt paraphrasieren.
- **Keine Craft Constraints.** Kein POV, kein Tempus, keine Längenangabe, keine Tonkalibrierung, keine Erinnerung an die Plant-Verteilung. Ohne das rät Claude — und rät bei jedem Kapitel anders.
- **Kein "was NICHT tun".** Diese Story hat strukturelle Fallen (Plants clustern, den Swap zu früh verraten, Sable Dinge erklären lassen, die sie nur bemerken soll). Der Prompt muss diese benennen.

---

## Empfohlene Prompt-Struktur (gleiches Skelett für jedes Kapitel)

```markdown
## Chapter [N] — [working title]

### Formula coverage
[Den/die relevanten Step(s) aus dem 12-Step-Doc wörtlich zitieren,
nicht paraphrasieren. Wenn das Kapitel zwei Steps umspannt, beide
zitieren und vermerken, wo der Kapitelbruch fällt.]

### Scenes to hit
[2–4 Bullet-Beats in Reihenfolge. Konkret: "boarding handshake",
"first dinner in the saloon", "discovery of the body".
Nicht vage: "introduce the suspects".]

### Plants landing in this chapter
[Die spezifischen Plants aus der Bibel benennen, die in diesem
Kapitel landen, mit Deployment-Hinweis: welche Figur bemerkt es,
in welcher Szene, was die innere Reaktion ist. Explizit auflisten,
welche Plants hier NICHT landen.]

### Continuity
[1–3 Sätze: wo das vorherige Kapitel endete, was der Leser bis
hier weiß, welchen Ton wir mitnehmen. Für Kapitel 1: "N/A — opening chapter."]

### What NOT to do this chapter
[Spoiler vermeiden, Foreshadowing subtil halten, Charakter-Moves,
die zu früh landen würden. Z.B. für Ch. 1: "Sable does not yet
meet Theron in a scene-driving way; she's a passing presence.
Theron does not yet seem charmed."]

### Length and shape
[Zielwortzahl. Z.B. 3,500–4,500 Wörter. Ungefähre Szenenzahl.]
```

---

## Standing Style Block (in jeden Chapter-Prompt einfügen)

```markdown
## Standing instructions (apply every chapter)

POV: Third-person limited, Theron only. Sable's interiority
stays off-page; we read her through what she does and says.
This protects the shared-reveal contract.

Tense: Past tense.

Tone: Cozy beach-read on the surface, with one death that has
real weight. Banter is welcome. Grim atmosphere is not. The
weight is carried by how characters treat each other, not by
darkness on the page.

System screens: Sparse. Use them only when they earn the
interruption. Format them as indented italic blocks, not as
HUD-style boxes. Theron reacts to them like a graduate who's
still pleased the System exists.

Prose: Lean, image-led. Avoid stacked adjectives. No
Capitalised Worldbuilding Nouns unless the bible uses them
that way. Dialogue carries character; don't overstuff tags.

Plants: When a planted detail lands, plant it — don't underline
it. The reader passes it without stopping.

What to never do: don't summarize the bible into the chapter,
don't foreshadow the Act 2 reveal directly, don't have any
character "almost catch" the swap, don't explain the System
to the reader.
```

---

## Worked Example — Chapter 1 Prompt

```markdown
## Chapter 1 — Boarding the Wyrm

### Formula coverage
Step 1 from the 12-step doc, verbatim:
"Hook — Boarding the Wyrm. Theron boards alone, slightly
insufferable, tugging at his graduation pin. Wisp and the
three drakes carry the texture. Sable boards with her own
reason for traveling — a small inheritance, a cottage on the
coast she's grumpy about going to claim — established before
she has any narrative function in the mystery. 'Vannic' makes
a loud entrance and starts collecting enemies on sight.
Plant: calluses. Theron registers a working mage's ridge on
the side of 'Vannic's' index finger at the boarding handshake
and files it as a noble who dabbles. Plant: first kindness.
'Vannic' thanks the steward by name as he's shown to his
cabin. Sable clocks it without comment."

### Scenes to hit
1. Theron at the dock, alone, taking in the gondola and the
   drakes. Wisp in the background handling them.
2. Sable boarding — brief, from Theron's POV across the
   crowd, a passing impression. She is grumpy. He doesn't
   know who she is.
3. "Vannic" boards loudly. The handshake (calluses plant).
   The steward thank-you (kindness plant), witnessed by Sable
   in the same wider scene but a different beat.
4. The Wyrm lifts off. End on a small private moment for
   Theron — the graduation pin, the holiday ahead.

### Plants landing in this chapter
- Calluses (Theron, boarding handshake, filed as "noble who
  dabbles")
- First kindness (steward thanked by name; Sable clocks it
  silently)

NOT landing yet: accent slip, carved fish, niece-softness,
second/third kindnesses, Sable's "wasn't as bad as I expected"
line. All are later chapters.

### Continuity
N/A — opening chapter.

### What NOT to do
- Sable and Theron do not have a real conversation yet. She
  is texture in this chapter, not a scene partner.
- Theron is not charmed by anyone. He is pleased with himself.
- Don't foreshadow the murder. The reader should be settling
  into a holiday book.
- Don't explain the System. Let it be ambient.
- Don't cluster the two plants in the same beat. Calluses at
  the handshake; the steward thank-you in a separate beat with
  Sable's silent observation as the closing image of that scene.

### Length and shape
3,500–4,500 words. Roughly four scenes as listed above.
```

---

## Workflow ab Kapitel 2

Empfehlung: **eine Konversation pro Kapitel, jedes Mal frisch starten.** Gründe:

- Claudes Project Files sind sowieso im Kontext, persistente Konversation bringt nichts dazu.
- Frische Konversationen verhindern, dass früherer Draft-Text in Stimme oder Bildwiederholungen einsickert.
- Du überarbeitest Kapitel N bis es passt, startest dann Kapitel N+1 in einem neuen Chat mit Standing Block + neuem Chapter Spec + einem kurzen "was gerade passiert ist"-Recap.

### Running Recap Document

Ein zusätzliches Arbeitsdokument im Projekt führen: einen **Running Recap** — drei bis fünf Sätze pro abgeschlossenem Kapitel, nur Fakten und Tonnotizen.

Beispiel:
> Ch. 3 ends with the body discovered. Sable and Theron are now working together. Calden has spoken only to Sable so far.

Nach jedem fertigen Kapitel aktualisieren. Den relevanten Tail in den `### Continuity`-Block des nächsten Kapitels einfügen. Das hält Stimm- und Faktenkontinuität straff, ohne Prompts aufzublähen.

### Revision innerhalb eines Kapitels

In derselben Konversation bleiben, gezielte Passes anfragen:
> "Tighten the handshake scene — the calluses observation is reading too obvious; make Theron file it faster."

Keine kompletten Rewrites anfragen, sondern den spezifischen Beat. Kapitel locken, dann neuen Chat fürs nächste öffnen.

---

## Eine Vorab-Entscheidung

**Chapter-to-Step Mapping.** Am einfachsten: 12 Kapitel, eines pro Step — passt sauber zu den Pacing Notes.

Wenn ein längeres Buch gewünscht ist: jetzt entscheiden, wo die Splits liegen. **Step 6 (das Reveal)** und **Step 10 (der Academy-Theory-Klick)** sind die beiden Beats, die laut Pacing Notes Raum brauchen — also die natürlichen Kandidaten, jeweils auf zwei Kapitel zu splitten.
