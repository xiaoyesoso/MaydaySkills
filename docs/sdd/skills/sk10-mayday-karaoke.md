# SK10 · mayday-karaoke

> 隶属：[Mayday Skills SDD](../README.md) · 状态：⏳ v1.1 规划中 · 优先级 P1
> 计划实现位置：`/mayday-karaoke/`

## 1. 一句话定义

教用户**怎么唱**任意一首五月天：标出高音/转音/换气点，给难度评分，并制定 N 天练唱计划。

## 2. 用户故事

- 「我想练《倔强》，副歌总是破音怎么办」
- 「以我的音域（C–G2），五月天哪些歌适合 K」
- 「30 天我能不能把《如烟》练到 KTV 100 分水准」
- 「《派对动物》的换气点在哪几处」

## 3. SKILL.md 关键字段

| 字段 | 内容 |
|------|------|
| `name` | `mayday-karaoke` |
| `category` | `vocal-coaching` |
| `compatibility` | No external dependencies; future: pitch-detection via `librosa` (optional) |

## 4. 输入

| 字段 | 必填 | 说明 |
|------|------|------|
| song | ☑️ | 曲名（mode=guide / score）|
| vocal_range | ☑️ | 用户音域，如 `C3-A4`（mode=recommend）|
| level | ⏸️ | beginner / intermediate / advanced |
| goal_days | ⏸️ | 练唱计划天数 |

## 5. 输出

### Guide 模式
- 难度评分（0–10）+ 难度原因（最高音/升 key/快速换气）
- 每段歌词标注：🔴 高音、🟡 转音、💨 换气点、🎯 副歌升 key
- 建议练习顺序：先慢速哼唱 → 跟唱 → 全速

### Score 模式（需要用户输入录音；MVP 可先做谱面比对）
- 每段评分 + 改进建议

### Recommend 模式
- 按用户 vocal_range 从 lyrics-db 中过滤可唱曲目
- 输出按难度从易到难排序

### Plan 模式
- N 天练习计划，每天 30 分钟，分阶段拆解曲目

## 6. 数据依赖

- `references/lyrics-db/`（取 key、bpm、segments、tags）
- `references/karaoke-difficulty.json` ← 每首歌的难度元数据
- `scripts/score-pitch.py`（MVP 阶段：基于歌词长度 + 换气间隔的启发式评分）

## 7. 流程

### Guide
1. 加载歌曲 metadata
2. 计算难度（最高音 ↑ ＋ 升 key 次数 ↑ ＋ BPM ↑ → 分数 ↑）
3. 在 segments 上标注重点
4. 输出含色块的练唱指南

### Recommend
1. 用户输入音域
2. 过滤 lyrics-db 中 `key` 对应的最高音超出用户范围的曲目
3. 按难度升序排，输出 5–10 首

### Plan
1. 根据 goal_days 拆段：周一－段落练习；周二－全曲慢练；周三－全速跟唱；周四－换气专项；…
2. 每天输出当天目标 + 重点段落 + 自测打卡格式

## 8. Edge Cases

- 用户没标音域 → 用问题诱导：「你能舒服地唱到哪个高音？《温柔》『让我们 *自由*』那个『自』」
- 用户曲目不在 lyrics-db → 提示从相似曲目类推
- 用户希望「精确录音评分」但系统只有谱面 → 明确告知 MVP 限制，推荐外接 KTV App 录音

## 9. 与其它 Skill 协作

- 共享 lyrics-db，难度评分逻辑可与 SK2 mayday-chords 的升 key 分析互通
- SK6 concert-prep 可用本 Skill 给"必唱曲"打难度标签
- SK9 mayday-radio 可在「演唱会倒计时」节目中调用本 Skill 给听众小练习

## 10. 难度评分草案

```
difficulty = 0.4 × normalize(highest_note)
           + 0.2 × normalize(bpm)
           + 0.2 × (key_change_count > 0 ? 1 : 0)
           + 0.2 × normalize(continuous_singing_seconds)
           ∈ [0, 10]
```

| 分数 | 标签 |
|------|------|
| 0–3 | 入门  |
| 4–6 | 进阶  |
| 7–8 | 困难  |
| 9–10 | 唯神能唱 |