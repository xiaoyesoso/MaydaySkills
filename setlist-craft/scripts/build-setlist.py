#!/usr/bin/env python3
"""build-setlist.py — Compose a custom Mayday setlist.

Reads lyrics-db for song metadata, applies mood-curve matching with
must-include / must-exclude / max-high constraints, and outputs a JSON
setlist with track list, timing, and an ASCII mood curve.

Usage:
    python build-setlist.py --occasion "生日趴" --count 20 --curve "平到嗨"
    python build-setlist.py --occasion "纪念日" --count 10 \\
        --include 突然好想你,OAOA --exclude 轧车,派对动物 --max-high 1
    python build-setlist.py --occasion "巡演" --count 14 \\
        --custom-curve 6,9,7,9,5,3,4,6,8,9,7,5
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
LYRICS_DB = SKILL_DIR / "references" / "lyrics-db"
PRESETS = SKILL_DIR / "references" / "curve-presets.json"

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


# ── Mood scoring (same formula as mayday-mood) ────────────────

def mood_distance(song: dict, target_E: float, target_V: float) -> float:
    """Smaller = better. -sqrt(ΔE² + ΔV²)."""
    m = song.get("mood", {})
    s_E = m.get("energy", 5)
    s_V = m.get("valence", 5)
    dE = s_E - target_E
    dV = s_V - target_V
    return -math.sqrt(dE * dE + dV * dV)


# ── Duration estimation (same as mayday-radio) ────────────────

def estimate_duration(song: dict) -> int:
    """Estimate song duration in seconds.
    Heuristic: verse≈30s, chorus≈35s, other segments≈20s.
    Min 180s, max 360s. Falls back to duration_seconds or BPM-based guess.
    """
    if song.get("duration_seconds"):
        return max(180, min(360, song["duration_seconds"]))
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
    bpm = song.get("bpm") or 100
    return max(180, min(360, int(240 * 100 / max(bpm, 60))))


# ── Preset lookup ──────────────────────────────────────────────

def load_presets() -> dict:
    if PRESETS.exists():
        return json.loads(PRESETS.read_text(encoding="utf-8"))
    return {"presets": []}


def find_preset(presets: dict, name: str) -> dict | None:
    for p in presets.get("presets", []):
        if name in (p.get("id", ""), p.get("name", ""), p.get("name_en", "")):
            return p
    return None


def resolve_curve(
    count: int,
    curve_name: str | None,
    custom_curve: list[tuple[float, float]] | None,
    presets: dict,
) -> list[tuple[float, float]]:
    """Resolve mood curve to a list of (E, V) pairs of length `count`."""
    if custom_curve:
        # custom_curve is already list of (E, V) pairs
        if len(custom_curve) >= count:
            return custom_curve[:count]
        # extend by repeating last value
        return custom_curve + [custom_curve[-1]] * (count - len(custom_curve))

    if curve_name:
        p = find_preset(presets, curve_name)
        if p:
            E = p.get("energy_curve", [])
            V = p.get("valence_curve", [])
            pairs = list(zip(E, V))
            if len(pairs) >= count:
                return pairs[:count]
            return pairs + [pairs[-1]] * (count - len(pairs))

    # Default: gentle rise
    return [(3 + i * 4 / max(count - 1, 1), 4 + i * 3 / max(count - 1, 1))
            for i in range(count)]


# ── Why explanation ────────────────────────────────────────────

def explain(song: dict, target_E: float, target_V: float) -> str:
    """One-line explanation of why this song fits the slot."""
    s_E = song.get("mood", {}).get("energy", 5)
    s_V = song.get("mood", {}).get("valence", 5)
    parts = []
    if s_E <= 3:
        parts.append("平静")
    elif s_E >= 8:
        parts.append("高能")
    else:
        parts.append("中速")
    if s_V <= 3:
        parts.append("情绪偏沉")
    elif s_V >= 7:
        parts.append("情绪上扬")
    else:
        parts.append("情绪中性")
    if song.get("mood", {}).get("anchor_emotion"):
        parts.append(f"— {song['mood']['anchor_emotion']}")
    return "，".join(parts)


# ── Build setlist ──────────────────────────────────────────────

def build_setlist(
    occasion: str,
    count: int,
    curve_name: str | None = None,
    custom_curve: list[tuple[float, float]] | None = None,
    must_include: list[str] | None = None,
    must_exclude: list[str] | None = None,
    max_high: int | None = None,
) -> dict:
    songs = load_songs()
    presets = load_presets()
    must_include = must_include or []
    must_exclude = set(must_exclude or [])

    # Filter pool
    available = [s for s in songs if s["title"] not in must_exclude]
    if not available:
        return {"error": "no_songs_after_exclude", "setlist": []}

    # Resolve curve
    curve = resolve_curve(count, curve_name, custom_curve, presets)

    # First pass: slot must-include songs in their best-matching positions
    # (greedy: place each must-include at the slot whose target it matches best)
    slots: list[dict | None] = [None] * count
    used_titles: set[str] = set()

    for mi_title in must_include:
        match = next((s for s in available if s["title"] == mi_title), None)
        if not match:
            return {
                "error": "must_include_not_found",
                "missing": mi_title,
                "setlist": [],
            }
        # Find best slot
        best_idx = 0
        best_score = -math.inf
        for i, (tE, tV) in enumerate(curve):
            if slots[i] is not None:
                continue
            sc = mood_distance(match, tE, tV)
            if sc > best_score:
                best_score = sc
                best_idx = i
        slots[best_idx] = match
        used_titles.add(match["title"])

    # Second pass: fill remaining slots with best matches
    high_count = 0
    for i, (tE, tV) in enumerate(curve):
        if slots[i] is not None:
            if slots[i].get("mood", {}).get("energy", 0) >= 8:
                high_count += 1
            continue

        candidates = [
            s for s in available
            if s["title"] not in used_titles
            and (max_high is None or high_count < max_high
                 or s.get("mood", {}).get("energy", 0) < 8)
        ]
        if not candidates:
            # relax max_high constraint if no candidates
            candidates = [s for s in available if s["title"] not in used_titles]
        if not candidates:
            slots[i] = None  # gap
            continue

        candidates.sort(key=lambda s: mood_distance(s, tE, tV), reverse=True)
        chosen = candidates[0]
        slots[i] = chosen
        used_titles.add(chosen["title"])
        if chosen.get("mood", {}).get("energy", 0) >= 8:
            high_count += 1

    # Build track list
    tracks: list[dict] = []
    total_seconds = 0
    for i, song in enumerate(slots):
        if song is None:
            tracks.append({
                "slot": i + 1,
                "title": None,
                "note": "no_match",
            })
            continue
        dur = estimate_duration(song)
        total_seconds += dur
        tE, tV = curve[i]
        tracks.append({
            "slot": i + 1,
            "title": song["title"],
            "album": song.get("_album", ""),
            "year": song.get("_year", 0),
            "energy": song.get("mood", {}).get("energy", 5),
            "valence": song.get("mood", {}).get("valence", 5),
            "themes": song.get("mood", {}).get("themes", []),
            "duration_seconds": dur,
            "lyrics_excerpt": song.get("lyrics_excerpt", ""),
            "target_E": tE,
            "target_V": tV,
            "why": explain(song, tE, tV),
            "locked": song["title"] in must_include,
        })

    # Encore candidates: high-V, high-E songs not in the setlist
    encore_pool = [
        s for s in available
        if s["title"] not in used_titles
        and s.get("mood", {}).get("energy", 0) >= 7
        and s.get("mood", {}).get("valence", 0) >= 7
    ]
    encore_pool.sort(
        key=lambda s: s.get("mood", {}).get("valence", 0)
        + s.get("mood", {}).get("energy", 0),
        reverse=True,
    )
    encore = [s["title"] for s in encore_pool[:3]]

    return {
        "setlist_name": f"{occasion} Setlist",
        "occasion": occasion,
        "curve_name": curve_name or "custom",
        "track_count": sum(1 for t in tracks if t.get("title")),
        "total_duration_seconds": total_seconds,
        "total_duration_minutes": round(total_seconds / 60, 1),
        "mood_curve": [
            {"slot": i + 1, "target_E": e, "target_V": v}
            for i, (e, v) in enumerate(curve)
        ],
        "tracks": tracks,
        "encore_candidates": encore,
        "warnings": _warnings(tracks, must_include, curve),
    }


def _warnings(tracks: list[dict], must_include: list[str],
              curve: list[tuple[float, float]]) -> list[str]:
    warns: list[str] = []
    gaps = [t for t in tracks if t.get("title") is None]
    if gaps:
        warns.append(f"{len(gaps)} 个 slot 未找到匹配曲目")
    for t in tracks:
        if not t.get("title"):
            continue
        # Detect flatness: locked must-include far from target
        if t.get("locked"):
            dE = abs(t["energy"] - t["target_E"])
            dV = abs(t["valence"] - t["target_V"])
            if math.sqrt(dE * dE + dV * dV) > 4:
                warns.append(
                    f"slot {t['slot']} 的必选《{t['title']}》"
                    f"与目标曲线偏离较远（Δ={math.sqrt(dE*dE + dV*dV):.1f}）"
                )
    return warns


# ── CLI ────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description="Build a custom Mayday setlist")
    parser.add_argument("--occasion", required=True, help="Occasion name")
    parser.add_argument("--count", type=int, required=True, help="Number of songs")
    parser.add_argument("--curve", default=None,
                        help="Preset curve name (e.g. 平到嗨, lyrical-night)")
    parser.add_argument("--custom-curve", default=None,
                        help="Custom E/V curve: E1,V1,E2,V2,...")
    parser.add_argument("--include", default=None,
                        help="Comma-separated must-include song titles")
    parser.add_argument("--exclude", default=None,
                        help="Comma-separated must-exclude song titles")
    parser.add_argument("--max-high", type=int, default=None,
                        help="Max number of high-energy (E>=8) songs")
    args = parser.parse_args()

    custom_curve = None
    if args.custom_curve:
        vals = [float(x) for x in args.custom_curve.split(",")]
        if len(vals) < 2 or len(vals) % 2 != 0:
            sys.stderr.write("custom-curve must be pairs: E1,V1,E2,V2,...\n")
            return 1
        custom_curve = [(vals[i], vals[i + 1]) for i in range(0, len(vals), 2)]

    include = [s.strip() for s in args.include.split(",")] if args.include else None
    exclude = [s.strip() for s in args.exclude.split(",")] if args.exclude else None

    result = build_setlist(
        occasion=args.occasion,
        count=args.count,
        curve_name=args.curve,
        custom_curve=custom_curve,
        must_include=include,
        must_exclude=exclude,
        max_high=args.max_high,
    )
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
