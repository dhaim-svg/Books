#!/usr/bin/env python3
"""
normalize_us_spelling.py — Normalize British spellings to US for The Skybound Wyrm.

Phase A, deterministic spelling pass. Reads chapters from one draft, applies a
CURATED UK->US word map (no -ise stemming — only explicitly listed words are
touched), preserves capitalization, and writes normalized chapters to a target
draft. Reports a per-word replacement count.

Why curated and not regex-stemmed:
  - The manuscript is full of always-'-ise' words (surprise, promise, precise,
    advise, exercise, disguise, advertise, otherwise, noise, raise, revise).
    A blanket -ise->-ize rule would corrupt them. Only 'recognise' is UK here.
  - 'Gray Quay' is a proper noun already in US form; 'grey' (the color) is the
    only thing that should change. No UK-spelled proper nouns exist in the book.
  - Em-dashes are intentionally unspaced in interrupted dialogue and are NOT
    touched by this tool.

USAGE:
    # Dry run — count what WOULD change, write nothing:
    python tools/normalize_us_spelling.py --dry-run

    # Build Draft_6 from Draft_5 (default src=Draft_5, dst=Draft_6):
    python tools/normalize_us_spelling.py

    # Custom drafts:
    python tools/normalize_us_spelling.py --src Draft_5 --dst Draft_6

    # Verify no residual UK forms remain after a run:
    python tools/normalize_us_spelling.py --src Draft_6 --dry-run --audit
"""

import argparse
import io
import re
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parent.parent
STORY_DIR = REPO_ROOT / "Murder-Mystery-Novel-Fantasy-LitRPG-Story"


# ---------------------------------------------------------------------------
# Curated UK -> US map (lowercase keys). Inflections enumerated explicitly.
# Every key is a UK-ONLY spelling (never a valid US word), so matches are safe.
# ---------------------------------------------------------------------------

