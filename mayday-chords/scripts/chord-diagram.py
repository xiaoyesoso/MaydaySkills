#!/usr/bin/env python3
"""chord-diagram.py — print ASCII/Unicode guitar chord diagrams.

Used by the `mayday-chords` skill. Looks up a chord by name in a small
built-in dictionary and prints a 6-string fretboard diagram.

Usage:
    python chord-diagram.py <chord-name>
    python chord-diagram.py Am
    python chord-diagram.py "F#m7"

Exit codes:
    0  success
    1  unknown chord
    2  bad usage

This is a scaffold implementation. The chord dictionary covers the most
common open-position shapes used in Mayday's catalog. Extend `CHORDS` as
needed.
"""
from __future__ import annotations

import sys
from typing import List

# Each chord = list of 6 fret values from low E (string 6) to high E (string 1).
# Convention: -1 = muted, 0 = open, n = fretted at fret n.
CHORDS: dict[str, list[int]] = {
    # Open-position major
    "C":  [-1, 3, 2, 0, 1, 0],
    "D":  [-1, -1, 0, 2, 3, 2],
    "E":  [0, 2, 2, 1, 0, 0],
    "F":  [1, 3, 3, 2, 1, 1],
    "G":  [3, 2, 0, 0, 0, 3],
    "A":  [-1, 0, 2, 2, 2, 0],
    "B":  [-1, 2, 4, 4, 4, 2],
    # Open-position minor
    "Am": [-1, 0, 2, 2, 1, 0],
    "Dm": [-1, -1, 0, 2, 3, 1],
    "Em": [0, 2, 2, 0, 0, 0],
    "Bm": [-1, 2, 4, 4, 3, 2],
    "F#m": [2, 4, 4, 2, 2, 2],
    # Sevenths
    "Am7": [-1, 0, 2, 0, 1, 0],
    "Dm7": [-1, -1, 0, 2, 1, 1],
    "Em7": [0, 2, 0, 0, 0, 0],
    "G7":  [3, 2, 0, 0, 0, 1],
    "E7":  [0, 2, 0, 1, 0, 0],
    "Bm7": [-1, 2, 4, 2, 3, 2],
}

STRING_NAMES = ["E", "A", "D", "G", "B", "e"]  # low to high


def render(name: str, frets: List[int]) -> str:
    """Return a printable ASCII fretboard for the given chord."""
    max_fret = max((f for f in frets if f > 0), default=0)
    span = max(max_fret, 4)  # show at least 4 frets

    header_states = ["x" if f == -1 else ("o" if f == 0 else " ") for f in frets]
    # Top header: open/muted markers, low-E left → high-E right.
    header = "    " + "  ".join(header_states)

    rows = [header]
    # Build each fret row.
    for fret in range(1, span + 1):
        cells = []
        for f in frets:
            if f == fret:
                cells.append("●")
            else:
                cells.append("│")
        rows.append(f" {fret}  " + "──".join(cells))
    rows.append("    " + "  ".join(STRING_NAMES))

    return f"Chord: {name}\n" + "\n".join(rows)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("usage: chord-diagram.py <chord-name>\n")
        return 2
    name = argv[1]
    if name not in CHORDS:
        sys.stderr.write(
            f"unknown chord '{name}'. Known: {', '.join(sorted(CHORDS))}\n"
        )
        return 1
    print(render(name, CHORDS[name]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
