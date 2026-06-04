# SK1 · ashin-lyrics

> 隶属：[Mayday Skills SDD](../README.md) · Skill 状态：✅ v1.0 已交付
> 实现位置：[`/ashin-lyrics/`](../../../ashin-lyrics/)

## 1. 一句话定义

按用户给的主题/语气/长度，生成**原创**中文歌词，风格模仿阿信。

## 2. 用户故事

- 「我失恋了，写一段五月天风格的副歌」
- 「帮我用阿信风格写一段毕业季的歌词，要有怀旧感」
- 「我有一个鼓点和旋律，需要副歌词，希望热血一点」

## 3. SKILL.md 关键字段

| 字段 | 内容 |
|------|------|
| `name` | `ashin-lyrics` |
| `category` | `creative-writing` |
| `compatibility` | No external dependencies |

## 4. 输入

| 字段 | 必填 | 说明 |
|------|------|------|
| topic | ✅ | 主题/场景，自由文本 |
| tone | ⏸️ | `inspirational` / `melancholic` / `passionate`，默认询问 |
| length | ⏸️ | `verse × N` / `chorus` / `full` |

## 5. 输出

- 1–3 段候选歌词（候选时各标 rhyme scheme 与阿信范式）
- 用户选定后扩写为完整歌词，分段标注 verse/chorus/bridge

## 6. 数据依赖

- `references/lyric-techniques.md`
- `references/lyrics-db/`（由 sync 脚本维护）

## 7. 流程

1. 询问主题、语气、长度
2. 从 lyrics-db 抽取与 tone 匹配的样本作为参考
3. 生成 3 段候选 + 范式标注
4. 用户选定 → 扩展为完整歌词
5. 输出 verse/chorus/bridge 结构清单

## 8. Edge Cases

- 输入太模糊 → 追问 1 个澄清问题再生成
- 用户认为"不像阿信" → 解释偏差并给出修订
- **绝不**逐字输出现有五月天歌词

## 9. 与其它 Skill 协作

- 升级路径：与 SK2 mayday-chords 联合可输出「词 + 和弦小样」
- 与 SK11 fanfic 共享 lyrics-db，未来可基于「同人小说」生成插曲