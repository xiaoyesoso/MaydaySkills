---
name: mayday-quotes
description: >
  Generate Mayday-style Golden Quotes for social media, presentations, letters,
  or any life occasion. Use when the user needs a Mayday lyric to accompany a
  social post, wants to rewrite their text in Mayday style, asks to find a
  fitting Mayday quote for a specific life moment (resignation, graduation,
  confession, etc.), or needs lyrical inspiration for a message.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: copywriting
compatibility: No external dependencies.
---

# Mayday Golden Quote Generator

## Overview
The copywriting companion for fans — match any life moment to a Mayday lyric,
or rewrite arbitrary text in that unmistakable Mayday voice.

## Core Functions

### 1. Quote Match (`quote-matching`)
- **Input**: A life scenario described by the user (e.g. 「要辞职了，帮我想一句五月天」).
- Parse the scenario into keywords (resignation → freedom, new-beginning, courage).
- Search `references/quote-categories.md` and `references/lyrics-db/` for the
  best matches.
- **Output**: Top 3 matching lyrics, ranked by relevance, each with song +
  album attribution and a one-line "why it fits" note.

### 2. Style Rewrite (`style-transfer`)
- **Input**: User's original text (a 朋友圈 post, PPT title, letter).
- **Output**: Same message rewritten in Mayday lyric style.
- **Modes**: `热血版` / `温柔版` / `黑色幽默版` — let user pick or default to 温柔版.

### 3. Occasion Templates (`occasion-based`)
Pre-built categories covering 20+ life scenarios — see
`references/quote-categories.md` for the full list:

- **职场**：离职、入职、加班、团建、升职
- **感情**：告白、分手、纪念日、异地、和好
- **成长**：毕业、成年、迷茫、起航、生日
- **日常**：通勤、夜宵、失眠、下雨、独处

## Instruction Flow
1. Identify the user's intent — `quote-match`, `style-rewrite`, or `occasion`.
2. **For quote-match**:
   - Parse keywords → search quote-categories → score candidates → present top 3.
3. **For style-rewrite**:
   - Detect text structure (statement / question / list).
   - Apply Mayday patterns (short clauses, image anchors, end-rhyme attempts).
   - Output rewritten text + a one-paragraph note explaining what changed.
4. **For occasion**:
   - Look up the scenario in `quote-categories.md`.
   - Return the template's recommended lyrics + a customizable opener.

## Output Format (quote-match)

```
🎵 你的 [场景] 适合：
━━━━━━━━━━━━━━━━━
1. 「[lyric line]」
   ——《[song]》[album]
   ✨ Why this fits: [1-sentence explanation]

2. 「[lyric line]」
   ——《[song]》[album]
   ✨ Why this fits: [1-sentence explanation]

3. 「[lyric line]」
   ——《[song]》[album]
   ✨ Why this fits: [1-sentence explanation]
```

## References
- `references/quote-categories.md` — 20+ scenario → quote index.
- `references/lyrics-db/` — Source of lyric excerpts (citation-length only).

## Edge Cases
- **No matching scenario** — Offer style-rewrite as fallback.
- **Multiple scenarios in one request** — Ask which one is primary; do not
  return more than 3 quotes total to avoid noise.
- **Copyright** — Only cite excerpts already present in `lyrics-db`'s
  `lyrics_excerpt` field; never reproduce full lyrics.
- **Sensitive contexts** (e.g. 葬礼) — Decline gently, suggest the user choose
  a quote themselves with care.
