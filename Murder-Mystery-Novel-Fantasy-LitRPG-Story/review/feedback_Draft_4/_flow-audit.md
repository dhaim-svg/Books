# Flow Audit — *The Skybound Wyrm* Draft_4

## Überblick

Die automatische Messung bestätigt Davids Eindruck und zeigt: Das Problem ist **buchweit** — alle 40 Kapitel überschreiten mindestens einen Schwellwert. Schlimmste Ausreißer (Score-Hierarchie): **Kap. 34 (146), Kap. 30 (138), Kap. 09 (135), Kap. 38 (135), Kap. 37 (132)** — relativ am unauffälligsten sind **Kap. 22 (67), Kap. 20 (70), Kap. 22 (75)**. Der Score-Bereich (67–146) zeigt, dass es **keine binäre OK/nicht-OK-Entscheidung** gibt, sondern eine klare Prioritätsliste für Revisionen.

Das Problem ist kein Gesamtversagen, sondern ein *Register-Clash*: Beschreibung und Analyse laufen flüssig (oft 40–80 Wörter pro Satz), aber zwei spezifische Strukturpositionen brechen den Fluss — (1) **Szenenübergang-Einzeiler** (`Theron went.` / `He got up.` / `He waited.`) und (2) **Dialog-Regieanweisungen** (`He wrote: … He looked up … He stood`). Beide sind repetitiv kurz und subjekt-initial; der Sprung zwischen den Registern ist das, was sich als „abgehackt" anfühlt.

**Methodische Anmerkung:** Die Messung arbeitet auf Satzebene (Satzgrenzen per Regex). Die Opener-Ketten sind deshalb meist `"The"`, nicht `"He"` — `"He"`-Ketten erscheinen eher auf Absatz-Ebene (Ein-Satz-Absätze). Beide Phänomene sind Indikatoren desselben Tics; `%Subj` enthält `He/She/Theron/Sable/His/Her/They/It/The`. Die qualitativen Hotspot-Zitate (Abschnitt unten) zeigen die konkreten Textstellen.

## Flag-Schwellen

| Indikator | Rot wenn … |
|---|---|
| Avg sentence length (words) | < 11.5 |
| % short sentences (≤6 w) | > 26.0% |
| Longest consecutive short-sentence chain | ≥ 3 |
| Longest consecutive same-opener chain | ≥ 3 |
| % subject-opener sentences | > 33.0% |

## Heatmap — alle Kapitel (sortiert nach Score)

| Ch | Avg(w) | %Short | MaxShortChain | %Subj | MaxOpenerChain | Score | Flag |
|---|---|---|---|---|---|---|---|
| **34** | 11.4 | 45.4% | 8 | 54.2% | 10 | 146.3 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **30** | 10.8 | 46.7% | 11 | 57.5% | 7 | 137.9 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **09** | 10.9 | 50.2% | 11 | 46.3% | 7 | 135.4 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **38** | 14.9 | 50.3% | 8 | 58.6% | 8 | 135.0 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **37** | 14.5 | 43.0% | 6 | 70.3% | 9 | 131.5 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **32** | 11.0 | 48.3% | 6 | 55.8% | 6 | 129.3 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **33** | 12.9 | 38.6% | 6 | 57.4% | 11 | 127.2 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **40** | 15.5 | 41.2% | 9 | 58.2% | 8 | 122.7 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **06** | 10.5 | 47.0% | 6 | 45.8% | 9 | 120.7 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **36** | 12.2 | 47.8% | 7 | 55.4% | 7 | 119.0 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **31** | 11.2 | 42.4% | 7 | 58.3% | 6 | 117.8 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **35** | 9.6 | 52.8% | 7 | 44.2% | 4 | 115.7 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **29** | 14.5 | 28.8% | 4 | 78.1% | 9 | 110.6 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **11** | 11.8 | 44.4% | 5 | 54.9% | 6 | 109.2 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **12** | 11.5 | 44.0% | 5 | 59.8% | 6 | 109.2 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **39** | 15.3 | 42.1% | 5 | 57.2% | 7 | 109.2 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **05** | 10.3 | 48.0% | 6 | 43.8% | 7 | 108.3 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **08** | 12.6 | 45.2% | 9 | 46.5% | 5 | 104.3 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **10** | 12.4 | 45.3% | 6 | 47.8% | 5 | 103.9 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **07** | 9.7 | 52.2% | 7 | 45.0% | 4 | 102.2 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **03** | 10.9 | 46.8% | 6 | 41.9% | 7 | 99.9 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **16** | 11.2 | 44.4% | 6 | 52.3% | 5 | 96.5 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **28** | 13.4 | 37.7% | 5 | 65.9% | 5 | 96.1 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **04** | 12.0 | 42.1% | 7 | 48.9% | 4 | 94.0 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **15** | 9.9 | 48.8% | 9 | 36.7% | 4 | 92.4 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **14** | 10.1 | 47.7% | 9 | 38.3% | 3 | 92.2 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **23** | 10.8 | 43.8% | 10 | 41.4% | 4 | 91.4 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **27** | 12.3 | 34.3% | 5 | 63.3% | 5 | 87.4 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **26** | 12.8 | 34.3% | 5 | 49.8% | 6 | 87.3 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **02** | 11.8 | 41.9% | 10 | 47.3% | 2 | 86.1 | 🚩 %short>26.0%, chain≥3, %subj>33.0% |
| **17** | 10.1 | 46.9% | 8 | 38.5% | 3 | 86.0 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **13** | 10.4 | 46.8% | 6 | 42.9% | 3 | 82.9 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **01** | 14.2 | 34.1% | 5 | 52.0% | 5 | 82.8 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **21** | 9.5 | 49.2% | 7 | 34.3% | 3 | 81.1 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **19** | 11.5 | 36.6% | 8 | 36.2% | 4 | 79.8 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **18** | 11.4 | 37.4% | 5 | 44.4% | 4 | 76.8 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **24** | 11.4 | 40.3% | 5 | 42.7% | 4 | 75.8 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **25** | 13.8 | 35.1% | 4 | 55.6% | 4 | 75.8 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **20** | 10.4 | 49.0% | 5 | 32.4% | 3 | 69.7 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3 |
| **22** | 9.5 | 41.7% | 5 | 28.4% | 3 | 67.0 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3 |

## Hotspots — flagged chapters

_Longest short-sentence chains and same-opener chains with quoted snippets. Sentence indices are zero-based within the cleaned prose (excluding markdown headings and system notes)._

### Chapter 34 (score 146.3, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (8 sents <=6w, sents 235-242):** ""Miss Verrin," she said." / ""Miss Renn."" / ""You're named on the order."" / ""I am."" …
  - **Short-chain (5 sents <=6w, sents 172-176):** "One row passes all six lines."" / ""That row is mine."" / ""That row is yours."" / "She did not say yes" …
  - **Short-chain (5 sents <=6w, sents 132-136):** "Quiet method, mostly" / "He did not write it down."" / "He set the letter back down." / "He did not look up" …
  - **Opener-chain (10× "She", sents 81–90):** "She looked at it." / "She did not lean forward" / "She did not need to lean forward; the desk was small and she could…" / "She read it" …
  - **Opener-chain (5× "He", sents 186–190):** "He waited." / "He had decided in his cabin that the waiting would not be a tactic" / "He had decided that he would put the work down on the desk and would…" / "He had decided, in the slow count he had done with his hands flat on…" …
  - **Opener-chain (4× "The", sents 263–266):** "The hum through the deck was the hum" / "The cup on the desk was a cup" / "The sealed sheet beside the cup was sealed" / "The case book was closed."

