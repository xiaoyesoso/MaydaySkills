# 10 · 仓库架构 与 公共能力模块

> 隶属：[Mayday Skills SDD](./README.md)
> 版本：v1.1

## 1. 仓库结构

```
mayday-skills/
├── README.md                          # 顶层入口（中文）
├── AGENTS.md                          # 给 AI agent 的研发指引
├── LICENSE
├── docs/sdd/                          # ← 本目录：SDD 文档集
│   ├── README.md
│   ├── 00-overview.md
│   ├── 10-architecture.md             # 本文件
│   ├── 20-roadmap.md
│   ├── 30-quality.md
│   ├── skills/                        # 各 Skill SDD
│   ├── appendix/
│   └── archive/                       # 历史 SDD
├── scripts/                           # 仓库级辅助脚本
│   ├── sync-lyrics-db.sh              # 把 lyrics-db 同步到各 skill
│   └── gen-trivia.py                  # 重新生成 trivia-db.json
│
├── ashin-lyrics/                      # 每个 Skill 都是自包含目录
│   ├── SKILL.md                       #   规范主体
│   ├── README.md                      #   中文说明
│   ├── references/                    #   渐进式加载的参考资源
│   │   └── lyrics-db/                 #     由 sync 脚本维护
│   └── ...
├── chat-ashin/
├── concert-prep/
├── mayday-chords/
├── mayday-data/
├── mayday-mood/                       # lyrics-db 主源所在地
├── mayday-quotes/
├── mayday-trivia/
│
└── (v1.1 新增 Skill 目录将按相同模式新建)
    ├── mayday-radio/
    ├── mayday-karaoke/
    ├── mayday-fanfic/
    ├── setlist-craft/
    └── mayday-dictionary/
```

## 2. 公共能力模块

### 2.1 `lyrics-db/` — 歌词元数据库

主源：[`mayday-mood/references/lyrics-db/`](../../mayday-mood/references/lyrics-db/)
同步：[`scripts/sync-lyrics-db.sh`](../../scripts/sync-lyrics-db.sh) → 推送到 `ashin-lyrics` / `chat-ashin` / `mayday-quotes` / `mayday-trivia`，未来还包括 SK9–SK13 中需要它的 skill。

**规模**：9 张录音室专辑（1999–2016），120 首歌曲，统一 schema。

**字段**（详见 [`schema.json`](../../mayday-mood/references/lyrics-db/schema.json)）：

| 字段 | 用途 |
|------|------|
| `album / year / release_date / label` | 专辑基础信息 |
| `songs[].title / lyricist / composer / arranger` | 词曲制作 |
| `songs[].key / bpm / duration_seconds` | 音乐参数（驱动 SK2/SK10）|
| `songs[].lyrics_excerpt` | 1–2 句引用片段（版权安全）|
| `songs[].segments[]` | 结构化段落 + 锚句 |
| `songs[].mood` | 三轴情绪标签（驱动 SK4/SK9）|
| `songs[].tags` | 自由标签 |

### 2.2 `knowledge-base/` — 事实知识库

| 文件 | 内容 | 服务于 |
|------|------|--------|
| `band-members.md` | 五人资料（生日/乐器/外号/副业/趣闻） | SK3, SK5, SK13 |
| `album-history.md` | 9 张专辑的创作背景、市场反响 | SK3, SK6, SK11 |
| `concert-archives.md` | 历次巡演（城市/场次/名场面） | SK3, SK6, SK12 |
| `timeline.md` | 1997–至今大事年表 | SK3, SK5, SK11 |

> 这些文件在 `chat-ashin/` `concert-prep/` `mayday-trivia/` 下各有一份独立副本。当前未做同步脚本，因为修改频率较低；未来如频繁修订可加 `scripts/sync-knowledge-base.sh`。

### 2.3 `persona/` — 角色资源

- [`chat-ashin/references/persona/ashin-persona.md`](../../chat-ashin/references/persona/ashin-persona.md)：阿信人设完整指南，仅 SK5 使用。
- v1.1 拟新增其他成员 persona（玛莎/怪兽/石头/冠佑）供 SK11 同人创作使用。

### 2.4 `scripts/` — 仓库级脚本

| 脚本 | 用途 |
|------|------|
| `scripts/sync-lyrics-db.sh` | 主源 → 各 skill 单向同步 |
| `scripts/gen-trivia.py` | 由 lyrics-db + knowledge-base 重新生成 trivia-db.json |
| `mayday-data/scripts/data-fetcher.py` | Spotify / YouTube API + mock fallback |
| `mayday-chords/scripts/chord-diagram.py` | 和弦图渲染 |
| _v1.1 拟新增_ | `mayday-radio/scripts/build-program.py`，`mayday-karaoke/scripts/score-pitch.py` 等 |

## 3. Skill 间数据流约束

1. **单向依赖**：所有 skill 只读 lyrics-db / knowledge-base，绝不写。新数据先入主源，再 sync。
2. **离线优先**：所有 Skill 必须在「无外网」状态下也能完成核心流程；外部 API 走可选增强（参考 SK8 的 `_meta.source` 模式）。
3. **零跨目录引用**：SKILL.md 内不写 `../shared/...` 之类的相对路径，资源全在自身 `references/` 下。

## 4. 命名约定

| 类型 | 规则 | 例 |
|------|------|----|
| Skill 目录 | kebab-case，小写 | `mayday-radio/` |
| SKILL.md name | 与目录同名 | `name: mayday-radio` |
| SDD 文件 | `sk{N}-{name}.md` | `sk9-mayday-radio.md` |
| 脚本文件 | `verb-noun.py` | `build-program.py` |
| 数据 JSON | `<year>-<标题>.json` 或 `<domain>-db.json` | `2016-自传.json` / `trivia-db.json` |
