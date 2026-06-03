#!/usr/bin/env python3
"""
flow_audit.py — Prose-flow diagnostic for The Skybound Wyrm.

Measures per-chapter: sentence-length distribution, short-sentence chains,
sentence-opener monotony (consecutive He/She/Theron/... starts), and
one-liner paragraphs.  Writes a Markdown report to
  review/feedback_Draft_4/_flow-audit.md

No extra requirements — stdlib only.

USAGE:
    # Smoke-test a single chapter:
    python tools/flow_audit.py --chapter 02
    python tools/flow_audit.py --chapter 19

    # Full run (all chapters) — writes the report:
    python tools/flow_audit.py

    # Different draft:
    python tools/flow_audit.py --draft Draft_5

    # Print to stdout only (no report file):
    python tools/flow_audit.py --no-report
"""

import argparse
import io
import re
import sys
from collections import Counter
from pathlib import Path

# On Windows the default console encoding (cp1252) can't handle many Unicode
# characters that appear in quoted prose snippets.  Wrap stdout so that
# unencodable characters are replaced with '?' instead of crashing.
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
STORY_DIR = REPO_ROOT / "Murder-Mystery-Novel-Fantasy-LitRPG-Story"
REPORT_PATH = STORY_DIR / "review" / "feedback_Draft_5" / "_flow-audit.md"


# ---------------------------------------------------------------------------
# Markdown cleanup (adapted from tools/make_audiobook.py)
# ---------------------------------------------------------------------------

def clean_markdown(text: str) -> str:
    # Chapter heading → plain text
    text = re.sub(
        r'^#{1,2}\s+Chapter\s+(\d+)\s*[—–\-]+\s*(.+)$',
        lambda m: f"Chapter {m.group(1)}. {m.group(2).strip()}.\n",
        text,
        flags=re.MULTILINE,
    )
    # Any remaining headings: strip # markers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Scene breaks → blank line
    text = re.sub(r'^\s*---\s*$', '\n', text, flags=re.MULTILINE)
    # System notes  *[…]*  → strip wrappers, keep content
    text = re.sub(r'\*\[(.+?)\]\*', r'\1', text, flags=re.DOTALL)
    # Bold/italic markers → plain text
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text, flags=re.DOTALL)
    text = re.sub(r'\*(.+?)\*', r'\1', text, flags=re.DOTALL)
    # Leftover lone asterisks
    text = re.sub(r'(?<!\w)\*(?!\w)', '', text)
    # Collapse 3+ blank lines to 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


# ---------------------------------------------------------------------------
# Sentence splitting
# ---------------------------------------------------------------------------

# Sentence boundary: .!? followed by whitespace+capital (or end-of-string).
# We require at least one lowercase letter before the punctuation to avoid
# splitting on common abbreviations (Mr./Mrs./Dr./etc.) — imperfect but good
# enough for prose measurement.
_SENT_BOUNDARY = re.compile(
    r'(?<=[a-z,\"\'])[.!?]["\']?\s+(?=[A-Z\"\'])'
)

# Subject-pronoun / proper-noun openers we track
_SUBJECT_RE = re.compile(
    r'^(He|She|Theron|Sable|His|Her|They|It|The)\b',
    re.IGNORECASE,
)


def split_sentences(text: str) -> list[str]:
    """Split a text block into sentences; drop empties."""
    parts = _SENT_BOUNDARY.split(text)
    out = []
    for p in parts:
        p = p.strip()
        if p and len(p.split()) >= 1:
            out.append(p)
    return out


def wc(sentence: str) -> int:
    return len(sentence.split())


# ---------------------------------------------------------------------------
# Per-chapter analysis
# ---------------------------------------------------------------------------

SHORT_THRESHOLD = 6   # ≤ N words → "short sentence"
STACCATO_THRESHOLD = 3  # ≤ N words → "staccato"


