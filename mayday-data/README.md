# mayday-data · Mayday 音乐数据面板

> 用图表呈现五月天的数据 — 销量、串流、演唱会、搜寻热度。

## 这个 Skill 能做什么

1. **专辑表现时间线** — 选择指标（streaming / sales / awards），按时间轴出图。
2. **演唱会热力图** — 按城市统计场次与估计入场人数。
3. **单曲热度趋势** — 输入一首或多首歌，给出多年搜寻 / 串流时间序列对比。
4. **时代对比** — 给两个时间区间，并排显示销量、巡演、奖项、歌词主题分布。

## 适合什么场景

- 媒体 / 内容创作者需要数据图。
- 五迷想看自己喜欢的歌「火过几次」。
- 研究华语流行音乐发展。

## 怎么触发我

| 中文 | English |
|------|---------|
| 五月天数据 | mayday data |
| 帮我画专辑销量趋势 | plot album sales trend |
| 倔强这首歌的搜索趋势 | search trend of 倔强 |

## 目录结构

```
mayday-data/
├── SKILL.md
├── README.md
└── scripts/
    └── data-fetcher.py               # 多源数据采集 CLI（输出 JSON）
```

## 脚本用法

```bash
python scripts/data-fetcher.py album-trend
python scripts/data-fetcher.py concert-map
python scripts/data-fetcher.py song-trend 倔强 突然好想你
python scripts/data-fetcher.py era-compare 2004 2008 2016 2020
```

## 状态

- 当前 `data-fetcher.py` 为脚手架实现，所有子命令返回结构稳定的 stub JSON。
- 生产化前需要：接入 Spotify / YouTube / KKBOX / Wikipedia 等真实 API，并加入 `~/.cache/mayday-data/` 缓存。

## 注意事项

- ⚠️ API 限流：脚本未来需缓存，并对外提示数据时间戳。
- ⚠️ 缺失数据：永不伪造，缺口用空值标记。
- ⚠️ 多源冲突：取范围并标注每个来源。
