#!/usr/bin/env python3
"""
make_audiobook.py — Convert Skybound Wyrm manuscript chapters to audio via Kokoro TTS.

SETUP (one-time):
    python -m venv .venv-audiobook
    .venv-audiobook\\Scripts\\Activate.ps1        # PowerShell
    pip install -r tools/requirements-audiobook.txt

USAGE:
    # Smoke-test with chapter 1 only (do this first):
    python tools/make_audiobook.py --chapter 01

    # Full batch (all 40 chapters — runs overnight on CPU):
    python tools/make_audiobook.py

    # Different voice or speed:
    python tools/make_audiobook.py --voice am_michael --speed 1.1

Available voices:
    British male  : bm_george (default), bm_lewis
    British female: bf_emma, bf_isabella
    American male : am_michael, am_adam
    American female: af_bella, af_sarah, af_sky, af_nicole

Output: audiobook/Draft_3/chapter-NN.wav  (play in VLC — use [ ] to adjust speed)
Resumable: already-rendered chapters are skipped automatically.
"""

import argparse
import re
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf

# ---------------------------------------------------------------------------
# Markdown cleanup — converts chapter markdown to clean narration text
# ---------------------------------------------------------------------------

def clean_markdown(text: str) -> str:
    # Chapter heading: "# Chapter 3 — The Long Descent" → "Chapter 3. The Long Descent."
    text = re.sub(
        r'^#{1,2}\s+Chapter\s+(\d+)\s*[—–\-]+\s*(.+)$',
        lambda m: f"Chapter {m.group(1)}. {m.group(2).strip()}.\n",
        text,
        flags=re.MULTILINE,
    )

    # Any remaining headings: strip the # markers, keep the text
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)

    # Scene break (--- on its own line) → a noticeable narration pause
    text = re.sub(r'^\s*---\s*$', '\n\n', text, flags=re.MULTILINE)

    # System notes:  *[Investigator — Insight +1. She read your paper.]*
    # Strip the *[ and ]* wrappers; read the inner text as a plain beat in the prose.
    text = re.sub(r'\*\[(.+?)\]\*', r'\1', text, flags=re.DOTALL)

    # Bold (**text**) and italic (*text*) — strip markers, keep text
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text, flags=re.DOTALL)
    text = re.sub(r'\*(.+?)\*', r'\1', text, flags=re.DOTALL)

    # Any leftover lone asterisks or brackets
    text = re.sub(r'(?<!\w)\*(?!\w)', '', text)

    # Collapse 3+ blank lines to 2
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()


# ---------------------------------------------------------------------------
# Chunking — Kokoro performs best on chunks ≤ ~800 chars; split at paragraphs
# ---------------------------------------------------------------------------

def split_into_chunks(text: str, max_chars: int = 800) -> list[str]:
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0

    for para in paragraphs:
        if current and current_len + len(para) > max_chars:
            chunks.append('\n\n'.join(current))
            current = [para]
            current_len = len(para)
        else:
            current.append(para)
            current_len += len(para)

    if current:
        chunks.append('\n\n'.join(current))

    return chunks


# ---------------------------------------------------------------------------
# TTS rendering — returns a float32 numpy array at 24 kHz
# ---------------------------------------------------------------------------

SILENCE_BETWEEN_CHUNKS = 0.25  # seconds of silence between text chunks


