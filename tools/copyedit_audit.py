#!/usr/bin/env python3
"""
copyedit_audit.py — Mechanical proofread/copyedit diagnostic for The Skybound Wyrm.

This is the *deterministic* layer of the final language pass (Phase A). It flags
the things a machine can catch with near-zero false positives — leaving genuine
grammar/tense/missing-word judgement to the agent-driven copyedit that runs on
top of it.

Checks, per chapter + aggregated:
  - Doubled words            ("the the", "and and") — legit doubles allow-listed
  - Double / multiple spaces between words
  - Space *before* , . ; : ! ?  and missing space *after*
  - Stray multiple punctuation (",,", "..", ";;")  (… and ?! are left alone)
  - Ellipsis-style consistency  ("…" vs "..." vs ". . .")
  - Em-dash spacing consistency (spaced " — " vs unspaced "—") + " - " typo for dash
  - Curly vs straight quote consistency (counts; for Pandoc smart-quotes later)
  - Unbalanced double-quotes in a paragraph (possible dropped quote mark)
  - US / UK spelling mix (curated pair list; reports the minority variant)
  - Trailing whitespace / tabs

Writes a Markdown report to:
  review/feedback_Draft_5/_copyedit-mechanical.md

No extra requirements — stdlib only.

USAGE:
    python tools/copyedit_audit.py                  # full run, writes report
    python tools/copyedit_audit.py --chapter 01     # single chapter, stdout only
    python tools/copyedit_audit.py --draft Draft_6  # different draft
    python tools/copyedit_audit.py --no-report      # print to stdout only
"""

import argparse
import io
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Windows console can't always encode quoted prose snippets — replace, don't crash.
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bookconfig  # noqa: E402


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
STORY_DIR = REPO_ROOT / "Murder-Mystery-Novel-Fantasy-LitRPG-Story"
DEFAULT_DRAFT = "Draft_5"


# ---------------------------------------------------------------------------
# What counts as a prose line
# ---------------------------------------------------------------------------

def is_prose_line(line: str) -> bool:
    """Skip markdown headings, scene-break rules, and blank lines."""
    s = line.strip()
    if not s:
        return False
    if s.startswith("#"):
        return False
    if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", s):
        return False
    return True


# ---------------------------------------------------------------------------
# Curated US / UK spelling pairs (US, UK) — common in fiction prose.
# We report whichever variant is the *minority* so the author can normalise.
# ---------------------------------------------------------------------------

US_UK_PAIRS = [
    ("color", "colour"), ("colors", "colours"), ("colored", "coloured"),
    ("favor", "favour"), ("favorite", "favourite"), ("honor", "honour"),
    ("neighbor", "neighbour"), ("neighbors", "neighbours"), ("odor", "odour"),
    ("rumor", "rumour"), ("savor", "savour"), ("harbor", "harbour"),
    ("armor", "armour"), ("behavior", "behaviour"), ("labor", "labour"),
    ("vapor", "vapour"), ("clamor", "clamour"), ("splendor", "splendour"),
    ("center", "centre"), ("theater", "theatre"), ("meter", "metre"),
    ("somber", "sombre"), ("scepter", "sceptre"), ("specter", "spectre"),
    ("traveled", "travelled"), ("traveler", "traveller"), ("traveling", "travelling"),
    ("marveled", "marvelled"), ("modeled", "modelled"), ("signaled", "signalled"),
    ("labeled", "labelled"), ("counselor", "counsellor"), ("jewelry", "jewellery"),
    ("gray", "grey"), ("grayed", "greyed"), ("plow", "plough"),
    ("mold", "mould"), ("smolder", "smoulder"), ("molt", "moult"),
    ("realize", "realise"), ("realized", "realised"), ("recognize", "recognise"),
    ("recognized", "recognised"), ("apologize", "apologise"),
    ("organize", "organise"), ("organized", "organised"),
    ("memorize", "memorise"), ("memorized", "memorised"),
    ("emphasize", "emphasise"), ("scrutinize", "scrutinise"),
    ("defense", "defence"), ("offense", "offence"), ("license", "licence"),
    ("practice", "practise"), ("gauge", "guage"),  # (guage is just a typo guard)
    ("toward", "towards"), ("backward", "backwards"), ("forward", "forwards"),
    ("gotten", "got"),  # weak signal; reported but low-weight
    ("ax", "axe"), ("dialog", "dialogue"), ("catalog", "catalogue"),
    ("mustache", "moustache"), ("pl0w", "plough"),
]
# Drop the deliberately-noisy guards from the real comparison set:
US_UK_PAIRS = [(u, k) for (u, k) in US_UK_PAIRS if u not in {"pl0w", "gotten", "gauge"}]