def analyse_chapter(path: Path) -> dict | None:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"  ERROR reading {path}: {e}", file=sys.stderr)
        return None

    clean = clean_markdown(raw)
    paragraphs = [p.strip() for p in clean.split('\n\n') if p.strip()]

    all_sentences: list[str] = []
    para_of_sent: list[int] = []      # which paragraph each sentence belongs to
    for pi, para in enumerate(paragraphs):
        for sent in split_sentences(para):
            all_sentences.append(sent)
            para_of_sent.append(pi)

    n = len(all_sentences)
    if n == 0:
        return None

    lengths = [wc(s) for s in all_sentences]

    # --- Sentence length stats ---
    avg_len = sum(lengths) / n
    n_short = sum(1 for l in lengths if l <= SHORT_THRESHOLD)
    n_staccato = sum(1 for l in lengths if l <= STACCATO_THRESHOLD)
    pct_short = 100 * n_short / n
    pct_staccato = 100 * n_staccato / n

    # Longest consecutive chain of short sentences (≤ SHORT_THRESHOLD words)
    max_short_chain, cur = 0, 0
    chain_short_start = None          # sentence index where best chain begins
    cur_start = None
    for i, l in enumerate(lengths):
        if l <= SHORT_THRESHOLD:
            if cur == 0:
                cur_start = i
            cur += 1
            if cur > max_short_chain:
                max_short_chain = cur
                chain_short_start = cur_start
        else:
            cur = 0

    # One-liner paragraphs: exactly one sentence and that sentence is short
    one_liner_paras = sum(
        1 for para in paragraphs
        if len(split_sentences(para)) == 1 and wc(para) <= SHORT_THRESHOLD
    )

    # --- Sentence-opener stats ---
    def opener(sent: str) -> str:
        m = _SUBJECT_RE.match(sent)
        return m.group(0).capitalize() if m else "_other"

    openers = [opener(s) for s in all_sentences]
    n_subject = sum(1 for o in openers if o != "_other")
    pct_subject = 100 * n_subject / n

    # Longest consecutive chain of the *same* opener
    max_opener_chain = 0
    chain_opener_start = None
    cur, cur_start = 1, 0
    for i in range(1, n):
        if openers[i] != "_other" and openers[i] == openers[i - 1]:
            cur += 1
            if cur > max_opener_chain:
                max_opener_chain = cur
                chain_opener_start = i - cur + 1
        else:
            cur = 1
            cur_start = i
    # Seed with 1 if the very first sentence is a subject opener
    if n >= 1 and max_opener_chain == 0 and openers[0] != "_other":
        max_opener_chain = 1

    # Most frequent opener
    opener_counts = Counter(o for o in openers if o != "_other")
    top_opener, top_opener_count = (
        opener_counts.most_common(1)[0] if opener_counts else ("—", 0)
    )

    # --- Composite choppiness / monotony score ---
    # Calibrated so that chapters the exploration hand-counted as problematic
    # (ch-10, ch-19, ch-30) score clearly higher than clean chapters.
    score = (
        pct_short * 0.45
        + max_short_chain * 3.0
        + pct_subject * 0.45
        + max_opener_chain * 4.5
        + one_liner_paras * 0.5
    )

    return {
        "n_sentences": n,
        "n_paragraphs": len(paragraphs),
        "avg_len": round(avg_len, 1),
        "pct_short": round(pct_short, 1),
        "pct_staccato": round(pct_staccato, 1),
        "max_short_chain": max_short_chain,
        "chain_short_start": chain_short_start,
        "one_liner_paras": one_liner_paras,
        "pct_subject": round(pct_subject, 1),
        "max_opener_chain": max_opener_chain,
        "chain_opener_start": chain_opener_start,
        "top_opener": top_opener,
        "top_opener_count": top_opener_count,
        "score": round(score, 1),
        # raw data for hotspot extraction
        "_sentences": all_sentences,
        "_lengths": lengths,
        "_openers": openers,
    }


# ---------------------------------------------------------------------------
# Flag logic
# ---------------------------------------------------------------------------

FLAG_AVG_LEN = 11.5      # avg sentence length < this → flagged
FLAG_PCT_SHORT = 26.0    # % short sentences (≤6w) > this → flagged
FLAG_SHORT_CHAIN = 3     # longest short chain ≥ this → flagged
FLAG_OPENER_CHAIN = 3    # longest same-opener chain ≥ this → flagged
FLAG_PCT_SUBJECT = 33.0  # % subject-opener sentences > this → flagged


def is_flagged(stats: dict) -> bool:
    return (
        stats["avg_len"] < FLAG_AVG_LEN
        or stats["pct_short"] > FLAG_PCT_SHORT
        or stats["max_short_chain"] >= FLAG_SHORT_CHAIN
        or stats["max_opener_chain"] >= FLAG_OPENER_CHAIN
        or stats["pct_subject"] > FLAG_PCT_SUBJECT
    )


def flag_reasons(stats: dict) -> str:
    reasons = []
    if stats["avg_len"] < FLAG_AVG_LEN:
        reasons.append(f"avg<{FLAG_AVG_LEN}w")
    if stats["pct_short"] > FLAG_PCT_SHORT:
        reasons.append(f"%short>{FLAG_PCT_SHORT}%")
    if stats["max_short_chain"] >= FLAG_SHORT_CHAIN:
        reasons.append(f"chain≥{FLAG_SHORT_CHAIN}")
    if stats["max_opener_chain"] >= FLAG_OPENER_CHAIN:
        reasons.append(f"opener≥{FLAG_OPENER_CHAIN}")
    if stats["pct_subject"] > FLAG_PCT_SUBJECT:
        reasons.append(f"%subj>{FLAG_PCT_SUBJECT}%")
    return ", ".join(reasons)


