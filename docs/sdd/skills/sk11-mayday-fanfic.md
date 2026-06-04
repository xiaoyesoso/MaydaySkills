# SK11 · mayday-fanfic

> 隶属：[Mayday Skills SDD](../README.md) · 状态：⏳ v1.1 规划中 · 优先级 P1
> 计划实现位置：`/mayday-fanfic/`

## 1. 一句话定义

在合规边界内，生成与五月天相关的同人短篇（fan-fiction）：可基于歌曲世界观、巡演幕后、角色 AU 等。

## 2. 用户故事

- 「写一篇《志明与春娇》多年后再相遇的短篇」
- 「给《如烟》写一个 800 字的伴生小说」
- 「五个团员上同一所大学的 AU 短篇」
- 「以《诺亚方舟》巡演为背景写一段歌迷视角的故事」

## 3. SKILL.md 关键字段

| 字段 | 内容 |
|------|------|
| `name` | `mayday-fanfic` |
| `category` | `creative-writing` |
| `compatibility` | No external dependencies |

## 4. 输入

| 字段 | 必填 | 说明 |
|------|------|------|
| premise | ✅ | 故事前提（基于歌词 / AU / 真实事件演绎）|
| length_words | ⏸️ | 默认 800；可选 300 / 1500 / 3000 |
| pov | ⏸️ | first / second / third（默认第三人称）|
| anchor_song | ⏸️ | 锚定曲目（结尾或意象会致敬）|
| tone | ⏸️ | `warm` / `bittersweet` / `dramatic` / `slice-of-life` |

## 5. 输出

短篇小说 + 文末注解：

```
《[标题]》
[正文，约 N 字]

---
✨ 灵感来源：《[曲名]》—— [专辑]
🎵 文中嵌入歌词锚句：「...」（1 句以内，引用而非复制）
⚖️ 创作声明：本文为同人虚构，与艺人本人立场无关；非商业用途。
```

## 6. 数据依赖

- `references/lyrics-db/`（取曲目锚句作为灵感）
- `references/knowledge-base/`（保证演唱会/年表/成员背景一致）
- `references/persona/`（多成员人设，v1.1 新增玛莎/怪兽/石头/冠佑）
- `references/fanfic-templates.md`（场景模板：初遇 / 巡演幕后 / 退役后 / AU）
- `references/fanfic-guidelines.md`（红线清单）

## 7. 流程

1. 询问 premise + length + pov + tone
2. 查 lyrics-db 选锚句（若用户未指定 anchor_song，由 mood 自动匹配）
3. 查 persona 拿到角色性格特征
4. 套用模板生成草稿
5. 自检红线（见 §8）
6. 输出 + 文末三段注解（灵感 / 锚句 / 创作声明）

## 8. 红线（必查）

- ❌ 不可包含 R18 / 暴力 / 涉政内容
- ❌ 不可丑化、抹黑、捏造侮辱性事件给真人
- ❌ 不可暗示真实恋爱关系（CP 文需明确标记 "纯虚构"）
- ❌ 不可使用任何完整歌词（只能引用 1 句锚句，且必须标注出处）
- ❌ 不可虚构成员公开发言或采访内容并伪造可信度
- ✅ 必须在末尾附「创作声明」

## 9. 与其它 Skill 协作

- 与 SK1 ashin-lyrics：当短篇需要"虚构歌曲"时，可调用 SK1 生成
- 与 SK5 chat-ashin：当短篇含对话时，可用 chat-ashin 的人设输出阿信台词
- 与 SK4 mood：无 anchor_song 时由 mood 推荐
- 与 SK13 dictionary：可调用词典确保黑话使用准确

## 10. 模板示例（fanfic-templates.md 草案）

| 模板名 | 场景 | 适配 mood | 锚定曲 |
|--------|------|-----------|--------|
| 初遇 1997 | 大安森林公园的最初成立 | growth / dream-chasing | 拥抱 |
| 兵役分别 | 2001 暂别歌坛 | loss / friendship | 风若吹 |
| 鸟巢之夜 | 2012 首次鸟巢 | celebration | 诺亚方舟 |
| 退役后的日常 | 假想的告别巡演之后 | nostalgia / growth | 转眼 |
| 大学时代 AU | 五人都是同班同学 | growth / friendship | 后青春期的诗 |