# ---------------------------------------------------------------------------
# Legitimate doubled words (valid English repeats)
# ---------------------------------------------------------------------------

LEGIT_DOUBLES = {"had", "that", "is", "is.", "the", "no", "blah"}
# We still surface "had had"/"that that" but tag them as usually-legit.
USUALLY_LEGIT = {"had", "that"}


# ---------------------------------------------------------------------------
# Per-chapter analysis
# ---------------------------------------------------------------------------

WORD_RE = re.compile(r"[A-Za-z][A-Za-z'’]*")


def analyse_chapter(path: Path) -> dict | None:
    try:
        raw_lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as e:
        print(f"  ERROR reading {path}: {e}", file=sys.stderr)
        return None

    findings: dict[str, list[tuple[int, str]]] = defaultdict(list)
    counts = Counter()

    # Quote/dash/ellipsis style counters
    counts["dq_straight"] = 0
    counts["dq_curly"] = 0
    counts["sq_straight"] = 0
    counts["sq_curly"] = 0
    counts["emdash_spaced"] = 0
    counts["emdash_unspaced"] = 0
    counts["ellipsis_unicode"] = 0
    counts["ellipsis_ascii"] = 0
    counts["ellipsis_spaced"] = 0

    spelling_hits = Counter()  # variant-string -> count

    para_buf: list[str] = []
    para_start_line = 0

    def flush_paragraph(buf: list[str], start_line: int):
        if not buf:
            return
        text = " ".join(buf)
        # Unbalanced straight double-quotes within a paragraph
        if text.count('"') % 2 == 1:
            findings["unbalanced_quotes"].append(
                (start_line, _snip(text))
            )

    for idx, line in enumerate(raw_lines, start=1):
        # Paragraph accumulation (blank line = paragraph break)
        if line.strip() == "":
            flush_paragraph(para_buf, para_start_line)
            para_buf = []
            continue

        if not is_prose_line(line):
            # heading / scene break ends the current paragraph
            flush_paragraph(para_buf, para_start_line)
            para_buf = []
            continue

        if not para_buf:
            para_start_line = idx
        para_buf.append(line)

        # ---- line-level checks ----
        # trailing whitespace / tabs
        if line != line.rstrip():
            findings["trailing_ws"].append((idx, _snip(line)))
        if "\t" in line:
            findings["tabs"].append((idx, _snip(line)))

        # double / multiple spaces (not leading indentation)
        if re.search(r"\S  +\S", line):
            findings["multi_space"].append((idx, _snip(line)))

        # space before terminal punctuation
        for m in re.finditer(r"\s+([,.;:!?])", line):
            # allow " ..." style ellipsis and " —" dash handled elsewhere
            findings["space_before_punct"].append((idx, _snip(line, m.start())))
            break

        # stray repeated punctuation (exclude … as ... handled separately, and ?! !?)
        if re.search(r",,|;;|::|(?<!\.)\.\.(?!\.)", line):
            findings["repeated_punct"].append((idx, _snip(line)))

        # missing space after sentence punctuation (letter.letter) — guard decimals/abbr
        for m in re.finditer(r"[a-z]{2}([.!?])([A-Z])", line):
            findings["missing_space_after"].append((idx, _snip(line, m.start())))
            break

        # doubled words
        for m in re.finditer(r"\b(\w+)\s+\1\b", line, flags=re.IGNORECASE):
            w = m.group(1).lower()
            tag = "  (usually legit)" if w in USUALLY_LEGIT else ""
            findings["doubled_word"].append((idx, f'"{m.group(0)}"{tag}  — {_snip(line, m.start())}'))

        # " - " used where an em-dash likely belongs
        if re.search(r"\S +- +\S", line):
            findings["hyphen_for_dash"].append((idx, _snip(line)))

        # ---- style counters ----
        counts["dq_straight"] += line.count('"')
        counts["dq_curly"] += line.count("“") + line.count("”")
        counts["sq_curly"] += line.count("‘") + line.count("’")
        counts["emdash_spaced"] += len(re.findall(r"\s—\s", line))
        counts["emdash_unspaced"] += len(re.findall(r"\S—\S", line))
        counts["ellipsis_unicode"] += line.count("…")
        counts["ellipsis_ascii"] += len(re.findall(r"(?<!\.)\.\.\.(?!\.)", line))
        counts["ellipsis_spaced"] += len(re.findall(r"\.\s\.\s\.", line))

        # ---- spelling variants ----
        words_lower = [w.lower() for w in WORD_RE.findall(line)]
        wset = Counter(words_lower)
        for us, uk in US_UK_PAIRS:
            if wset.get(us):
                spelling_hits[us] += wset[us]
            if wset.get(uk):
                spelling_hits[uk] += wset[uk]

    flush_paragraph(para_buf, para_start_line)

    return {
        "findings": dict(findings),
        "counts": counts,
        "spelling": spelling_hits,
        "n_findings": sum(len(v) for v in findings.values()),
    }


