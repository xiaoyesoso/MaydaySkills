#!/usr/bin/env python3
"""lookup.py — Mayday fan-culture dictionary lookup tool.

Supports 4 modes:
    lookup   — exact match on term or alias
    search   — fuzzy search by substring
    daily    — date-stable random term
    random   — completely random term
    list     — list all terms in a category

Usage:
    python lookup.py --term "升 key 战神"
    python lookup.py --mode search --query "升"
    python lookup.py --mode daily
    python lookup.py --mode random
    python lookup.py --mode list --category concert-slang
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
DICT_PATH = SKILL_DIR / "references" / "dictionary.json"


# ── Normalize for matching ────────────────────────────────────

def normalize(s: str) -> str:
    """Normalize for case/whitespace-insensitive matching.
    Strips spaces, lowercases, removes punctuation variations.
    """
    return re.sub(r"\s+", "", s).lower()


# ── Load ───────────────────────────────────────────────────────

def load_dict() -> dict:
    if not DICT_PATH.exists():
        return {"terms": []}
    return json.loads(DICT_PATH.read_text(encoding="utf-8"))


# ── Modes ──────────────────────────────────────────────────────

def mode_lookup(data: dict, term: str) -> dict:
    """Exact match on term or alias (normalized)."""
    target = normalize(term)
    for t in data.get("terms", []):
        if normalize(t.get("term", "")) == target:
            return {"found": True, "mode": "lookup", "term": t}
        if any(normalize(a) == target for a in t.get("aliases", [])):
            return {"found": True, "mode": "lookup", "term": t,
                    "matched_via": "alias"}
    # Fallback: fuzzy
    fuzzy = mode_search(data, term)
    if fuzzy.get("results"):
        return {
            "found": False,
            "mode": "lookup",
            "query": term,
            "suggestions": [r["term"] for r in fuzzy["results"][:5]],
        }
    return {"found": False, "mode": "lookup", "query": term, "suggestions": []}


def mode_search(data: dict, query: str) -> dict:
    """Substring search across term, aliases, definition."""
    q = normalize(query)
    results: list[dict] = []
    for t in data.get("terms", []):
        haystacks = [t.get("term", "")]
        haystacks += t.get("aliases", [])
        haystacks.append(t.get("definition", ""))
        hay_normalized = " ".join(normalize(h) for h in haystacks)
        if q in hay_normalized:
            results.append({
                "id": t.get("id"),
                "term": t.get("term"),
                "category": t.get("category"),
            })
    return {"mode": "search", "query": query, "count": len(results), "results": results}


def mode_daily(data: dict) -> dict:
    """Date-stable random term (same term all day)."""
    today = datetime.date.today().isoformat()
    digest = hashlib.sha256(today.encode("utf-8")).hexdigest()
    terms = data.get("terms", [])
    if not terms:
        return {"mode": "daily", "error": "no_terms"}
    idx = int(digest, 16) % len(terms)
    return {
        "mode": "daily",
        "date": today,
        "term": terms[idx],
    }


def mode_random(data: dict) -> dict:
    """Completely random term."""
    import random
    terms = data.get("terms", [])
    if not terms:
        return {"mode": "random", "error": "no_terms"}
    return {"mode": "random", "term": random.choice(terms)}


def mode_list(data: dict, category: str | None) -> dict:
    """List all terms, optionally filtered by category."""
    terms = data.get("terms", [])
    if category:
        terms = [t for t in terms if t.get("category") == category]
    return {
        "mode": "list",
        "category": category,
        "count": len(terms),
        "terms": [{"id": t.get("id"), "term": t.get("term"),
                   "category": t.get("category")} for t in terms],
    }


# ── CLI ────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Mayday fan-culture dictionary lookup")
    parser.add_argument("--term", help="Term to look up (exact match)")
    parser.add_argument("--mode", default="lookup",
                        choices=["lookup", "search", "daily", "random", "list"],
                        help="Operation mode")
    parser.add_argument("--query", help="Search query (for mode=search)")
    parser.add_argument("--category", help="Category filter (for mode=list)")
    args = parser.parse_args()

    data = load_dict()

    if args.mode == "lookup":
        if not args.term:
            sys.stderr.write("--term required for lookup mode\n")
            return 1
        result = mode_lookup(data, args.term)
    elif args.mode == "search":
        if not args.query:
            sys.stderr.write("--query required for search mode\n")
            return 1
        result = mode_search(data, args.query)
    elif args.mode == "daily":
        result = mode_daily(data)
    elif args.mode == "random":
        result = mode_random(data)
    elif args.mode == "list":
        result = mode_list(data, args.category)
    else:
        result = {"error": "unknown_mode"}

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
