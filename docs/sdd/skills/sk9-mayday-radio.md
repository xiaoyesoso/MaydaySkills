# SK9 · mayday-radio

> 隶属：[Mayday Skills SDD](../README.md) · 状态：⏳ v1.1 规划中 · 优先级 P0
> 计划实现位置：`/mayday-radio/`

## 1. 一句话定义

按用户指定的**主题 / 时长 / 心情**，自动编排一档完整的「五月天主题广播节目」，包含开场白、串场、曲目、结束语。

## 2. 用户故事

- 「给我做一档 30 分钟的失恋治愈电台」
- 「我今晚加班 2 小时，配一档励志五月天电台陪我」
- 「明天演唱会前夜，给我做一档复习电台 + DJ 念白」
- 「父亲生日，做一档我爸（五迷）听的怀旧电台」

## 3. SKILL.md 关键字段

| 字段 | 内容 |
|------|------|
| `name` | `mayday-radio` |
| `category` | `immersive-companion`（沉浸陪伴）|
| `compatibility` | No external dependencies; optional TTS pipeline for audio output |

## 4. 输入

| 字段 | 必填 | 说明 |
|------|------|------|
| theme | ✅ | 节目主题（失恋 / 通勤 / 演唱会前 / 怀旧 / 自定义）|
| duration_minutes | ✅ | 30 / 60 / 90 / 120 |
| mood_arc | ⏸️ | 情绪弧度（如「悲伤 → 治愈」），默认按 theme 智能选择 |
| dj_style | ⏸️ | `warm` / `philosophical` / `playful` / `nostalgic`（默认按 theme）|
| skip_songs | ⏸️ | 用户不想听的歌列表 |

## 5. 输出

完整节目脚本，包含：

```
🎙️ [节目名] · [时长]
━━━━━━━━━━━━━━━━━

[00:00] 开场白
  DJ：（旁白文本，~60-90 词）

[01:30] 🎵 《[曲名]》— [专辑] (X分Y秒)
  DJ 串场：（曲目导入背景，~30 词）

[XX:XX] 中场互动 / 转场
  DJ：（情绪转折前的过渡语）

[YY:YY] 🎵 《[最后一首]》
  DJ 收尾：（情绪收束 + 留念，~60-90 词）

📝 节目总览
  - 曲目数：6
  - 总时长：30 分钟
  - 情绪弧度：低-中-高-中（治愈型）
```

## 6. 数据依赖

- `references/lyrics-db/`（沿用同步机制）
- `references/program-templates.json` ← 4 个内置节目模板
- `references/dj-voice.md` ← DJ 语调指南
- 复用 SK4 mayday-mood 的匹配公式（直接调用而非重复实现）

## 7. 流程

1. 询问 theme + duration_minutes
2. 按 theme 加载模板（含目标情绪弧度、曲目数量范围）
3. 调用 mood 引擎，根据情绪弧度的每个段位筛选候选曲目
4. 用 `scripts/build-program.py` 组装时长 ≈ duration，每两首之间插入串场
5. 为开场白 / 串场 / 收尾分别生成文本（参考 dj-voice.md）
6. 输出完整脚本 + 总览统计

## 8. Edge Cases

- 时长超过 120 分钟 → 拆成 2 档节目
- 用户 skip_songs 导致候选不足 → 提示 "Pool 太小，建议解除某条限制"
- 全曲都不被用户喜欢 → 进入「探索模式」，推荐 1–2 首陌生曲目
- 没有指定 mood_arc → 按 theme 内置模板（失恋 = 低→中→治愈；演唱会前 = 中→高→爆发）

## 9. 与其它 Skill 协作

- 依赖 SK4 mood 匹配公式
- 与 SK7 quotes 互补：quotes 提供单句金句作开场词
- 与 SK8 data 联动：可选用 Spotify popularity 决定要不要冒险放冷门曲
- 输出脚本可进一步交给 TTS 系统（外部）渲染成真实音频

## 10. 内置模板（program-templates.json 草案）

| 模板 | 时长目标 | 情绪弧度 | 推荐主题词 |
|------|----------|----------|------------|
| 失恋治愈电台 | 30 / 60 | 低 → 中 → 治愈 | 突然好想你 / 后来的我们 / 倔强 / 笑忘歌 |
| 通勤励志早班 | 30 / 45 | 中 → 高 → 中 | 干杯 / 派对动物 / 倔强 / 时光机 |
| 深夜疗愈台 | 60 / 90 | 中 → 低 → 治愈 | 温柔 / 如烟 / 转眼 / 任意门 |
| 演唱会倒计时 | 60 / 90 | 中 → 高 → 爆发 | 离开地球表面 / 倔强 / OAOA / 诺亚方舟 |