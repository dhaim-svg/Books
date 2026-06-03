# Flow Audit — *The Skybound Wyrm* Draft_5

## Überblick

Die automatische Messung bestätigt Davids Eindruck: **40 von 40 Kapiteln** (100%) liegen bei mindestens einem Fluss-Indikator im roten Bereich. Schlimmste Ausreißer: **Kap. 32, Kap. 35, Kap. 38, Kap. 30, Kap. 34**. Das Problem ist kein Gesamtversagen, sondern ein *Register-Clash*: Beschreibung und Analyse laufen flüssig (oft 40–80 Wörter pro Satz), aber Szenenübergänge (`Theron went.` / `He got up.`) und Dialog-Regieanweisungen (`He wrote: … He looked up … He stood`) sind repetitiv kurz und subjekt-initial — der Sprung zwischen beiden Registern ist es, der sich als abgehackt anfühlt. Die Hotspot-Liste unten zeigt die genauen Stellen.

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
| **32** | 11.2 | 46.7% | 6 | 55.2% | 5 | 123.4 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **35** | 9.9 | 50.8% | 8 | 42.4% | 4 | 116.9 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **38** | 15.6 | 46.7% | 8 | 54.9% | 5 | 115.2 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **30** | 11.2 | 45.3% | 5 | 56.7% | 6 | 113.9 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **34** | 12.0 | 42.8% | 8 | 51.0% | 4 | 111.7 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **09** | 11.0 | 49.6% | 8 | 45.4% | 4 | 110.8 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **31** | 11.2 | 41.3% | 5 | 58.0% | 6 | 110.2 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **37** | 15.0 | 41.4% | 4 | 69.1% | 6 | 108.7 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **40** | 16.1 | 37.4% | 9 | 54.6% | 5 | 105.4 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **36** | 12.7 | 46.9% | 6 | 52.0% | 5 | 105.0 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **11** | 12.0 | 42.9% | 5 | 54.3% | 5 | 103.2 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **12** | 11.8 | 40.8% | 5 | 58.8% | 5 | 102.3 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **16** | 11.4 | 43.1% | 6 | 52.6% | 5 | 96.1 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **05** | 10.8 | 47.0% | 6 | 42.7% | 4 | 94.4 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **10** | 12.7 | 42.9% | 5 | 45.8% | 4 | 94.4 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **07** | 9.9 | 50.6% | 6 | 43.7% | 3 | 93.4 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **29** | 14.7 | 26.1% | 3 | 75.8% | 6 | 91.9 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **08** | 12.8 | 43.4% | 8 | 45.3% | 3 | 91.4 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **33** | 13.3 | 36.9% | 5 | 57.3% | 4 | 91.4 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **06** | 10.9 | 44.2% | 5 | 43.4% | 4 | 90.9 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **39** | 15.4 | 40.9% | 4 | 54.1% | 4 | 89.7 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **28** | 13.7 | 34.4% | 4 | 64.7% | 4 | 83.6 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **14** | 10.3 | 45.8% | 8 | 37.0% | 2 | 83.3 | 🚩 avg<11.5w, %short>26.0%, chain≥3, %subj>33.0% |
| **04** | 12.2 | 39.8% | 5 | 47.6% | 3 | 81.9 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **02** | 12.0 | 39.5% | 9 | 45.5% | 2 | 81.2 | 🚩 %short>26.0%, chain≥3, %subj>33.0% |
| **17** | 10.1 | 46.7% | 8 | 36.7% | 2 | 80.5 | 🚩 avg<11.5w, %short>26.0%, chain≥3, %subj>33.0% |
| **03** | 11.1 | 44.3% | 4 | 39.3% | 4 | 77.6 | 🚩 avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **27** | 12.8 | 29.6% | 3 | 58.6% | 5 | 77.2 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **15** | 10.3 | 47.8% | 7 | 36.4% | 2 | 76.9 | 🚩 avg<11.5w, %short>26.0%, chain≥3, %subj>33.0% |
| **23** | 11.0 | 42.5% | 8 | 40.1% | 2 | 75.2 | 🚩 avg<11.5w, %short>26.0%, chain≥3, %subj>33.0% |
| **26** | 13.0 | 33.7% | 5 | 47.3% | 3 | 72.4 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **13** | 10.7 | 45.2% | 4 | 42.5% | 2 | 71.5 | 🚩 avg<11.5w, %short>26.0%, chain≥3, %subj>33.0% |
| **21** | 9.7 | 46.8% | 5 | 33.8% | 2 | 68.7 | 🚩 avg<11.5w, %short>26.0%, chain≥3, %subj>33.0% |
| **01** | 14.5 | 32.4% | 3 | 51.4% | 3 | 66.7 | 🚩 %short>26.0%, chain≥3, opener≥3, %subj>33.0% |
| **18** | 11.6 | 34.8% | 5 | 42.9% | 2 | 66.0 | 🚩 %short>26.0%, chain≥3, %subj>33.0% |
| **20** | 10.5 | 48.1% | 5 | 31.4% | 2 | 64.3 | 🚩 avg<11.5w, %short>26.0%, chain≥3 |
| **24** | 11.5 | 38.3% | 4 | 41.1% | 2 | 62.2 | 🚩 %short>26.0%, chain≥3, %subj>33.0% |
| **25** | 14.5 | 31.5% | 2 | 52.7% | 3 | 61.9 | 🚩 %short>26.0%, opener≥3, %subj>33.0% |
| **22** | 9.7 | 41.1% | 5 | 27.5% | 2 | 61.4 | 🚩 avg<11.5w, %short>26.0%, chain≥3 |
| **19** | 11.8 | 34.1% | 5 | 35.7% | 2 | 60.4 | 🚩 %short>26.0%, chain≥3, %subj>33.0% |

## Hotspots — flagged chapters

_Longest short-sentence chains and same-opener chains with quoted snippets. Sentence indices are zero-based within the cleaned prose (excluding markdown headings and system notes)._