UK_TO_US = {
    # -our -> -or
    "colour": "color", "colours": "colors", "coloured": "colored",
    "colouring": "coloring", "colourful": "colorful", "colourless": "colorless",
    "discolour": "discolor", "discoloured": "discolored", "discolouration": "discoloration",
    "favour": "favor", "favours": "favors", "favoured": "favored",
    "favouring": "favoring", "favourite": "favorite", "favourites": "favorites",
    "favourable": "favorable", "favourably": "favorably", "favourable": "favorable",
    "honour": "honor", "honours": "honors", "honoured": "honored",
    "honouring": "honoring", "honourable": "honorable", "honourably": "honorably",
    "harbour": "harbor", "harbours": "harbors", "harboured": "harbored",
    "harbouring": "harboring", "harbourmaster": "harbormaster", "harbourmasters": "harbormasters",
    "labour": "labor", "labours": "labors", "laboured": "labored",
    "labouring": "laboring", "labourer": "laborer", "labourers": "laborers",
    "demeanour": "demeanor", "demeanours": "demeanors",
    "behaviour": "behavior", "behaviours": "behaviors", "behavioural": "behavioral",
    "neighbour": "neighbor", "neighbours": "neighbors",
    "neighbouring": "neighboring", "neighbourhood": "neighborhood", "neighbourhoods": "neighborhoods",
    "odour": "odor", "odours": "odors", "odourless": "odorless",
    "vapour": "vapor", "vapours": "vapors",
    "clamour": "clamor", "clamours": "clamors", "clamoured": "clamored", "clamouring": "clamoring",
    "splendour": "splendor", "splendours": "splendors",
    "rumour": "rumor", "rumours": "rumors", "rumoured": "rumored",
    "savour": "savor", "savours": "savors", "savoured": "savored",
    "savouring": "savoring", "savoury": "savory",
    "flavour": "flavor", "flavours": "flavors", "flavoured": "flavored",
    "flavouring": "flavoring", "flavourful": "flavorful",
    "parlour": "parlor", "parlours": "parlors",
    "armour": "armor", "armours": "armors", "armoured": "armored", "armoury": "armory",
    "endeavour": "endeavor", "endeavours": "endeavors", "endeavoured": "endeavored",
    "ardour": "ardor", "fervour": "fervor", "valour": "valor",
    "rigour": "rigor", "rigours": "rigors", "vigour": "vigor",
    "tumour": "tumor", "tumours": "tumors", "humour": "humor", "humours": "humors",
    "humoured": "humored", "humouring": "humoring", "humourless": "humorless",
    "saviour": "savior", "saviours": "saviors",
    # -re -> -er
    "centre": "center", "centres": "centers", "centred": "centered", "centring": "centering",
    "metre": "meter", "metres": "meters",
    "theatre": "theater", "theatres": "theaters",
    "sombre": "somber", "spectre": "specter", "spectres": "specters",
    "sceptre": "scepter", "sceptres": "scepters",
    "calibre": "caliber", "calibres": "calibers",
    "fibre": "fiber", "fibres": "fibers",
    "litre": "liter", "litres": "liters",
    "lustre": "luster", "lacklustre": "lackluster",
    "manoeuvre": "maneuver", "manoeuvres": "maneuvers",
    "manoeuvred": "maneuvered", "manoeuvring": "maneuvering",
    # grey -> gray
    "grey": "gray", "greys": "grays", "greyed": "grayed", "greying": "graying",
    "greyer": "grayer", "greyish": "grayish",
    # -ce noun -> -se
    "defence": "defense", "defences": "defenses", "defenceless": "defenseless",
    "offence": "offense", "offences": "offenses",
    "pretence": "pretense", "pretences": "pretenses",
    "licence": "license", "licences": "licenses", "licenced": "licensed",
    # practise (verb) -> practice
    "practise": "practice", "practised": "practiced", "practising": "practicing", "practises": "practices",
    # -ise -> -ize  (ONLY these; everything else stays -ise)
    "recognise": "recognize", "recognises": "recognizes", "recognised": "recognized",
    "recognising": "recognizing", "recognisable": "recognizable", "recognisably": "recognizably",
    "organise": "organize", "organised": "organized", "organising": "organizing",
    "organisation": "organization", "organisations": "organizations", "organiser": "organizer",
    "realise": "realize", "realised": "realized", "realising": "realizing", "realisation": "realization",
    "apologise": "apologize", "apologised": "apologized", "apologising": "apologizing",
    "emphasise": "emphasize", "emphasised": "emphasized", "emphasising": "emphasizing",
    "memorise": "memorize", "memorised": "memorized", "memorising": "memorizing",
    "scrutinise": "scrutinize", "scrutinised": "scrutinized", "scrutinising": "scrutinizing",
    "specialise": "specialize", "specialised": "specialized", "specialising": "specializing",
    "criticise": "criticize", "criticised": "criticized", "criticising": "criticizing",
    "summarise": "summarize", "summarised": "summarized", "summarising": "summarizing",
    "prioritise": "prioritize", "prioritised": "prioritized", "prioritising": "prioritizing",
    "analyse": "analyze", "analysed": "analyzed", "analysing": "analyzing", "analyser": "analyzer",
    "paralyse": "paralyze", "paralysed": "paralyzed", "paralysing": "paralyzing",
    # speciality
    "speciality": "specialty", "specialities": "specialties",
    # -logue -> -log
    "catalogue": "catalog", "catalogues": "catalogs",
    "catalogued": "cataloged", "cataloguing": "cataloging",
    # travel/level/etc. single-l (US) — UK doubles
    "travelling": "traveling", "travelled": "traveled", "traveller": "traveler", "travellers": "travelers",
    "levelled": "leveled", "levelling": "leveling", "leveller": "leveler",
    "signalled": "signaled", "signalling": "signaling",
    "marvelled": "marveled", "marvelling": "marveling",
    "modelled": "modeled", "modelling": "modeling",
    "labelled": "labeled", "labelling": "labeling",
    "counselled": "counseled", "counselling": "counseling",
    "counsellor": "counselor", "counsellors": "counselors",
    "channelled": "channeled", "channelling": "channeling",
    "cancelled": "canceled", "cancelling": "canceling",
    "fuelled": "fueled", "fuelling": "fueling",
    "totalled": "totaled", "totalling": "totaling",
    "quarrelled": "quarreled", "quarrelling": "quarreling",
    "funnelled": "funneled", "funnelling": "funneling",
    "grovelled": "groveled", "grovelling": "groveling",
    "shrivelled": "shriveled", "shrivelling": "shriveling",
    "snivelled": "sniveled", "snivelling": "sniveling",
    "revelled": "reveled", "revelling": "reveling",
    "shovelled": "shoveled", "shovelling": "shoveling",
    "jeweller": "jeweler", "jewellers": "jewelers", "jewellery": "jewelry",
    # single-l UK -> double-l US
    "enrol": "enroll", "enrolment": "enrollment", "enrolments": "enrollments",
    "instalment": "installment", "instalments": "installments",
    "fulfil": "fulfill", "fulfilment": "fulfillment", "fulfils": "fulfills",
    "skilful": "skillful", "skilfully": "skillfully",
    "wilful": "willful", "wilfully": "willfully",
    "instil": "instill", "instils": "instills",
    "distil": "distill", "distils": "distills",
    "enthral": "enthrall", "enthralled": "enthralled",
    # ae/oe -> e
    "anaesthetist": "anesthetist", "anaesthetists": "anesthetists",
    "anaesthetic": "anesthetic", "anaesthetics": "anesthetics",
    "anaesthesia": "anesthesia", "anaesthetise": "anesthetize",
    "manoeuvrable": "maneuverable", "foetus": "fetus", "foetal": "fetal",
    "oesophagus": "esophagus", "oestrogen": "estrogen",
    # ou -> o, gh, etc.
    "mould": "mold", "moulds": "molds", "moulded": "molded", "moulding": "molding", "mouldy": "moldy",
    "moult": "molt", "moulted": "molted", "moulting": "molting",
    "smoulder": "smolder", "smouldered": "smoldered", "smouldering": "smoldering",
    "plough": "plow", "ploughs": "plows", "ploughed": "plowed", "ploughing": "plowing",
    # NOTE: 'draught' deliberately NOT normalized — author keeps "sleeping draught".
    "storey": "story", "storeys": "stories", "storeyed": "storied",
    "kerb": "curb", "kerbs": "curbs",
    "tyre": "tire", "tyres": "tires",
    "sceptical": "skeptical", "scepticism": "skepticism", "sceptic": "skeptic", "sceptics": "skeptics",
    "cheque": "check", "cheques": "checks",
    "woollen": "woolen", "woollens": "woolens",
    "programme": "program", "programmes": "programs",
    "pyjamas": "pajamas", "sulphur": "sulfur", "moustache": "mustache", "moustaches": "mustaches",
    # cosy -> cozy
    "cosy": "cozy", "cosier": "cozier", "cosiest": "coziest", "cosily": "cozily", "cosiness": "coziness",
    # acknowledgement -> acknowledgment (US-preferred, for consistency)
    "acknowledgement": "acknowledgment", "acknowledgements": "acknowledgments",
    "judgement": "judgment", "judgements": "judgments",
}

