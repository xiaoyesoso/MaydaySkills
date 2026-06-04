# 20 · 研发 Roadmap

> 隶属：[Mayday Skills SDD](./README.md)
> 版本：v1.1

## Phase 概览

| 阶段 | 内容 | 状态 |
|------|------|------|
| Phase 0 | 公共资源初始化（schema、知识底稿、人设文档） | ✅ |
| Phase 1 | P0 三技能：ashin-lyrics / mayday-mood / mayday-quotes | ✅ |
| Phase 2 | P1 三技能：mayday-trivia / chat-ashin / concert-prep | ✅ |
| Phase 3 | P2 两技能：mayday-chords / mayday-data | ✅ |
| Phase 4 | 数据扩充（9 专辑 120 首 / 762 题 / Spotify+YouTube API） | ✅ |
| Phase 5 | SDD 文档重构 + 新 Skill 规划 | ✅（本文档）|
| **Phase 6** | **SK9 mayday-radio（AI 电台）研发实施** | ⏳ 待补 |
| **Phase 7** | **SK10 mayday-karaoke + SK11 mayday-fanfic 研发实施** | ⏳ 待补 |
| **Phase 8** | **SK12 setlist-craft + SK13 mayday-dictionary 研发实施** | ⏳ 待补 |
| **Phase 9** | **工作流编排（跨 Skill Pipeline）+ 发布平台搭建** | ⏳ 待补 |

## Phase 0–4 回顾

已全部完成。详见 [`archive/v1.0.md`](./archive/v1.0.md) §5。

## Phase 6 — SK9 mayday-radio（AI 电台）

### 动机

孤独听歌的场景天然存在（通勤、加班、失眠）。现有 SK4 只推荐歌单，不提供「听得下去的广播节目」。radio 能把推荐+念白+音乐知识串联成一档完整节目。

### 关键交付

| # | 任务 | 依赖 |
|---|------|------|
| R-1 | SKILL.md + README.md | — |
| R-2 | `scripts/build-program.py`：根据时长/主题/情绪自动编排节目结构 | lyrics-db, mood-taxonomy |
| R-3 | 主持人语调定义为嵌入式 prompt（非 TTS，纯文本朗读词） | SK5 人设素材 |
| R-4 | 节目模板：失恋电台 / 通勤BGM / 深夜疗愈 / 演唱会倒计时 | — |
| R-5 | 情绪弧度自动检测（从悲伤到治愈的音乐编排） | lyrics-db mood |

### 预计工时：中（~3 天）

## Phase 7 — SK10 mayday-karaoke + SK11 mayday-fanfic

### SK10 关键交付

| # | 任务 | 依赖 |
|---|------|------|
| K-1 | SKILL.md + README.md | — |
| K-2 | 歌词音素标注 + 难点标记（高音/转音/换气点） | lyrics-db segments |
| K-3 | 难度评分算法：基于最高音、BPM、升 key 次数 | chords + lyrics-db |
| K-4 | 练习计划模板：「30 天从入门到倔强副歌」 | — |

### SK11 关键交付

| # | 任务 | 依赖 |
|---|------|------|
| F-1 | SKILL.md + README.md | — |
| F-2 | 五月天宇宙设定参考（角色关系、时间线、风格限制） | knowledge-base + persona |
| F-3 | 场景模板：初遇 / 并肩巡演 / 退役后的日常 | — |
| F-4 | 版权边界声明：禁止商用 / 禁止 R18 / 禁止丑化真人 | 法律审核 |

### 预计工时：SK10 高（~5 天），SK11 中（~3 天）

## Phase 8 — SK12 setlist-craft + SK13 mayday-dictionary

### SK12 关键交付

| # | 任务 | 依赖 |
|---|------|------|
| S-1 | SKILL.md + README.md | — |
| S-2 | 情绪曲线引擎：按用户期望的前/中/后段情绪生成曲目序列 | lyrics-db mood |
| S-3 | 曲目约束系统：用户可选「不要某曲」「必选某曲」「限定共X首」 | — |
| S-4 | 输出：PDF 格式的可打印 Setlist 卡片 | setlist-template.md |

### SK13 关键交付

| # | 任务 | 依赖 |
|---|------|------|
| D-1 | SKILL.md + README.md | — |
| D-2 | `references/dictionary.json`：200+ 词条的五迷黑话词典 | 人工整理 |
| D-3 | 搜索 + 模糊匹配接口 | — |
| D-4 | 每日一词功能（随机推送 + 上下文例子） | — |

### 预计工时：SK12 中（~2 天），SK13 低（~1 天）

## Phase 9 — 工作流编排 + 发布

| # | 任务 | 产出 |
|---|------|------|
| W-1 | Skill Pipeline 概念定义：输入 → 拆解 → 分派到子 Skill → 聚合输出 | Pipeline 架构文档 |
| W-2 | 参考工作流：「生日心愿套餐」= SK7 quotes + SK4 mood + SK5 chat-ashin + SK12 setlist | 模板 X 3 |
| W-3 | 发布指南：注册到 Trae / Claude Skills / agentskills.io 的流程说明 | 发布手册 |
| W-4 | `scripts/validate-skill.sh`：一致性检查（name ↔ 目录名 / reference 存在性 / frontmatter 格式） | 质量门禁脚本 |

### 预计工时：高（~5 天）

## 风险与缓解

| 风险 | 概率 | 缓解 |
|------|------|------|
| SK10 音素标注缺乏数据 | 中 | 初始标注 30 首重点曲目，其余留空慢慢补 |
| SK9 节目文本过长超出 token 窗口 | 低 | 模块化：节目大纲 ≤2K tokens，每段脚本独立输出 |
| SK11 同人创作触及版权/名誉问题 | 中 | 严格限制在「可合理引用」范围内；用户生成内容免责声明 |
| 多个 Skill 同步更新 lyrics-db 不一致 | 低 | sync 脚本 + 每次 commit 前自动检测差异 |