### Chapter 32 (score 123.4, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 37-42):** "Quiet method, mostly" / "He did not write it down." / "He read it." / "He read it twice." …
  - **Short-chain (5 sents <=6w, sents 296-300):** "The reading is the courtesy."" / ""All right."" / ""All right."" / "Sable set the cup down" …
  - **Short-chain (5 sents <=6w, sents 230-234):** "She said it." / ""You wrote it," she said." / ""I wrote it."" / ""It's true."" …
  - **Opener-chain (5× "He", sents 206–210):** "He picked up the pencil." / "He held it for the length of one slow breath." / "He had been thinking about this moment, in the back of his head,…" / "He had not, at the time, known what the moment would feel like" …
  - **Opener-chain (4× "She", sents 238–241):** "She did not say anything for the length of a breath" / "She did not pick up her own pencil" / "She did not turn her notebook" / "She read the two words at the foot of the page with the steady look…"
  - **Opener-chain (4× "He", sents 223–226):** "He set the pencil down beside the case book." / "He had a strange small impulse to close the book" / "He did not close it" / "He let the page lie open between them."

### Chapter 35 (score 116.9, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (8 sents <=6w, sents 282-289):** ""Both of you."" / ""It was a question," Sable said" / ""It needed the answer it needed."" / "He considered that." …
  - **Short-chain (5 sents <=6w, sents 215-219):** "He didn't have to write that."" / ""No," Theron said" / ""He didn't."" / ""I'll do that."" …
  - **Short-chain (5 sents <=6w, sents 75-79):** ""That was the wooden fish."" / ""That was the wooden fish."" / ""You knew it was the niece's."" / ""Not on the day," Sable said" …
  - **Opener-chain (4× "He", sents 256–259):** "He took the leather strap off the chair-back where he had set it when…" / "He picked up the case book and slid it into the strap and tied the…" / "He did not pick up the folded paper on the desk" / "He left it where Halsa had set it."
  - **Opener-chain (4× "He", sents 159–162):** "He was not the only mage on the work — there were two of them — and…" / "He knew it was the kind of work that occasionally spilled" / "He took it" / "He had been trying to put aside enough to stop taking that kind of…"
  - **Opener-chain (3× "The", sents 237–239):** "The corridor will be the corridor" / "The morning service runs to second bell" / "The gondola sets down at Sannholt at the third bell"

### Chapter 38 (score 115.2, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (8 sents <=6w, sents 39-46):** ""That'll do."" / ""It will."" / "He looked at Sable." / ""Miss Verrin."" …
  - **Short-chain (7 sents <=6w, sents 24-30):** ""Mr" / "Mavik" / "Miss Verrin."" / ""Mr" …
  - **Short-chain (6 sents <=6w, sents 113-118):** "He did not write it down" / "Instead he wrote one more line." / "> J. Aldis" / "Coastal" …
  - **Opener-chain (5× "He", sents 120–124):** "He was aware, in the way a man was aware of a thing he had set on a…" / "He did not name the thing in the notebook, or to himself in any…" / "He left it where it was, which was on the shelf, which was a place a…" / "He drank the cider down and buckled the strap." …
  - **Opener-chain (3× "The", sents 105–107):** "The working case book is with Ottren" / "The matter is with the Sannholt office" / "The quest closed at the door of the warehouse."
  - **Opener-chain (3× "She", sents 144–146):** "She put preserve on a piece of bread with the back of the spoon and…" / "She did not eat fast" / "She drank her tea"

### Chapter 30 (score 113.9, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 173-177):** ""It doesn't register as cast magic."" / ""It registers as ambient field" / "If it registers at all."" / ""On standing-detection."" …
  - **Short-chain (5 sents <=6w, sents 134-138):** "She stopped at nine-T." / ""She did not pass cabin twelve."" / ""No."" / ""She did not need to."" …
  - **Short-chain (5 sents <=6w, sents 126-130):** ""Cabin twelve" / "Cabin eleven, empty" / "Cabin ten, the Stallens" / "Cabin nine, also empty by then" …
  - **Opener-chain (6× "The", sents 220–225):** "The cabin sketch" / "The scry log" / "The abstract turned face-up under all of it." / "The Arms was almost down for the night" …
  - **Opener-chain (5× "The", sents 109–113):** "The bolt was the Wyrm fitting, original, not tampered" / "The frame is steel-cored" / "The bolt seats into the frame" / "The only override is the steward's — a lift-key through the service…" …
  - **Opener-chain (4× "The", sents 246–249):** "The theory held." / "The theory held against the cabin" / "The theory held against the scry" / "The theory held against the eleven-year apprentice line and the…"

### Chapter 34 (score 111.7, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (8 sents <=6w, sents 224-231):** ""Miss Verrin," she said." / ""Miss Renn."" / ""You're named on the order."" / ""I am."" …
  - **Short-chain (5 sents <=6w, sents 83-87):** "The cabin-eight row was Esherel" / "The cabin-three row was Vellaine." / ""I'm reading it," she said." / ""Take what you need."" …
  - **Short-chain (4 sents <=6w, sents 196-199):** "She looked at the case book." / ""You have it right," she said" / ""What's in the book" / "You have it right.""
  - **Opener-chain (4× "She", sents 183–186):** "She had not, in the time he had been speaking, taken her left hand…" / "She took it out now" / "She set it on her right wrist where the right hand had been before" / "She looked at the case book a moment longer"
  - **Opener-chain (4× "It", sents 139–142):** "It has no commercial application" / "It has no defensive application" / "It has, on the face of it, no application at all" / "It does have the application of doing exactly what was done in cabin…"
  - **Opener-chain (4× "He", sents 169–172):** "He closed the case book." / "He did not push it across the desk" / "He left it where it was, square between them on the small writing…" / "He sat with his hands flat on the closed face of the book."

### Chapter 09 (score 110.8, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (8 sents <=6w, sents 246-253):** ""Are you teasing me."" / ""A little" / "She set the cup down" / ""Not unkindly" …
  - **Short-chain (8 sents <=6w, sents 194-201):** ""That's fair," she said." / ""Is it."" / ""I think so" / "It's your method" …
  - **Short-chain (6 sents <=6w, sents 24-29):** ""Yes."" / ""You knew."" / ""I thought so" / "He told me without telling me" …
  - **Opener-chain (4× "She", sents 127–130):** "She is sitting in her cabin and her dining room and she is rehearsing…" / "She has spent two days making it good" / "She has not slid it under his door" / "She was never going to"
  - **Opener-chain (4× "It", sents 136–139):** "It touched her at the corridor outside Vannic's cabin, where she had…" / "It touched the four rewrites of the third paragraph" / "It touched the half-page stopped at the fourth." / "It also touched, in a part of his attention he was less easily able…"
  - **Opener-chain (4× "He", sents 278–281):** "He went up the stair, let himself into his own cabin, and put the…" / "He moved his thumb off the graduation pin" / "He had not noticed his thumb arriving at the pin." / "He sat down to write up Calden."

