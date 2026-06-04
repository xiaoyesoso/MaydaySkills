# SK7 · mayday-quotes

> 隶属：[Mayday Skills SDD](../README.md) · Skill 状态：✅ v1.0 已交付
> 实现位置：[`/mayday-quotes/`](../../../mayday-quotes/)

## 1. 一句话定义

把任意生活场景或文本，匹配/改写为五月天歌词风格的金句。

## 2. 用户故事

- 「我要辞职了，发朋友圈用一句五月天」
- 「把这段毕业感言改成五月天风格」
- 「告白用哪句歌词最合适」

## 3. SKILL.md 关键字段

| 字段 | 内容 |
|------|------|
| `name` | `mayday-quotes` |
| `category` | `copywriting` |
| `compatibility` | No external dependencies |

## 4. 输入

| 字段 | 必填 | 说明 |
|------|------|------|
| scenario | ☑️ | 场景描述（quote-match）|
| original_text | ☑️ | 原文本（style-rewrite）|
| occasion | ☑️ | 模板分类 key（occasion-based）|
| style | ⏸️ | `热血` / `温柔` / `黑色幽默` |

## 5. 输出

- quote-match：Top 3 锚句卡片
- style-rewrite：改写文本 + diff 说明
- occasion：模板填空版

## 6. 数据依赖

- `references/quote-categories.md`
- `references/lyrics-db/`

## 7. 流程

1. 识别 intent（match / rewrite / occasion）
2. quote-match：关键词解析 → 查 lyrics-db → 排序 → 输出 top 3
3. style-rewrite：结构识别 → 应用阿信范式 → 改写
4. occasion：直接套模板，留 placeholder 给用户

## 8. Edge Cases

- 场景太模糊 → 追问 1 次场景细节
- 用户要求"逐字引用全曲" → 拒绝并解释版权
- 用户改写后还想"再热血一点" → 提供 3 档强度选择

## 9. 与其它 Skill 协作

- 与 SK1 ashin-lyrics 互补：quotes 是「找现成的」，lyrics 是「写新的」
- 与 SK5 chat-ashin 共享 lyrics-db 锚句机制