### Chapter 30 (score 137.9, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (11 sents <=6w, sents 266-276):** ""All right," she said." / ""All right."" / ""Tomorrow."" / ""Tomorrow."" …
  - **Short-chain (6 sents <=6w, sents 87-92):** "She set the finger down" / ""He didn't know it was there."" / ""No."" / ""He couldn't have noticed it" …
  - **Short-chain (5 sents <=6w, sents 178-182):** ""It doesn't register as cast magic."" / ""It registers as ambient field" / "If it registers at all."" / ""On standing-detection."" …
  - **Opener-chain (7× "The", sents 226–232):** "The cabin sketch" / "The scry log" / "The abstract turned face-up under all of it." / "The Arms was almost down for the night" …
  - **Opener-chain (5× "The", sents 107–111):** "The cabin was a rectangle" / "The door was a thicker line on the corridor side" / "The bolt was a small notch on the inside of the door" / "The porthole was a circle on the outer wall with a latch mark on the…" …
  - **Opener-chain (5× "He", sents 153–157):** "He had it because the Wyrm captain had given it to him on the first…" / "He had read the sheet at the time" / "He had filed it under no cast magic in cabin twelve during the third…" / "He unfolded it now" …

### Chapter 09 (score 135.4, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (11 sents <=6w, sents 241-251):** "That's all right."" / ""It's all right."" / ""It is."" / ""Are you teasing me."" …
  - **Short-chain (10 sents <=6w, sents 193-202):** ""That's fair," she said." / ""Is it."" / ""I think so" / "It's your method" …
  - **Short-chain (6 sents <=6w, sents 53-58):** ""You opened with the general."" / ""I opened with the general."" / ""And the time."" / ""And the time" …
  - **Opener-chain (7× "He", sents 274–280):** "He passed Calden's pantry on the way and did not look in" / "He passed cabin twelve and made the small registration he had been…" / "He went up the stair" / "He let himself into his own cabin and put the slate on the writing…" …
  - **Opener-chain (4× "The", sents 72–75):** "The early window was the one that mattered" / "The late window — the one that closed on Calden's return to the…" / "The early window was a different shape" / "The early window was three minutes before Calden had even left the…"
  - **Opener-chain (4× "She", sents 154–157):** "She booked the gondola specifically because Vannic had booked it" / "She placed herself within four hours of him for the duration of the…" / "She has, by her own account, no alibi for the early window on the…" / "She has an alibi for one point in the night — the four minutes Calden…"

### Chapter 38 (score 135.0, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (8 sents <=6w, sents 40-47):** ""That'll do."" / ""It will."" / "He looked at Sable." / ""Miss Verrin."" …
  - **Short-chain (7 sents <=6w, sents 24-30):** ""Mr" / "Mavik" / "Miss Verrin."" / ""Mr" …
  - **Short-chain (6 sents <=6w, sents 115-120):** "He did not write it down." / "He wrote one more line." / "> J. Aldis" / "Coastal" …
  - **Opener-chain (8× "He", sents 121–128):** "He sat for a moment with his hand on the cover" / "He was aware, in the way a man was aware of a thing he had set on a…" / "He did not name the thing in the notebook" / "He did not name it to himself in any sentence longer than the…" …
  - **Opener-chain (6× "She", sents 158–163):** "She finished her tea" / "She tore a small piece of bread and ate it without preserve" / "She set her cup down the half-inch back from the rim of the table…" / "She put her right hand into her coat pocket, briefly, and rested two…" …
  - **Opener-chain (4× "The", sents 167–170):** "The lane in front of the inn was a working lane at first bell with…" / "The southern morning light was lower and harder than the afternoon's…" / "The cat from the inn step was not on the step this morning" / "The step was wet from the boy's bucket and the cat had taken itself…"

### Chapter 37 (score 131.5, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 133-138):** ""There's a room here."" / ""They had two."" / ""Then there are two."" / ""Mm."" …
  - **Short-chain (5 sents <=6w, sents 115-119):** "The screen had dismissed itself" / "He had not asked it to." / ""All right," he said." / ""All right."" …
  - **Short-chain (5 sents <=6w, sents 17-21):** ""Cider" / "We've got a cider that's hot."" / ""That."" / ""Back porch?"" …
  - **Opener-chain (9× "She", sents 74–82):** "She was looking at him." / "She did not look away." / "She did not lift her hand to her mug" / "She did not pick up the pencil" …
  - **Opener-chain (8× "The", sents 55–62):** "The first sentence was the name of the talent and was a name." / "The second sentence was about the shape of the suspect he had been…" / "The gap was Halsa" / "The gap was every working illusionist on the Mirren coast he had been…" …
  - **Opener-chain (5× "She", sents 105–109):** "She let that sit." / "She picked up her mug, then" / "She wrapped both hands around it again" / "She did not drink" …

### Chapter 32 (score 129.3, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 306-311):** ""It's a quiet morning," she said." / ""It is."" / ""Quieter than I'd have thought."" / ""I'd have thought louder."" …
  - **Short-chain (6 sents <=6w, sents 127-132):** ""Mark it."" / "She read on." / "Cabin five" / "Cabin six" …
  - **Short-chain (6 sents <=6w, sents 92-97):** "The line was enough." / ""Cabin two."" / ""The Stallens" / "Mother and adult son" …
  - **Opener-chain (6× "He", sents 258–263):** "He gave it the small dry nod that was the only answer it had ever…" / "He looked at the name at the foot of the page." / "He let himself look at it for a slow count he did not count." / "He had not, on a Thursday morning in November, in a dining room two…" …
  - **Opener-chain (6× "He", sents 201–206):** "He turned the case book." / "He opened the requirements page to its second face" / "He had left it blank yesterday morning at the foot of the six working…" / "He had not, on Wednesday, known which it would be." …
  - **Opener-chain (5× "He", sents 280–284):** "He thought." / "He had not, until she asked, thought of the answer in the form of a…" / "He had thought of it in the form of a shape: a room, two doors, the…" / "He had not let himself dwell on the shape because the shape was…" …

### Chapter 33 (score 127.2, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 167-172):** ""I didn't think it would be."" / ""It's warm" / "That's all it was."" / "He took the cup" …
  - **Short-chain (6 sents <=6w, sents 7-12):** ""Mr" / "Mavik."" / ""He's expecting me."" / ""He is" …
  - **Short-chain (5 sents <=6w, sents 193-197):** "Sable was at his elbow." / ""Theron."" / ""I'm not going down there."" / ""I know" …
  - **Opener-chain (11× "He", sents 26–36):** "He read it once" / "He drank coffee" / "He read it a second time and turned the page." / "He read the scry log without comment, which Theron took as the answer…" …
  - **Opener-chain (5× "The", sents 157–161):** "The southbound morning service lifted from the Halverstow…" / "The dock was a quarter the size of the city dock at the southern…" / "The handler was a long-armed older woman whose name badge read Roe,…" / "The hum it made through the boot soles was the same hum the Wyrm had…" …
  - **Opener-chain (4× "He", sents 218–221):** "He did not walk to it yet." / "He set the leather strap on the writing desk" / "He set the case book on top of it" / "He sat with his hands flat on the case book for the length of a slow…"

