## Why

MaydaySkills 项目已有 8 个已实现的 Skill（SK1–SK8）和 5 个规划中的新 Skill（SK9–SK13），但 SDD 文档仍以手工维护的 `docs/sdd/` 目录为主，缺乏可执行的任务拆解和版本化追踪。需要用 OpenSpec 的 spec-driven workflow 将所有 13 个 Skill 的需求规格、技术设计和实施任务系统化地生成出来，实现「先对齐再动手」的开发范式。

## What Changes

- 为全部 13 个 Skill 生成 OpenSpec 标准格式的 spec 文档（每个 Skill 一个 capability）
- 将现有 `docs/sdd/skills/` 中的 13 份手工 SDD 迁移到 `openspec/specs/` 下的结构化 spec
- 生成统一的 design.md 描述跨 Skill 的技术架构与数据流
- 生成 tasks.md 将 Phase 6–9 的研发路线拆解为可执行的实施步骤

## Capabilities

### New Capabilities

- `ashin-lyrics`: SK1 阿信风格歌词生成 — 模仿阿信的写作范式生成原创中文歌词
- `mayday-chords`: SK2 五月天和弦秘籍 — 拆解怪兽的和弦进行、升 key 范式与编曲结构
- `mayday-trivia`: SK3 五月天 Trivia Master — 直答 28 年历史的冷知识 + 10 题闯关 Quiz（762 题库）
- `mayday-mood`: SK4 歌词情绪数据库 — 把用户情绪映射到三轴标签，从 120 首歌中推荐
- `chat-ashin`: SK5 和阿信聊聊 — 以阿信人设提供生活建议、安慰和闲聊
- `concert-prep`: SK6 演唱会备战助手 — Setlist 预测 + 应援练习 + 场馆攻略 + 必带清单
- `mayday-quotes`: SK7 五月天金句生成器 — 匹配/改写/生成五月天风格金句
- `mayday-data`: SK8 Mayday 音乐数据面板 — 可视化销量/串流/演唱会数据（Spotify + YouTube API）
- `mayday-radio`: SK9 AI 电台 DJ — 按主题/时长/心情编排完整的五月天主题广播节目
- `mayday-karaoke`: SK10 K 歌教练 — 标出高音/转音/换气点，难度评分，N 天练唱计划
- `mayday-fanfic`: SK11 五月天同人短篇 — 在合规边界内生成与五月天相关的同人短篇
- `setlist-craft`: SK12 自定义 Setlist — 按情绪曲线 + 约束编出个人定制版演唱会曲单
- `mayday-dictionary`: SK13 五迷词典 — 黑话/典故/彩蛋的语义词典 + 每日一词

### Modified Capabilities

_(无已有 OpenSpec spec 需要修改)_

## Impact

- **文档迁移**：`docs/sdd/skills/` 下 13 份 SDD 将被 `openspec/specs/` 下的 spec 文件取代；`docs/sdd/` 的横向文档（overview / architecture / roadmap / quality）保留不变
- **数据依赖**：所有 Skill 仍共享 `lyrics-db/`（120 首 / 9 专辑）和 `knowledge-base/`；sync 脚本不变
- **新增依赖**：SK9 依赖 SK4 的 mood 匹配公式；SK10 依赖 SK2 的和弦数据；SK11 依赖 SK5 的 persona
- **研发路线**：Phase 6–9 将从 roadmap 描述变为 tasks.md 中的可勾选任务清单
- **版本控制**：通过 OpenSpec 的 change/archive 机制追踪每个 Skill 从规划到交付的全过程