def render_chapter(pipeline, text: str, voice: str, speed: float = 1.0) -> np.ndarray:
    chunks = split_into_chunks(text)
    silence = np.zeros(int(24000 * SILENCE_BETWEEN_CHUNKS), dtype=np.float32)
    parts: list[np.ndarray] = []

    for chunk in chunks:
        try:
            for _, _, audio in pipeline(chunk, voice=voice, speed=speed):
                parts.append(np.asarray(audio, dtype=np.float32))
                parts.append(silence)
        except Exception as exc:
            print(f"\n  WARNING: TTS chunk failed ({exc!r}), skipping chunk.")

    return np.concatenate(parts) if parts else np.array([], dtype=np.float32)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description='Generate audiobook WAVs from manuscript chapters via Kokoro TTS.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        '--chapter', metavar='NN',
        help='Render only this chapter number, e.g. --chapter 01  (good for smoke-testing)'
    )
    parser.add_argument(
        '--voice', default='bm_george',
        help='Kokoro voice ID (default: bm_george — British male narrator)'
    )
    parser.add_argument(
        '--speed', type=float, default=1.0,
        help='Narration speed multiplier (default: 1.0; try 1.1 for slightly brisker pace)'
    )
    parser.add_argument(
        '--input-dir',
        default='Murder-Mystery-Novel-Fantasy-LitRPG-Story/manuscript/Draft_4',
        help='Directory containing chapter-NN.md files'
    )
    parser.add_argument(
        '--output-dir',
        default='audiobook/Draft_4',
        help='Output directory for WAV files'
    )
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)

    if not input_dir.is_dir():
        print(f"ERROR: Input directory not found: {input_dir}", file=sys.stderr)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    # Collect chapters
    if args.chapter:
        chapter_files = sorted(input_dir.glob(f'chapter-{args.chapter.zfill(2)}.md'))
    else:
        chapter_files = sorted(
            (f for f in input_dir.glob('chapter-[0-9]*.md')),
            key=lambda p: int(re.search(r'chapter-(\d+)', p.name).group(1)),
        )

    if not chapter_files:
        print(f"ERROR: No matching chapter files found in {input_dir}", file=sys.stderr)
        sys.exit(1)

    # Load Kokoro
    print(f"Loading Kokoro TTS (voice: {args.voice}) ...")
    try:
        from kokoro import KPipeline  # type: ignore
    except ImportError:
        print(
            "\nERROR: kokoro not installed.\n"
            "Run these commands first:\n"
            "  python -m venv .venv-audiobook\n"
            "  .venv-audiobook\\Scripts\\Activate.ps1\n"
            "  pip install -r tools/requirements-audiobook.txt\n"
            "\nOn first run, Kokoro downloads its model (~300 MB) automatically.",
            file=sys.stderr,
        )
        sys.exit(1)

    # 'b' = British English voices (bm_*, bf_*); 'a' = American (am_*, af_*)
    lang_code = 'b' if args.voice.startswith('b') else 'a'
    pipeline = KPipeline(lang_code=lang_code)
    print("Model ready.\n")

    total = len(chapter_files)
    for idx, md_path in enumerate(chapter_files, 1):
        out_path = output_dir / f"{md_path.stem}.wav"

        if out_path.exists():
            size_mb = out_path.stat().st_size / 1_048_576
            print(f"[{idx:2}/{total}] {md_path.stem}.wav  already exists ({size_mb:.0f} MB) — skipping.")
            continue

        raw = md_path.read_text(encoding='utf-8')
        word_count = len(raw.split())
        clean = clean_markdown(raw)

        print(f"[{idx:2}/{total}] Rendering {md_path.name}  ({word_count:,} words) ...", end='', flush=True)
        t0 = time.time()

        audio = render_chapter(pipeline, clean, voice=args.voice, speed=args.speed)

        if audio.size == 0:
            print(" ERROR: no audio produced for this chapter — check the input file.")
            continue

        sf.write(str(out_path), audio, samplerate=24000, subtype='PCM_16')

        elapsed = time.time() - t0
        duration_min = audio.size / 24000 / 60
        size_mb = out_path.stat().st_size / 1_048_576
        print(f" {duration_min:.1f} min audio, {size_mb:.0f} MB  (rendered in {int(elapsed // 60)}m{int(elapsed % 60):02d}s)")

    print(f"\nAll done. Files written to: {output_dir}/")
    print("Play WAVs in VLC — use [ and ] keys to slow down / speed up playback.")


if __name__ == '__main__':
    main()
