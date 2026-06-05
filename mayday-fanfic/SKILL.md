---
name: mayday-fanfic
description: >
  Generate constrained fan-fiction set in the Mayday universe — short
  stories based on song worlds, concert behind-the-scenes, or alternate
  universe scenarios. Use when the user wants a Mayday-themed short
  story, fan fiction, AU scenario, or creative writing inspired by
  Mayday songs and band history. All output follows content safety
  red lines and includes mandatory creation disclaimer.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: creative-writing
compatibility: No external dependencies.
---

# Mayday Fanfic · 五月天同人短篇

## Overview
在合规边界内，生成与五月天相关的同人短篇。可基于歌曲世界观、巡演幕后、角色 AU 等。

## Instruction Flow
1. 询问用户：**(a)** 故事前提 **(b)** 字数（300/800/1500/3000）** (c)** 人称（第一/第二/第三）
2. 从 lyrics-db 选锚句（若用户未指定 anchor_song，按 premise mood 自动匹配）
3. 查 persona/ 拿到角色性格特征（如有对话）
4. 套用 `references/fanfic-templates.md` 中的场景模板
5. **红线自检**（见下方）
6. 输出短篇小说 + 文末三段注解

## Content Safety Red Lines (MUST enforce)
- ❌ 不可包含 R18 / 暴力 / 涉政内容
- ❌ 不可丑化、抹黑、捏造侮辱性事件给真人
- ❌ 不可暗示真实恋爱关系（CP 文需明确标记 "纯虚构"）
- ❌ 不可使用任何完整歌词（只能引用 1 句锚句，且必须标注出处）
- ❌ 不可虚构成员公开发言或采访内容并伪造可信度

## Creation Disclaimer (MUST append to every output)
```
---
✨ 灵感来源：《[曲名]》—— [专辑]
🎵 文中嵌入歌词锚句：「...」（1 句以内，引用而非复制）
⚖️ 创作声明：本文为同人虚构，与艺人本人立场无关；非商业用途。
```

## Edge Cases
- 用户请求 R18 内容 → 拒绝并解释红线
- 用户请求 CP 文 → 生成但必须标 "纯虚构"
- 用户想续写 → 允许，但续写内容同样遵守红线
- 锚句超出 1 行 → 截断到 1 行

## Output Format
```
《[标题]》
[正文，约 N 字]

---
✨ 灵感来源：《[曲名]》—— [专辑]
🎵 锚句：「...」
⚖️ 创作声明：本文为同人虚构，与艺人本人立场无关；非商业用途。
```
