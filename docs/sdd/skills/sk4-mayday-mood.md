# SK4 · mayday-mood

> 隶属：[Mayday Skills SDD](../README.md) · Skill 状态：✅ v1.0 已交付
> 实现位置：[`/mayday-mood/`](../../../mayday-mood/)（同时是 lyrics-db **主源**）

## 1. 一句话定义

把用户的情绪自然语言映射到三轴标签，从 120 首歌中匹配最贴合的 3–5 首。

## 2. 用户故事

- 「最近被工作搞崩了，想被治愈但又想有点力量」
- 「失恋了，五月天推哪首」
- 「帮我编一个通勤→工作→午休→下班的歌单」

## 3. SKILL.md 关键字段

| 字段 | 内容 |
|------|------|
| `name` | `mayday-mood` |
| `category` | `music-discovery` |
| `compatibility` | No external dependencies |

## 4. 输入

| 字段 | 必填 | 说明 |
|------|------|------|
| mood | ✅ | 自由文本 |
| activities | ⏸️ | 活动序列（用于歌单生成） |

## 5. 输出

- 3–5 首歌：标题、专辑、年份、E/V/Themes 分值、锚句、「Why fits」一句话
- 可选：歌单名 + 收听顺序

## 6. 数据依赖

- `references/mood-taxonomy.md`
- `references/lyrics-db/`（主源）

## 7. 流程

1. 询问当前心情（free text）
2. 按 mood-taxonomy 把文本解析为 E / V / themes
3. 计算每首歌：`score = -sqrt(ΔE²+ΔV²) + 2·|theme_overlap|`
4. 取 top 3–5
5. 输出 + 解释 + 可选歌单 name/order

## 8. Edge Cases

- 模糊心情 → 追问 1 次再猜
- 中性/矛盾 → 推荐 E≈5 V≈5 段位，明确标注 ambiguity
- 用户驳回某曲 → 承认主观性，提供按时代/专辑过滤
- 数据库缺 mood → 跳过，不编造

## 9. 与其它 Skill 协作

- lyrics-db 主源，SK1/SK7/SK9/SK11/SK12 都消费它
- SK9 mayday-radio 直接复用 mood 匹配引擎来编排电台节目