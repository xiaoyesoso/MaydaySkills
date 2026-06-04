---
name: mayday-trivia
description: >
  Answer trivia questions about Mayday's 26-year history. Use when the user
  asks about album facts, concert stories, member backgrounds, MV production
  details, or any behind-the-scenes Mayday lore. Also supports interactive
  quiz mode for fan challenges.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: knowledge-qa
compatibility: No external dependencies.
---

# Mayday Trivia Master

## Overview
A comprehensive Q&A engine covering Mayday's career from 1997 onward. Answers
factual questions about the band and optionally runs interactive quizzes.
Question bank ships with **700+ entries** (`references/trivia-db.json`),
generated from `references/lyrics-db/` (9 albums / 120 songs) and the curated
`knowledge-base/` files.

## Knowledge Domains
1. **Band members** — Birthdays, instruments, side projects, nicknames.
2. **Albums** — Release dates, tracklists, producers, recording locations.
3. **Concerts** — Tour names, venues, attendance, memorable incidents.
4. **MVs** — Directors, filming locations, cameo appearances, storylines.
5. **Awards** — Golden Melody Awards, HITO, other honors.
6. **Collaborations** — Featured artists, cross-band projects, charity work.

## Instruction Flow

### Direct Q&A
1. Parse the user's question and identify the knowledge domain.
2. Search `references/trivia-db.json` for a matching entry.
3. Respond concisely with the fact + source attribution (album/tour/date).
4. If not in the local database, fall back to web search and explicitly note
   the answer comes from an external source.

### Quiz Mode
- Trigger phrases: `quiz`, `挑战`, `考考我`, `出题`.
- Flow:
  1. Ask user for difficulty: `easy` / `medium` / `hard` / `nightmare`.
  2. Randomly select **10** questions from `trivia-db.json` at that difficulty.
  3. Present one question at a time; wait for the user's answer.
  4. Score each response; show the correct answer + background story.
  5. Final score with a Mayday-themed rating:
     - 10/10 → 第五位团员 (Fifth Member)
     - 7-9/10 → 资深五迷 (Veteran Fan)
     - 4-6/10 → 路人粉 (Casual Fan)
     - 0-3/10 → 还不快去听歌 (Go Listen Now!)

## References
- `references/trivia-db.json` — Question bank (id, domain, difficulty, Q, A, source).
- `references/knowledge-base/band-members.md`
- `references/knowledge-base/album-history.md`
- `references/knowledge-base/concert-archives.md`
- `references/knowledge-base/timeline.md`

## Edge Cases
- **Ambiguous question** — Ask one clarifying question (e.g., 「你说的是哪一次巡演？」).
- **Time-sensitive question** — If the answer may have changed after the
  database cutoff (see `timeline.md`), warn the user.
- **Rumors / unverified facts** — Decline to assert; cite that the info is
  unconfirmed.
- **Quiz answer fuzziness** — Accept reasonable variants (e.g. 「玛莎」 = 「蔡升晏」);
  if uncertain, ask the user whether their answer counts.
