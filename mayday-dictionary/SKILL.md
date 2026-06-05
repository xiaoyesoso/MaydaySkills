---
name: mayday-dictionary
description: >
  Look up Mayday (五月天) fan slang, band nicknames, song easter eggs,
  timeline events, memes, and era tags. Use when the user asks what a
  fan-culture term means, wants a daily vocabulary lesson, or wants to
  understand inside references like 升 key 战神, OAOA, 灯海蓝, T1213121,
  鸟巢, 信哥, etc. Supports lookup / daily / search / random modes.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: knowledge-qa
compatibility: No external dependencies. Python 3.12+ for lookup.py (stdlib only).
---

# Mayday Dictionary — 五迷黑话 / 术语 / 典故词典

## Overview
五迷文化的语义词典：可查可解释，也可"每日一词"科普。覆盖
演唱会术语、歌曲彩蛋、乐队昵称、时代事件、Meme、年代标签六大类。

## Capabilities

### 1. Lookup（精确/模糊查询）
- 输入「升 key 战神」→ 给出分类、释义、出处、相关词、例句

### 2. Daily（每日一词）
- 按日期哈希取一个稳定的随机词条
- 输出完整释义 + 例句 + 1 个真实使用场景

### 3. Search（模糊搜索）
- 输入关键字「升」→ 返回所有包含的词条（升 key、升 key 战神、…）

### 4. Random（随机推荐）
- 完全随机一词，作为冷知识 / 谈资

## Instruction Flow

### Flow A: Lookup
1. 接受 term 输入
2. 调 `scripts/lookup.py --term "升 key 战神"`
3. 解析 JSON：分类 / 释义 / 出处 / 相关 / 例句
4. 按 SKILL.md 的 Output Format 渲染

### Flow B: Daily
1. 调 `scripts/lookup.py --mode daily`
2. 输出完整词条 + 一句"今日用法"

### Flow C: Search
1. 调 `scripts/lookup.py --mode search --query "升"`
2. 返回所有匹配的 term 列表，让用户选

### Flow D: Random
1. 调 `scripts/lookup.py --mode random`
2. 直接给一词

## Output Format

### Lookup
```
📚 升 key 战神
━━━━━━━━━━━━━━━━━
分类：演唱会术语
释义：能在阿信副歌升 key 之后仍稳稳跟唱到底的五迷
出处：常用于《倔强》《突然好想你》后段副歌升 key 时
相关：升 key / 副歌升 / A→B
近义：高音 KO / 副歌之神
例句：「她副歌完没破音，是升 key 战神」

💡 今日用法：演唱会尾声段如果要《温柔》+《倔强》连唱，
   提前润嗓 + 备好水。
```

### Daily
```
📅 每日一词 · [日期]
━━━━━━━━━━━━━━━━━
🎲 今日词条：《拥抱》

📚 拥抱
分类：歌曲彩蛋
释义：1999 年同名曲，被五迷视为「失恋 / 告白的万能底色」
出处：首张创作专辑同名曲，1999
相关：温柔 / 突然好想你
例句：「那年的拥抱，是回不去的青春」

🎤 今日场景：K 歌结束时点一首，让全场人回到那年夏天
```

### Search
```
🔍 搜索「升」— 4 个结果
━━━━━━━━━━━━━━━━━
1. 升 key 战神
2. 升 key 段位
3. 副歌升 key
4. B 段升 key
```

## Edge Cases
- **用户输入半个词** → 自动 search 模式给候选
- **词条不存在** → 提示「未收录，要不要联网查」+ 引导用户贡献
- **多义词** → 列出不同义项，问用户哪一个
- **拼写差异**（"升key" vs "升 key"）→ 自动归一化匹配

## References
- `references/dictionary.json` — 核心词条库（~200 词）
- `references/knowledge-base/` — 交叉验证用（与其它 skill 共享）

## Companion Skills
- **SK3 mayday-trivia** — 出题 + dictionary 提供术语注释
- **SK5 chat-ashin** — 聊到术语时引用词典作信息源
- **SK6 concert-prep** — 演唱会备战时插入"今日值得知道的演唱会黑话"
- **SK11 mayday-fanfic** — 写作时遇到术语 → 调用 dictionary 确保用法准确
