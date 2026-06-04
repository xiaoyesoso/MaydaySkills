---
name: mayday-mood
description: >
  Match Mayday songs to the user's emotional state using a mood-labeled lyrics
  database. Use when the user wants to find Mayday songs by feeling, needs a
  mood-based playlist, asks "what Mayday song fits my mood," or describes an
  emotional situation and wants a song recommendation.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: music-discovery
compatibility: No external dependencies.
---

# Mayday Mood Matcher

## Overview
A mood-to-song recommendation engine that labels every Mayday song across
multiple emotional dimensions and finds the best match for any user-described
state. Reads mood metadata from `references/lyrics-db/*.json`.

## Mood Taxonomy (3-Axis)

| Axis | Range | Description |
|------|-------|-------------|
| **Energy** | 0 (calm) → 10 (explosive) | Sonic / kinetic intensity. |
| **Valence** | 0 (sad) → 10 (joyful) | Emotional positivity. |
| **Theme** | enum | `love`, `friendship`, `dream-chasing`, `loss`, `nostalgia`, `rebellion`, `growth`, `celebration` |

Full taxonomy in `references/mood-taxonomy.md`.

## Instruction Flow

### A. Mood-Based Recommendation
1. Ask user: 「现在心情如何？」 (free-text response welcomed).
2. Parse the response into the 3-axis taxonomy:
   - Map emotional keywords to Energy/Valence scores (see taxonomy doc).
   - Extract themes from contextual clues.
3. Query `references/lyrics-db/*.json`, score each song by Euclidean distance
   on Energy+Valence plus +2 bonus for matching themes.
4. Return **3-5 songs** ranked by score. For each:
   - Song title + album + release year
   - Mood scorecard (E/V/Themes)
   - The anchor lyric (1 line, cited) + why it fits the user's mood
5. Offer: 「要不要帮你生成一个歌单名 + 收听顺序？」

### B. Scenario Discovery
Examples to handle:
- 「失恋听什么五月天？」
- 「加班崩溃时听哪首？」
- 「毕业季想哭，推荐一首？」
- 「考前打鸡血需要 5 首歌单」

Map the scenario to mood axes, then proceed as A.

### C. Activity-Based Playlist
- Input: ordered activity list (e.g. 「通勤 → 工作 → 午休 → 下班 → 夜跑」).
- Output: 5-track playlist whose Energy curve mirrors the activity arc.
- Explain transitions briefly ("从专注到爆发").

## Output Format (Recommendation)

```
🎵 为你挑的五月天
━━━━━━━━━━━━━━━━━
1. 《[song]》— [album] ([year])
   E:[n]/10  V:[n]/10  Themes: [...]
   锚句：「[lyric excerpt]」
   ✨ Why: [1-sentence fit explanation]
```

## References
- `references/mood-taxonomy.md` — Mood scoring rules and keyword mapping table.
- `references/lyrics-db/` — Source of song-level mood metadata.

## Edge Cases
- **Vague mood input** — Ask one follow-up before guessing.
- **Neutral / ambivalent mood** — Recommend mid-energy songs (E:5±1, V:5±1)
  and explicitly note the ambiguity.
- **User rejects a match** — Acknowledge subjectivity; offer manual filter by
  era (early Mayday / mid-period / mature) or album.
- **Missing metadata** — If a song lacks `mood` in the JSON, skip it rather
  than fabricate scores.