### Chapter 40 (score 122.7, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (9 sents <=6w, sents 109-117):** ""I'll hold it."" / ""She'll write you from the cottage."" / ""She said so."" / ""All right."" …
  - **Short-chain (6 sents <=6w, sents 124-129):** ""Mirren Vale," Theron said." / ""Inland coach" / "The half of one."" / ""That."" …
  - **Short-chain (5 sents <=6w, sents 138-142):** "The lower's all coach traffic."" / ""The upper."" / ""I'll mark it in the chit."" / "He marked it in the chit" …
  - **Opener-chain (8× "He", sents 99–106):** "He read the line once" / "He did not nod for it" / "He set it down inside his head where he had set the line on the…" / "He took the slip off the table." …
  - **Opener-chain (6× "The", sents 160–165):** "The strap was warm in the cold of the early afternoon, the leather…" / "The driver's elbow found the rest on the door rail with the small…" / "The coach moved" / "The lane began to slide back at the slow working pace of a coach…" …
  - **Opener-chain (6× "The", sents 64–69):** "The paper was a clerk's paper, not a chandler's" / "The fold was a clerk's fold" / "The lines on the inside were two — a fee in a number that meant…" / "The date was the third of July of the same year" …

### Chapter 06 (score 120.7, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 180-185):** ""I'll speak to the captain."" / ""Sir."" / ""Calden."" / ""Sir."" …
  - **Short-chain (5 sents <=6w, sents 196-200):** "He could feel his page accumulating" / "It was a satisfying feeling." / ""Thank you, Calden."" / ""Sir."" …
  - **Short-chain (5 sents <=6w, sents 167-171):** "Theron made a note." / ""Calden" / "The administrative matter."" / ""Sir."" …
  - **Opener-chain (9× "He", sents 220–228):** "He had not poured the noon pot either" / "He poured neither now." / "He opened the notebook to Esherel's page" / "He read the page through" …
  - **Opener-chain (8× "He", sents 209–216):** "He had Esherel on the page" / "He had Calden's with the captain's leave on the page" / "He had the M. Tannin amendment for the captain at second-watch end,…" / "He kept the lounge" …
  - **Opener-chain (5× "He", sents 239–243):** "He felt the small steadying pleasure of a method working" / "He did not know that he was feeling it" / "He felt it the way he felt the harness chains through the deck — as a…" / "He moved his thumb off the graduation pin" …

### Chapter 36 (score 119.0, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (7 sents <=6w, sents 41-47):** "She did not lock it" / "She picked the bag back up." / ""Mr" / "Mavik."" …
  - **Short-chain (6 sents <=6w, sents 84-89):** ""Mr" / "Mavik."" / ""Master Ottren."" / ""Mr" …
  - **Short-chain (5 sents <=6w, sents 134-138):** "Mavik."" / ""It was Mr" / "Davren's manner" / "I was carrying it."" …
  - **Opener-chain (7× "He", sents 7–13):** "He stood." / "He put on the coat he had hung on the hook by the door" / "He picked up the leather strap" / "He slid the case book into the strap and tied the strap with the…" …
  - **Opener-chain (5× "The", sents 65–69):** "The gondola had set down while they were in the corridor" / "The gangway was already laid" / "The Sannholt slip was a working slip, not a passenger pier —…" / "The gull on the pile had not moved" …
  - **Opener-chain (5× "She", sents 38–42):** "She had her right hand free" / "She looked at Theron and at Sable and at the strap under Theron's arm…" / "She set the bag down beside her foot to close the door of cabin six" / "She did not lock it" …

### Chapter 31 (score 117.8, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (7 sents <=6w, sents 244-250):** "She did not take the coat" / "She left it on the chair" / ""I have to write to Pessel."" / ""What about?"" …
  - **Short-chain (7 sents <=6w, sents 16-22):** ""You haven't written."" / ""No."" / ""You're waiting."" / ""I was waiting for you" …
  - **Short-chain (5 sents <=6w, sents 257-261):** ""Theron."" / ""Yes."" / ""The list is good."" / ""Thank you."" …
  - **Opener-chain (6× "The", sents 164–169):** "The first line: Pessel, eleven years, Sunday afternoon" / "The second line: Pessel again, because that was what an apprentice…" / "The third line: the thesis abstract and the working-theory four lines…" / "The fourth line: trigger known to caster, not to target — the…" …
  - **Opener-chain (5× "The", sents 214–218):** "The shape on the page had a person in it" / "The person was not on the page" / "The person was, however, on the passenger manifest at the…" / "The person had eleven years of Pessel's testimony behind her and a…" …
  - **Opener-chain (5× "He", sents 103–107):** "He turned to a fresh page in the case book." / "He did not write Halsa Renn across the top" / "He did not write a date" / "He wrote, in the unindented hand he used for working theory not yet…" …

### Chapter 35 (score 115.7, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (7 sents <=6w, sents 289-295):** ""Both of you."" / ""It was a question," Sable said" / ""It needed the answer it needed."" / ""Yes."" …
  - **Short-chain (7 sents <=6w, sents 16-22):** "Did anyone use his real name."" / "Theron waited a count." / ""His real name," he said." / ""Joren Aldis" …
  - **Short-chain (6 sents <=6w, sents 106-111):** "Not a magistrate's letter" / "A person" / "He heard it" / "He did not argue."" …
  - **Opener-chain (4× "She", sents 234–237):** "She set both hands flat on her knees again, palms down, the way she…" / "She looked at the case book" / "She looked at the sealed-and-now-unsealed note" / "She looked at the folded paper."
  - **Opener-chain (4× "She", sents 222–225):** "She put her right hand into the right pocket of her coat" / "She brought out a small flat object — a piece of folded paper, folded…" / "She set it on the desk beside the case book" / "She did not slide it toward him."
  - **Opener-chain (4× "She", sents 204–207):** "She picked it up." / "She broke the wax with her thumb the way a person broke the wax of a…" / "She unfolded the sheet" / "She read it once"

### Chapter 29 (score 110.6, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (4 sents <=6w, sents 141-144):** ""Now," Theron said." / ""Good answer" / "The host moved on." / "He ate the soup"
  - **Short-chain (3 sents <=6w, sents 110-112):** "He read it back" / "The pencil hovered" / "He did not underline."
  - **Short-chain (3 sents <=6w, sents 79-81):** "He went on reading" / "The abstract was a page long" / "He read the entire page"
  - **Opener-chain (9× "He", sents 91–99):** "He opened the case book to the method page." / "He did not write the method is the scryproof glamour exploit." / "He had written that kind of sentence before, in his second-year…" / "He had carried the marginal note since" …
  - **Opener-chain (7× "He", sents 101–107):** "He had written, nine months ago, non-laboratory conditions in the dry…" / "He had not written, anywhere in the thesis, what a non-laboratory…" / "He had not been writing a case" / "He had been writing a theoretical paper" …
  - **Opener-chain (6× "The", sents 206–211):** "The tide was on the turn, and the rope-master from yesterday had a…" / "The Arms' kitchen smelled, now, of bread, which meant the host had…" / "The coach to Halverstow from the north was due at last bell." / "The case book sat on the table" …

### Chapter 11 (score 109.2, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 50-54):** "I am siding with Gravel" / "He is not getting it" / "I am giving him time" / "Wisp capped the gauge" …
  - **Short-chain (5 sents <=6w, sents 37-41):** "He did not say so." / ""You're listening for something," Wisp said." / ""I'm listening to it."" / ""All right."" …
  - **Short-chain (4 sents <=6w, sents 267-270):** "Tannin at the second tier" / "Vellaine at the third" / "The two windows in series" / "The corridor in pencil"
  - **Opener-chain (6× "He", sents 163–168):** "He read it" / "He read it twice" / "He thought about flinching at it and chose, again, not to." / "He capped the pencil" …
  - **Opener-chain (5× "The", sents 269–273):** "The two windows in series" / "The corridor in pencil" / "The lunch scene noted with a tick under demeanor under stress" / "The four-crate scene with a second tick beside it" …
  - **Opener-chain (5× "He", sents 141–145):** "He took the bench at the end that was not the brass and put the slate…" / "He worked the page." / "He drew Esherel's column with a finer hand than yesterday" / "He drew the corridor's geometry from the long memory of having walked…" …