### Chapter 31 (score 110.2, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 245-249):** ""I have to write to Pessel."" / ""What about?"" / ""About the seven years."" / "She did not elaborate" …
  - **Short-chain (5 sents <=6w, sents 224-228):** ""Was the work today."" / ""Yes."" / ""Tomorrow is the exclusivity."" / ""Tomorrow is the exclusivity."" …
  - **Short-chain (5 sents <=6w, sents 147-151):** "Required from the victim's side" / "Trust-shaped, not coercion-shaped." / "He read that back twice." / "He did not amend it." …
  - **Opener-chain (6× "The", sents 164–169):** "The first line: Pessel, eleven years, Sunday afternoon" / "The second line: Pessel again, because that was what an apprentice…" / "The third line: the thesis abstract and the working-theory four lines…" / "The fourth line: trigger known to caster, not to target — the…" …
  - **Opener-chain (4× "She", sents 140–143):** "She did not say prodigy" / "She did not say unusual" / "She did not say anything" / "She turned her cup so the handle pointed away from the table edge and…"
  - **Opener-chain (4× "He", sents 197–200):** "He read the line" / "He did not strike it out" / "He did not want to strike it out — striking it out would have been…" / "He picked up the pencil."

### Chapter 37 (score 108.7, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (4 sents <=6w, sents 129-132):** ""There's a room here."" / ""They had two."" / ""Then there are two."" / ""Mm"
  - **Short-chain (4 sents <=6w, sents 37-40):** ""A week," she said." / ""A week."" / ""Counting today."" / ""Counting today.""
  - **Short-chain (3 sents <=6w, sents 123-125):** "They ate." / "The stew was a stew" / "It was the right stew"
  - **Opener-chain (6× "The", sents 56–61):** "The first sentence was the name of the talent and was a name." / "The second sentence was about the shape of the suspect he had been…" / "The gap was Halsa" / "The gap was every working illusionist on the Mirren coast he had been…" …
  - **Opener-chain (4× "The", sents 139–142):** "The slip-cranes worked at the eastern arm." / "The customs boat sat at its tie" / "The oarsman had not come back" / "The gondola at the visitor slip had its two drakes on their tethered…"
  - **Opener-chain (4× "The", sents 1–4):** "The harbour wall ran along the slip for a hundred yards and then bent…" / "The first of them was a chandlery, closed for the afternoon" / "The second was an oil-merchant's" / "The third was an inn with a board hung outside it and one word…"

### Chapter 40 (score 105.4, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (9 sents <=6w, sents 106-114):** ""I'll hold it."" / ""She'll write you from the cottage."" / ""She said so."" / ""All right."" …
  - **Short-chain (6 sents <=6w, sents 121-126):** ""Mirren Vale," Theron said." / ""Inland coach" / "The half of one."" / ""That."" …
  - **Short-chain (4 sents <=6w, sents 90-93):** ""No."" / ""No one."" / ""No one."" / ""All right.""
  - **Opener-chain (5× "The", sents 154–158):** "The strap was warm in the cold of the early afternoon, the leather…" / "The driver's elbow found the rest on the door rail with the small…" / "The coach moved, and the lane began to slide back at the slow working…" / "The wheels found their rhythm at the second turn of the lane and held…" …
  - **Opener-chain (5× "The", sents 116–120):** "The bell at the door rang once on the going out." / "The coach office was across the lane and three doors up from the…" / "The clerk was a thin man at a high desk with a ledger open in front…" / "The chalk for Mirren Vale was clean" …
  - **Opener-chain (4× "The", sents 141–144):** "The barman had bread on the bar and the cold midday cider in the…" / "The strap was on the bench beside him." / "The personal notebook was in the strap." / "The slip with the device on the corner was in the back pocket of the…"

### Chapter 36 (score 105.0, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 77-82):** ""Mr" / "Mavik."" / ""Master Ottren."" / ""Mr" …
  - **Short-chain (5 sents <=6w, sents 127-131):** "Mavik."" / ""It was Mr" / "Davren's manner" / "I was only carrying it."" …
  - **Short-chain (5 sents <=6w, sents 46-50):** "He inclined his head a half-inch." / ""Mr" / "Mavik."" / ""Master Pell."" …
  - **Opener-chain (5× "He", sents 139–143):** "He read the screen." / "He read it a second time, slower, the way a man read a sheet of paper…" / "He had read the quest line in cabin twelve as Solve the Death Aboard…" / "He had carried that title in his head for the better part of a…" …
  - **Opener-chain (3× "The", sents 66–68):** "The order had not been arranged" / "The order had set itself in the corridor." / "The receiving room was the second warehouse from the slip."
  - **Opener-chain (3× "She", sents 151–153):** "She was looking at the gondola in its mooring at the visitor slip" / "She did not look at him" / "She had not seen the screen and she was not going to ask."

### Chapter 11 (score 103.2, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 37-41):** "He did not say so." / ""You're listening for something," Wisp said." / ""I'm listening to it."" / ""All right" …
  - **Short-chain (4 sents <=6w, sents 221-224):** "It is restful."" / ""It is restful."" / ""You should try it sometime."" / "He almost smiled"
  - **Short-chain (4 sents <=6w, sents 203-206):** "There is a slight economy" / "I am being paid in observations" / "She broke the bread" / ""You answered her well.""
  - **Opener-chain (5× "He", sents 97–101):** "He had a moment, in the back of his teeth, where the entire structure…" / "He could ask her now, in this room, about the early window" / "He could ask her about the late one" / "He could ask her about the letter in the folio she had just set her…" …
  - **Opener-chain (4× "He", sents 278–281):** "He was, on inspection, comfortable." / "He did not write the underline on opportunity" / "He turned it over for the length of time it took the lamp oil to warm…" / "He went to find dinner."
  - **Opener-chain (4× "He", sents 157–160):** "He drew the lunch scene under demeanor under stress with a tick" / "He drew the four-crate scene under the same heading with a tick" / "He drew the dining-room arch in pencil and the merchant's table at…" / "He underlined demeanor once and looked at the underline, and decided…"

