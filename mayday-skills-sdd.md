# 五月天 Agent Skills — SDD（Spec-Driven Development）

> 基于 [agentskills.io](https://agentskills.io/specification) 规范 v1.0  
> 作者：WorkBuddy × 五月天歌迷  
> 创建日期：2026-06-04  
> 版本：v1.0-draft

---

## 目录

1. [项目概述](#1-项目概述)
2. [技术规范引用](#2-技术规范引用)
3. [全体 Skill 架构](#3-全体-skill-架构)
4. [Skill 详细规格](#4-skill-详细规格)
   - [SK1 · 阿信风格歌词生成](#sk1--阿信风格歌词生成)
   - [SK2 · 五月天和弦秘籍](#sk2--五月天和弦秘籍)
   - [SK3 · 五月天 Trivia Master](#sk3--五月天-trivia-master)
   - [SK4 · 歌词情绪数据库](#sk4--歌词情绪数据库)
   - [SK5 · 和阿信聊聊](#sk5--和阿信聊聊)
   - [SK6 · 演唱会备战助手](#sk6--演唱会备战助手)
   - [SK7 · 五月天金句生成器](#sk7--五月天金句生成器)
   - [SK8 · Mayday 音乐数据面板](#sk8--mayday-音乐数据面板)
5. [研发 Roadmap](#5-研发-roadmap)
6. [公共能力模块](#6-公共能力模块)
7. [质量与验证标准](#7-质量与验证标准)

---

## 1. 项目概述

### 1.1 愿景

构建一套围绕**五月天乐队**的 Agent Skills 生态——让 AI 助手成为最懂五月天的「第六位成员」。每个 Skill 独立可安装、可组合、可跨平台复用。

### 1.2 技能矩阵

| ID | Skill 名称 | 分类 | 依赖 | 复杂度 | 优先级 |
|----|-----------|------|------|--------|--------|
| SK1 | ashin-lyrics | 创作陪伴 | 公共歌词库 | 中 | P0 |
| SK2 | mayday-chords | 创作陪伴 | 公共歌曲库 | 高 | P2 |
| SK3 | mayday-trivia | 知识问答 | 公共知识库 | 低 | P1 |
| SK4 | mayday-mood | 知识问答 | 公共歌词库 | 中 | P0 |
| SK5 | chat-ashin | 互动陪伴 | 公共知识库 + persona | 高 | P1 |
| SK6 | concert-prep | 互动陪伴 | 公共歌曲库 | 中 | P1 |
| SK7 | mayday-quotes | 实用工具 | 公共歌词库 | 低 | P0 |
| SK8 | mayday-data | 实用工具 | 外部 API 接入 | 高 | P2 |

---

## 2. 技术规范引用

本文档所有 Skill 均遵循 [agentskills.io Specification v1.0](https://agentskills.io/specification)：

- `SKILL.md` 使用 **YAML frontmatter + Markdown Body** 结构
- `name`：1-64 字符，小写字母+数字+连字符，与目录名一致
- `description`：1-1024 字符，包含激活关键词
- Body 正文 ≤ 5000 tokens，详细内容拆分至 `references/`
- 渐进式加载：元数据(~100 tokens) → 指令(<5000 tokens) → 按需加载资源

---

## 3. 全体 Skill 架构

```
mayday-skills/                          # 仓库根目录
├── shared/                             # 公共模块（非 Skill，供各 Skill 引用）
│   ├── lyrics-db/                      #   歌词数据库（结构化 JSON）
│   │   ├── albums/                     #     按专辑分文件
│   │   └── schema.json                 #     数据格式定义
│   ├── knowledge-base/                 #   知识库
│   │   ├── band-members.md             #     成员资料
│   │   ├── album-history.md            #     专辑历史
│   │   ├── concert-archives.md         #     演唱会档案
│   │   └── timeline.md                 #     大事年表
│   └── persona/                        #   角色扮演资源
│       └── ashin-persona.md            #     阿信人设指南
│
├── ashin-lyrics/                       # SK1
│   ├── SKILL.md
│   └── references/
│       └── lyric-techniques.md
│
├── mayday-chords/                      # SK2
│   ├── SKILL.md
│   ├── references/
│   │   └── chord-patterns.md
│   └── scripts/
│       └── chord-diagram.py
│
├── mayday-trivia/                      # SK3
│   ├── SKILL.md
│   └── references/
│       └── trivia-db.json
│
├── mayday-mood/                        # SK4
│   ├── SKILL.md
│   └── references/
│       └── mood-taxonomy.md
│
├── chat-ashin/                         # SK5
│   ├── SKILL.md
│   └── references/
│       ├── ashin-voice.md
│       └── conversation-examples.md
│
├── concert-prep/                       # SK6
│   ├── SKILL.md
│   └── assets/
│       └── setlist-template.md
│
├── mayday-quotes/                      # SK7
│   ├── SKILL.md
│   └── references/
│       └── quote-categories.md
│
└── mayday-data/                        # SK8
    ├── SKILL.md
    └── scripts/
        └── data-fetcher.py
```

---

## 4. Skill 详细规格

---

### SK1 · 阿信风格歌词生成

#### SKILL.md

```yaml
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
compatibility: Requires access to shared/lyrics-db/ for reference material.
---
```

#### Body 大纲

```markdown
# Ashin Style Lyrics Generator

## Overview
Generate original Chinese lyrics mimicking Ashin's signature writing style —
story-driven, everyday-heroism themes, concrete imagery carrying grand emotions.

## Ashin's Writing Patterns
1. **First-person plural**: Uses "我们" over "我" to create shared experience.
2. **Micro-moments**: Small daily details (a cup, a street, a rain) anchoring
   big feelings.
3. **Progressive intensity**: Verses build quietly, chorus erupts.
4. **Image repertoire**: Stars, oceans, light, roads, summer, youth, wind.
5. **Rhyme scheme**: ABAB or AABB in Mandarin, vowel-rich end rhymes.

## Instruction Flow
1. Ask the user: (a) topic/emotion, (b) tone preference
   (inspirational/melancholic/passionate), (c) length (verse × N or full song).
2. Load relevant samples from `../shared/lyrics-db/` matching the chosen tone.
3. Generate 3 draft verses, each annotated with:
   - Rhyme scheme used
   - Which Ashin pattern it employs
4. Present options; let the user pick one to expand into a full lyric.
5. Output a final lyric sheet with verse/chorus labels.

## Tone Parameters
- inspirational: 梦想/坚持/未来 — ref: 倔强, 憨人, 出头天
- melancholic: 告别/遗憾/回忆 — ref: 突然好想你, 后来的我们, 好好
- passionate: 青春/自由/反抗 — ref: 恋爱ing, OAOA, 派对动物

## Edge Cases
- If user input is too vague, ask clarifying questions before generating.
- If the result feels "off-brand," explain why and offer a revision.
- Never output pre-existing Mayday lyrics verbatim; always generate original.
```

#### 依赖资源

| 文件 | 类型 | 说明 |
|------|------|------|
| `../shared/lyrics-db/` | 参考 | 按专辑组织的五月天全量歌词 |
| `references/lyric-techniques.md` | 参考 | 阿信写作技法深度分析 |

---

### SK2 · 五月天和弦秘籍

#### SKILL.md

```yaml
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
compatibility: Requires git. Python 3.12+ for chord-diagram.py script.
---
```

#### Body 大纲

```markdown
# Mayday Chord Secrets

## Overview
Deconstruct Monster's (怪兽) arranging philosophy — the chord patterns,
structural builds, and emotional stacking techniques that define Mayday's sound.

## Core Capabilities
1. **Chord lookup**: Given a song name, output full chord chart (verse/chorus/
   bridge) in both standard notation and Roman numeral analysis.
2. **Pattern mining**: Identify recurring chord progression templates across
   albums (e.g., I-V-vi-IV with variants).
3. **Key change analysis**: Explain how Mayday uses key changes in climactic
   moments (e.g., 倔强副歌升key逻辑, 你不是真正的快乐半音上行).
4. **Learning roadmap**: Recommend a practice sequence — which songs to learn
   first for different skill levels.

## Instruction Flow
1. Ask user: song name or learning goal.
2. If song name given:
   - Load or infer the key using references/chord-patterns.md.
   - Run scripts/chord-diagram.py to generate visual chord diagrams.
   - Output: roman numeral analysis + standard chord chart + text explanation.
3. If learning goal given:
   - Match to closest songs in the pattern database.
   - Output a 3-step practice plan ordered by difficulty.

## References
- Load `references/chord-patterns.md` for detailed chord pattern database.
- Run `scripts/chord-diagram.py <song-key>` for visual chord output.

## Output Format
```
Song: 倔强
Key: A Major
Verse: [A - E - F#m - D] × 2  (I-V-vi-IV)
Pre-Chorus: [Bm7 - E7 - A - F#m] ...
[text explanation of why this works emotionally]
```
```

#### 依赖资源

| 文件 | 类型 | 说明 |
|------|------|------|
| `references/chord-patterns.md` | 参考 | 五月天高频和弦模式数据库 |
| `scripts/chord-diagram.py` | 脚本 | 输出 ASCII/Unicode 和弦图 |

---

### SK3 · 五月天 Trivia Master

#### SKILL.md

```yaml
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
---
```

#### Body 大纲

```markdown
# Mayday Trivia Master

## Overview
A comprehensive Q&A engine covering Mayday's complete career from 1999-2025.
Answer factual questions about the band and optionally run interactive quizzes.

## Knowledge Domains
1. **Band members**: Birthdays, instruments, side projects, nicknames.
2. **Albums**: Release dates, tracklists, producers, recording locations, easter eggs.
3. **Concerts**: Tour names, venues, attendance, memorable incidents per show.
4. **MVs**: Directors, filming locations, cameo appearances, storylines.
5. **Awards**: Golden Melody Awards, HITO, other honors.
6. **Collaborations**: Featured artists, cross-band projects, charity work.

## Instruction Flow

### Direct Q&A
1. Parse the user's question and identify the knowledge domain.
2. Search `references/trivia-db.json` for the answer.
3. Respond concisely with the fact, plus source attribution (album/tour/date).
4. If the answer is not in the database, search the web and explain the source
   is external.

### Quiz Mode (trigger: "quiz", "挑战", "考考我")
1. Ask user for difficulty: easy/medium/hard/nightmare.
2. Randomly select 10 questions from trivia-db.json at stated difficulty.
3. Present one question at a time, wait for user answer.
4. Score each response; show correct answer with background story.
5. Final score with a Mayday-themed rating scale:
   - 10/10: 第五位团员 (Fifth Member)
   - 7-9/10: 资深五迷 (Veteran Fan)
   - 4-6/10: 路人粉 (Casual Fan)
   - 0-3/10: 还不快去听歌 (Go Listen Now!)

## Edge Cases
- Ambiguous questions: ask for disambiguation (e.g., "Which album tour?")
- Time-sensitive questions: note the data cutoff date if a recent event may
  not be covered.
```

#### 依赖资源

| 文件 | 类型 | 说明 |
|------|------|------|
| `references/trivia-db.json` | 参考 | 结构化问答题库（含难度、领域标签） |
| `../shared/knowledge-base/` | 共享 | 乐队成员、专辑历史、演唱会档案 |

---

### SK4 · 歌词情绪数据库

#### SKILL.md

```yaml
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
compatibility: Requires access to shared/lyrics-db/ for lyrics indexing.
---
```

#### Body 大纲

```markdown
# Mayday Mood Matcher

## Overview
A mood-to-song recommendation engine that labels every Mayday song across
multiple emotional dimensions and finds the best match for any user-described
state.

## Mood Taxonomy (3-Axis)
- **Energy**: low → high (calm to explosive)
- **Valence**: sad → happy (melancholy to joyful)
- **Theme**: love / friendship / dream-chasing / loss / nostalgia / rebellion
  / growth / celebration

## Instruction Flow

### Mood-Based Playlist
1. Ask user: "How are you feeling right now?" (free-text response).
2. Parse the response to extract mood descriptors, map them to the 3-axis
   taxonomy.
3. Query the mood dataset for top matches (min 3, max 5 songs).
4. For each song, output:
   - Song name + album
   - Mood score breakdown (Energy / Valence / Theme)
   - The single most fitting lyrics line (with emotional annotation)
5. Offer: "Want me to generate a playlist name + listening order?"

### Emotion-Driven Discovery
- Support queries like: "什么歌适合失恋听" / "加班到崩溃时该听哪首" /
  "毕业季最应景的五月天"
- Map natural language to mood axes, proceed as above.

### Playlist Generator
- Input: list of moods/activities (e.g., "通勤→工作→午休→下班→夜跑")
- Output: 5-part playlist with transition logic explained.

## Data Format (per song in mood-db)
```json
{
  "song": "倔强",
  "album": "神的孩子都在跳舞",
  "energy": 8,
  "valence": 7,
  "themes": ["dream-chasing", "rebellion"],
  "anchor_lyric": "当我和世界不一样，那就让我不一样",
  "anchor_emotion": "被世界误解时的自我确认"
}
```

## Edge Cases
- Vague user input: probe with follow-up questions rather than guessing.
- Neutral/ambivalent mood: suggest "mid-energy" songs, explicitly note the
  ambiguity.
- User disagrees with a match: acknowledge subjectivity, offer manual search
  by album/era as fallback.
```

#### 依赖资源

| 文件 | 类型 | 说明 |
|------|------|------|
| `references/mood-taxonomy.md` | 参考 | 情绪分类体系及标注方法论 |
| `../shared/lyrics-db/` | 共享 | 全量歌词（作为情绪锚点来源） |

---

### SK5 · 和阿信聊聊

#### SKILL.md

```yaml
---
name: chat-ashin
description: >
  Roleplay as Ashin (阿信) from Mayday — respond with his worldview, humor,
  and lyrical wisdom. Use when the user wants life advice "from Ashin," asks
  "what would Ashin say about this," needs a motivational boost in Ashin's
  voice, or wants to have a casual chat in Mayday's rock-philosophy style.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: roleplay
compatibility: Requires access to ../shared/persona/ashin-persona.md and
  ../shared/knowledge-base/ for accurate characterization.
---
```

#### Body 大纲

```markdown
# Chat with Ashin

## Overview
Adopt Ashin's persona — his speaking patterns, life philosophy, and signature
blend of warmth, dry humor, and emotional honesty. Respond to user messages as
if Ashin were giving advice, telling stories, or just hanging out.

## Persona Profile

### Voice Characteristics
- **Warm but not cheesy**: Genuine care, never saccharine.
- **Humorous deflection**: When things get too heavy, crack a self-deprecating
  joke or switch perspective humorously.
- **Philosophical layering**: Wrap simple truths in poetic metaphors — but
  always land them with an everyday example.
- **Code-switching**: Blend Mandarin with occasional Taiwanese Hokkien phrases
  (自然, 没差, 很赞, 歹势) and casual English interjections.

### Core Beliefs (reflected in responses)
1. 平凡人的故事就是最伟大的故事
2. 倔强不是不认输，而是知道自己为什么站起来
3. 人生不是结果，是一段过程
4. 五月天可以当背景音乐，但你的故事要自己唱

### Emotional Range
- Encouragement: 励志 but never preachy — "你自己选的路，跪着也要走完，但记得偶尔站起来看看风景"
- Comfort: Acknowledges pain before offering hope — "现在很难过对吧？那就难过一下，没关系的"
- Humor: Playful, often self-targeting — on looks, on getting old, on being
  "the least cool rock star"

## Instruction Flow
1. Load `references/ashin-voice.md` and `../shared/persona/ashin-persona.md`
   for full characterization.
2. Load `../shared/knowledge-base/` for factual accuracy when referencing
   band history.
3. Read `references/conversation-examples.md` to calibrate tone.
4. For each user message:
   a. Parse emotional intent — is the user seeking advice, comfort, or casual
      chat?
   b. If advice-seeking: respond with philosophy + practical angle, end with a
      relevant Mayday lyric (cited).
   c. If comfort-seeking: validate first, then offer perspective, close with
      warmth.
   d. If casual: keep it light, throw in a band-related anecdote if natural.
   e. If requested, cite which Mayday song lyric inspired the response.

## Constraints
- Never claim Ashin actually said something he didn't. Use phrasing:
  "如果是阿信，他可能会说……" for original content.
- Avoid sensitive topics: politics, interpersonal band rumors, financial
  matters.
- Stay in Mandarin; use Hokkien sparingly for flavor.
- Never roleplay as other band members unless explicitly asked.
```

#### 依赖资源

| 文件 | 类型 | 说明 |
|------|------|------|
| `references/ashin-voice.md` | 参考 | 阿信语言模式深度拆解 |
| `references/conversation-examples.md` | 参考 | 对话风格范例集 |
| `../shared/persona/ashin-persona.md` | 共享 | 阿信人设完整指南 |
| `../shared/knowledge-base/` | 共享 | 乐队知识库（确保引用准确） |

---

### SK6 · 演唱会备战助手

#### SKILL.md

```yaml
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
```

#### Body 大纲

```markdown
# Mayday Concert Battle Plan

## Overview
Turn anxious fans into concert-ready warriors. From setlist mastery to venue
survival tips, this skill covers everything a "五迷" needs before the big night.

## Capabilities

### 1. Setlist Intelligence
- Input: Tour name or concert date.
- Output: Predicted setlist based on recent shows on the same tour.
  Mark songs with: 🎤 must-sing-along, ⚡ high-energy/jump moment, 🕯️
  light-stick slow-wave moment, 🎸 guitar solo showcase.
- "Rapid Review" mode: 15-minute condensed audio checklist for last-minute prep.

### 2. Fan Tradition Coach
- Teach official fan chants (e.g., "五月天！五月天！")
- Encores: explain the "安可" rhythm — stomping, chanting, light-stick patterns
  organized by section.
- Special traditions per tour (e.g., specific colored light sticks, paper
  airplane moments, specific songs where phones come out).

### 3. Logistics Planner
- Venue info: capacity, seating map description, best entry gates, restroom
  locations, food options.
- Transport: nearest MRT/subway stations, last-train times, parking guidance.
- Packing checklist: light stick (charged), portable charger, tissues,
  throat lozenges, ID, ticket screenshot backup.

### 4. Post-Concert Wrap
- "Post-concert depression" comfort kit: playlist suggestions, fan community
  links, tips for processing the experience.

## Instruction Flow
1. Ask user: (a) which concert/tour, (b) date, (c) venue city.
2. Load relevant dataset from shared knowledge base.
3. Generate a "Battle Plan" covering all 4 capabilities above.
4. Offer to export as a printable checklist using `assets/setlist-template.md`.

## Output Format
```
🎸 五月天 [Tour Name] — 备战手册
📍 [City] · [Venue] · [Date]

📋 预测 Setlist (基于最近 3 场)
[numbered list with emoji markers]

📣 应援指南
[chants, encores, traditions]

🚇 场馆攻略
[transport, entry, survival tips]

🎒 必带清单
[√ checkboxes]
```
```

#### 依赖资源

| 文件 | 类型 | 说明 |
|------|------|------|
| `assets/setlist-template.md` | 资源 | 可打印的 Setlist 模板 |
| `../shared/knowledge-base/concert-archives.md` | 共享 | 历史演唱会数据 |

---

### SK7 · 五月天金句生成器

#### SKILL.md

```yaml
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
---
```

#### Body 大纲

```markdown
# Mayday Golden Quote Generator

## Overview
The ultimate copywriting companion for fans — match any life moment to a
Mayday lyric, or generate new text in that unmistakable Mayday voice.

## Core Functions

### 1. Quote Match (quote-matching)
- Input: A life scenario described by the user (e.g., "我要辞职了, 帮我想一句五月天").
- Parse the scenario into keywords (resignation → freedom, new-beginning, courage).
- Search `references/quote-categories.md` and lyrics database for best matches.
- Output: Top 3 matching lyrics with song name + album, ranked by relevance.
- Format each quote in a shareable card layout (quote + attribution).

### 2. Style Rewrite (style-transfer)
- Input: User's original text (e.g., a 朋友圈 post, PPT title, letter).
- Output: The same message rewritten in Mayday lyric style.
- Modes: "热血版" / "温柔版" / "黑色幽默版".

### 3. Occasion Templates (occasion-based)
Pre-built categories covering 20+ life scenarios:
- 职场: 离职 / 入职 / 加班 / 团建
- 感情: 告白 / 分手 / 纪念日 / 异地
- 成长: 毕业 / 成年 / 迷茫 / 起航
- 日常: 通勤 / 夜宵 / 失眠 / 下雨

## Instruction Flow
1. Identify the user's intent: quote-match, style-rewrite, or occasion.
2. For quote-match: parse keywords → search database → rank → present top 3.
3. For style-rewrite: analyze original text structure → apply Mayday patterns
   (see `../shared/lyrics-db/` for pattern reference) → output rewritten version
   with explanation of changes.
4. For occasion: directly match to pre-built template, allow user to customize.

## Output Format (quote-match)
```
🎵 你的 [场景] 适合：
━━━━━━━━━━━━━━━━
1. "[lyric line]"
   ——《[song]》[album]
   ✨ Why this fits: [1-sentence explanation]

2. "[lyric line]"
   ——《[song]》[album]
   ✨ Why this fits: [1-sentence explanation]
```
```

#### 依赖资源

| 文件 | 类型 | 说明 |
|------|------|------|
| `references/quote-categories.md` | 参考 | 按场景分类的金句索引 |
| `../shared/lyrics-db/` | 共享 | 全量歌词库 |

---

### SK8 · Mayday 音乐数据面板

#### SKILL.md

```yaml
---
name: mayday-data
description: >
  Visualize Mayday's music data — album sales, streaming trends, concert
  attendance, and search popularity across platforms. Use when the user asks
  for data about Mayday's popularity, wants to see trends in their music,
  requests charts or statistics about the band, or asks for comparative
  analysis of albums, tours, or eras.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: data-visualization
compatibility: Requires Python 3.12+, internet access, matplotlib, requests.
---
```

#### Body 大纲

```markdown
# Mayday Music Data Dashboard

## Overview
Collect, process, and visualize quantitative data about Mayday's career —
turning 26 years of music into readable charts and insights.

## Data Sources
1. Streaming platforms: Spotify, KKBOX, QQ Music (search APIs).
2. YouTube: MV view counts, trends.
3. Wikipedia / fan wikis: Album sales, concert attendance records.
4. Public archives: Golden Melody Awards data.

## Capabilities

### 1. Album Performance Timeline
- Input: Metric choice (streaming / sales / awards).
- Output: Line/bar chart showing albums chronologically, annotated with
  significant events (member military service, comeback, genre shifts).

### 2. Concert Heatmap
- Input: None (full history) or specific tour.
- Output: World map or city grid showing concert frequency × attendance
  estimates by location.

### 3. Song Popularity Trends
- Input: Song name(s).
- Output: Time-series chart of search interest / streaming count over years.
  Compare multiple songs on one chart.

### 4. Era Comparison
- Input: Two time periods (e.g., 2004-2008 vs 2016-2020).
- Output: Side-by-side metrics — avg album sales, tour frequency, award count,
  lyrical theme distribution.

## Instruction Flow
1. Ask user: what data view they want (from 4 capabilities above).
2. Run `scripts/data-fetcher.py <query-type> <parameters>` to collect data.
3. Parse the script output (JSON format).
4. Render the chart/visualization in the response.
5. Provide a plain-text summary interpretation of the data.

## Script Usage
See `scripts/data-fetcher.py` — a modular Python CLI:
```bash
python scripts/data-fetcher.py album-trend    # returns JSON of album metrics
python scripts/data-fetcher.py concert-map     # returns JSON of concert geo-data
python scripts/data-fetcher.py song-trend <song-ids>  # returns time-series JSON
python scripts/data-fetcher.py era-compare <start1> <end1> <start2> <end2>
```

## Edge Cases
- API rate limits: cache results in a temp file; warn user of stale data.
- Missing data: clearly mark in charts; never fabricate numbers.
- Data conflicts: if multiple sources disagree, show range and cite sources.
```

#### 依赖资源

| 文件 | 类型 | 说明 |
|------|------|------|
| `scripts/data-fetcher.py` | 脚本 | 多源数据采集 CLI |

---

## 5. 研发 Roadmap

### Phase 0 — 基础设施（共享模块）

| # | 任务 | 产出 | 工时 | 阻塞 |
|---|------|------|------|------|
| P0-1 | 构建 `shared/lyrics-db/` 歌词数据库 | JSON 结构化歌词（按专辑） | 中 | 无 |
| P0-2 | 构建 `shared/knowledge-base/` 知识库 | 成员/专辑/演唱会/年表 Markdown | 中 | 无 |
| P0-3 | 构建 `shared/persona/ashin-persona.md` | 阿信人设文档 | 低 | P0-2 |

### Phase 1 — P0 技能（先发体验）

| # | Skill | 关键交付 | 依赖 | 工时 |
|---|-------|---------|------|------|
| SK1 | ashin-lyrics | SKILL.md + lyric-techniques.md + 3-style prompt template | P0-1 | 低 |
| SK4 | mayday-mood | SKILL.md + mood-taxonomy.md + 全量歌词情绪标注 | P0-1 | 高 |
| SK7 | mayday-quotes | SKILL.md + quote-categories.md + 20-scenario templates | P0-1 | 中 |

### Phase 2 — P1 技能（核心扩展）

| # | Skill | 关键交付 | 依赖 | 工时 |
|---|-------|---------|------|------|
| SK3 | mayday-trivia | SKILL.md + trivia-db.json (500+ Q&A) | P0-2 | 高 |
| SK5 | chat-ashin | SKILL.md + ashin-voice.md + conversation-examples.md | P0-2, P0-3 | 高 |
| SK6 | concert-prep | SKILL.md + setlist-template.md + tour data updated | P0-2 | 中 |

### Phase 3 — P2 技能（深度能力）

| # | Skill | 关键交付 | 依赖 | 工时 |
|---|-------|---------|------|------|
| SK2 | mayday-chords | SKILL.md + chord-patterns.md + chord-diagram.py | 外部和弦数据 | 高 |
| SK8 | mayday-data | SKILL.md + data-fetcher.py + API 对接 | 外部 API | 高 |

---

## 6. 公共能力模块

### 6.1 `shared/lyrics-db/` — 歌词数据库

```
shared/lyrics-db/
├── schema.json               # 数据格式定义
├── 1999-第一张创作专辑.json
├── 2000-爱情万岁.json
├── 2001-人生海海.json
├── 2003-时光机.json
├── 2004-神的孩子都在跳舞.json
├── 2006-为爱而生.json
├── 2008-后青春期的诗.json
├── 2011-第二人生.json
├── 2016-自传.json
└── singles.json              # 单曲 + EP
```

**`schema.json` 结构：**

```json
{
  "album": "神的孩子都在跳舞",
  "year": 2004,
  "songs": [
    {
      "title": "倔强",
      "lyricist": "阿信",
      "composer": "阿信",
      "lyrics": "当我和世界不一样 那就让我不一样\n...",
      "segments": [
        {"type": "verse", "text": "..."},
        {"type": "chorus", "text": "..."},
        {"type": "bridge", "text": "..."}
      ]
    }
  ]
}
```

### 6.2 `shared/knowledge-base/` — 知识库

| 文件 | 内容 | 行数 |
|------|------|------|
| `band-members.md` | 五人资料（生日/乐器/外号/副业/趣闻） | ~200 |
| `album-history.md` | 九张专辑的创作背景、录制故事、市场反响 | ~500 |
| `concert-archives.md` | 历次巡演数据（城市/场次/规模/名场面） | ~400 |
| `timeline.md` | 1997-至今大事年表 | ~300 |

### 6.3 `shared/persona/` — 角色资源

```
shared/persona/
└── ashin-persona.md          # 阿信人设完整指南
    ├── 语言习惯
    ├── 价值观体系
    ├── 幽默风格
    ├── 禁忌话题
    └── 典型回应示例
```

---

## 7. 质量与验证标准

### 7.1 规范合规检查

每个 Skill 发布前必须通过：

```bash
skills-ref validate ./skill-name/
```

检查项：
- `name` 与目录名一致
- `name` 仅含小写字母+数字+连字符
- `description` 非空且 ≤1024 字符
- `compatibility`（若有）≤500 字符
- `metadata`（若有）为 `map<string,string>`

### 7.2 内容质量检查

| 维度 | 标准 | 验证方法 |
|------|------|----------|
| 指令完整性 | Body 包含明确的 step-by-step 指令 | 人工审查 |
| 关键词覆盖 | description 覆盖该 Skill 的所有典型触发词 | 触发词矩阵测试 |
| Token 预算 | Body ≤ 5000 tokens | 字数统计 |
| 跨平台兼容 | 无平台特定假设（除非 compatibility 声明） | 在 2+ 平台测试 |
| 引用有效性 | 所有 `references/` `scripts/` `assets/` 路径可解析 | 文件存在性校验 |

### 7.3 音乐版权声明

> 所有 Skill 不直接分发五月天受版权保护的歌词全文。歌词仅以「引用」形式出现，且注明出处。完整歌词数据仅供 Skill 内部检索使用，不对外暴露下载能力。

---

## 附录 A · 触发词矩阵

| Skill | 中文触发词 | 英文触发词 |
|-------|-----------|-----------|
| SK1 ashin-lyrics | 写歌词、模仿阿信、五月天风格写词 | write mayday lyrics, ashin style lyrics |
| SK2 mayday-chords | 和弦、吉他谱、怪兽编曲、升key | mayday chords, guitar, key change |
| SK3 mayday-trivia | 冷知识、问答、考考我、阿信生日 | mayday trivia, quiz, facts |
| SK4 mayday-mood | 心情、适合、歌单、推荐、失恋听什么 | mood, playlist, recommend, feeling |
| SK5 chat-ashin | 阿信说、如果阿信、和阿信聊天 | chat ashin, what would ashin say |
| SK6 concert-prep | 演唱会、备战、歌单、安可、场馆 | concert, setlist, encore, venue |
| SK7 mayday-quotes | 金句、朋友圈、文案、辞职信 | quote, social post, copywriting |
| SK8 mayday-data | 数据、趋势、销量、统计 | data, trends, statistics, charts |

---

## 附录 B · 变更记录

| 日期 | 版本 | 变更 |
|------|------|------|
| 2026-06-04 | v1.0-draft | 初稿，全部 8 个 Skill 的 SDD 规格 |

---

> *「这一生只愿只要平凡快乐 谁说这样不伟大呢」*  
> ——五月天《笑忘歌》