### Chapter 12 (score 109.2, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 194-198):** "She offered."" / ""She did, did she."" / ""I had not asked."" / ""Of course you had not asked" …
  - **Short-chain (5 sents <=6w, sents 171-175):** ""Held."" / ""You asked Wisp."" / ""I asked the bolt" / "Wisp confirmed."" …
  - **Short-chain (5 sents <=6w, sents 105-109):** "The early window" / "The late window" / "The corridor sightline from the table" / "The corridor sightline from the door" …
  - **Opener-chain (6× "He", sents 127–132):** "He listened for the secondary note he had named yesterday and was…" / "He left it in the cabin-twelve margin and did not connect it to…" / "He was not at that page." / "He was at this one." …
  - **Opener-chain (5× "The", sents 7–11):** "The two windows in series, drawn on a single line" / "The corridor in pencil" / "The lunch scene with its tick" / "The four-crate scene with its tick" …
  - **Opener-chain (5× "He", sents 232–236):** "He almost smiled" / "He did not, but the not-smiling was, again, the kind the table got…" / "He took the slate up to his cabin at the close of the bronzed hour." / "He set it on the writing desk parallel to the desk's far edge, in the…" …

### Chapter 39 (score 109.2, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 124-128):** ""You're going on holiday," she said." / ""I'm going on holiday."" / ""You haven't said where."" / ""I haven't decided" …
  - **Short-chain (5 sents <=6w, sents 13-17):** "He took his palm back." / "Investigator — field interval" / "The street is quiet" / "Read the street." …
  - **Short-chain (4 sents <=6w, sents 150-153):** ""Two days," she said." / ""Two days."" / ""Then the coach."" / ""Then the coach.""
  - **Opener-chain (7× "She", sents 112–118):** "She picked up the two papers together." / "She did not separate them" / "She opened her notebook to the back, where the cover-fold made a…" / "She closed the notebook" …
  - **Opener-chain (5× "The", sents 56–60):** "The outer face had Joren's family's name at the top and a place…" / "The place was three lines: the parish, the road, the marker" / "The parish was Tellan's Cross" / "The road was the inner coast road, by the chandler's stile" …
  - **Opener-chain (4× "The", sents 1–4):** "The front room of the inn did not have very much to do at first bell…" / "The basket-and-dog woman had finished her tea and left a small clean…" / "The carters in the lane outside had finished one load and were on the…" / "The barman had moved from glasses to spoons and was working a thin…"

### Chapter 05 (score 108.3, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 233-238):** "He went over" / "He did not sit." / ""Dr" / "Vellaine."" …
  - **Short-chain (6 sents <=6w, sents 189-194):** ""Mr" / "Mavik" / "Sit, if you're sitting."" / "He sat." …
  - **Short-chain (6 sents <=6w, sents 137-142):** "A knock at the door" / "Two raps, light." / ""Mr" / "Mavik?"" …
  - **Opener-chain (7× "He", sents 293–299):** "He held his palm against the plate a moment longer than he needed to." / "He had a working list" / "He had a captain's silence on the wireless to the last hour" / "He had Esherel at 1 and a sealed administrative amendment at 2 and a…" …
  - **Opener-chain (6× "He", sents 282–287):** "He turned to go" / "He had taken two steps before her last answer caught up with him —…" / "He did not turn around" / "He did not have the second pot of categorical thinking in him yet for…" …
  - **Opener-chain (4× "He", sents 133–136):** "He read it twice" / "He couldn't tell whether his class was being instructive or dry" / "He chose to read it as both" / "He had nine hours to do the rest of it before he had any business…"

### Chapter 08 (score 104.3, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (9 sents <=6w, sents 173-181):** "He set the cup down." / ""I'll find you after," he said." / ""In the corridor" / "I'll be at the alcove."" …
  - **Short-chain (7 sents <=6w, sents 28-34):** ""Cabin," she said." / ""He'll say or he won't" / "The captain didn't authorize the cabin."" / ""Mm" …
  - **Short-chain (6 sents <=6w, sents 6-11):** ""He gave it," Theron said, sitting." / ""Conditional?"" / ""On Calden's consent" / "Which he'll give."" …
  - **Opener-chain (5× "The", sents 189–193):** "The man had a morning behind him — Theron didn't know what, exactly;…" / "The man had a half-second slowing past a door because he had been…" / "The man had stood off-station for twelve minutes on the fourth watch…" / "The man would have a face when Theron arrived" …
  - **Opener-chain (4× "He", sents 194–197):** "He was going to ask him a difficult question" / "He should arrive at the question by the route a person would, not by…" / "He had the captain's order" / "He did not have to use it as the first sentence."
  - **Opener-chain (4× "He", sents 106–109):** "He could have answered the forty-one correction more cleanly than he…" / "He took his coffee black" / "He left the lemon biscuits alone the first day and ate them the second" / "He noticed the cook the second night — not the steward, the cook, who…"

### Chapter 10 (score 103.9, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 216-221):** ""At my cabin" / "After dinner" / "Or in the morning."" / ""In the morning."" …
  - **Short-chain (6 sents <=6w, sents 199-204):** ""You said."" / ""I'm saying it again."" / "He walked it" / "Motive" …
  - **Short-chain (6 sents <=6w, sents 134-139):** ""She did not raise her voice" / "She raised the body" / "The room heard her."" / ""Yes."" …
  - **Opener-chain (5× "He", sents 236–240):** "He did not write the underline." / "He thought about it" / "He sat with the pencil capped in his hand for the length of time it…" / "He decided that the morning was the right shape and that the morning…" …
  - **Opener-chain (5× "He", sents 112–116):** "He looked at both columns" / "He became, briefly and with no productive result, aware of how much…" / "He capped the pencil" / "He had not written the conclusion" …
  - **Opener-chain (4× "The", sents 205–208):** "The four-crate scene at the breakfast and the small clean way the…" / "The early window and the late window in series" / "The corridor geometry" / "The letter as one weight on one side of a beam that had three weights…"

### Chapter 07 (score 102.2, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (7 sents <=6w, sents 112-118):** "He moved on." / ""What about Calden?"" / "She considered" / ""Calden likes him."" …
  - **Short-chain (7 sents <=6w, sents 16-22):** "He cleared his throat." / "Calden's chin lifted" / ""Mr" / "Mavik" …
  - **Short-chain (6 sents <=6w, sents 200-205):** ""But Calden would" / "He'd come out for every round" / "He told you that, didn't he" / "Quiet through every pass."" …
  - **Opener-chain (4× "The", sents 166–169):** "The first-class corridor on deck four was the kind of quiet that…" / "The captain's address had ended, the passengers had returned, and the…" / "The cabin twelve door was sealed with Calden's wax and a small folded…" / "The lamp at the corridor's mid-point was lit; the lamp at the end…"
  - **Opener-chain (3× "He", sents 185–187):** "He stood here while we were talking yesterday afternoon and shifted…" / "He shifts when he's been here a while" / "He didn't think about it"
  - **Opener-chain (3× "He", sents 143–145):** "He didn't say what the errand was" / "He said he'd need the captain's leave for that, same as he told you" / "He just answered me before he said it"