### Chapter 12 (score 102.3, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 189-193):** "She offered."" / ""She did, did she."" / ""I had not asked."" / ""Of course you had not asked" …
  - **Short-chain (5 sents <=6w, sents 86-90):** ""Thank you, Dr" / "Vellaine."" / ""Mm" / "Have the bread."" …
  - **Short-chain (4 sents <=6w, sents 200-203):** ""I am — grateful."" / ""Mm."" / ""I would have asked."" / ""You would have"
  - **Opener-chain (5× "He", sents 228–232):** "He almost smiled" / "He did not, but the not-smiling went the way of the table again." / "He took the slate up to his cabin at the close of the bronzed hour." / "He set it on the writing desk parallel to the desk's far edge, in the…" …
  - **Opener-chain (5× "He", sents 108–112):** "He was not in the column for completeness" / "He was in it for what was carried." / "He uncapped the pencil" / "He held it for a careful breath" …
  - **Opener-chain (5× "He", sents 14–18):** "He drew the gap on the line and put a tick under it" / "He drew Esherel's table position at the dining-room arch, the…" / "He had built the page on the sightline from the table." / "He had not built it on the sightline from her cabin door." …

### Chapter 16 (score 96.1, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 92-97):** "Three times" / "That's the shape of it."" / "Theron sat with it." / ""The accent," she said." …
  - **Short-chain (5 sents <=6w, sents 125-129):** "Joren Aldis's hands."" / ""Joren Aldis's hands."" / "He waited." / ""The fourth," she said" …
  - **Short-chain (5 sents <=6w, sents 60-64):** "Thank you" / "For the — all of it" / "The boarding business" / "Not a performance" …
  - **Opener-chain (5× "He", sents 150–154):** "He held the stillness" / "He was aware of the window, the harbor, the coal barge making its…" / "He was aware of the cloth bag on the desk" / "He was aware of the specific texture of the morning three days ago in…" …
  - **Opener-chain (4× "He", sents 156–159):** "He had heard it" / "He had stored it under small talk between two people who have been…" / "He had turned the slate over." / "He had not asked why."
  - **Opener-chain (4× "He", sents 70–73):** "He took a ginger sweet from the condiment dish on his tray — the one…" / "He went on eating."" / "He had not seen it" / "He had been facing the opposite direction."

### Chapter 05 (score 94.4, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 191-196):** ""Mr" / "Mavik" / "Sit, if you're sitting."" / "He sat across from her." …
  - **Short-chain (5 sents <=6w, sents 235-239):** "He went over without sitting." / ""Dr" / "Vellaine."" / ""Mr" …
  - **Short-chain (5 sents <=6w, sents 226-230):** ""Noted."" / ""That isn't a yes."" / ""It's a noted."" / "She nodded once" …
  - **Opener-chain (4× "He", sents 294–297):** "He had a captain's silence on the wireless to the last hour, Esherel…" / "He had the method his class had been built to use, and he had…" / "He took his hand off the plate." / "He went to find Calden, who had a sealed administrative note to…"
  - **Opener-chain (4× "He", sents 60–63):** "He filed it with the porthole and the deck hatch and the unbroken…" / "He hung his coat" / "He poured" / "He sat down."
  - **Opener-chain (3× "The", sents 176–178):** "The first-class lounge at noon was the quietest noon it had ever been." / "The captain had made his address at the forward arch ten minutes…" / "The wife of the Henner family had taken her two children to the…"

### Chapter 10 (score 94.4, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 225-229):** "Esherel at the top" / "Tannin at the second tier" / "Vellaine at the third" / "The two windows in series" …
  - **Short-chain (5 sents <=6w, sents 213-217):** ""At my cabin, after dinner" / "Or in the morning."" / ""In the morning."" / ""Probably in the morning."" …
  - **Short-chain (5 sents <=6w, sents 122-126):** ""How was it," she said." / ""How was what."" / ""The four-crate morning."" / ""You heard?"" …
  - **Opener-chain (4× "He", sents 15–18):** "He went down the corridor at the pace he walked when he was thinking…" / "He passed cabin twelve and made the registration he had made eleven…" / "He passed the place where the corridor's slight kink put the porthole…" / "He stopped at it because the geometry had become a habit of stopping,…"
  - **Opener-chain (3× "The", sents 228–230):** "The two windows in series" / "The corridor in pencil" / "The four-crate scene noted under demeanor under stress with a small…"
  - **Opener-chain (3× "The", sents 101–103):** "The line through the columns was uninterrupted" / "The early window covered the approach" / "The late window covered the return."

### Chapter 07 (score 93.4, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (6 sents <=6w, sents 152-157):** "The pen stayed where it was." / ""Theron," he said." / ""Theron."" / ""Not sir."" …
  - **Short-chain (6 sents <=6w, sents 57-62):** ""That's what I have, too" / "She angled her chin slightly" / ""Mostly" / "I have the corridor."" …
  - **Short-chain (6 sents <=6w, sents 16-21):** "He cleared his throat." / "Calden's chin lifted" / ""Mr" / "Mavik" …
  - **Opener-chain (3× "He", sents 124–126):** "He went a half-second slower on every round past Vannic's door" / "He's been going a half-second slower today, too, in the corridors…" / "He doesn't know he's doing it.""
  - **Opener-chain (3× "He", sents 116–118):** "He paused" / "He had been about to ask why she thought so and had heard, in his own…" / "He took a swallow of coffee instead"
  - **Opener-chain (3× "He", sents 89–91):** "He found he was writing" / "He had not consciously decided to write" / "He set the pen down."

### Chapter 29 (score 91.9, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (3 sents <=6w, sents 58-60):** "Th" / "Mavik, final year, Conservatory." / "He read his own abstract."
  - **Short-chain (2 sents <=6w, sents 208-209):** "It was not solved." / "He let it be unsolved"
  - **Short-chain (2 sents <=6w, sents 193-194):** "Investigator — Method page updated" / "Working theory logged"
  - **Opener-chain (6× "He", sents 168–173):** "He was a working investigator now" / "He had been one for three weeks." / "He closed the notebook." / "He sat with the case book open on the method page and the…" …
  - **Opener-chain (6× "He", sents 126–131):** "He let it be a negative shape" / "He did not let it be more" / "He had been at the table for three hours and the host had come past…" / "He did write, in plain ink, under the four lines: To be tested…" …
  - **Opener-chain (5× "He", sents 185–189):** "He picked up the pencil" / "He turned to the back-of-book page, where the Sunday note about the…" / "He wrote, at the bottom of that page, in the smallest hand he had:…" / "He read it." …

