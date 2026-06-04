# 00 · 项目概述

> 隶属：[Mayday Skills SDD](./README.md)
> 版本：v1.1（2026-06-04）

## 1. 愿景

构建一套围绕**五月天乐队**的 Agent Skills 生态——让 AI 助手成为最懂五月天的「第六位成员」。每个 Skill 独立可安装、可组合、可跨平台复用。

## 2. 技能矩阵

### 2.1 v1.0 既有 Skill（8 个）

| ID | Skill | 分类 | 优先级 | 复杂度 | 状态 |
|----|-------|------|--------|--------|------|
| SK1 | ashin-lyrics | 创作陪伴 | P0 | 中 | ✅ |
| SK2 | mayday-chords | 创作陪伴 | P2 | 高 | ✅ |
| SK3 | mayday-trivia | 知识问答 | P1 | 低 | ✅（762 题）|
| SK4 | mayday-mood | 知识问答 | P0 | 中 | ✅ |
| SK5 | chat-ashin | 互动陪伴 | P1 | 高 | ✅ |
| SK6 | concert-prep | 互动陪伴 | P1 | 中 | ✅ |
| SK7 | mayday-quotes | 实用工具 | P0 | 低 | ✅ |
| SK8 | mayday-data | 实用工具 | P2 | 高 | ✅（Spotify/YouTube）|

### 2.2 v1.1 新增 Skill（5 个）

| ID | Skill | 分类 | 优先级 | 复杂度 | 触发场景 |
|----|-------|------|--------|--------|----------|
| SK9 | mayday-radio | 沉浸陪伴 | P0 | 中 | 「给我做一档 30 分钟的失恋专题电台」 |
| SK10 | mayday-karaoke | 创作陪伴 | P1 | 高 | 「我想练唱倔强，副歌总是破音」 |
| SK11 | mayday-fanfic | 创作陪伴 | P1 | 中 | 「写个志明春娇大学时代的小短篇」 |
| SK12 | setlist-craft | 互动陪伴 | P2 | 中 | 「帮我编一份生日演唱会曲单」 |
| SK13 | mayday-dictionary | 知识问答 | P2 | 低 | 「五迷术语『升 key 战神』什么意思」 |

### 2.3 跨 Skill 共生关系

```
        ┌──────────────────────────────┐
        │   lyrics-db (120 首/9 专辑)   │
        └──────────┬───────────────────┘
                   │
   ┌───────────────┼────────────────┐
   │               │                │
   ▼               ▼                ▼
SK1 lyrics    SK4 mood        SK7 quotes
   │            │                │
   ▼            ▼                ▼
SK11 fanfic   SK9 radio      SK12 setlist
                 │
        ┌────────┴────────┐
        ▼                 ▼
   SK10 karaoke       SK6 concert-prep
        │                 │
        ▼                 ▼
     SK2 chords        SK13 dictionary

   SK3 trivia ← knowledge-base + lyrics-db
   SK5 chat-ashin ← persona + knowledge-base
   SK8 data ← Spotify/YouTube API
```

## 3. 设计原则

1. **每个 Skill 自给自足**：不依赖仓库其他 skill。公共资源通过 `scripts/sync-*.sh` 复制而非引用，确保单 Skill 打包后可独立运行。
2. **渐进式加载**：`SKILL.md` 元数据 ~100 tokens；正文 ≤ 5000 tokens；细节进 `references/`。
3. **版权安全**：歌词字段只保存 1–2 句引用片段（见 [`30-quality.md`](./30-quality.md) §版权策略）。
4. **中文优先**：`README.md` 中文，`SKILL.md` 描述中英双语关键词。
5. **跨平台**：Skill 不假设特定平台；如需依赖，在 `compatibility` 字段声明。

## 4. 版本演进

| 版本 | 日期 | 主要变化 |
|------|------|---------|
| v1.0 | 2026-06-04 | 8 个 Skill 初稿，Phase 0-3 完成 |
| v1.0.1 | 2026-06-04 | Phase 4 数据扩充（9 专辑 120 首 / 762 题 / Spotify+YouTube API） |
| v1.1 | 2026-06-04 | SDD 文档拆分；新增 SK9–SK13 五个 Skill 规划 |

## 5. 引用规范

本文档所有 Skill 均遵循 [agentskills.io Specification v1.0](https://agentskills.io/specification)：

- `SKILL.md` 使用 **YAML frontmatter + Markdown Body** 结构
- `name`：1–64 字符，小写字母+数字+连字符，与目录名一致
- `description`：1–1024 字符，包含激活关键词
- Body 正文 ≤ 5000 tokens，详细内容拆分至 `references/`
- 渐进式加载：元数据(~100 tokens) → 指令(<5000 tokens) → 按需加载资源
