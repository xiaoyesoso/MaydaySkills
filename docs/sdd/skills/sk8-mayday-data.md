# SK8 · mayday-data

> 隶属：[Mayday Skills SDD](../README.md) · Skill 状态：✅ v1.0 / Phase 4 已接入 Spotify + YouTube API
> 实现位置：[`/mayday-data/`](../../../mayday-data/)

## 1. 一句话定义

把五月天的销量 / 串流 / 演唱会数据，做成可读的图表与对比分析。

## 2. 用户故事

- 「五月天哪张专辑串流最高」
- 「《突然好想你》在 YouTube 上的播放量」
- 「比较一下 2004-2008 vs 2016-2020 这两段时期」

## 3. SKILL.md 关键字段

| 字段 | 内容 |
|------|------|
| `name` | `mayday-data` |
| `category` | `data-visualization` |
| `compatibility` | Python 3.12+ stdlib only; charting needs matplotlib in consumer env; SPOTIFY_CLIENT_ID/SECRET + YOUTUBE_API_KEY for live data |

## 4. 输入

| 字段 | 必填 | 说明 |
|------|------|------|
| view | ✅ | `album-trend` / `concert-map` / `song-trend` / `era-compare` / `spotify-popularity` / `youtube-views` |
| params | ⏸️ | view 对应参数 |

## 5. 输出

- 结构化 JSON（stdout）
- `_meta.source` 标记：`stub` / `spotify` / `spotify-cache` / `youtube` / `youtube-cache`
- 由上层渲染层画图

## 6. 数据依赖

- `scripts/data-fetcher.py`（stdlib HTTP，6h 磁盘缓存）

## 7. 流程

1. 选 view + 参数
2. 调用 `python scripts/data-fetcher.py <view> [args]`
3. 解析 JSON
4. 渲染图表
5. 给一段文字解读

## 8. Edge Cases

- API rate limit → 优先用缓存，警告 "stale data"
- 缺失数据 → 明确标记空缺，绝不编造
- 多源冲突 → 显示范围 + cite 每个来源
- 无外网 → 用 stub fallback；输出依旧可渲染

## 9. 与其它 Skill 协作

- 未来 SK9 mayday-radio 可消费 YouTube 高播放数据来决定"开场曲"
- SK12 setlist-craft 可消费 Spotify popularity 帮用户避开"冷门曲"