### Chapter 08 (score 91.4, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (8 sents <=6w, sents 170-177):** ""I'll find you after," he said." / ""In the corridor" / "I'll be at the alcove."" / ""At the alcove."" …
  - **Short-chain (5 sents <=6w, sents 202-206):** "Calden looked back" / "Calden was waiting to be addressed." / "He let the hand come down." / ""Calden," he said" …
  - **Short-chain (5 sents <=6w, sents 6-10):** ""He gave it," Theron said, sitting." / ""Conditional?"" / ""On Calden's consent, which he'll give."" / ""Today?"" …
  - **Opener-chain (3× "The", sents 121–123):** "The steward took it over" / "The mother didn't see who it came from" / "The child stopped going green about three minutes after she ate it"
  - **Opener-chain (3× "He", sents 190–192):** "He was going to ask him a difficult question" / "He should arrive at the question by the route a person would, not by…" / "He had the captain's order, but he did not have to use it as the…"
  - **Opener-chain (3× "He", sents 149–151):** "He pulled the slate back over, turned it the right way up, and they…" / "He drew the fourth watch as a line; he marked the cabin twelve door…" / "He didn't object"

### Chapter 33 (score 91.4, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 196-200):** "Sable was at his elbow." / ""Theron."" / ""I'm not going down there."" / ""I know" …
  - **Short-chain (5 sents <=6w, sents 124-128):** ""Two copies," he said." / ""Two copies."" / ""The original goes with you" / "The duplicate sits here" …
  - **Short-chain (3 sents <=6w, sents 173-175):** ""I didn't think it would be."" / ""It's warm" / "That's all it was.""
  - **Opener-chain (4× "He", sents 180–183):** "He saw the clerk shake hands with the gondola purser and hand him a…" / "He saw a small grey bag set down beside the clerk's case" / "He did not see the woman who had set it there" / "He looked back at his own gangway and finished the cup."
  - **Opener-chain (3× "The", sents 206–208):** "The river was a thin grey line" / "The wool warehouses were small dark blocks at the harbour edge" / "The two drakes pulled out into the slipstream in a tighter formation…"
  - **Opener-chain (3× "The", sents 165–167):** "The handler was a long-armed older woman whose name badge read Roe,…" / "The hum it made through the boot soles was the same hum the Wyrm had…" / "The bone was the same bone."

### Chapter 06 (score 90.9, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 180-184):** ""I'll speak to the captain."" / ""Sir."" / ""Calden" / "The sealed amendment" …
  - **Short-chain (4 sents <=6w, sents 168-171):** ""Calden" / "The administrative matter."" / ""Sir."" / ""Was it the M. Tannin amendment.""
  - **Short-chain (4 sents <=6w, sents 128-131):** ""Calden."" / ""Mr" / "Mavik."" / ""The night before discovery"
  - **Opener-chain (4× "He", sents 210–213):** "He kept the lounge a moment, the chin in the right hand" / "He filed Verrin, S., still at corner table, still in property papers…" / "He had taken three steps when he registered that he had filed her…" / "He stopped on the stair for a half-second."
  - **Opener-chain (3× "The", sents 191–193):** "The steward poured without looking up" / "The pour was steady" / "The pantry smelled of the same coffee Calden had set in his cabin…"
  - **Opener-chain (3× "The", sents 47–49):** "The letter ran across three pages in a clear merchant's hand" / "The third paragraph was crossed out and rewritten in the margin twice" / "The fourth paragraph was a half-page and stopped mid-sentence."

### Chapter 39 (score 89.7, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (4 sents <=6w, sents 143-146):** "I'll tell you about it after."" / ""After."" / ""After."" / "That was the whole of it."
  - **Short-chain (4 sents <=6w, sents 42-45):** "The inheritance papers" / "Her own." / ""He had it?"" / ""I'd brought it"
  - **Short-chain (4 sents <=6w, sents 13-16):** "Investigator — field interval" / "The street is quiet" / "Read the street." / "He did, for a little while"
  - **Opener-chain (4× "She", sents 50–53):** "She did not open either paper." / "She turned the top one — Pessel's address — through ninety degrees…" / "She did not unfold it" / "She read the outer face"
  - **Opener-chain (3× "The", sents 57–59):** "The parish was Tellan's Cross" / "The road was the inner coast road, by the chandler's stile" / "The marker was third house above the white stone."
  - **Opener-chain (3× "She", sents 111–113):** "She picked up the two papers together." / "She did not separate them" / "She opened her notebook to the back, where the cover-fold made a…"

### Chapter 28 (score 83.6, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (4 sents <=6w, sents 109-112):** "Method — unknown." / "He drank the cold coffee." / "The afternoon brought the second post." / "There was no letter from Sable"
  - **Short-chain (3 sents <=6w, sents 212-214):** "He finished the pie" / "He paid for it" / "He went up the stair."
  - **Short-chain (3 sents <=6w, sents 153-155):** "The door was bolted from inside" / "There was no visible wound" / "The body was Joren Aldis"
  - **Opener-chain (4× "He", sents 175–178):** "He read the System line." / "He did not particularly want the System to be helpful tonight" / "He wanted to be the one who got there" / "He read the line through twice anyway, because the System was not in…"
  - **Opener-chain (4× "He", sents 169–172):** "He stopped writing because he had reached the edge of what he could…" / "He had the shape of the how in the negative" / "He did not have the how in the positive." / "He set the pencil down."
  - **Opener-chain (4× "He", sents 121–124):** "He approved of it without making a particular point of approving of…" / "He drew the working profile out, and the partial transcript, and the…" / "He had the who." / "He read the column down"