### Chapter 03 (score 99.9, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 158-163):** "Vellaine turned a page" / ""It's not even third watch."" / ""I know."" / ""Then you'll lie there and think."" …
  - **Short-chain (5 sents <=6w, sents 123-127):** ""I'm going to sleep."" / ""All right" / "She didn't argue" / ""Then dinner's in an hour, sir" …
  - **Short-chain (5 sents <=6w, sents 83-87):** ""You like Petal best."" / ""I like Petal most peacefully" / "I don't have favorites" / "Don't write that down."" …
  - **Opener-chain (7× "He", sents 187–193):** "He hung his coat" / "He took the slate out of the breast pocket and laid it on the writing…" / "He undid the collar of his shirt" / "He sat on the edge of the bed." …
  - **Opener-chain (4× "The", sents 34–37):** "The drawer was not locked" / "The slate was within reach" / "The exercise was not for the slate" / "The exercise was for him."
  - **Opener-chain (4× "He", sents 196–199):** "He couldn't tell, again, whether the System was being dry on purpose" / "He chose, again, to read it as such" / "He found that he was smiling at the slate and that he didn't…" / "He turned the lamp down."

### Chapter 16 (score 96.5, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 94-99):** "Three times" / "That's the shape of it."" / "Theron sat with it." / ""The accent," she said." …
  - **Short-chain (5 sents <=6w, sents 128-132):** "Joren Aldis's hands."" / ""Joren Aldis's hands."" / "He waited." / ""The fourth," she said" …
  - **Short-chain (5 sents <=6w, sents 75-79):** ""The elderly passenger on the step" / "He waited" / "No gesture, no production" / "Just the three seconds."" …
  - **Opener-chain (5× "He", sents 153–157):** "He held the stillness" / "He was aware of the window, the harbor, the coal barge making its…" / "He was aware of the cloth bag on the desk" / "He was aware of the specific texture of the morning three days ago in…" …
  - **Opener-chain (4× "He", sents 159–162):** "He had heard it" / "He had stored it under small talk between two people who have been…" / "He had turned the slate over." / "He had not asked why."
  - **Opener-chain (4× "He", sents 109–112):** "He wrote nothing" / "He had no slate" / "He was aware of the absence of the slate in the way he had been…" / "He was not sure whether to name the absence out loud and decided not…"

### Chapter 28 (score 96.1, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 96-100):** "He stopped." / "He read the line." / "He did not underline anything." / "He sat back" …
  - **Short-chain (4 sents <=6w, sents 202-205):** "The method was not coming tonight." / "He was, however, certain" / "He let the certainty be private" / "He kept the case book closed."
  - **Short-chain (4 sents <=6w, sents 111-114):** "Method — unknown." / "He drank the cold coffee." / "The afternoon brought the second post." / "There was no letter from Sable"
  - **Opener-chain (5× "He", sents 122–126):** "He would have done the same" / "He approved of it without making a particular point of approving of…" / "He drew the working profile out, and the partial transcript, and the…" / "He had the who." …
  - **Opener-chain (5× "He", sents 11–15):** "He kept the order he had practised: cabin nine-T, the Kolach…" / "He named the apprentice line from Pessel and was careful to say…" / "He did not raise his voice" / "He did not say the suspect" …
  - **Opener-chain (4× "He", sents 183–186):** "He took it as the acknowledgement it was." / "He turned the case book back to the column page and looked at the…" / "He had been certain about the who since Davren's first question this…" / "He had not articulated the certainty in those words because the…"

### Chapter 04 (score 94.0, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (7 sents <=6w, sents 69-75):** ""Calden," he said" / ""Step out, please" / "Keep the corridor as it is" / "Nobody in, nobody past."" …
  - **Short-chain (5 sents <=6w, sents 212-216):** ""Are you all right, Mr" / "Mavik," she said" / "It was not a question." / ""I'd prefer to be by lunch."" …
  - **Short-chain (5 sents <=6w, sents 167-171):** "The trouser pockets last" / "A short comb" / "Three coins, low denomination" / "A blue-headed pin." …
  - **Opener-chain (4× "The", sents 117–120):** "The dressing coat was good wool, dark blue, cut for a man with…" / "The collar was pinned with the enamel knot, pinned correctly, evenly,…" / "The hands were not clenched" / "The right hand lay open on the bedclothes, the fingers where he had…"
  - **Opener-chain (4× "The", sents 98–101):** "The pen was on the blotter, dry, the nib cleaned" / "The chair was tucked in" / "The desk lamp was unlit." / "The porthole"
  - **Opener-chain (4× "His", sents 59–62):** "His shoes were off and on the floor beside the bed, square to one…" / "His right hand was open on the bedclothes, palm half up" / "His eyes were closed" / "His mouth was very slightly open"

### Chapter 15 (score 92.4, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (9 sents <=6w, sents 230-238):** "Traveling through to Sannholt" / "Family" / "Cash" / "Early sleeper" …
  - **Short-chain (7 sents <=6w, sents 182-188):** ""Through to Sannholt" / "I have family there" / "Her voice was level, unhurried." / ""You'll take the coast road?"" …
  - **Short-chain (6 sents <=6w, sents 34-39):** ""Alone?"" / ""As far as I saw" / "Briefly" / "He paused again" …
  - **Opener-chain (4× "She", sents 57–60):** "She had her receipts in order" / "She had heard nothing unusual on the third night" / "She had been awake at first watch reading contracts and asleep before…" / "She had not, to her knowledge, interacted with any other third-class…"
  - **Opener-chain (3× "She", sents 189–191):** "She said she did small-contract labour, seasonal, had spent the last…" / "She had paid cash, which she acknowledged plainly, because she always…" / "She had no professional reference he could check, which she also…"
  - **Opener-chain (3× "He", sents 77–79):** "He confirmed the funeral, gave the name of his brother, named the…" / "He had taken his sleeping draught at second watch and had no memory…" / "He showed Theron the empty vial still tucked in the pocket of his…"

### Chapter 14 (score 92.2, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (9 sents <=6w, sents 92-100):** "She set the cup down" / ""What was he, really" / "The illusionist."" / ""A professional" …
  - **Short-chain (6 sents <=6w, sents 127-132):** "Theron looked up from the notebook" / ""When did you notice that?"" / ""Second night" / "Before the first-class lounge closed" …
  - **Short-chain (5 sents <=6w, sents 242-246):** "Theron looked at the manifest" / "Fourteen names" / "Four blanks" / "One address in a shared port." …
  - **Opener-chain (3× "He", sents 257–259):** "He had been carrying it since cabin three-T without opening it, and…" / "He now had the beginnings of the questions" / "He untied the cord."
  - **Opener-chain (3× "He", sents 72–74):** "He was just — present" / "He listened when people spoke" / "He looked at the room"
  - **Opener-chain (2× "The", sents 265–266):** "The third confirmed the final payment and gave Joren's boarding time…" / "The fourth was shorter."

