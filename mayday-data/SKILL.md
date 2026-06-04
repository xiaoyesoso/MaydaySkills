---
name: mayday-data
description: >
  Visualize Mayday's music data — album sales, streaming trends, concert
  attendance, and search popularity across platforms. Use when the user asks
  for data about Mayday's popularity, wants to see trends in their music,
  requests charts or statistics about the band, or asks for comparative
  analysis of albums, tours, or eras.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: data-visualization
compatibility: Requires Python 3.12+, internet access, and the matplotlib +
  requests Python packages.
---

# Mayday Music Data Dashboard

## Overview
Collect, process, and visualize quantitative data about Mayday's career —
turning years of music into readable charts and insights.

## Data Sources (intended)
1. Streaming platforms — Spotify, KKBOX, QQ Music (where APIs available).
2. YouTube — official MV view counts and trends.
3. Wikipedia / fan wikis — album sales, concert attendance.
4. Public award archives — Golden Melody Awards data.

## Capabilities

### 1. Album Performance Timeline
- Input: metric (`streaming` / `sales` / `awards`).
- Output: chronological line/bar chart of albums with annotations for
  significant events (member service breaks, label change, genre shifts).

### 2. Concert Heatmap
- Input: none (full history) or specific tour.
- Output: world map / city grid of concert frequency × attendance estimates.

### 3. Song Popularity Trends
- Input: one or more song names.
- Output: time-series chart of search interest / streaming count over years.

### 4. Era Comparison
- Input: two time ranges (e.g., 2004-2008 vs 2016-2020).
- Output: side-by-side metrics — avg album sales, tour frequency, awards,
  lyrical theme distribution.

## Instruction Flow
1. Ask the user which view they want (1-4 above).
2. Run `scripts/data-fetcher.py <query-type> <parameters>`.
3. Parse the JSON the script returns.
4. Render the chart/visualization in the response.
5. Provide a plain-text interpretation summary.

## Script Usage

```bash
python scripts/data-fetcher.py album-trend                  # album metrics
python scripts/data-fetcher.py concert-map                   # geo data
python scripts/data-fetcher.py song-trend <song> [<song>...] # time series
python scripts/data-fetcher.py era-compare <s1> <e1> <s2> <e2>
```

See `scripts/data-fetcher.py` — modular CLI with cached JSON output.

## References
- `scripts/data-fetcher.py` — multi-source CLI.

## Edge Cases
- **API rate limits** — Cache JSON results; warn the user when data is stale.
- **Missing data** — Mark gaps explicitly; never invent numbers.
- **Conflicting sources** — Show the range and cite each source.
- **No internet** — Fall back to whatever cached data exists; tell the user
  the chart is offline-mode.
