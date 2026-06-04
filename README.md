# Mayday Skills · 五月天 Agent Skills 集合

> 一套围绕五月天乐队的 Agent Skills 生态。每个 Skill 都是**独立资源包**，可单独安装、可组合、可跨平台复用。
> 规范遵循 [agentskills.io v1.0](https://agentskills.io/specification)。

## 技能总览

### v1.0 既有（已实现）

| ID | Skill | 分类 | 一句话简介 |
|----|-------|------|------------|
| SK1 | [ashin-lyrics](./ashin-lyrics/) | 创作陪伴 | 模仿阿信风格写原创中文歌词 |
| SK2 | [mayday-chords](./mayday-chords/) | 创作陪伴 | 拆解怪兽的和弦进行与升 key 范式 |
| SK3 | [mayday-trivia](./mayday-trivia/) | 知识问答 | 直答 + 10 题挑战赛（762 题）|
| SK4 | [mayday-mood](./mayday-mood/) | 知识问答 | 按心情推荐五月天歌单 |
| SK5 | [chat-ashin](./chat-ashin/) | 互动陪伴 | 以阿信口吻给建议 / 安慰 / 闲聊 |
| SK6 | [concert-prep](./concert-prep/) | 互动陪伴 | 演唱会备战手册（Setlist + 应援 + 场馆）|
| SK7 | [mayday-quotes](./mayday-quotes/) | 实用工具 | 五月天金句匹配 + 风格改写 |
| SK8 | [mayday-data](./mayday-data/) | 实用工具 | 销量 / 串流 / 演唱会数据面板（接 Spotify+YouTube）|

### v1.1 规划中（SDD 已完成）

| ID | Skill | 分类 | 一句话简介 |
|----|-------|------|------------|
| SK9 | [mayday-radio](./docs/sdd/skills/sk9-mayday-radio.md) | 沉浸陪伴 | AI 电台 DJ：把任意时长拼成一档主题广播 |
| SK10 | [mayday-karaoke](./docs/sdd/skills/sk10-mayday-karaoke.md) | 创作陪伴 | K 歌教练：标难点 + 难度评分 + N 天练唱计划 |
| SK11 | [mayday-fanfic](./docs/sdd/skills/sk11-mayday-fanfic.md) | 创作陪伴 | 五月天宇宙的同人短篇生成器（合规约束）|
| SK12 | [setlist-craft](./docs/sdd/skills/sk12-setlist-craft.md) | 互动陪伴 | 自定义演唱会 Setlist：用情绪曲线编一场你的五月天 |
| SK13 | [mayday-dictionary](./docs/sdd/skills/sk13-mayday-dictionary.md) | 知识问答 | 五迷词典：黑话、典故、彩蛋的语义词典 |

## 仓库结构

```
MaydaySkills/
├── README.md                          # 本文档
├── AGENTS.md                          # 给 AI agent 的研发指引
├── LICENSE
│
├── docs/sdd/                          # SDD 文档集（v1.1）
│   ├── README.md                      #   入口索引
│   ├── 00-overview.md / 10-architecture.md
│   ├── 20-roadmap.md / 30-quality.md
│   ├── skills/                        #   每 Skill 一份 SDD
│   ├── appendix/                      #   触发词矩阵 / changelog
│   └── archive/v1.0.md                #   原 SDD 归档
│
├── scripts/                           # 仓库级辅助脚本
│   ├── sync-lyrics-db.sh
│   └── gen-trivia.py
│
├── ashin-lyrics/                      # 每个 Skill 都是独立资源包
│   ├── SKILL.md
│   ├── README.md
│   ├── references/
│   └── ...
├── mayday-chords/
├── mayday-trivia/
├── mayday-mood/                       # lyrics-db 主源所在地
├── chat-ashin/
├── concert-prep/
├── mayday-quotes/
└── mayday-data/
```

## 设计原则

1. **每个 Skill 都自给自足** — 不依赖仓库内任何外部目录。歌词库、知识库、人设等公共资源直接内嵌到需要它们的 Skill 目录下。
2. **渐进式加载** — `SKILL.md` 元数据约 100 tokens；正文 ≤ 5000 tokens；细节资源放 `references/`，按需读取。
3. **版权安全** — 所有歌词字段仅保存 1-2 句引用片段（见每个 lyrics-db 下的 README 与 SDD §7.3）。
4. **中文优先** — `README.md` 一律中文，`SKILL.md` 描述中英双语关键词以最大化触发率。
5. **跨平台** — Skill 不假设特定平台；如有依赖在 `compatibility` 字段声明。

## 快速开始

任选一个 Skill 目录使用：

```bash
# 例如：体验「演唱会备战助手」
cat concert-prep/README.md
cat concert-prep/SKILL.md
```

或将整个 Skill 目录复制到你的 Agent 框架（Claude Skills / Trae / 自研 Agent 等）的 skills 加载路径下。

## 研发路线（出自 SDD §5）

| 阶段 | 内容 | 状态 |
|------|------|------|
| Phase 0 | 公共资源初始化（数据 schema、知识底稿、人设文档） | ✅ 已内嵌到各 Skill |
| Phase 1 | P0 三技能：ashin-lyrics / mayday-mood / mayday-quotes | ✅ 脚手架完成 |
| Phase 2 | P1 三技能：mayday-trivia / chat-ashin / concert-prep | ✅ 脚手架完成 |
| Phase 3 | P2 两技能：mayday-chords / mayday-data | ✅ 脚手架完成（含示例脚本） |
| Phase 4 | 数据扩充（歌词 9 张专辑全量/120 首、762 题题库、Spotify + YouTube API） | ✅ 完成 |
| Phase 5 | SDD 文档重构 + 新 Skill 规划 | ✅ 完成 |
| Phase 6 | SK9 mayday-radio（AI 电台）研发 | ⏳ |
| Phase 7 | SK10 mayday-karaoke + SK11 mayday-fanfic 研发 | ⏳ |
| Phase 8 | SK12 setlist-craft + SK13 mayday-dictionary 研发 | ⏳ |
| Phase 9 | 工作流编排 + 发布平台 | ⏳ |

### Phase 4 交付明细

- **歌词元数据**：9 张录音室专辑 / 120 首歌曲，统一 schema，仅存 1–2 句引用片段 + 调性 / BPM / 三轴情绪 / 锚句 / 标签。主源在 [`mayday-mood/references/lyrics-db/`](./mayday-mood/references/lyrics-db/)，通过 [`scripts/sync-lyrics-db.sh`](./scripts/sync-lyrics-db.sh) 复制到 `ashin-lyrics` / `chat-ashin` / `mayday-quotes` / `mayday-trivia`。
- **题库**：[`mayday-trivia/references/trivia-db.json`](./mayday-trivia/references/trivia-db.json) 共 **762 题**，覆盖 members / albums / concerts / mvs / awards / collaborations 六大领域，四档难度。由 [`scripts/gen-trivia.py`](./scripts/gen-trivia.py) 基于歌词库 + 知识库一键再生成。
- **API 接入**：[`mayday-data/scripts/data-fetcher.py`](./mayday-data/scripts/data-fetcher.py) 新增 `spotify-popularity` 与 `youtube-views` 两条子命令，凭据走环境变量 `SPOTIFY_CLIENT_ID` / `SPOTIFY_CLIENT_SECRET` / `YOUTUBE_API_KEY`；无凭据时自动 fallback 到 mock 数据，结果统一带 `_meta.source` 标识。响应缓存于 `~/.cache/mayday-data/`，TTL 6 小时。

### Phase 5 交付明细

- SDD 从单文档 `mayday-skills-sdd.md` 拆分为 **19 份文档**的 SDD 集（[`docs/sdd/`](./docs/sdd/)）：
  - 4 份横向文档（overview / architecture / roadmap / quality）
  - 8 份既有 Skill SDD + 5 份新 Skill SDD
  - 附录（trigger-matrix / changelog）+ 归档
- 新增 5 个 Skill 规划：mayday-radio / mayday-karaoke / mayday-fanfic / setlist-craft / mayday-dictionary
- 新增 Phase 6–9 的详细研发路线图

## 质量与版权

- 完整规范见 [`docs/sdd/`](./docs/sdd/) 下各文档，特别是 [`docs/sdd/30-quality.md`](./docs/sdd/30-quality.md)（质量门禁）与 [`docs/sdd/00-overview.md`](./docs/sdd/00-overview.md)（概述）。
- 歌词版权：每个 Skill 内的 `lyrics-db/` 仅存放短引用片段，绝不分发完整歌词。

---

> *「这一生只愿只要平凡快乐 谁说这样不伟大呢」*  
> ——五月天《笑忘歌》