### Chapter 23 (score 91.4, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (10 sents <=6w, sents 73-82):** ""I have."" / ""The cargo trace" / "It wasn't a question." / ""Partial result," he said" …
  - **Short-chain (9 sents <=6w, sents 125-133):** "The voice" / "Not Esherel's voice" / "Similar precision, different register." / ""I'm sorry," he said" …
  - **Short-chain (5 sents <=6w, sents 235-239):** "Returned to pocket" / "Private." / "Below that: Not afraid" / "Himself." …
  - **Opener-chain (4× "He", sents 208–211):** "He had written Joren's name across the top of the case file when the…" / "He had not known about the corridor" / "He had not known about the second-watch moment, the small private…" / "He closed the case book."
  - **Opener-chain (2× "The", sents 183–184):** "The outer coat pocket" / "The right one."
  - **Opener-chain (2× "The", sents 124–125):** "The confusion lasted one more beat — and then he had it" / "The voice"

### Chapter 27 (score 87.4, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 117-121):** "The child's mother knows" / "The child does not" / "Pessel held the money." / "He read that" …
  - **Short-chain (5 sents <=6w, sents 27-31):** "She made the tea" / "She handed me a cup" / "She sat down" / "Then she said:" …
  - **Short-chain (4 sents <=6w, sents 6-9):** "The column was four lines long" / "Cabin nine-T. Booking credential through Kolach" / "Sannholt destination" / "Status: in front of us"
  - **Opener-chain (5× "She", sents 59–63):** "She held the money, Theron" / "She has been holding it for two years" / "She had been waiting for him to come home and tell the mother what he…" / "She said this without any tone in it" …
  - **Opener-chain (5× "She", sents 43–47):** "She made them clean enough for the registries he had to file with" / "She did not ask him what the work was" / "She had a sense" / "She is not naive." …
  - **Opener-chain (5× "He", sents 108–112):** "He stopped" / "He read the column." / "He added a fourth line, under the others: Question four — what…" / "He did not answer it" …

### Chapter 26 (score 87.3, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 56-60):** "He paused" / ""Mavik."" / ""Yes."" / ""The name on that list" …
  - **Short-chain (4 sents <=6w, sents 192-195):** "Status: in front of us." / "He set the pencil down." / "Investigator — Working column: Renn, Halsa" / "Status updated: in front of us."
  - **Short-chain (4 sents <=6w, sents 103-106):** "Joren's professional network" / "Status: working suspect, evidentiary basis incomplete." / "He read the System line once" / "He didn't touch it"
  - **Opener-chain (6× "He", sents 73–78):** "He had filed Halsa Renn at the time of the Wyrm interview as…" / "He had marked the cash booking as low-tier, because his frame was…" / "He had been wrong about the frame" / "He had written that down in the working column." …
  - **Opener-chain (4× "The", sents 89–92):** "The Sannholt destination he had filed as innocuous geography" / "The cabin-nine-T late lamp Calden had flagged with uncertain…" / "The observation Sable had made about how Renn watched corridors" / "The detail in the Wyrm interview about hearing a creak from toward…"
  - **Opener-chain (3× "He", sents 155–157):** "He did not write Halsa Renn was Joren's apprentice in the case book" / "He had not earned that line" / "He wrote, in the new column: Sannholt source confirms coastal female…"

### Chapter 02 (score 86.1, %short>26.0%, chain≥3, %subj>33.0%)

  - **Short-chain (10 sents <=6w, sents 149-158):** "The look was thorough." / ""Investigator class," he said" / ""First posting" / "I do that."" …
  - **Short-chain (8 sents <=6w, sents 111-118):** "He liked classifiers" / "They were easier to talk to." / ""Juridical theory," he said" / ""Anything I'd have come across?"" …
  - **Short-chain (8 sents <=6w, sents 92-99):** ""Theron Mavik" / "The pin gives me away?"" / ""You keep it straight" / "She returned to the book" …
  - **Opener-chain (2× "The", sents 170–171):** "The Wyrm shifted slightly as Mottled corrected her stroke — he felt…" / "The pastries had been very good"
  - **Opener-chain (2× "The", sents 68–69):** "The seal on the folio's cover was a family firm, not a registered…" / "The ring on her right hand was formal silver; the traveling clothes…"
  - **Opener-chain (2× "The", sents 33–34):** "The correction rippled backward through the lines and emerged at the…" / "The equipment hatch at the far end of the promenade opened"

### Chapter 17 (score 86.0, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (8 sents <=6w, sents 107-114):** "She turned one page" / ""The review concluded eighteen months ago" / "I have the letter."" / ""I — yes," Vannic said" …
  - **Short-chain (6 sents <=6w, sents 221-226):** ""The east yard," he said" / ""Would it overlap with the west" / "Berric Toll is west harbour, Mirren."" / ""Not naturally" …
  - **Short-chain (5 sents <=6w, sents 191-195):** ""I know of him."" / ""Maret Fell" / "East Mirren harbour, shipping assessment."" / "The pilot's face shifted slightly" …
  - **Opener-chain (3× "He", sents 144–146):** "He found the footnote" / "He read it" / "He set the folio on the desk."
  - **Opener-chain (3× "He", sents 37–39):** "He'll give you the full account; he's been expecting it" / "He hired Aldis for the performance and met him twice — once at the…" / "He has no motive I've identified for Aldis's death, and his presence…"
  - **Opener-chain (2× "The", sents 189–190):** "The pilot made a face that was not quite a confirmation and not quite…" / "The kind of face people made when they had an opinion about a name…"

### Chapter 13 (score 82.9, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 123-128):** "You boarded separately as Petor Vann" / "Who knew?"" / ""The factor" / "Joren, obviously" …
  - **Short-chain (5 sents <=6w, sents 216-220):** ""The apology is implicit."" / "The corner of Sable's mouth moved" / ""Start with the word sorry" / "It takes four seconds."" …
  - **Short-chain (4 sents <=6w, sents 209-212):** "He looked up" / "The lamp ticked again" / ""I owe Esherel a conversation."" / ""You owe her an apology"
  - **Opener-chain (3× "The", sents 32–34):** "The third-class starboard passage was painted a yellower white than…" / "The lamp at the far end needed trimming" / "The gondola's hang had a slight asymmetry here, a lean in the deck…"
  - **Opener-chain (2× "The", sents 230–231):** "The lamp at the top of the landing was well-trimmed and bright" / "The one at the bottom had needed work"
  - **Opener-chain (2× "The", sents 227–228):** "The question is not who had access" / "The question is who had reason."

### Chapter 01 (score 82.8, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 143-147):** ""Calden" / "A brief pause" / ""Thank you" / "For — all of it" …
  - **Short-chain (4 sents <=6w, sents 182-185):** "Adjusting" / ""Hm" / "He released the handshake" / ""Well"
  - **Short-chain (3 sents <=6w, sents 187-189):** "Calden followed" / "Theron stood with his key." / "First posting, and no active case"
  - **Opener-chain (5× "He", sents 72–76):** "He had not needed it twice." / "He was aware, standing there, that a man who had just passed his…" / "He was also aware that this awareness was itself slightly insufferable" / "He noted it" …
  - **Opener-chain (4× "He", sents 244–247):** "He had made the right choice not to become a naturalist" / "He would have been insufferable about drakes." / "He moved his thumb off the pin, and left it there." / "He became aware, sometime in the next few minutes, that he didn't…"
  - **Opener-chain (4× "He", sents 106–109):** "He tested the lamp; it worked" / "He pressed once on the mattress to confirm it was a mattress rather…" / "He set his case on the writing desk, hung his coat on the hook by the…" / "He was getting air"

