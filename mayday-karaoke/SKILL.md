---
name: mayday-karaoke
description: >
  Teach users how to sing any Mayday song with difficulty scoring, vocal
  annotations, and N-day practice plans. Use when the user wants to
  practice singing a Mayday song, asks about vocal difficulty, needs
  karaoke coaching, or wants a practice roadmap for Mayday songs.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: vocal-coaching
compatibility: No external dependencies. Python 3.12+ for score-pitch.py (stdlib only).
---

# Mayday Karaoke · K 歌教练

## Overview
教用户怎么唱任意一首五月天：标出高音/转音/换气点，给难度评分，制定 N 天练唱计划。

## Instruction Flow

### Flow A: Vocal Guide（曲目指导）
1. 询问用户：想练哪首歌？
2. 运行 `scripts/score-pitch.py --song <曲名>`
3. 输出：
   - **难度评分**（0–10）+ 难度原因（最高音/升 key/BPM/持续演唱时长）
   - **分段标注**：🔴 高音 / 🟡 转音 / 💨 换气点 / 🎯 副歌升 key
   - **建议练习顺序**：先慢速哼唱 → 跟唱 → 全速

### Flow B: Song Recommendation（按音域推荐）
1. 询问用户音域（如 C3–G4）
2. 运行 `scripts/score-pitch.py --range C3:G4`
3. 输出 5–10 首可唱曲目，按难度升序排列

### Flow C: Practice Plan（N 天练习计划）
1. 询问用户：目标曲目 + 练习天数
2. 运行 `scripts/score-pitch.py --song <曲名> --plan <天数>`
3. 输出 day-by-day 计划（每天 30 分钟，分阶段拆解）

## Difficulty Score Formula
```
difficulty = 0.4 × normalize(highest_note)
           + 0.2 × normalize(bpm)
           + 0.2 × (has_key_change ? 1 : 0)
           + 0.2 × normalize(continuous_singing_seconds)
```
| 分数 | 标签 |
|------|------|
| 0–3 | 入门 |
| 4–6 | 进阶 |
| 7–8 | 困难 |
| 9–10 | 唯神能唱 |

## Output Format (Guide)
```
🎤 《倔强》K歌指南
━━━━━━━━━━━━━━━━━
难度：8/10 🔴 困难
原因：最高音 A4 / BPM 132 / 升 key ×1 / 副歌连续 15s

📋 分段标注
  Verse:  正常 → 正常 → 💨换气 → 🔴高音
  Chorus: 🎯升key → 🔴高音 → 💨换气 → 🔴高音

🎯 练习建议
  1. 先哼旋律 3 遍（不咬字）
  2. 跟唱 verse（慢速）
  3. 重点练副歌升 key 处
  4. 全速跟唱
```

## Edge Cases
- 用户不知道自己音域 → 用问题诱导：「你能舒服地唱到《温柔》"自由"那个"自"吗？」
- 曲目不在 lyrics-db → 提示从相似曲目类推
- 用户希望录音评分 → 明确告知 MVP 限制，推荐外接 KTV App