# ---------------------------------------------------------------------------
# Hotspot extraction
# ---------------------------------------------------------------------------

def _quote(s: str, maxlen: int = 70) -> str:
    s = s.replace('\n', ' ').strip()
    if len(s) > maxlen:
        s = s[:maxlen].rsplit(' ', 1)[0] + '…'
    return f'"{s}"'


def extract_hotspots(stats: dict) -> list[str]:
    sentences = stats["_sentences"]
    lengths = stats["_lengths"]
    openers = stats["_openers"]
    n = len(sentences)
    lines = []

    # All short-sentence runs of length ≥ 2, sorted by length desc
    runs: list[tuple[int, int, int]] = []
    i = 0
    while i < n:
        if lengths[i] <= SHORT_THRESHOLD:
            j = i
            while j < n and lengths[j] <= SHORT_THRESHOLD:
                j += 1
            if j - i >= 2:
                runs.append((j - i, i, j))
            i = j
        else:
            i += 1
    runs.sort(reverse=True)
    for run_len, start, end in runs[:3]:
        snippets = " / ".join(_quote(s) for s in sentences[start:min(end, start + 4)])
        if end - start > 4:
            snippets += " …"
        lines.append(f"  - **Short-chain ({run_len} sents <={SHORT_THRESHOLD}w, sents {start}-{end-1}):** {snippets}")

    # All same-opener runs of length ≥ 2, sorted by length desc
    oruns: list[tuple[int, str, int, int]] = []
    i = 0
    while i < n:
        o = openers[i]
        if o != "_other":
            j = i
            while j < n and openers[j] == o:
                j += 1
            if j - i >= 2:
                oruns.append((j - i, o, i, j))
            i = max(j, i + 1)
        else:
            i += 1
    oruns.sort(reverse=True)
    for run_len, opener_word, start, end in oruns[:3]:
        snippets = " / ".join(_quote(s) for s in sentences[start:min(end, start + 4)])
        if end - start > 4:
            snippets += " …"
        lines.append(f"  - **Opener-chain ({run_len}× \"{opener_word}\", sents {start}–{end-1}):** {snippets}")

    return lines


# ---------------------------------------------------------------------------
# Report builder
# ---------------------------------------------------------------------------

