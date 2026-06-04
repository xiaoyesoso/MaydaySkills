# SK2 · mayday-chords

> 隶属：[Mayday Skills SDD](../README.md) · Skill 状态：✅ v1.0 已交付
> 实现位置：[`/mayday-chords/`](../../../mayday-chords/)

## 1. 一句话定义

拆解怪兽的和弦进行、升 key 范式与编曲结构，并能为任意曲目输出和弦谱。

## 2. 用户故事

- 「《倔强》最后一段是怎么升 key 的？」
- 「我想学吉他，先弹哪几首五月天最合适？」
- 「分析一下《温柔》的副歌为什么这么催泪」

## 3. SKILL.md 关键字段

| 字段 | 内容 |
|------|------|
| `name` | `mayday-chords` |
| `category` | `music-theory` |
| `compatibility` | Requires Python 3.12+ for chord-diagram.py |

## 4. 输入

| 字段 | 必填 | 说明 |
|------|------|------|
| song | ☑️ | 曲名（与 mode=lookup 配合）|
| goal | ☑️ | 学习目标（与 mode=roadmap 配合）|
| mode | ⏸️ | `lookup` / `pattern` / `key-change` / `roadmap`（默认按输入猜测）|

## 5. 输出

- Roman numeral 分析 + 标准和弦
- ASCII 和弦图（`scripts/chord-diagram.py`）
- 1 段文字解读情绪与编曲意图

## 6. 数据依赖

- `references/chord-patterns.md` — 五月天高频和弦模板
- `references/lyrics-db/`（由 sync 脚本维护）— 来源 key/bpm

## 7. 流程

1. 解析输入意图（lookup / roadmap / 分析）
2. 查 chord-patterns + lyrics-db，组装和弦数据
3. 调用 chord-diagram.py 输出图形
4. 用文字解释为什么这套和弦/升 key 在情绪上 work

## 8. Edge Cases

- 数据库无该曲 → 联网查询并明确标注 "外部来源"
- 用户给的不是曲名而是 mood → 转 SK4 mayday-mood 推荐曲目，再回到 SK2

## 9. 与其它 Skill 协作

- 升级路径：为 SK10 mayday-karaoke 提供「难点判定」的和弦/升 key 数据
- 与 SK1 ashin-lyrics 联合可输出"词+和弦"小样