def _snip(s: str, around: int | None = None, width: int = 64) -> str:
    s = s.strip()
    if around is not None and len(s) > width:
        start = max(0, around - width // 3)
        seg = s[start:start + width]
        return ("…" if start else "") + seg.strip() + "…"
    if len(s) > width:
        return s[:width].rsplit(" ", 1)[0] + "…"
    return s


# ---------------------------------------------------------------------------
# Aggregation + report
# ---------------------------------------------------------------------------

FINDING_LABELS = {
    "doubled_word": "Doubled words",
    "multi_space": "Multiple spaces",
    "space_before_punct": "Space before punctuation",
    "missing_space_after": "Missing space after sentence",
    "repeated_punct": "Stray repeated punctuation",
    "hyphen_for_dash": 'Spaced hyphen " - " (em-dash?)',
    "unbalanced_quotes": "Unbalanced double-quote in paragraph",
    "trailing_ws": "Trailing whitespace",
    "tabs": "Tab character",
}
# Order findings most-actionable first
FINDING_ORDER = [
    "doubled_word", "unbalanced_quotes", "missing_space_after",
    "space_before_punct", "repeated_punct", "multi_space",
    "hyphen_for_dash", "trailing_ws", "tabs",
]


def resolve_spelling(spelling_totals: Counter) -> list[str]:
    """Return human lines describing US/UK mixes (both variants present)."""
    out = []
    pair_map = {us: uk for us, uk in US_UK_PAIRS}
    pair_map_rev = {uk: us for us, uk in US_UK_PAIRS}
    seen = set()
    for us, uk in US_UK_PAIRS:
        if (us, uk) in seen:
            continue
        seen.add((us, uk))
        nu, nk = spelling_totals.get(us, 0), spelling_totals.get(uk, 0)
        if nu and nk:
            out.append(f"  - **MIX**: `{us}` ×{nu} (US) vs `{uk}` ×{nk} (UK)")
    return out


def overall_spelling_lean(spelling_totals: Counter) -> str:
    us_total = sum(spelling_totals.get(us, 0) for us, _ in US_UK_PAIRS)
    uk_total = sum(spelling_totals.get(uk, 0) for _, uk in US_UK_PAIRS)
    if us_total == uk_total == 0:
        return "no tracked spelling-variant words found"
    lean = "US" if us_total >= uk_total else "UK"
    return f"manuscript leans **{lean}** (US-variant tokens: {us_total}, UK-variant tokens: {uk_total})"


def build_report(results: list[tuple[str, dict | None]], draft: str) -> str:
    valid = [(ch, s) for ch, s in results if s]
    total_findings = sum(s["n_findings"] for _, s in valid)

    # aggregate counts
    agg = Counter()
    agg_spelling = Counter()
    per_type = Counter()
    for _, s in valid:
        agg.update(s["counts"])
        agg_spelling.update(s["spelling"])
        for k, v in s["findings"].items():
            per_type[k] += len(v)

    lines: list[str] = []
    lines += [
        f"# Copyedit Audit (mechanical) — *The Skybound Wyrm* {draft}\n\n",
        "_Deterministic proofread layer. These are machine-detectable issues; treat each as a\n"
        "**candidate** for the human/agent copyedit, not an automatic change. Grammar, tense,\n"
        "missing words, and dialogue logic are out of scope here — that's the agent pass._\n\n",
    ]

    # ---------- summary ----------
    lines += ["## Summary\n\n", f"- **{total_findings}** mechanical findings across **{len(valid)}** chapters.\n"]
    for k in FINDING_ORDER:
        if per_type.get(k):
            lines.append(f"- {FINDING_LABELS[k]}: **{per_type[k]}**\n")
    lines.append("\n")

    # ---------- style consistency ----------
    lines += ["## Style consistency (whole manuscript)\n\n"]
    lines += [
        f"- **Quotes:** straight double `\"` ×{agg['dq_straight']}, curly “/” ×{agg['dq_curly']}, "
        f"curly single ‘/’ ×{agg['sq_curly']}. "
        + ("Mixed — normalise before/at Pandoc build.\n"
           if agg["dq_curly"] and agg["dq_straight"] else
           "Consistent (Pandoc `--smart` can curl straight quotes at build time).\n"),
        f"- **Em-dash:** spaced ` — ` ×{agg['emdash_spaced']}, unspaced `—` ×{agg['emdash_unspaced']}. "
        + ("Mixed — pick one convention.\n" if agg["emdash_spaced"] and agg["emdash_unspaced"]
           else "Consistent.\n"),
        f"- **Ellipsis:** unicode `…` ×{agg['ellipsis_unicode']}, ascii `...` ×{agg['ellipsis_ascii']}, "
        f"spaced `. . .` ×{agg['ellipsis_spaced']}. "
        + ("Mixed — pick one.\n" if sum(1 for x in (agg['ellipsis_unicode'], agg['ellipsis_ascii'], agg['ellipsis_spaced']) if x) > 1
           else "Consistent.\n"),
        f"- **Spelling:** {overall_spelling_lean(agg_spelling)}.\n",
    ]
    mix = resolve_spelling(agg_spelling)
    if mix:
        lines.append("  - Variant mixes to resolve:\n")
        for m in mix:
            lines.append("  " + m + "\n")
    lines.append("\n")

    # ---------- per-chapter detail ----------
    lines += ["## Per-chapter findings\n\n"]
    for ch, s in valid:
        if s["n_findings"] == 0:
            continue
        ch_short = ch.replace("chapter-", "")
        lines.append(f"### Chapter {ch_short} — {s['n_findings']} finding(s)\n\n")
        for k in FINDING_ORDER:
            items = s["findings"].get(k)
            if not items:
                continue
            lines.append(f"**{FINDING_LABELS[k]}** ({len(items)}):\n")
            for ln, detail in items[:25]:
                lines.append(f"  - L{ln}: {detail}\n")
            if len(items) > 25:
                lines.append(f"  - …and {len(items) - 25} more\n")
            lines.append("\n")

    clean = [ch.replace("chapter-", "") for ch, s in valid if s["n_findings"] == 0]
    if clean:
        lines.append("## Clean chapters (no mechanical findings)\n\n")
        lines.append(", ".join(clean) + "\n\n")

    lines += [
        "---\n\n",
        "*Generated by `tools/copyedit_audit.py`. Next: the agent-driven copyedit pass reads the\n"
        "prose for grammar/tense/missing-word issues and merges its findings with these into the\n"
        "`_copyedit.md` triage.*\n",
    ]
    return "".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Mechanical copyedit/proofread audit — The Skybound Wyrm")
    p.add_argument("--chapter", metavar="NN", help="Audit a single chapter (e.g. 01).")
    p.add_argument("--draft", default=DEFAULT_DRAFT, help=f"Manuscript draft (default: {DEFAULT_DRAFT}).")
    p.add_argument("--no-report", action="store_true", help="Print to stdout only; do not write report.")
    bookconfig.add_book_arg(p)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    book = bookconfig.resolve_book(args)
    manuscript_dir = book.manuscript(args.draft)
    if not manuscript_dir.is_dir():
        print(f"ERROR: manuscript directory not found:\n  {manuscript_dir}", file=sys.stderr)
        sys.exit(1)

    if args.chapter:
        files = sorted(manuscript_dir.glob(f"chapter-{args.chapter.zfill(2)}.md"))
        if not files:
            print(f"ERROR: chapter-{args.chapter.zfill(2)}.md not found in {manuscript_dir}", file=sys.stderr)
            sys.exit(1)
    else:
        files = sorted(manuscript_dir.glob("chapter-*.md"))
        if not files:
            print(f"ERROR: no chapter-*.md found in {manuscript_dir}", file=sys.stderr)
            sys.exit(1)

    results: list[tuple[str, dict | None]] = []
    for f in files:
        ch = f.stem
        stats = analyse_chapter(f)
        results.append((ch, stats))
        n = stats["n_findings"] if stats else 0
        print(f"  {ch} … {n} finding(s)")

    if args.chapter or args.no_report:
        for ch, s in results:
            if not s:
                continue
            print(f"\n=== {ch} ===")
            for k in FINDING_ORDER:
                for ln, detail in s["findings"].get(k, []):
                    print(f"  [{FINDING_LABELS[k]}] L{ln}: {detail}")
        return

    report = build_report(results, args.draft)
    rp = book.feedback(args.draft) / "_copyedit-mechanical.md"
    rp.parent.mkdir(parents=True, exist_ok=True)
    rp.write_text(report, encoding="utf-8")
    print(f"\nReport written → {rp.relative_to(REPO_ROOT)}")
    print(f"Total findings: {sum(s['n_findings'] for _, s in results if s)}")


if __name__ == "__main__":
    main()
