# lyrics-db · 歌词参考库（Skill 内置）

> 五月天歌词结构化数据，**Skill 自包含**，无外部依赖。

## 文件清单

| 文件 | 状态 |
|------|------|
| `schema.json` | ✅ 最终版（schema 定义） |
| `2004-神的孩子都在跳舞.json` | 🔸 示例（1 首） |
| `2008-后青春期的诗.json` | 🔸 示例（2 首） |

后续可按 `schema.json` 补全其它 7 张专辑与单曲。

## 字段说明

| 字段 | 必填 | 含义 |
|------|------|------|
| `album` | ✅ | 专辑名 |
| `year` | ✅ | 发行年份 |
| `songs[].title` | ✅ | 歌名 |
| `songs[].lyricist / composer` | ✅ | 词曲作者 |
| `songs[].key / bpm` | ⏸️ | 音乐信息（用于 mayday-chords） |
| `songs[].lyrics_excerpt` | ⏸️ | **仅 1-2 句引用片段** |
| `songs[].segments[]` | ⏸️ | 结构性段落标记 + 锚句 |
| `songs[].mood` | ⏸️ | 三轴情绪标签（用于 mayday-mood） |

## 版权策略

遵循 `mayday-skills-sdd.md` §7.3：本目录**仅**存放引用长度的歌词片段，**绝不**存放完整歌词。如需全文请前往授权平台。

## 新增条目流程

1. 提交前用 `schema.json` 验证结构。
2. `lyrics_excerpt` ≤ 2 行。
3. `mood` 字段如实标注，它直接驱动推荐排序。
