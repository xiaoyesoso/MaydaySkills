---
name: concert-prep
description: >
  Prepare Mayday fans for upcoming concerts — setlist previews, singalong
  practice, chant/flash-mob coordination, venue logistics, and packing
  checklists. Use when the user has concert tickets, asks about a tour's
  setlist, needs to prepare for a Mayday show, or wants to know about venue
  tips and fan traditions.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: event-planning
compatibility: Internet access recommended for real-time venue/weather data.
---

# Mayday Concert Battle Plan

## Overview
Turn anxious fans into concert-ready warriors. From setlist mastery to venue
survival tips, this skill covers everything a 五迷 needs before the big night.

## Capabilities

### 1. Setlist Intelligence
- **Input**: Tour name or concert date.
- **Output**: Predicted setlist based on recent shows on the same tour. Mark
  each track with one or more of:
  - 🎤 must-sing-along
  - ⚡ high-energy / jump moment
  - 🕯️ light-stick slow-wave
  - 🎸 guitar solo showcase
- **Rapid Review mode**: a 15-minute condensed audio checklist for
  last-minute preparation.

### 2. Fan Tradition Coach
- Teach official fan chants (e.g. 「五月天！五月天！」 four-beat loop).
- Encores: the 安可 rhythm — stomping, chanting, light-stick patterns
  organized by section.
- Tour-specific traditions: paper airplanes for 《后青春期的诗》, phone-light
  moments, color-coded sections.

### 3. Logistics Planner
- Venue info: capacity, seating map summary, best entry gates, restroom
  locations, food options.
- Transport: nearest MRT/subway stations, last-train times, parking guidance.
- Packing checklist: light stick (charged), portable charger, tissues, throat
  lozenges, ID, ticket screenshot backup.

### 4. Post-Concert Wrap
- Post-concert depression comfort kit: playlist suggestions, fan community
  links, tips for processing the experience.

## Instruction Flow
1. Ask user: (a) which concert/tour, (b) date, (c) venue/city.
2. Load relevant entries from `references/knowledge-base/concert-archives.md`.
3. If internet access is allowed, fetch the most recent setlist for that tour
   from a public source; otherwise use the predicted setlist baseline.
4. Generate a Battle Plan covering all 4 capabilities above.
5. Offer to export as a printable checklist using `assets/setlist-template.md`.

## Output Format

```
🎸 五月天 [Tour Name] — 备战手册
📍 [City] · [Venue] · [Date]

📋 预测 Setlist (基于最近 3 场)
1. [song] 🎤⚡
2. [song] 🕯️
...

📣 应援指南
- 安可节奏：[...]
- 灯海时刻：[...]
- 特殊传统：[...]

🚇 场馆攻略
- 交通：[...]
- 入场：[...]
- 散场：[...]

🎒 必带清单
[ ] 灯棒已充电
[ ] 行动电源
[ ] 喉糖
[ ] 卫生纸
[ ] 身分证 / 票面截图
```

## References
- `assets/setlist-template.md` — Printable battle plan template.
- `references/knowledge-base/concert-archives.md` — Historical concert data.

## Edge Cases
- **Unknown tour** — Ask for the official tour name; do not invent setlists.
- **Multi-city tour with rotating setlists** — Clearly mark items as
  "可能 / 高机率 / 必唱" based on recent-show frequency.
- **Weather-sensitive outdoor venue** — Recommend checking a real-time
  weather source; do not guess.
- **Safety** — Always include: arrive early, hydrate, know your nearest exit.
