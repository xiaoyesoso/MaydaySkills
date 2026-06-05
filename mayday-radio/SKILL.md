---
name: mayday-radio
description: >
  Compose a complete Mayday-themed radio program with DJ monologues,
  track transitions, and mood arcs. Use when the user wants a radio
  show, DJ program, late-night Mayday broadcast, or themed listening
  experience with narration between songs. Supports themes like breakup
  healing, commute motivation, late-night comfort, and concert countdown.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: immersive-companion
compatibility: No external dependencies. Python 3.12+ for build-program.py (stdlib only).
---

# Mayday Radio — AI 电台 DJ

## Overview
把任意时长拼成一档五月天主题广播节目：开场白 → 曲目 + DJ 串场 → 收尾。曲目选择复用 mayday-mood 的三轴匹配公式，DJ 串场按 dj-voice.md 风格生成。

## Instruction Flow

### Flow A: 主题电台
1. 询问用户：**(a)** 主题 / **(b)** 时长（30/60/90/120 分钟）
2. 从 `references/program-templates.json` 匹配最接近的模板，获取默认 mood arc + dj_style
3. 询问是否要排除某些歌（skip_songs）
4. 运行 `scripts/build-program.py --theme <theme> --duration <min> [--arc E1,V1,E2,V2,...] [--skip 歌A,歌B]`
5. 解析 JSON 输出，为每段生成 DJ 串场文本（按 `references/dj-voice.md` 指南）
6. 组装完整节目脚本并输出

### Flow B: 自定义情绪曲线
1. 用户直接描述想要的情绪旅程（如"先悲伤再治愈最后爆发"）
2. 将描述映射为 E/V 曲线
3. 同 Flow A 步骤 4–6

## DJ 串场生成规则
- 开场白（60–90 词）：点题 + 引入第一首歌 + 今晚的节目承诺
- 串场（20–40 词）：上一首的感受 + 过渡到下一首的意境
- 收尾（60–90 词）：回顾今晚旅程 + 留下念想 + 告别语
- 风格由 dj_style 参数控制（warm / philosophical / playful / nostalgic）
- 参考 `references/dj-voice.md` 的范例与避免清单

## Output Format
```
🎙️ [节目名] · [时长]
━━━━━━━━━━━━━━━━━

[00:00] 开场白
  DJ：（串场文本）

[01:30] 🎵 《[曲名]》— [专辑] (约X分Y秒)
  DJ 串场：（过渡文本）

...

[XX:XX] 🎵 《[最后一首]》
  DJ 收尾：（收束文本）

📝 节目总览
  - 曲目数：N
  - 总时长：约 X 分钟
  - 情绪弧度：[描述]
```

## Edge Cases
- 时长 > 120 分钟 → 拆成 2 档节目
- skip_songs 导致候选不足 → 提示"曲池太小，建议放宽限制"
- 无匹配模板 → 用通用模板（mid-energy, balanced valence）
- 用户指定不存在的主题 → 追问澄清
