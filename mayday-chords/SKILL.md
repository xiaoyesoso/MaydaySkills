---
name: mayday-chords
description: >
  Analyze the chord progressions, arrangement structures, and key change
  techniques in Mayday's songs. Use when the user asks about guitar chords
  for Mayday songs, wants to learn Mayday-style songwriting, or requests
  music theory analysis of Chinese rock ballads. Covers Monster's arranging
  style and progressive key shifts.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: music-theory
compatibility: Requires Python 3.12+ to run scripts/chord-diagram.py.
---

# Mayday Chord Secrets

## Overview
Deconstruct Monster's (怪兽) arranging philosophy — the chord patterns,
structural builds, and emotional stacking techniques that define Mayday's sound.

## Core Capabilities
1. **Chord lookup** — Given a song name, output the full chord chart
   (verse/chorus/bridge) in both standard notation and Roman-numeral analysis.
2. **Pattern mining** — Identify recurring progression templates across albums
   (e.g. `I-V-vi-IV` with variants).
3. **Key change analysis** — Explain how Mayday uses key changes at climactic
   moments (e.g. 倔强 副歌升 key 逻辑、你不是真正的快乐 半音上行).
4. **Learning roadmap** — Recommend a practice sequence — which songs to
   learn first for different skill levels.

## Instruction Flow
1. Ask the user: a specific song, or a learning goal.
2. **Song path**:
   - Look up the song's key in `references/chord-patterns.md`.
   - Run `scripts/chord-diagram.py <song>` to generate ASCII chord diagrams.
   - Output Roman-numeral analysis + standard chord chart + a short paragraph
     on why the progression works emotionally.
3. **Learning-goal path**:
   - Match the goal to the closest pattern in the database.
   - Output a 3-step practice plan ordered by difficulty.

## Output Format

```
Song: 倔强
Key: A Major
Verse: [A - E - F#m - D] × 2  (I-V-vi-IV)
Pre-Chorus: [Bm7 - E7 - A - F#m]
Chorus: [A - E - F#m - D - Bm7 - E - A]
Bridge: modulates A → B (whole-step up)

✏️ Why it works:
- The classic I-V-vi-IV is the "everyman" pop progression — instantly singable.
- The Bridge's whole-step modulation amplifies the "倔强" theme.
```

## References
- `references/chord-patterns.md` — High-frequency chord pattern database.
- `scripts/chord-diagram.py` — CLI that prints ASCII/Unicode chord diagrams.

## Edge Cases
- **Unknown song** — Ask the user to provide a recording link or partial
  lyric; do not fabricate a chord chart.
- **Multiple known voicings** — Pick the most common live-version voicing and
  note the alternative.
- **Capo / tuning differences** — Always state assumptions explicitly.
- **Copyright** — Charts here are for educational analysis; do not bundle
  full tablature with copyrighted lyrics in the same output.