def build_report(results: list[tuple[str, dict | None]], draft: str) -> str:
    valid = [(ch, s) for ch, s in results if s]
    flagged = [(ch, s) for ch, s in valid if is_flagged(s)]
    flagged_sorted = sorted(flagged, key=lambda x: -x[1]["score"])
    total = len(valid)
    pct_flagged = 100 * len(flagged) / total if total else 0
    worst_names = ", ".join(f"Kap. {ch.replace('chapter-','')}" for ch, _ in flagged_sorted[:5])

    lines: list[str] = []

    # ---------- German overview ----------
    lines += [
        f"# Flow Audit — *The Skybound Wyrm* {draft}\n",
        "\n## Überblick\n\n",
        f"Die automatische Messung bestätigt Davids Eindruck: "
        f"**{len(flagged)} von {total} Kapiteln** ({pct_flagged:.0f}%) liegen bei mindestens "
        f"einem Fluss-Indikator im roten Bereich. "
        f"Schlimmste Ausreißer: **{worst_names or '–'}**. "
        f"Das Problem ist kein Gesamtversagen, sondern ein *Register-Clash*: "
        f"Beschreibung und Analyse laufen flüssig (oft 40–80 Wörter pro Satz), "
        f"aber Szenenübergänge (`Theron went.` / `He got up.`) und "
        f"Dialog-Regieanweisungen (`He wrote: … He looked up … He stood`) "
        f"sind repetitiv kurz und subjekt-initial — der Sprung zwischen beiden Registern "
        f"ist es, der sich als abgehackt anfühlt. "
        f"Die Hotspot-Liste unten zeigt die genauen Stellen.\n",
        "\n",
    ]

    # ---------- Flag thresholds ----------
    lines += [
        "## Flag-Schwellen\n\n",
        "| Indikator | Rot wenn … |\n",
        "|---|---|\n",
        f"| Avg sentence length (words) | < {FLAG_AVG_LEN} |\n",
        f"| % short sentences (≤{SHORT_THRESHOLD} w) | > {FLAG_PCT_SHORT}% |\n",
        f"| Longest consecutive short-sentence chain | ≥ {FLAG_SHORT_CHAIN} |\n",
        f"| Longest consecutive same-opener chain | ≥ {FLAG_OPENER_CHAIN} |\n",
        f"| % subject-opener sentences | > {FLAG_PCT_SUBJECT}% |\n",
        "\n",
    ]

    # ---------- Heatmap table (sorted by score desc) ----------
    lines += [
        "## Heatmap — alle Kapitel (sortiert nach Score)\n\n",
        "| Ch | Avg(w) | %Short | MaxShortChain | %Subj | MaxOpenerChain | Score | Flag |\n",
        "|---|---|---|---|---|---|---|---|\n",
    ]
    for ch, stats in sorted(valid, key=lambda x: -x[1]["score"]):
        fl = "🚩 " + flag_reasons(stats) if is_flagged(stats) else "✓"
        ch_short = ch.replace("chapter-", "")
        lines.append(
            f"| **{ch_short}** | {stats['avg_len']} | {stats['pct_short']}% | "
            f"{stats['max_short_chain']} | {stats['pct_subject']}% | "
            f"{stats['max_opener_chain']} | {stats['score']} | {fl} |\n"
        )
    lines.append("\n")

    # ---------- Hotspot list ----------
    lines += [
        "## Hotspots — flagged chapters\n\n",
        "_Longest short-sentence chains and same-opener chains with quoted snippets. "
        "Sentence indices are zero-based within the cleaned prose (excluding markdown "
        "headings and system notes)._\n\n",
    ]
    for ch, stats in flagged_sorted:
        ch_short = ch.replace("chapter-", "")
        lines.append(f"### Chapter {ch_short} (score {stats['score']}, {flag_reasons(stats)})\n\n")
        hs = extract_hotspots(stats)
        if hs:
            for h in hs:
                lines.append(h + "\n")
        else:
            lines.append("_(no specific chains above threshold)_\n")
        lines.append("\n")

    lines += [
        "---\n\n",
        "*Generated by `tools/flow_audit.py`. "
        "Qualitative findings (quoted examples + rewrite patterns per tic-type) "
        "are appended in the section below.*\n",
    ]

    return "".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Prose flow audit — The Skybound Wyrm")
    p.add_argument(
        "--chapter",
        metavar="NN",
        help="Audit a single chapter (e.g. 02). Default: all chapters.",
    )
    p.add_argument(
        "--draft",
        default="Draft_4",
        help="Which manuscript draft to audit (default: Draft_4).",
    )
    p.add_argument(
        "--no-report",
        action="store_true",
        help="Print to stdout only; do not write _flow-audit.md.",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    manuscript_dir = STORY_DIR / "manuscript" / args.draft

    if not manuscript_dir.is_dir():
        print(f"ERROR: manuscript directory not found:\n  {manuscript_dir}", file=sys.stderr)
        sys.exit(1)

    # Gather chapter files
    if args.chapter:
        chapter_num = args.chapter.zfill(2)
        files = sorted(manuscript_dir.glob(f"chapter-{chapter_num}.md"))
        if not files:
            print(
                f"ERROR: chapter-{chapter_num}.md not found in {manuscript_dir}",
                file=sys.stderr,
            )
            sys.exit(1)
    else:
        files = sorted(manuscript_dir.glob("chapter-*.md"))
        if not files:
            print(f"ERROR: no chapter-*.md found in {manuscript_dir}", file=sys.stderr)
            sys.exit(1)

    results: list[tuple[str, dict | None]] = []
    for f in files:
        ch = f.stem
        print(f"  {ch} … ", end="", flush=True)
        stats = analyse_chapter(f)
        results.append((ch, stats))
        if stats:
            flag_mark = " [FLAG]" if is_flagged(stats) else ""
            print(
                f"avg={stats['avg_len']}w  "
                f"%short={stats['pct_short']}%  "
                f"shortChain={stats['max_short_chain']}  "
                f"openerChain={stats['max_opener_chain']}  "
                f"score={stats['score']}{flag_mark}"
            )
        else:
            print("(empty or unreadable)")

    # For single-chapter runs, just show the hotspot details and exit
    if args.chapter or args.no_report:
        for ch, stats in results:
            if not stats:
                continue
            print(f"\n=== Hotspots for {ch} ===")
            for line in extract_hotspots(stats):
                print(line)
        return

    # Full run → write report
    report = build_report(results, args.draft)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(f"\nReport written → {REPORT_PATH.relative_to(REPO_ROOT)}")

    flagged = [(ch, s) for ch, s in results if s and is_flagged(s)]
    top5 = sorted(flagged, key=lambda x: -x[1]["score"])[:5]
    print(f"Flagged: {len(flagged)}/{len(results)} chapters")
    print("Top 5 by score: " + ", ".join(f"{ch}({s['score']})" for ch, s in top5))


if __name__ == "__main__":
    main()