### Chapter 21 (score 81.1, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (7 sents <=6w, sents 131-137):** "Serious commission work, not one-off assessments" / "I was never offered that category."" / ""Why not?"" / ""I didn't want it offered" …
  - **Short-chain (6 sents <=6w, sents 219-224):** "He passed the note to Sable." / "She read it" / ""Active box" / "Real address."" …
  - **Short-chain (6 sents <=6w, sents 29-34):** "Then she looked at Theron." / ""TL-9," he said" / ""Not a standard dock-authority code" / "Not in the Gray Quay key" …
  - **Opener-chain (3× "She", sents 12–14):** "She wore the same coat as the factors' board day, or one like it —…" / "She looked at the table, at the slate, at Sable's notebook, and at…" / "She sat when the constable indicated the chair."
  - **Opener-chain (2× "The", sents 212–213):** "The note was from the clearing house at the south Halverstow station" / "The handwriting was a clerk's, neat and quick and impersonal"
  - **Opener-chain (2× "The", sents 20–21):** "The word doing its small work." / "The first ten minutes established the facts both parties already knew…"

### Chapter 19 (score 79.8, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (8 sents <=6w, sents 178-185):** "A moment passed" / ""He knew someone was looking."" / ""He suspected" / "Or he'd been warned" …
  - **Short-chain (5 sents <=6w, sents 240-244):** "Investigator — Status: Fell/Toll thread confirmed" / "Joren's awareness noted" / "Next step: location of Fell" / "Thread is narrowing." …
  - **Short-chain (5 sents <=6w, sents 223-227):** ""I don't know," he said" / ""I'll go back."" / ""Don't," Sable said" / ""Write him a note" …
  - **Opener-chain (4× "The", sents 12–15):** "The packet held three sheets" / "The first was a cover from the clerk, formal and brief: the TL-9 flag…" / "The results were attached" / "The clerk had underlined the result in the second sheet himself,…"
  - **Opener-chain (2× "The", sents 261–262):** "The case had the right name in it" / "The thread had the right shape"
  - **Opener-chain (2× "The", sents 6–7):** "The messenger was twelve, the kind of twelve that had done this many…" / "The wax impression on the seal was the magistrate's stamp, which…"

### Chapter 18 (score 76.8, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 139-143):** "Sable came level with him" / ""That's a day" / "Possibly two."" / ""Yes" …
  - **Short-chain (4 sents <=6w, sents 78-81):** ""Looking for what?"" / ""The coach schedule" / "The Sannholt run."" / "He turned from the window"
  - **Short-chain (3 sents <=6w, sents 163-165):** ""If Pessel writes promptly."" / ""If Pessel writes at all" / "He turned from the harbor"
  - **Opener-chain (4× "He", sents 157–160):** "He had the TL-9 notation" / "He had the six-day gap" / "He had the factors' board flagged and the Sannholt letter drafted in…" / "He had the correct name in the case log, and the case log was where…"
  - **Opener-chain (2× "The", sents 184–185):** "The harbor water moved under the boards" / "The unlit lantern sat on its crate, patient."
  - **Opener-chain (2× "The", sents 150–151):** "The TL-9 notation sat in his notes between two known facts and one gap" / "The notation was new: spring only, absent from the autumn and winter…"

### Chapter 24 (score 75.8, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 161-165):** ""I know" / "She closed the notebook" / ""And if she's protective —"" / ""She will be."" …
  - **Short-chain (5 sents <=6w, sents 147-151):** "That's the thread I'm running here" / "He tapped the third-class list" / ""And the re-examination."" / ""Any movement on the re-examination?"" …
  - **Short-chain (4 sents <=6w, sents 98-101):** "She pointed to a row" / ""There are three in that category" / "One of them is Maret Fell."" / "He looked at the page"
  - **Opener-chain (4× "He", sents 191–194):** "He worked until mid-afternoon, when the light through the window…" / "He had built a new working column: the re-examination, the four…" / "He had written to the harbor registry about Vantrel Secured Storage's…" / "He had noted Calden's lamp observation in its proper place, uncertain…"
  - **Opener-chain (3× "He", sents 108–110):** "He said one of the quiet-cabin ones, the no-contact passengers, had a…" / "He'd noted it at the time as insomnia or reading and hadn't flagged…" / "He wasn't certain which cabin.""
  - **Opener-chain (3× "He", sents 48–50):** "He had written down that Sable had said the same thing about Renn…" / "He put the pencil down." / "He wrote across the bottom of the Renn entry: Revisit"

### Chapter 25 (score 75.8, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (4 sents <=6w, sents 29-32):** "That was not nothing." / ""The Kolach vouching entry," Theron said." / "The clerk nodded" / ""Unusual"
  - **Short-chain (3 sents <=6w, sents 131-133):** "He didn't say anything" / "There was nothing particular to say." / "She took it"
  - **Short-chain (2 sents <=6w, sents 169-170):** "That was something" / "The rest was work."
  - **Opener-chain (4× "The", sents 140–143):** "The door latched." / "The yard man stepped back" / "The driver released the brake and spoke to the horses — the same…" / "The coach rolled across the yard stones toward the gate, iron wheels…"
  - **Opener-chain (4× "The", sents 106–109):** "The driver finished with the harness and climbed to the box, settling…" / "The yard man called the boarding" / "The woman at the window picked up her bags" / "The two merchants concluded their argument and moved toward the door"
  - **Opener-chain (3× "The", sents 149–151):** "The second coach was still being loaded" / "The woman who had been arguing with the booking clerk was at the…" / "The boy went past with an empty cart and disappeared into the stable…"

### Chapter 20 (score 69.7, avg<11.5w, %short>26.0%, chain≥3, opener≥3)

  - **Short-chain (5 sents <=6w, sents 197-201):** "Sable paused" / ""She's not clean on TL-9."" / ""No" / "He stood" …
  - **Short-chain (5 sents <=6w, sents 64-68):** ""Toll also named Joren to you" / "By name, or by description?"" / ""By name" / "Joren" …
  - **Short-chain (4 sents <=6w, sents 247-250):** ""Start with Fell," Sable said" / ""The rest follows, or it doesn't" / "She gathered her satchel" / ""Write the magistrate's note now"
  - **Opener-chain (3× "The", sents 19–21):** "The room was large — harbor-facing, as reported, with a window…" / "The bed was made" / "The writing desk had a stack of correspondence on it, half-sorted,…"
  - **Opener-chain (3× "He", sents 255–257):** "He had Roven's name" / "He had Fell's location" / "He had the shape of the fourth point and a meeting in the morning."
  - **Opener-chain (2× "He", sents 119–120):** "He was not performing anything now" / "He just looked tired, and somewhat chastened, and also like a man who…"

### Chapter 22 (score 67.0, avg<11.5w, %short>26.0%, chain≥3, opener≥3)

  - **Short-chain (5 sents <=6w, sents 194-198):** "The postmark was Sannholt." / "He broke the seal." / "Mr" / "Mavik —" …
  - **Short-chain (4 sents <=6w, sents 237-240):** ""I know," he said." / ""You don't need to come" / "She said it without edge" / "Purely practical"
  - **Short-chain (4 sents <=6w, sents 229-232):** "He looked at her." / ""Friday run," she said" / ""It's Wednesday" / "That's two days"
  - **Opener-chain (3× "The", sents 192–194):** "The seal was a small wax impression he didn't recognize" / "The direction on the outside was his name at the Arms, in a hand he…" / "The postmark was Sannholt."
  - **Opener-chain (2× "He", sents 201–202):** "He had written to say he would be here by the third week of the month…" / "He is now past his expected date by eleven days, which I had put down…"
  - **Opener-chain (2× "He", sents 77–78):** "He said this after I asked a similar question" / "He was not hostile about it, but he was clear"