### Chapter 14 (score 83.3, avg<11.5w, %short>26.0%, chain≥3, %subj>33.0%)

  - **Short-chain (8 sents <=6w, sents 95-102):** ""What was he, really" / "The illusionist."" / ""A professional" / "He'd done impersonation work before."" …
  - **Short-chain (6 sents <=6w, sents 129-134):** "From the notebook Theron looked up" / ""When did you notice that?"" / ""Second night" / "Before the first-class lounge closed" …
  - **Short-chain (5 sents <=6w, sents 115-119):** ""I thought it was an affectation" / "Some kind of — statement" / "Aristocratic eccentricity" / "She looked at Theron's notebook" …
  - **Opener-chain (2× "The", sents 260–261):** "The packet held four letters and a contract sheet, all written on the…" / "The letters were dated — the earliest was six weeks before the…"
  - **Opener-chain (2× "She", sents 211–212):** "She pushed the manifest toward him" / "She had drawn a soft grid on the corner of a separate sheet — one of…"
  - **Opener-chain (2× "She", sents 204–205):** "She caught the wine-glass grip" / "She observed him orienting to the room.""

### Chapter 04 (score 81.9, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 208-212):** ""Are you all right, Mr" / "Mavik," she said" / "It was not a question." / ""I'd prefer to be by lunch."" …
  - **Short-chain (5 sents <=6w, sents 163-167):** "The trouser pockets last" / "A short comb" / "Three coins, low denomination" / "A blue-headed pin." …
  - **Short-chain (5 sents <=6w, sents 21-25):** ""Mr" / "Mavik," Calden said." / ""How long?"" / ""Six minutes since the first round" …
  - **Opener-chain (3× "The", sents 100–102):** "The deck hatch above the wardrobe" / "The same." / "The chain trunk in the rear wall, the narrow cased channel that…"
  - **Opener-chain (3× "The", sents 89–91):** "The luggage at the bottom: the boarding cart's three cases, all of…" / "The latches had not been opened since they were set in place" / "The dust seal on the brass had not been broken"
  - **Opener-chain (3× "The", sents 54–56):** "The lamp was out" / "The porthole was sealed" / "The deck hatch above the wardrobe was sealed, the brass ring on the…"

### Chapter 02 (score 81.2, %short>26.0%, chain≥3, %subj>33.0%)

  - **Short-chain (9 sents <=6w, sents 147-155):** ""Investigator class," he said" / ""First posting" / "I do that."" / ""At least you know" …
  - **Short-chain (7 sents <=6w, sents 84-90):** "Looked at his coat" / "Looked at his pin." / ""Investigator" / "Said exactly, not unkindly" …
  - **Short-chain (6 sents <=6w, sents 158-163):** ""The reconstruction paper," he said." / ""I have thoughts" / "She turned a page" / ""Some of them favorable."" …
  - **Opener-chain (2× "The", sents 98–99):** "The pin was exactly level, and he did not touch it." / "The coffee arrived in a small copper pot and was, in fact, excellent"
  - **Opener-chain (2× "The", sents 29–30):** "The whole of it had the particular distance of altitude, where cities…" / "The drakes were off the starboard bow, pulling in their spread…"
  - **Opener-chain (2× "The", sents 5–6):** "The cabin was small and well-considered: two portholes, a writing…" / "The lamp bracket was angled exactly right for reading in bed, and the…"

### Chapter 17 (score 80.5, avg<11.5w, %short>26.0%, chain≥3, %subj>33.0%)

  - **Short-chain (8 sents <=6w, sents 107-114):** "She turned one page" / ""The review concluded eighteen months ago" / "I have the letter."" / ""I — yes," Vannic said" …
  - **Short-chain (6 sents <=6w, sents 218-223):** ""The east yard," he said" / ""Would it overlap with the west" / "Berric Toll is west harbour, Mirren."" / ""Not naturally" …
  - **Short-chain (5 sents <=6w, sents 188-192):** ""I know of him."" / ""Maret Fell" / "East Mirren harbour, shipping assessment."" / "Something shifted in the pilot's face" …
  - **Opener-chain (2× "The", sents 73–74):** "The door closed" / "The magistrate looked at Theron."
  - **Opener-chain (2× "The", sents 61–62):** "The aide's chalk went" / "The magistrate wrote two lines"
  - **Opener-chain (2× "The", sents 27–28):** "The aide's chalk moved" / "The magistrate's expression did not."

### Chapter 03 (score 77.6, avg<11.5w, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (4 sents <=6w, sents 175-178):** "He looked up." / ""Good evening, sir."" / ""Good evening."" / ""Drakes are settling"
  - **Short-chain (4 sents <=6w, sents 158-161):** "Vellaine turned a page" / ""It's not even third watch."" / ""I know."" / ""Then you'll lie there and think"
  - **Short-chain (4 sents <=6w, sents 105-108):** ""How do they sleep," he said" / ""In flight."" / ""They don't" / "Not the way you mean"
  - **Opener-chain (4× "He", sents 28–31):** "He could think of three illegitimate ones too, and he watched himself…" / "He picked one at random — the merchant — and filed it there" / "He pulled the intake-notes page up over the manifest and wrote,…" / "He looked at the words"
  - **Opener-chain (3× "He", sents 89–91):** "He had the slate in his jacket" / "He'd forgotten putting it there" / "He must have collected it from the desk drawer on the way out without…"
  - **Opener-chain (2× "The", sents 41–42):** "The exterior promenade was empty when he got there — at this hour,…" / "The drakes were out on long tether, half a sky from the gondola,…"

### Chapter 27 (score 77.2, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (3 sents <=6w, sents 120-122):** "Sable —" / "I have the letter" / "Read it twice"
  - **Short-chain (3 sents <=6w, sents 111-113):** "The child's mother knows" / "The child does not" / "Pessel held the money."
  - **Short-chain (3 sents <=6w, sents 53-55):** "The child's mother knows" / "I held the money."" / "She held the money, Theron"
  - **Opener-chain (5× "He", sents 9–13):** "He had stopped there yesterday afternoon because he had wanted to…" / "He picked up the pencil now to keep going — and then set it down…" / "He had understood that yesterday" / "He did not need to write it out twice." …
  - **Opener-chain (4× "The", sents 154–157):** "The fourth was still open, and he was content to leave it open until…" / "The post-coach to Sannholt left at fourth bell" / "The wire transcript was due Wednesday or Thursday" / "The working profile was on a page, in the order he wanted it in front…"
  - **Opener-chain (4× "The", sents 1–4):** "The Arms was quieter on Sunday than on the working mornings, and…" / "The pot came without asking" / "The toast came without asking" / "The host nodded at his case book and went back to the kitchen."