# Special multi-word / hyphen fixes handled separately (not single tokens):
SPECIAL = [
    (re.compile(r"\bno-one\b"), "no one"),
    (re.compile(r"\bNo-one\b"), "No one"),
]


def preserve_case(src: str, repl: str) -> str:
    if src.isupper():
        return repl.upper()
    if src[0].isupper():
        return repl[0].upper() + repl[1:]
    return repl


# One big alternation, longest-first so 'colours' matches before 'colour'.
_KEYS_SORTED = sorted(UK_TO_US.keys(), key=len, reverse=True)
_WORD_RE = re.compile(r"\b(" + "|".join(_KEYS_SORTED) + r")\b", re.IGNORECASE)


def normalize_text(text: str, counter: Counter) -> str:
    def _sub(m: re.Match) -> str:
        src = m.group(0)
        repl = UK_TO_US[src.lower()]
        counter[f"{src.lower()} -> {repl}"] += 1
        return preserve_case(src, repl)

    text = _WORD_RE.sub(_sub, text)
    for pat, repl in SPECIAL:
        def _sub2(m, repl=repl):
            counter[f"{m.group(0)} -> {repl}"] += 1
            return repl
        text = pat.sub(_sub2, text)
    return text


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Normalize UK->US spelling — The Skybound Wyrm")
    p.add_argument("--src", default="Draft_5", help="Source draft (default Draft_5)")
    p.add_argument("--dst", default="Draft_6", help="Destination draft (default Draft_6)")
    p.add_argument("--dry-run", action="store_true", help="Count only; write nothing.")
    p.add_argument("--audit", action="store_true", help="With --dry-run on a normalized draft: list any residual UK forms found.")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    src_dir = STORY_DIR / "manuscript" / args.src
    dst_dir = STORY_DIR / "manuscript" / args.dst
    if not src_dir.is_dir():
        print(f"ERROR: source not found: {src_dir}", file=sys.stderr)
        sys.exit(1)

    files = sorted(src_dir.glob("chapter-*.md"))
    if not files:
        print(f"ERROR: no chapter files in {src_dir}", file=sys.stderr)
        sys.exit(1)

    total = Counter()
    if not args.dry_run:
        dst_dir.mkdir(parents=True, exist_ok=True)

    for f in files:
        text = f.read_text(encoding="utf-8")
        ch_counter = Counter()
        out = normalize_text(text, ch_counter)
        total.update(ch_counter)
        n = sum(ch_counter.values())
        if not args.dry_run:
            (dst_dir / f.name).write_text(out, encoding="utf-8")
        print(f"  {f.stem}: {n} replacement(s)")

    print(f"\n{'DRY RUN — ' if args.dry_run else ''}Total replacements: {sum(total.values())}")
    print("By word:")
    for word, n in total.most_common():
        print(f"  {n:4d}  {word}")

    if args.audit:
        print("\n(audit) Residual UK forms still present in source:")
        residual = Counter()
        for f in files:
            for m in _WORD_RE.finditer(f.read_text(encoding="utf-8")):
                residual[m.group(0).lower()] += 1
        if residual:
            for w, n in residual.most_common():
                print(f"  {n:4d}  {w}")
        else:
            print("  none — clean.")


if __name__ == "__main__":
    main()
