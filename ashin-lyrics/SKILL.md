---
name: ashin-lyrics
description: >
  Generate original lyrics in the style of Ashin (阿信) from Mayday.
  Use when the user asks to write song lyrics like Mayday, generate
  Chinese lyrics with Ashin's signature voice, or create lyrics in
  the style of Taiwanese rock ballads. Supports tone switching between
  inspirational, melancholic, and passionate modes.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: creative-writing
compatibility: No external dependencies.
---

# Ashin Style Lyrics Generator

## Overview
Generate **original** Chinese lyrics that mimic Ashin's signature writing style —
story-driven, everyday-heroism themes, with concrete imagery carrying grand
emotions. Output is always new text; existing Mayday lyrics are never reproduced
verbatim.

## Ashin's Writing Patterns
1. **First-person plural** — Uses 「我们」 over 「我」 to create a shared experience.
2. **Micro-moments** — Small daily details (a cup, a street, a rain shower) anchor
   big feelings.
3. **Progressive intensity** — Verses build quietly; chorus erupts.
4. **Image repertoire** — Stars, oceans, light, roads, summer, youth, wind.
5. **Rhyme scheme** — ABAB or AABB in Mandarin, vowel-rich end rhymes (ang / ong / ai / ou).
6. **Structural framing** — Each verse should narrow the lens; the chorus zooms out.

## Instruction Flow
1. Ask the user three things in one prompt:
   - (a) topic / emotion / scenario
   - (b) tone preference: `inspirational` / `melancholic` / `passionate`
   - (c) length: single verse / verse + chorus / full song
2. Load relevant samples from `references/lyrics-db/` matching the chosen tone
   (see Tone Parameters below for the song shortlist).
3. Generate **3 distinct draft verses**, each annotated with:
   - Rhyme scheme used (e.g. `ABAB / ang-ai-ang-ai`)
   - Which Ashin pattern from §"Writing Patterns" it employs
4. Present the 3 drafts side-by-side; ask the user to pick one to expand
   into the requested length.
5. Output a final lyric sheet labeled by section (`[Verse 1]`, `[Pre-Chorus]`,
   `[Chorus]`, `[Bridge]`).

## Tone Parameters

| Tone | Themes | Reference songs (style only, not text) |
|------|--------|----------------------------------------|
| inspirational | 梦想 / 坚持 / 未来 | 倔强, 憨人, 出头天 |
| melancholic | 告别 / 遗憾 / 回忆 | 突然好想你, 后来的我们, 好好 |
| passionate | 青春 / 自由 / 反抗 | 恋爱ing, OAOA, 派对动物 |

## References
- `references/lyric-techniques.md` — Deep dive into Ashin's writing techniques.
- `references/lyrics-db/` — Album-organized lyric excerpts for style reference.

## Edge Cases
- **Vague input** — Ask clarifying questions before generating. Do not guess.
- **Off-brand drafts** — If a draft feels unlike Ashin, explain why (which
  pattern is missing) and offer a revision.
- **Copyright** — Never output existing Mayday lyrics. If the user asks for
  the lyrics of an existing song, direct them to authorized lyric platforms.
- **Other languages** — If the user requests English/Hokkien/Japanese lyrics,
  warn that the style is calibrated for Mandarin and offer best-effort output
  with a caveat.
