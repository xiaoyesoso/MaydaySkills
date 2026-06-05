#!/usr/bin/env python3
"""build-program.py — Compose a Mayday-themed radio program.

Reads lyrics-db for song metadata, applies mood arc matching,
and outputs a JSON program structure with track list and timing.

Usage:
    python build-program.py --theme 失恋治愈 --duration 30
    python build-program.py --theme 通勤励志 --duration 45 --skip 派对动物,轧车
    python build-program.py --theme 自定义 --duration 60 --arc 3,2,5,4,8,7
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
LYRICS_DB = SKILL_DIR / "references" / "lyrics-db"
TEMPLATES = SKILL_DIR / "references" / "program-templates.json"

# ── Load lyrics-db ─────────────────────────────────────────────

def load_songs() -> list[dict]:
    """Load all songs from lyrics-db JSON files."""
    songs: list[dict] = []
    if not LYRICS_DB.is_dir():
        return songs
    for fp in sorted(LYRICS_DB.glob("*.json")):
        if fp.name == "schema.json":
            continue
        data = json.loads(fp.read_text(encoding="utf-8"))
        album = data.get("album", "")
        year = data.get("year", 0)
        for s in data.get("songs", []):
            s["_album"] = album
            s["_year"] = year
            songs.append(s)
    return songs


# ── Mood matching ──────────────────────────────────────────────

def mood_score(song: dict, target_E: float, target_V: float,
               target_themes: list[str] | None = None) -> float:
    """Score a song against target mood. Higher = better match.
    Formula: score = -sqrt(ΔE² + ΔV²) + 2·|theme_overlap|
    (Same formula as mayday-mood's mood-taxonomy.md)
    """
    m = song.get("mood", {})
    s_E = m.get("energy", 5)
    s_V = m.get("valence", 5)
    s_themes = m.get("themes", [])

    dE = s_E - target_E
    dV = s_V - target_V
    distance = math.sqrt(dE * dE + dV * dV)

    overlap = 0
    if target_themes:
        overlap = len(set(s_themes) & set(target_themes))

    return -distance + 2 * overlap


def estimate_duration(song: dict) -> int:
    """Estimate song duration in seconds from BPM and segments.
    Heuristic: verse≈30s, chorus≈35s, other segments≈20s.
    Minimum 180s (3 min), maximum 360s (6 min).
    """
    segments = song.get("segments", [])
    if segments:
        total = 0
        for seg in segments:
            seg_type = seg.get("type", "verse")
            if seg_type == "chorus":
                total += 35
            elif seg_type == "verse":
                total += 30
            else:
                total += 20
        return max(180, min(360, total))
    # fallback: BPM-based guess
    bpm = song.get("bpm", 100)
    return max(180, min(360, int(240 * 100 / max(bpm, 60))))


# ── Program builder ────────────────────────────────────────────

def load_templates() -> dict:
    if TEMPLATES.exists():
        return json.loads(TEMPLATES.read_text(encoding="utf-8"))
    return {"templates": []}


def find_template(templates: dict, theme: str) -> dict | None:
    for t in templates.get("templates", []):
        if theme in (t.get("id", ""), t.get("name", ""), t.get("name_en", "")):
            return t
    return None


def build_program(
    theme: str,
    duration_minutes: int,
    arc: list[tuple[float, float]] | None = None,
    skip_songs: list[str] | None = None,
) -> dict:
    songs = load_songs()
    templates = load_templates()
    skip_set = set(skip_songs or [])

    # Filter skipped songs
    available = [s for s in songs if s["title"] not in skip_set]

    # Resolve mood arc
    if arc is None:
        tmpl = find_template(templates, theme)
        if tmpl:
            arc = [
                (seg["target_E"], seg["target_V"])
                for seg in tmpl.get("mood_arc", [])
            ]
        else:
            # Default: mid-energy balanced arc
            n_segments = max(3, duration_minutes // 6)
            arc = [
                (4 + i * 2 / n_segments, 4 + i * 2 / n_segments)
                for i in range(n_segments)
            ]

    # Infer themes from template if available
    tmpl = find_template(templates, theme)
    target_themes = None
    if tmpl:
        # Derive themes from the arc endpoints (heuristic)
        dj_style = tmpl.get("dj_style", "warm")
        style_themes = {
            "warm": ["love", "growth"],
            "philosophical": ["growth", "dream-chasing"],
            "playful": ["celebration", "friendship"],
            "nostalgic": ["nostalgia", "growth"],
        }
        target_themes = style_themes.get(dj_style)

    # Select tracks: for each arc segment, pick best-matching unused song
    target_seconds = duration_minutes * 60
    # Reserve ~10% for DJ text
    music_seconds = int(target_seconds * 0.85)

    selected: list[dict] = []
    used_titles: set[str] = set()
    elapsed = 0
    arc_idx = 0

    while elapsed < music_seconds and available:
        # Current arc segment (cycle through arc if needed)
        t_E, t_V = arc[arc_idx % len(arc)]
        # Shift target themes based on arc position
        remaining_ratio = 1 - elapsed / music_seconds
        current_themes = target_themes if target_themes else None

        # Score all available songs
        candidates = [
            (s, mood_score(s, t_E, t_V, current_themes))
            for s in available
            if s["title"] not in used_titles
        ]
        if not candidates:
            break

        # Pick best
        candidates.sort(key=lambda x: x[1], reverse=True)
        best_song, best_score = candidates[0]

        dur = estimate_duration(best_song)
        selected.append({
            "title": best_song["title"],
            "album": best_song.get("_album", ""),
            "year": best_song.get("_year", 0),
            "duration_seconds": dur,
            "energy": best_song.get("mood", {}).get("energy", 5),
            "valence": best_song.get("mood", {}).get("valence", 5),
            "themes": best_song.get("mood", {}).get("themes", []),
            "anchor_emotion": best_song.get("mood", {}).get("anchor_emotion", ""),
            "lyrics_excerpt": best_song.get("lyrics_excerpt", ""),
            "segment_label": f"segment_{arc_idx % len(arc) + 1}",
        })

        used_titles.add(best_song["title"])
        elapsed += dur
        arc_idx += 1

    # Build output
    template_name = tmpl.get("name", theme) if tmpl else theme
    dj_style = tmpl.get("dj_style", "warm") if tmpl else "warm"

    return {
        "program_name": f"五月天{template_name}电台",
        "theme": theme,
        "duration_minutes": duration_minutes,
        "dj_style": dj_style,
        "track_count": len(selected),
        "total_music_seconds": elapsed,
        "suggested_opener": tmpl.get("suggested_opener", "") if tmpl else "",
        "suggested_closer": tmpl.get("suggested_closer", "") if tmpl else "",
        "mood_arc": [{"target_E": e, "target_V": v} for e, v in arc],
        "tracks": selected,
    }


# ── CLI ────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description="Build a Mayday radio program")
    parser.add_argument("--theme", required=True, help="Program theme")
    parser.add_argument("--duration", type=int, required=True,
                        help="Duration in minutes (30/60/90/120)")
    parser.add_argument("--arc", default=None,
                        help="Custom mood arc as E1,V1,E2,V2,...")
    parser.add_argument("--skip", default=None,
                        help="Comma-separated song titles to skip")

    args = parser.parse_args()

    arc = None
    if args.arc:
        vals = [float(x) for x in args.arc.split(",")]
        if len(vals) < 2 or len(vals) % 2 != 0:
            sys.stderr.write("Arc must have pairs: E1,V1,E2,V2,...\n")
            return 1
        arc = [(vals[i], vals[i + 1]) for i in range(0, len(vals), 2)]

    skip = args.skip.split(",") if args.skip else None

    result = build_program(args.theme, args.duration, arc, skip)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
