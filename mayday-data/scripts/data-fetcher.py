#!/usr/bin/env python3
"""data-fetcher.py — modular CLI for Mayday music data.

Used by the `mayday-data` skill. Each subcommand returns JSON to stdout so
the skill can parse it and render charts.

Subcommands:
    album-trend             Album-level metrics (sales/streaming/awards)
    concert-map             Concert geo-distribution (city, count, est. attendance)
    song-trend <song...>    Time-series search/streaming interest per song
    era-compare <s1> <e1> <s2> <e2>   Side-by-side era statistics
    spotify-popularity      Live Spotify popularity for Mayday top tracks
    youtube-views <q>       Live YouTube view counts for query (videos)

Live integrations are activated by environment variables. When credentials
are missing, the command falls back to deterministic mock data with a
"_meta.source": "stub" marker so downstream charts still render.

Required env vars (only if you want LIVE data):
    SPOTIFY_CLIENT_ID
    SPOTIFY_CLIENT_SECRET
    YOUTUBE_API_KEY

Optional:
    MAYDAY_DATA_CACHE_DIR (default ~/.cache/mayday-data)
"""
from __future__ import annotations

import base64
import json
import os
import sys
import time
from pathlib import Path
from typing import Any
from urllib import error as urlerror
from urllib import parse, request

USAGE = """\
usage: data-fetcher.py <subcommand> [args]

subcommands:
  album-trend
  concert-map
  song-trend <song> [<song>...]
  era-compare <start1> <end1> <start2> <end2>
  spotify-popularity
  youtube-views <query>
"""

CACHE_DIR = Path(os.environ.get(
    "MAYDAY_DATA_CACHE_DIR",
    str(Path.home() / ".cache" / "mayday-data"),
))
CACHE_TTL_SECONDS = 60 * 60 * 6  # 6h


def _cache_path(name: str) -> Path:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in name)
    return CACHE_DIR / f"{safe}.json"


def _cache_get(name: str) -> dict | None:
    path = _cache_path(name)
    if not path.exists():
        return None
    if time.time() - path.stat().st_mtime > CACHE_TTL_SECONDS:
        return None
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return None


def _cache_put(name: str, data: dict) -> None:
    _cache_path(name).write_text(json.dumps(data, ensure_ascii=False))


def _stub(payload: dict[str, Any]) -> dict[str, Any]:
    payload["_meta"] = {
        "source": "stub",
        "note": "Scaffold output. Set API env vars to enable live data.",
    }
    return payload


def _live(payload: dict[str, Any], source: str) -> dict[str, Any]:
    payload["_meta"] = {"source": source}
    return payload


# ────────────────────────────────────────────────────────────────────────
# Stub subcommands (no external calls)
# ────────────────────────────────────────────────────────────────────────
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
                    "dream-chasing": 0.32, "love": 0.21, "growth": 0.18,
                    "rebellion": 0.12, "other": 0.17,
                },
            },
            {
                "label": f"{s2}-{e2}",
                "avg_album_sales_k": 260,
                "tours": 3,
                "awards": 7,
                "themes": {
                    "dream-chasing": 0.22, "love": 0.18, "growth": 0.28,
                    "rebellion": 0.10, "other": 0.22,
                },
            },
        ],
    })


# ────────────────────────────────────────────────────────────────────────
# Live integrations: Spotify Web API & YouTube Data API
# ────────────────────────────────────────────────────────────────────────
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE = "https://api.spotify.com/v1"
YOUTUBE_API_BASE = "https://www.googleapis.com/youtube/v3"

# Spotify artist id for 五月天 (Mayday) — public, verified.
MAYDAY_SPOTIFY_ARTIST_ID = "0eDvMgVFoNV3TpwtrVCoTj"


def _http_get(url: str, headers: dict[str, str] | None = None,
              params: dict[str, str] | None = None,
              timeout: int = 10) -> dict[str, Any]:
    if params:
        url = f"{url}?{parse.urlencode(params)}"
    req = request.Request(url, headers=headers or {})
    with request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _http_post_form(url: str, form: dict[str, str],
                    headers: dict[str, str] | None = None,
                    timeout: int = 10) -> dict[str, Any]:
    data = parse.urlencode(form).encode("utf-8")
    req = request.Request(url, data=data, headers=headers or {})
    with request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _spotify_token() -> str | None:
    """Get a Spotify client-credentials access token, cached on disk."""
    cid = os.environ.get("SPOTIFY_CLIENT_ID")
    csec = os.environ.get("SPOTIFY_CLIENT_SECRET")
    if not cid or not csec:
        return None

    cache = _cache_get("spotify_token")
    if cache and cache.get("expires_at", 0) > time.time() + 30:
        return cache["access_token"]

    auth = base64.b64encode(f"{cid}:{csec}".encode()).decode()
    data = _http_post_form(
        SPOTIFY_TOKEN_URL,
        {"grant_type": "client_credentials"},
        {"Authorization": f"Basic {auth}"},
    )
    token = data["access_token"]
    expires = int(time.time()) + int(data.get("expires_in", 3600))
    _cache_put("spotify_token", {"access_token": token, "expires_at": expires})
    return token


