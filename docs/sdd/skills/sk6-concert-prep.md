# SK6 · concert-prep

> 隶属：[Mayday Skills SDD](../README.md) · Skill 状态：✅ v1.0 已交付
> 实现位置：[`/concert-prep/`](../../../concert-prep/)

## 1. 一句话定义

为即将看演唱会的五迷做一份「备战手册」：Setlist 预测 + 应援练习 + 场馆攻略 + 必带清单。

## 2. 用户故事

- 「下周六台北小巨蛋的五月天，要准备什么」
- 「人生无限公司北京站可能唱什么歌」
- 「带朋友第一次看五月天，怎么教他喊安可」

## 3. SKILL.md 关键字段

| 字段 | 内容 |
|------|------|
| `name` | `concert-prep` |
| `category` | `event-planning` |
| `compatibility` | Internet recommended for venue/weather |

## 4. 输入

| 字段 | 必填 | 说明 |
|------|------|------|
| tour | ✅ | 巡演名或场次日期 |
| city | ✅ | 场馆所在城市 |
| date | ⏸️ | YYYY-MM-DD |

## 5. 输出

- 📋 预测 Setlist（带 emoji 标记）
- 📣 应援指南
- 🚇 场馆攻略
- 🎒 必带清单（可勾选）

## 6. 数据依赖

- `references/knowledge-base/concert-archives.md`
- `references/knowledge-base/timeline.md`
- `assets/setlist-template.md`

## 7. 流程

1. 询问 tour / city / date
2. 查 concert-archives 拿到该巡演近期场次的曲目
3. 用 lyrics-db 给曲目打标 🎤⚡🕯️🎸
4. 渲染四块输出 + 提示是否生成可打印 PDF

## 8. Edge Cases

- 巡演已结束 → 改为「回顾型 setlist」
- 全新巡演无数据 → 基于该期间近似巡演推测，明确标注 confidence=低
- 户外场地 → 加雨具/防晒/防寒物品

## 9. 与其它 Skill 协作

- SK12 setlist-craft 是 SK6 的"主动版"：用户自己编曲单，concert-prep 是"预测版"
- 两者共享 lyrics-db + concert-archives