### Chapter 15 (score 76.9, avg<11.5w, %short>26.0%, chain≥3, %subj>33.0%)

  - **Short-chain (7 sents <=6w, sents 179-185):** ""Through to Sannholt" / "I have family there" / "Her voice was level, unhurried." / ""You'll take the coast road?"" …
  - **Short-chain (5 sents <=6w, sents 59-63):** ""Do you know her by sight?"" / "She thought about it" / ""Brown coat" / "Keeps to herself" …
  - **Short-chain (5 sents <=6w, sents 34-38):** ""Alone?"" / ""As far as I saw" / "Briefly" / "Another pause, then: "She's quiet" …
  - **Opener-chain (2× "The", sents 76–77):** "The empty vial was still tucked in the pocket of his coat, and he…" / "The small kindness of showing it unprompted, the wanting to do the…"
  - **Opener-chain (2× "She", sents 186–187):** "She did small-contract labour, seasonal, she said, and had spent the…" / "She had paid cash, which she acknowledged plainly, because she always…"
  - **Opener-chain (2× "He", sents 265–266):** "He did not know whether Pessel was family or colleague or something…" / "He folded the manifest and put it in his coat."

### Chapter 23 (score 75.2, avg<11.5w, %short>26.0%, chain≥3, %subj>33.0%)

  - **Short-chain (8 sents <=6w, sents 124-131):** "Not Esherel's voice" / "Similar precision, different register." / ""I'm sorry," he said" / ""Please come in" …
  - **Short-chain (7 sents <=6w, sents 75-81):** ""Partial result," he said" / ""Useful, not conclusive."" / "She looked at him steadily" / ""Are you going to get there?"" …
  - **Short-chain (5 sents <=6w, sents 231-235):** "Returned to pocket" / "Private." / "Below that: Not afraid" / "Himself." …
  - **Opener-chain (2× "He", sents 245–246):** "He walked quickly" / "He had letters to write before evening."
  - **Opener-chain (2× "He", sents 206–207):** "He had not known about the corridor, the second-watch moment, the…" / "He closed the case book."
  - **Opener-chain (2× "He", sents 174–175):** "He hadn't seen her — or if he had, he hadn't acknowledged it" / "He put whatever it was back in his pocket after a moment and walked…"

### Chapter 26 (score 72.4, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 56-60):** "He turned the handle, then stopped" / ""Mavik."" / ""Yes."" / ""The name on that list" …
  - **Short-chain (4 sents <=6w, sents 190-193):** "Status: in front of us." / "He set the pencil down." / "Investigator — Working column: Renn, Halsa" / "Status updated: in front of us."
  - **Short-chain (3 sents <=6w, sents 169-171):** "She was in his network" / "Not Vannic's" / "Joren's."
  - **Opener-chain (3× "He", sents 153–155):** "He did not write Halsa Renn was Joren's apprentice in the case book" / "He had not earned that line" / "He wrote, in the new column: Sannholt source confirms coastal female…"
  - **Opener-chain (3× "He", sents 73–75):** "He had filed Halsa Renn at the time of the Wyrm interview as…" / "He had marked the cash booking as low-tier, because his frame was…" / "He had been wrong about the frame, and he had written that down in…"
  - **Opener-chain (3× "He", sents 51–53):** "He did not ask the name aloud" / "He did not offer an interpretation" / "He simply returned to his work, which was, Theron thought, exactly…"

### Chapter 13 (score 71.5, avg<11.5w, %short>26.0%, chain≥3, %subj>33.0%)

  - **Short-chain (4 sents <=6w, sents 138-141):** ""He can confirm everything" / "I have his correspondence."" / ""I'll want the correspondence."" / "Vannic nodded"
  - **Short-chain (4 sents <=6w, sents 122-125):** "Who knew?"" / ""The factor" / "Joren, obviously, and—" Vannic stopped" / "A muscle in his jaw moved"
  - **Short-chain (4 sents <=6w, sents 110-113):** "Then he looked at Theron" / ""Duke Esseven's daughter" / "She is forty-four" / "I am twenty-eight"
  - **Opener-chain (2× "The", sents 225–226):** "The lamp at the top of the landing was well-trimmed and bright" / "The one at the bottom had needed work"
  - **Opener-chain (2× "The", sents 222–223):** "The question is not who had access" / "The question is who had reason."
  - **Opener-chain (2× "The", sents 184–185):** "The page had simply acquired a new first line." / "The Tannin amendment was still in the first-class manifest and still…"

### Chapter 21 (score 68.7, avg<11.5w, %short>26.0%, chain≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 152-156):** "She said it steadily" / ""Not the passenger manifest" / "The freight side."" / ""I'll need the job reference numbers."" …
  - **Short-chain (5 sents <=6w, sents 130-134):** ""Why not?"" / ""I didn't want it offered" / "She met his eyes" / ""I was doing legitimate work, Mr" …
  - **Short-chain (4 sents <=6w, sents 216-219):** ""Active box" / "Real address."" / ""Real address," he said" / ""Pessel exists"
  - **Opener-chain (2× "She", sents 164–165):** "She knew the passage had a Toll connection" / "She almost certainly knew the shape of what she was on the same…"
  - **Opener-chain (2× "Her", sents 105–106):** "Her hands, in her lap, stopped" / "Her gaze, which had been moving between him and the table, stopped."

### Chapter 01 (score 66.7, %short>26.0%, chain≥3, opener≥3, %subj>33.0%)

  - **Short-chain (3 sents <=6w, sents 180-182):** ""Hm" / "He released the handshake" / ""Well"
  - **Short-chain (3 sents <=6w, sents 143-145):** ""Thank you" / "For — all of it" / "The boarding business.""
  - **Short-chain (3 sents <=6w, sents 84-86):** ""Thank you, Calden."" / ""Of course, Mr" / "Mavik.""
  - **Opener-chain (3× "The", sents 223–225):** "The dock had gone" / "The city was going — rooftops, market towers, the long green stripe…" / "The harness chains were singing one clear note in the slipstream."
  - **Opener-chain (3× "He", sents 186–188):** "He was aware of the pin the way he'd been aware of it all morning —…" / "He was also aware that it would take roughly six months to stop…" / "He got the lock open on the fourth angle."
  - **Opener-chain (3× "He", sents 72–74):** "He had not needed it twice." / "He was aware, standing there, that a man who had just passed his…" / "He noted it, and looked at the drakes."

