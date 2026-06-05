#!/usr/bin/env python3
"""score-pitch.py — Mayday karaoke difficulty scorer and practice planner.

Usage:
    python score-pitch.py --song 倔强
    python score-pitch.py --range C3:G4
    python score-pitch.py --song 倔强 --plan 30
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
LYRICS_DB = SKILL_DIR / "references" / "lyrics-db"
DIFFICULTY_DB = SKILL_DIR / "references" / "karaoke-difficulty.json"

# ── Note-to-MIDI mapping ──────────────────────────────────────
NOTE_MAP = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}

def note_to_midi(note: str) -> int:
    """Convert note like 'A4' or 'C#5' to MIDI number."""
    note = note.strip()
    if not note:
        return 60
    name = note[0].upper()
    idx = 1
    accidental = 0
    if idx < len(note) and note[idx] == "#":
        accidental = 1
        idx += 1
    elif idx < len(note) and note[idx] == "b":
        accidental = -1
        idx += 1
    octave = int(note[idx:]) if idx < len(note) else 4
    return (octave + 1) * 12 + NOTE_MAP.get(name, 0) + accidental


# ── Load data ───────────────────────────────────────────────────

def load_songs() -> list[dict]:
    songs: list[dict] = []
    if not LYRICS_DB.is_dir():
        return songs
    for fp in sorted(LYRICS_DB.glob("*.json")):
        if fp.name == "schema.json":
            continue
        data = json.loads(fp.read_text(encoding="utf-8"))
        for s in data.get("songs", []):
            s["_album"] = data.get("album", "")
            s["_year"] = data.get("year", 0)
            songs.append(s)
    return songs


def load_difficulty_db() -> dict:
    if DIFFICULTY_DB.exists():
        data = json.loads(DIFFICULTY_DB.read_text(encoding="utf-8"))
        return {d["title"]: d for d in data}
    return {}


# ── Difficulty scoring ─────────────────────────────────────────

def compute_difficulty(song: dict) -> dict:
    """Compute difficulty score 0-10."""
    key = song.get("key") or "C Major"
    bpm = song.get("bpm") or 100
    segments = song.get("segments", [])

    # Parse highest note from key (heuristic: Major key → root + major 3rd up ~2 octaves)
    # For manual accuracy, check difficulty_db first
    db = load_difficulty_db()
    title = song.get("title", "")
    if title in db:
        return db[title]

    # Heuristic scoring
    # Estimate highest note: root note + major 7th (e.g., C Major → B4)
    root_note = key.split()[0] if key else "C"
    try:
        root_midi = note_to_midi(root_note)
        highest_midi = root_midi + 11  # major 7th up
    except (ValueError, IndexError):
        highest_midi = 71  # B4 default

    # Normalize highest note: C3(48)=0, C6(84)=1
    norm_note = max(0, min(1, (highest_midi - 48) / 36))
    # Normalize BPM: 60=0, 180=1
    norm_bpm = max(0, min(1, (bpm - 60) / 120))
    # Key change: check tags
    has_key_change = 1 if any("升key" in t or "升 key" in t
                              for t in song.get("tags", [])) else 0
    # Continuous singing: segment count × 10s, normalize 0-30s
    cont = min(1.0, len(segments) * 10 / 30)

    score = 0.4 * norm_note + 0.2 * norm_bpm + 0.2 * has_key_change + 0.2 * cont
    score_10 = round(score * 10, 1)

    if score_10 <= 3:
        label = "入门"
    elif score_10 <= 6:
        label = "进阶"
    elif score_10 <= 8:
        label = "困难"
    else:
        label = "唯神能唱"

    return {
        "title": title,
        "album": song.get("_album", ""),
        "difficulty": score_10,
        "label": label,
        "highest_note": f"MIDI {highest_midi}",
        "bpm": bpm,
        "key_changes": has_key_change,
        "hard_parts": [],
    }


# ── Vocal range filter ─────────────────────────────────────────

def filter_by_range(songs: list[dict], low_note: str, high_note: str) -> list[dict]:
    """Filter songs whose highest note is within user's range."""
    try:
        user_high = note_to_midi(high_note)
    except (ValueError, IndexError):
        return []

    results = []
    for song in songs:
        diff = compute_difficulty(song)
        # Parse difficulty's highest_note
        hn = diff.get("highest_note", "")
        if hn.startswith("MIDI "):
            song_high = int(hn.split()[1])
        else:
            try:
                song_high = note_to_midi(hn)
            except (ValueError, IndexError):
                song_high = 71  # B4 default

        if song_high <= user_high:
            results.append(diff)

    results.sort(key=lambda d: d["difficulty"])
    return results


# ── Practice plan ──────────────────────────────────────────────

def generate_plan(difficulty: dict, days: int) -> list[dict]:
    """Generate a day-by-day practice plan."""
    title = difficulty.get("title", "未知")
    label = difficulty.get("label", "进阶")
    plan = []

    if days <= 7:
        phases = [
            (1, days // 2, "段落熟悉", "分段慢速哼唱，不咬字"),
            (days // 2 + 1, days, "全曲跟唱", "慢速→原速渐进"),
        ]
    else:
        phases = [
            (1, days // 4, "段落拆解", "逐段慢速哼唱，重点练难段"),
            (days // 4 + 1, days // 2, "慢速全曲", "0.7x 速度全曲跟唱"),
            (days // 2 + 1, 3 * days // 4, "原速挑战", "原速跟唱 + 换气专项"),
            (3 * days // 4 + 1, days, "精细打磨", "情感表达 + 弱段加强"),
        ]

    for start, end, phase_name, task in phases:
        plan.append({
            "day_range": f"Day {start}–{end}",
            "phase": phase_name,
            "daily_task": task,
            "duration_minutes": 30,
            "target_song": title,
        })

    return plan


# ── CLI ────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description="Mayday karaoke scorer")
    parser.add_argument("--song", default=None, help="Song title to score")
    parser.add_argument("--range", default=None,
                        help="Vocal range as low:high (e.g., C3:G4)")
    parser.add_argument("--plan", type=int, default=None,
                        help="Generate N-day practice plan")

    args = parser.parse_args()
    songs = load_songs()

    if args.song:
        target = None
        for s in songs:
            if s["title"] == args.song:
                target = s
                break
        if not target:
            # Fuzzy match
            for s in songs:
                if args.song in s["title"] or s["title"] in args.song:
                    target = s
                    break
        if not target:
            sys.stderr.write(f"Song not found: {args.song}\n")
            return 1

        diff = compute_difficulty(target)
        output = {"guide": diff}

        if args.plan:
            output["plan"] = generate_plan(diff, args.plan)

        json.dump(output, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")

    elif args.range:
        parts = args.range.split(":")
        if len(parts) != 2:
            sys.stderr.write("Range format: C3:G4\n")
            return 1
        results = filter_by_range(songs, parts[0], parts[1])
        json.dump({"vocal_range": args.range, "recommended": results},
                  sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        sys.stderr.write("Use --song or --range\n")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