---

*Generated by `tools/flow_audit.py`. Qualitative findings (quoted examples + rewrite patterns per tic-type) are appended in the section below.*

---

## Qualitative Findings

_Read by Explore agents against the flagged hotspot locations. Findings are organized by tic-type, not by chapter, because the same structural problem drives all the scores._

### Tic-Type A — Dialogue Stage-Direction One-Liners

The dominant pattern across all 40 chapters: action beats staged as single short sentences opening with a subject pronoun, often standing as their own one-line paragraph.

**Representative example — Chapter 34, lines 27–31:**
> "They came to cabin six.
>
> He knocked.
>
> He knocked once and waited..."

**Representative example — Chapter 38, lines 147–149:**
> "He drank the cider down.
>
> He buckled the strap.
>
> He inclined his half-inch..."

These are mostly type **(B) dialogue stage-direction beats** — procedural, tense, deliberate. They are not wrong individually. The problem is density: when every beat-transition in a scene is written this way, the reader stops feeling the intended precision and starts reading through the tics. Three or more of these in one scene costs the *recoil effect* the short sentence should produce.

**Fix principle: Merge two beats into one compound, or use an adverbial lead for the second.**

> *Before:* "He drank the cider down. He buckled the strap."
> *After:* "He drank the cider down and buckled the strap." *(one compound action)*
>
> *Before:* "He knocked. He knocked once and waited."
> *After:* "He knocked once and waited." *(collapse the false doublet)*

---

### Tic-Type B — Anaphoric "She/He did not" Chains

The worst-scoring chapter for this is **Chapter 37 (score 131.5, %subj 70.3%)**, where the following passage appears (approximately lines 75–89):

> "She did not look away.
>
> She did not lift her hand to her mug. She did not pick up the pencil. She did not turn her face toward the harbour. She sat with her hands in her lap below the edge of the table and she watched him read the screen a second time..."

Five "She" openers in 14 lines. The negation anaphora ("She did not X / She did not Y / She did not Z") is syntactically identical in each clause and creates mechanical repetition that undercuts the intended effect of patient witness.

**Fix principle: Adverbial lead + object-first restructuring + selective merging.**

> *Before:* "She did not look away. She did not lift her hand to her mug. She did not pick up the pencil. She did not turn her face toward the harbour. She sat with her hands in her lap..."
>
> *After:* "Without looking away, without lifting her hand to her mug or picking up the pencil or turning her face toward the harbour, Sable sat with her hands in her lap and watched him read the screen a second time."

*Principle:* Consolidate the four "She did not" negations into a single adverbial unit. Replace the final "she" with "Sable" to break the pronoun run and provide a strong subject anchor. The effect of unwavering refusal is preserved; the mechanical anaphora is not.

A related instance in **Chapter 38, lines 133–139:**
> "He stopped.
>
> He looked at the line he had written and at the white space below it. He had written the procedure. He had not written the case.
>
> He did not write it down.
>
> He wrote one more line."

Four "He" openers in 6–7 sentences. Here the fix is opener variation:

> *After:* "He stopped. The line he had written sat under his pencil; below it, white space. He had written the procedure. The case was the part he had been carrying since cabin twelve, and he did not write it down. One more line, then he closed the notebook."

---

### Tic-Type C — Procedural Narration (He read / He wrote / He folded)

**Chapter 30, lines 213–221** — the "Halsa Renn satisfied" and "The theory explained" anaphoric structures:

> "The theory explained the cabin. The theory explained the scry. The theory required three things..."
>
> "Halsa Renn satisfied the first. Halsa Renn satisfied the second, by inference. Halsa Renn satisfied the third because the trigger was hers."

Both passages are intentionally anaphoric (echoing the structure of legal argumentation), which *works* as a deliberate rhetorical device. This is **type C — intentional staccato that serves the scene**. The mechanical audit flags it; the qualitative read confirms it's structurally justified. **These chains should not be revised.**

By contrast, **Chapter 33, lines 139–141** shows an accidental echo that should be revised:
> "It's warm. That's all it was. He took the cup. It was warm. That was all it was."

The near-verbatim repetition ("It's warm. That's all it was." / "It was warm. That was all it was.") reads as an authorial stutter rather than an intentional callback. One instance should be cut.

---

### Chapter 9 — Note on Type C (Intentional, Working)

**Chapter 9, lines 163–165:**
> "He stopped. He did not put the pencil down. He let it rest on the slate at the angle it was at."

This was classified by the agent as **(C) intentional staccato that works** — Theron's mental and physical arrest when confronted with Sable's reinterpretation of Esherel's letter. The choppy micro-beats reinforce processing under pressure. The mechanical score is high for this chapter, but this particular cluster is structurally justified. The overall chapter score (135.4) reflects density across multiple scenes, not that every short sequence needs fixing.

**Key distinction:** A short-sentence chain in a discovery/reaction beat (type C) is a deliberate rhythmic tool and should be kept. The same chain in a pedestrian stage-direction beat (type B) or a scene-transition (type A) is a tic that costs flow without gaining effect.

---

### Tic-Type D — Screenplay Beat Marker ("A beat.")

Found in **3 chapters only** (02, 06, 16). Example from Chapter 2, line 21:

> *A beat. "Wisp's been adjusting the harness rigging since first watch."*

`A beat.` is a screenwriting stage direction. In theatre and film scripts it signals a pause to the actor; in a novel it *describes* a pause rather than showing it through action, silence, or rhythm. It reads as meta and slightly theatrical — an instruction to an actor that slipped through into the narration.

**Low frequency, easy fix.** Three occurrences means it won't affect the flow score, but each instance is a simple inline replacement during revision.

**Fix principle: Replace with a small grounding action, or let the paragraph break carry the pause.**

> *Before:* "A beat. "Wisp's been adjusting the harness rigging since first watch.""
>
> *After (action):* "Calden smoothed the towel once across his arm. "Wisp's been adjusting the harness rigging since first watch.""
>
> *After (paragraph break alone):* End the previous line as its own paragraph; the dialogue opens the next one cold. The pause is already latent in the surrounding prose — removing `A beat.` without replacement is often sufficient.

---

### Summary: Four Fix Principles for Revision Agents

When revising for flow, apply these in order of frequency:

| Priority | Tic | Fix principle | Where it appears |
|---|---|---|---|
| 1 (most common) | Stage-direction one-liner chains (He/She + short verb, 3+ in a row) | Merge two beats into one compound, or use adverbial lead for the second | All 40 chapters; worst in ch-34, ch-30 |
| 2 | "She/He did not X / did not Y / did not Z" negation anaphora | Adverbial consolidation ("Without X-ing or Y-ing, she...") | Ch-37, ch-38, ch-09 |
| 3 | Accidental verbatim echo within a paragraph | Cut one instance | Ch-33 |
| 4 | Screenplay beat marker ("A beat.") | Replace with small grounding action, or remove and let the paragraph break carry the pause | Ch-02, ch-06, ch-16 only |

**Do NOT revise:** Intentional anaphora for rhetorical effect (Halsa/theory chains in ch-30; discovery-beat staccato in ch-09 lines 163–165). When in doubt, classify by function: if the chain is carrying *procedural* information (he moved, he looked, he picked up), vary it; if it's carrying *psychological* information (she would not yield; he could not name it), keep it.

---

*End of qualitative findings. Next step: targeted revision of the highest-scoring chapters, starting with ch-34 (146.3) and ch-37 (131.5), using `tools/flow_audit.py` post-revision as objective before/after verification.*