def spotify_popularity() -> dict[str, Any]:
    token = _spotify_token()
    if not token:
        return _stub({
            "metric": "spotify_popularity",
            "unit": "0-100",
            "data": [
                {"track": "突然好想你", "popularity": 72},
                {"track": "倔强",        "popularity": 70},
                {"track": "干杯",        "popularity": 68},
                {"track": "后来的我们",   "popularity": 75},
                {"track": "我不愿让你一个人", "popularity": 76},
            ],
        })

    cached = _cache_get("spotify_top_tracks")
    if cached:
        return _live(cached, "spotify-cache")

    try:
        data = _http_get(
            f"{SPOTIFY_API_BASE}/artists/{MAYDAY_SPOTIFY_ARTIST_ID}/top-tracks",
            headers={"Authorization": f"Bearer {token}"},
            params={"market": "TW"},
        )
    except urlerror.HTTPError as exc:
        return _stub({
            "metric": "spotify_popularity",
            "error": f"HTTP {exc.code} from Spotify",
            "data": [],
        })

    tracks = [
        {
            "track": t["name"],
            "album": t["album"]["name"],
            "release_date": t["album"]["release_date"],
            "popularity": t["popularity"],
            "preview_url": t.get("preview_url"),
            "spotify_id": t["id"],
        }
        for t in data.get("tracks", [])
    ]
    payload = {
        "metric": "spotify_popularity",
        "unit": "0-100",
        "artist_id": MAYDAY_SPOTIFY_ARTIST_ID,
        "market": "TW",
        "data": tracks,
    }
    _cache_put("spotify_top_tracks", payload)
    return _live(payload, "spotify")


def youtube_views(query: str) -> dict[str, Any]:
    key = os.environ.get("YOUTUBE_API_KEY")
    if not key:
        return _stub({
            "metric": "youtube_views",
            "query": query,
            "unit": "views",
            "data": [
                {"title": f"{query} (mock)", "video_id": "stub",
                 "views": 12_345_678, "channel": "Stub Records"},
            ],
        })

    cache_key = f"youtube_search_{query}"
    cached = _cache_get(cache_key)
    if cached:
        return _live(cached, "youtube-cache")

    try:
        search = _http_get(
            f"{YOUTUBE_API_BASE}/search",
            params={
                "key": key, "part": "snippet", "type": "video",
                "q": f"五月天 {query}", "maxResults": "10",
            },
        )
        video_ids = [item["id"]["videoId"] for item in search.get("items", [])]
        if not video_ids:
            return _stub({
                "metric": "youtube_views", "query": query, "data": [],
            })

        stats = _http_get(
            f"{YOUTUBE_API_BASE}/videos",
            params={
                "key": key, "part": "snippet,statistics",
                "id": ",".join(video_ids),
            },
        )
    except urlerror.HTTPError as exc:
        return _stub({
            "metric": "youtube_views", "query": query,
            "error": f"HTTP {exc.code} from YouTube",
            "data": [],
        })

    rows = [
        {
            "title": item["snippet"]["title"],
            "video_id": item["id"],
            "channel": item["snippet"]["channelTitle"],
            "published_at": item["snippet"]["publishedAt"],
            "views": int(item["statistics"].get("viewCount", 0)),
            "likes": int(item["statistics"].get("likeCount", 0)),
        }
        for item in stats.get("items", [])
    ]
    rows.sort(key=lambda r: r["views"], reverse=True)
    payload = {
        "metric": "youtube_views", "query": query, "unit": "views",
        "data": rows,
    }
    _cache_put(cache_key, payload)
    return _live(payload, "youtube")


# ────────────────────────────────────────────────────────────────────────
# CLI dispatch
# ────────────────────────────────────────────────────────────────────────
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
        elif cmd == "spotify-popularity":
            result = spotify_popularity()
        elif cmd == "youtube-views":
            if len(argv) < 3:
                sys.stderr.write("youtube-views needs a search query\n")
                return 2
            result = youtube_views(" ".join(argv[2:]))
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
