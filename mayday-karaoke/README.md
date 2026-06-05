# Mayday Karaoke · K 歌教练

教你怎么唱每一首五月天：难度评分、高音/换气标注、N 天练唱计划。

## 功能

- **曲目指导**：给出难度评分 + 分段标注（🔴高音 / 🟡转音 / 💨换气点 / 🎯升key）
- **按音域推荐**：根据你的音域筛选可唱曲目
- **练习计划**：N 天 day-by-day 计划，每天 30 分钟

## 使用

```bash
# 曲目指导
python scripts/score-pitch.py --song 倔强

# 按音域推荐
python scripts/score-pitch.py --range C3:G4

# 练习计划
python scripts/score-pitch.py --song 倔强 --plan 30
```

## 依赖

- lyrics-db（通过 sync 脚本同步）
- Python 3.12+（stdlib only）
