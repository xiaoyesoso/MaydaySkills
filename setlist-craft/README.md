# Setlist Craft · 私人定制五月天 Setlist

让用户自己当艺术总监，按情绪曲线 + 必选 / 必避约束，从五月天曲库编出一份个人定制版 Setlist。

## 适用场景

- 生日趴、婚礼、纪念日
- 个人仪式、人生告别巡演
- 任何需要"属于我的五月天"的场合

## 快速使用

```bash
# 默认预置曲线（平到嗨，20 首）
python scripts/build-setlist.py --occasion "生日趴" --count 20 --curve "平到嗨"

# 必选 + 必避 + 高能上限
python scripts/build-setlist.py \
  --occasion "爷爷生日" \
  --count 10 \
  --curve "抒情之夜" \
  --include 知足,温柔,突然好想你 \
  --exclude 轧车,派对动物,爆肝 \
  --max-high 1

# 自定义情绪曲线（E1,V1,E2,V2,...）
python scripts/build-setlist.py \
  --occasion "纪念日" \
  --count 10 \
  --custom-curve 5,7,8,8,7,5,4,3,5,7 \
  --include 突然好想你,OAOA
```

## 输入字段

| 字段 | 必填 | 说明 |
|------|------|------|
| `occasion` | ✅ | 用途场景（生日 / 婚礼 / 个人仪式…） |
| `count` | ✅ | 期望曲目数 |
| `curve` | ⏸️ | 预置曲线名（`平到嗨` / `抒情之夜` / `情绪过山车` / `治愈wave` / `巡演级`） |
| `custom_curve` | ⏸️ | 自定义 E/V 数组，逗号分隔 |
| `include` | ⏸️ | 必选曲列表，逗号分隔 |
| `exclude` | ⏸️ | 必避曲列表，逗号分隔 |
| `max_high` | ⏸️ | 高能曲（E≥8）上限 |

## 预置曲线

| 名称 | E 曲线 | V 曲线 | 适用 |
|------|--------|--------|------|
| `平到嗨` | 4→6→8→9 | 5→6→7→8 | 派对 / 倒计时 |
| `抒情之夜` | 3→4→3→2 | 5→6→7→6 | 安静晚宴 |
| `情绪过山车` | 5→8→3→9→5 | 6→8→2→8→7 | 个人仪式 |
| `治愈wave` | 7→4→2→4→7 | 4→3→5→7→8 | 失恋恢复期 |
| `巡演级` | 6→9→7→9→5 | 7→8→6→9→7 | 真实演唱会逻辑 |

## 输出示例

```json
{
  "setlist_name": "生日趴 Setlist",
  "occasion": "生日趴",
  "track_count": 20,
  "total_duration_seconds": 5040,
  "total_duration_minutes": 84,
  "mood_curve": [
    {"slot": 1, "target_E": 4, "target_V": 5},
    ...
  ],
  "tracks": [
    {
      "slot": 1,
      "title": "知足",
      "album": "知足",
      "energy": 2,
      "valence": 6,
      "duration_seconds": 225,
      "why": "平静开场，V 温和收口"
    },
    ...
  ],
  "encore_candidates": ["OAOA", "拥抱", "笑忘歌"]
}
```

## 依赖

- `references/curve-presets.json`（5 个预置情绪曲线）
- `references/lyrics-db/`（通过 `scripts/sync-lyrics-db.sh` 同步）
- Python 3.12+（stdlib only）

## 关联 Skill

- **SK4 mayday-mood** — 评分公式来源
- **SK6 concert-prep** — 区别：预测官方 vs 自排
- **SK9 mayday-radio** — 一键转 radio 节目
