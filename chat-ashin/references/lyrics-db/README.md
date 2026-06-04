# lyrics-db · 歌词参考库（Skill 内置）

> 五月天 9 张录音室专辑的结构化元数据。**Skill 自包含**，无外部依赖。
> 主存放点为 `mayday-mood/references/lyrics-db/`，其他 skill 的同名目录由 `scripts/sync-lyrics-db.sh` 同步保持一致。

## 文件清单

| 文件 | 专辑 | 歌曲数 |
|------|------|--------|
| `1999-第一张创作专辑.json` | 第一张创作专辑 | 12 |
| `2000-爱情万岁.json` | 爱情万岁 | 12 |
| `2001-人生海海.json` | 人生海海 | 12 |
| `2003-时光机.json` | 时光机 | 15 |
| `2004-神的孩子都在跳舞.json` | 神的孩子都在跳舞 | 13 |
| `2006-为爱而生.json` | 为爱而生 | 13 |
| `2008-后青春期的诗.json` | 后青春期的诗 | 12 |
| `2011-第二人生.json` | 第二人生（末日版+明日版合并） | 16 |
| `2016-自传.json` | 自传 | 15 |
| `schema.json` | JSON Schema 定义 | — |

合计 **120 首** 录音室专辑曲目元数据。

## 字段说明

| 字段 | 必填 | 含义 |
|------|------|------|
| `album` | ✅ | 专辑名 |
| `year` | ✅ | 发行年份 |
| `release_date` | ⏸️ | ISO 日期 |
| `label` | ⏸️ | 唱片公司 |
| `english_title` | ⏸️ | 英文译名 |
| `songs[].title` | ✅ | 歌名 |
| `songs[].lyricist / composer` | ✅ | 词曲作者 |
| `songs[].key / bpm` | ⏸️ | 音乐信息（用于 mayday-chords） |
| `songs[].lyrics_excerpt` | ⏸️ | **仅 1-2 句引用片段**，instrumental 标 `(instrumental ...)` |
| `songs[].segments[]` | ⏸️ | 结构性段落标记 + 锚句 |
| `songs[].mood` | ⏸️ | 三轴情绪标签（用于 mayday-mood） |
| `songs[].tags` | ⏸️ | 自由标签 |

## 版权策略

遵循 SDD 版权条款（[`docs/sdd/30-quality.md`](../../../docs/sdd/30-quality.md) §3）：本目录**仅**存放引用长度的歌词片段，**绝不**存放完整歌词。如需全文请前往授权平台。

## 同步策略

`ashin-lyrics` / `chat-ashin` / `mayday-mood` / `mayday-quotes` 4 个 skill 各自维护一份完整副本，以保持每个 skill **自包含**。修改主源后请执行：

```bash
scripts/sync-lyrics-db.sh
```

脚本会从 `mayday-mood/references/lyrics-db/` 同步到其他 3 个 skill。

## 新增条目流程

1. 先在 `mayday-mood/references/lyrics-db/` 添加或修改 JSON。
2. 用 `schema.json` 验证结构。
3. `lyrics_excerpt` ≤ 2 行。
4. `mood` 字段如实标注，它直接驱动推荐排序。
5. 运行同步脚本。
