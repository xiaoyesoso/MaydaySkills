# Mayday Skills · SDD 文档集

> 基于 [agentskills.io v1.0](https://agentskills.io/specification) 的五月天 Agent Skills Spec-Driven Development 文档集。
> 当前版本：**v1.1**（2026-06-04）
> 原 v1.0 单文档已归档至 [`archive/v1.0.md`](./archive/v1.0.md)。

## 文档结构

### 横向文档（跨 Skill）

| 文档 | 内容 |
|------|------|
| [`00-overview.md`](./00-overview.md) | 项目愿景、技能矩阵、版本演进 |
| [`10-architecture.md`](./10-architecture.md) | 仓库结构、公共能力模块（lyrics-db / knowledge-base / persona） |
| [`20-roadmap.md`](./20-roadmap.md) | Phase 0-4 路线图与每个里程碑的交付 |
| [`30-quality.md`](./30-quality.md) | 合规检查、质量门禁、版权策略 |

### Skill SDD（每个 Skill 一份）

> 命名约定：`sk{N}-{skill-id}.md`，与 SKILL.md 的 `name` 字段对齐。

#### v1.0 既有 8 个 Skill

| ID | Skill | 状态 |
|----|-------|------|
| SK1 | [ashin-lyrics](./skills/sk1-ashin-lyrics.md) | ✅ 已交付 |
| SK2 | [mayday-chords](./skills/sk2-mayday-chords.md) | ✅ 已交付 |
| SK3 | [mayday-trivia](./skills/sk3-mayday-trivia.md) | ✅ 已交付（762 题） |
| SK4 | [mayday-mood](./skills/sk4-mayday-mood.md) | ✅ 已交付 |
| SK5 | [chat-ashin](./skills/sk5-chat-ashin.md) | ✅ 已交付 |
| SK6 | [concert-prep](./skills/sk6-concert-prep.md) | ✅ 已交付 |
| SK7 | [mayday-quotes](./skills/sk7-mayday-quotes.md) | ✅ 已交付 |
| SK8 | [mayday-data](./skills/sk8-mayday-data.md) | ✅ 已交付（Spotify/YouTube） |

#### v1.1 新增 5 个 Skill（规划中）

| ID | Skill | 一句话 | 优先级 |
|----|-------|--------|--------|
| SK9 | [mayday-radio](./skills/sk9-mayday-radio.md) | AI 电台 DJ：把任意时长拼成一档五月天主题广播 | P0 |
| SK10 | [mayday-karaoke](./skills/sk10-mayday-karaoke.md) | K 歌教练：教你怎么唱准每一首歌 + 难度评分 | P1 |
| SK11 | [mayday-fanfic](./skills/sk11-mayday-fanfic.md) | 五月天宇宙的同人短篇生成器（守规范守版权） | P1 |
| SK12 | [setlist-craft](./skills/sk12-setlist-craft.md) | 自定义演唱会 Setlist：用情绪曲线编一场你的五月天 | P2 |
| SK13 | [mayday-dictionary](./skills/sk13-mayday-dictionary.md) | 五迷词典：黑话、典故、彩蛋的语义词典 | P2 |

### 附录

| 文档 | 内容 |
|------|------|
| [`appendix/trigger-matrix.md`](./appendix/trigger-matrix.md) | 所有 Skill 的触发词矩阵 |
| [`appendix/changelog.md`](./appendix/changelog.md) | 文档变更记录 |

## 阅读指南

- **想了解整体规划** → [`00-overview.md`](./00-overview.md)
- **想新增一个 Skill** → 参考任一现成 SDD（如 [SK1](./skills/sk1-ashin-lyrics.md)），照 8 节模版填
- **要做发布前自检** → [`30-quality.md`](./30-quality.md)
- **想看 v1.0 原稿** → [`archive/v1.0.md`](./archive/v1.0.md)