### Chapter 18 (score 66.0, %short>26.0%, chain≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 138-142):** "Sable came level with him" / ""That's a day," she said" / ""Possibly two."" / ""Yes" …
  - **Short-chain (3 sents <=6w, sents 132-134):** ""We don't know" / "He put the notebook away" / ""But the T fits"
  - **Short-chain (3 sents <=6w, sents 115-117):** ""What's TL-9?"" / ""Not a standard code" / "It's not in the key"
  - **Opener-chain (2× "The", sents 149–150):** "The TL-9 notation sat in his notes between two known facts and one gap" / "The notation was new: spring only, absent from the autumn and winter…"
  - **Opener-chain (2× "The", sents 146–147):** "The barge moved on its steady course" / "The launch paced it."
  - **Opener-chain (2× "The", sents 106–107):** "The light was the particular flat yellow of a Halverstow afternoon in…" / "The harbor smell was different now than it had been at the gangway…"

### Chapter 20 (score 64.3, avg<11.5w, %short>26.0%, chain≥3)

  - **Short-chain (5 sents <=6w, sents 64-68):** ""Toll also named Joren to you" / "By name, or by description?"" / ""By name" / "Joren" …
  - **Short-chain (4 sents <=6w, sents 241-244):** ""Possibly Friday" / "Possibly Saturday."" / ""Possibly Friday" / "He closed the notebook"
  - **Short-chain (4 sents <=6w, sents 228-231):** "He's 'aware of the passage.'"" / ""Three points," Theron said." / ""Four" / "She turned from the chart"
  - **Opener-chain (2× "He", sents 255–256):** "He had Roven's name" / "He had Fell's location, and the shape of the fourth point, and a…"
  - **Opener-chain (2× "He", sents 119–120):** "He was not performing anything now" / "He just looked tired, and somewhat chastened, and also like a man who…"
  - **Opener-chain (2× "He", sents 24–25):** "He gestured at the window chair by way of invitation and apparently…" / "He looked at his hands instead."

### Chapter 24 (score 62.2, %short>26.0%, chain≥3, %subj>33.0%)

  - **Short-chain (4 sents <=6w, sents 51-54):** "Wrong frame at time of interview" / "Sannholt thread may have contact." / "Then he turned the page." / "He turned back to Fell's column."
  - **Short-chain (3 sents <=6w, sents 183-185):** "He looked at her" / ""I had bread."" / ""Half a piece," she said."
  - **Short-chain (3 sents <=6w, sents 148-150):** ""And the re-examination."" / ""Any movement on the re-examination?"" / ""Corrections," he said"
  - **Opener-chain (2× "The", sents 102–103):** "The observation-window question was already in his notes" / "The "no further contact" had a small additional mark beside it in…"
  - **Opener-chain (2× "The", sents 92–93):** "The register was Calden's" / "The notation was the same economical hand from the corridor passes…"
  - **Opener-chain (2× "The", sents 66–67):** "The warrant was already moving on Fell" / "The Sannholt thread was not moving yet."

### Chapter 25 (score 61.9, %short>26.0%, opener≥3, %subj>33.0%)

  - **Short-chain (2 sents <=6w, sents 158-159):** "That was the shape of it" / "Two threads"
  - **Short-chain (2 sents <=6w, sents 152-153):** "He read the page" / "It held together"
  - **Short-chain (2 sents <=6w, sents 149-150):** "Kolach vouching" / "Letter of introduction: afternoon"
  - **Opener-chain (3× "The", sents 114–116):** "The boy loaded the last case onto the boot and stepped back" / "The yard man checked it off his list, made a mark, looked up at the…" / "The coach door opened from inside — one of the merchants holding it…"
  - **Opener-chain (3× "He", sents 67–69):** "He had not made a decision about it" / "He had put it somewhere he could reach it and not thought about it…" / "He had taken it out once, in the captain's day-cabin at the dock with…"
  - **Opener-chain (2× "The", sents 137–138):** "The driver released the brake and spoke to the horses — the same…" / "The coach rolled across the yard stones toward the gate, iron wheels…"

### Chapter 22 (score 61.4, avg<11.5w, %short>26.0%, chain≥3)

  - **Short-chain (5 sents <=6w, sents 191-195):** "The postmark was Sannholt" / "He broke the seal." / "Mr" / "Mavik —" …
  - **Short-chain (4 sents <=6w, sents 147-150):** "The whole thing was threaded together."" / ""From Roven's end or from Toll's?"" / ""Both, I think" / "He turned the notebook over"
  - **Short-chain (4 sents <=6w, sents 58-61):** ""How many names" / "Theron asked." / "Vannic looked at him." / ""You said Roven supplied names"
  - **Opener-chain (2× "The", sents 190–191):** "The seal was a small wax impression he didn't recognize, and the…" / "The postmark was Sannholt"
  - **Opener-chain (2× "He", sents 198–199):** "He had written to say he would be here by the third week of the month…" / "He is now past his expected date by eleven days, which I had put down…"

### Chapter 19 (score 60.4, %short>26.0%, chain≥3, %subj>33.0%)

  - **Short-chain (5 sents <=6w, sents 188-192):** ""It's a triangle," Theron said" / ""Three points" / "We have the shape of it."" / ""We don't have how they connect."" …
  - **Short-chain (5 sents <=6w, sents 177-181):** ""He suspected, or he'd been warned" / "Either way, the precaution was specific" / "He showed her the notebook" / ""The TL-9 result came this morning" …
  - **Short-chain (5 sents <=6w, sents 78-82):** "Not just the face" / "He had a whole file."" / ""From whom?"" / ""I assumed Toll" …
  - **Opener-chain (2× "The", sents 12–13):** "The packet held three sheets" / "The first was a cover from the clerk, formal and brief: the TL-9 flag…"
  - **Opener-chain (2× "The", sents 3–4):** "The letter to Pessel at the Copper Finch had gone in Tuesday's…" / "The TL-9 flag was in at the magistrate's office"
  - **Opener-chain (2× "He", sents 251–252):** "He had already written Case of Joren Aldis at the top of the page" / "He showed her."

---

*Generated by `tools/flow_audit.py`. Qualitative findings (quoted examples + rewrite patterns per tic-type) are appended in the section below.*
