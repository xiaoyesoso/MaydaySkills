#!/usr/bin/env python3
"""data-fetcher.py — modular CLI for Mayday music data.

Used by the `mayday-data` skill. Each subcommand returns JSON to stdout so
the skill can parse it and render charts.

Subcommands:
    album-trend             Album-level metrics (sales/streaming/awards)
    concert-map             Concert geo-distribution (city, count, est. attendance)
    song-trend <song...>    Time-series search/streaming interest per song
    era-compare <s1> <e1> <s2> <e2>   Side-by-side era statistics

This is a SCAFFOLD. Real implementations should wire to Spotify, YouTube
Data API, KKBOX, Wikipedia, etc. Right now each subcommand returns a static
JSON sample so downstream consumers can integrate against a stable shape.

Replace `_TODO_real_*` helpers with live API calls and add caching to
`~/.cache/mayday-data/` for rate-limit safety.
"""
from __future__ import annotations

import json
import sys
from typing import Any

USAGE = """\
usage: data-fetcher.py <subcommand> [args]

subcommands:
  album-trend
  concert-map
  song-trend <song> [<song>...]
  era-compare <start1> <end1> <start2> <end2>
"""


def _stub(payload: dict[str, Any]) -> dict[str, Any]:
    payload["_meta"] = {
        "source": "stub",
        "note": "Scaffold output. Replace with live API integration.",
    }
    return payload


def album_trend() -> dict[str, Any]:
    return _stub({
        "metric": "streaming_index",
        "unit": "normalized (max=100)",
        "data": [
            {"album": "第一张创作专辑", "year": 1999, "value": 28},
            {"album": "爱情万岁",       "year": 2000, "value": 35},
            {"album": "人生海海",       "year": 2001, "value": 40},
            {"album": "时光机",         "year": 2003, "value": 52},
            {"album": "神的孩子都在跳舞", "year": 2004, "value": 70},
            {"album": "为爱而生",       "year": 2006, "value": 64},
            {"album": "后青春期的诗",   "year": 2008, "value": 88},
            {"album": "第二人生",       "year": 2011, "value": 82},
            {"album": "自传",           "year": 2016, "value": 100},
        ],
    })


def concert_map() -> dict[str, Any]:
    return _stub({
        "unit": "shows",
        "data": [
            {"city": "Taipei",     "country": "TW", "shows": 45},
            {"city": "Kaohsiung",  "country": "TW", "shows": 22},
            {"city": "Shanghai",   "country": "CN", "shows": 18},
            {"city": "Beijing",    "country": "CN", "shows": 16},
            {"city": "Hong Kong",  "country": "HK", "shows": 14},
            {"city": "Singapore",  "country": "SG", "shows": 9},
            {"city": "Tokyo",      "country": "JP", "shows": 6},
            {"city": "Los Angeles","country": "US", "shows": 4},
        ],
    })


def song_trend(songs: list[str]) -> dict[str, Any]:
    if not songs:
        raise SystemExit("song-trend requires at least one song name")
    years = list(range(2010, 2026))
    return _stub({
        "metric": "search_interest",
        "unit": "Google Trends (0-100)",
        "series": [
            {
                "song": s,
                "years": years,
                "values": [40 + (i * 3) % 60 for i, _ in enumerate(years)],
            }
            for s in songs
        ],
    })


def era_compare(s1: int, e1: int, s2: int, e2: int) -> dict[str, Any]:
    return _stub({
        "eras": [
            {
                "label": f"{s1}-{e1}",
                "avg_album_sales_k": 380,
                "tours": 2,
                "awards": 5,
                "themes": {
                    "dream-chasing": 0.32,
                    "love": 0.21,
                    "growth": 0.18,
                    "rebellion": 0.12,
                    "other": 0.17,
                },
            },
            {
                "label": f"{s2}-{e2}",
                "avg_album_sales_k": 260,
                "tours": 3,
                "awards": 7,
                "themes": {
                    "dream-chasing": 0.22,
                    "love": 0.18,
                    "growth": 0.28,
                    "rebellion": 0.10,
                    "other": 0.22,
                },
            },
        ],
    })


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        sys.stderr.write(USAGE)
        return 2

    cmd = argv[1]
    try:
        if cmd == "album-trend":
            result = album_trend()
        elif cmd == "concert-map":
            result = concert_map()
        elif cmd == "song-trend":
            result = song_trend(argv[2:])
        elif cmd == "era-compare":
            if len(argv) != 6:
                sys.stderr.write(
                    "era-compare needs 4 args: <start1> <end1> <start2> <end2>\n"
                )
                return 2
            s1, e1, s2, e2 = (int(x) for x in argv[2:6])
            result = era_compare(s1, e1, s2, e2)
        else:
            sys.stderr.write(USAGE)
            return 2
    except ValueError as exc:
        sys.stderr.write(f"bad argument: {exc}\n")
        return 2

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
