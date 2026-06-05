---
name: setlist-craft
description: >
  Craft a custom Mayday concert setlist by mood curve + must-include /
  must-exclude constraints. Use when the user wants to be their own artistic
  director — designing a setlist for a birthday, wedding, personal ritual,
  anniversary, or any occasion that needs a curated Mayday listening arc.
  Outputs an ordered track list with E/V tags, a duration estimate, an
  ASCII mood curve, and optional encore candidates.
license: MIT
metadata:
  author: mayday-skills
  version: "1.0"
  category: event-planning
compatibility: No external dependencies. Python 3.12+ for build-setlist.py (stdlib only). Optional PDF export needs reportlab.
---

# Setlist Craft — 私人定制五月天 Setlist

## Overview
让用户**自己当艺术总监**：按情绪曲线 + 必选 / 必避约束，从五月天曲库中
编出一份个人定制版 Setlist。可以是生日趴、婚礼、纪念日、个人仪式、人生
告别巡演——任何需要「属于我的五月天」的场景。

## Capabilities

### 1. 询问场景 & 收集约束
- **必填**：`occasion`、`song_count`
- **可选**：`mood_curve`（自定义数组 / 选预置）、`must_include`、`must_exclude`、`max_high_energy`

### 2. 预置情绪曲线
- 提供 5 个预置：`平到嗨` / `抒情之夜` / `情绪过山车` / `治愈wave` / `巡演级`
- 用户也可自定义 E/V 数组（如 `[5,6,8,9,7,5]`）

### 3. 编排求解
- 调用 `scripts/build-setlist.py`
  - 把 mood_curve 解析成 N 个时间槽位的目标 (E, V)
  - 在 lyrics-db 中按相似度填入候选
  - 检查约束：必选 / 必避 / 高能曲上限 / 不重复
  - 输出最优解

### 4. 渲染输出
- 编号曲目 + E/V 标签 + 时长
- ASCII 情绪曲线（E 柱状 / V 折线）
- Encore 备选（高契合度但未选入的 2-3 首）
- 可选 PDF 导出

## Instruction Flow

1. **询问 occasion + song_count**
   - 例子：「生日趴 20 首」「爷爷生日 10 首温柔向」
2. **选择曲线**：5 个预置任选一，或自定义数组
3. **询问约束**：
   - `must_include`：例如「必须有《倔强》」
   - `must_exclude`：例如「避开重摇滚」「不要《恋爱ing》」
   - `max_high_energy`：例如「高能曲最多 3 首」
4. **运行 build-setlist.py**：
   ```bash
   python scripts/build-setlist.py \
     --occasion "生日趴" \
     --count 20 \
     --curve "平到嗨" \
     --include 倔强,突然好想你 \
     --exclude 轧车,派对动物 \
     --max-high 3
   ```
5. **解析 JSON 输出**：
   - 渲染 ASCII 情绪曲线
   - 给出每首的「为什么选它」一句话解释
   - 标注 Encore 备选
6. **询问是否需要微调**：
   - `swap N "新曲"`：替换第 N 首
   - `regen`：重新求解（随机种子变化）
   - `export pdf`：导出 PDF 卡片

## Output Format
```
🎤 [用户取名] Setlist — 共 20 首 / 约 84 分钟
━━━━━━━━━━━━━━━━━

01. 《知足》              E2/V6  ⏱ 3:45   💭 平静开场
02. 《温柔》              E4/V5  ⏱ 4:10   💭 缓缓升温
…
20. 《倔强》              E9/V8  ⏱ 5:00   💭 锁定的必唱

📈 情绪曲线
   E ▇▇▇▇▇▇▇▇▇▇
                  ▇▇▇▇▇▇▇▇▇
   ▇▇▇▇▇
   V 5  6  7  8  7  6  5  4  6  8  9  7  5  6  7  8  8  7  6  7

🎁 Encore（备选）：《OAOA》《拥抱》《笑忘歌》
```

## Edge Cases
- **必选曲目情绪与曲线冲突** → 提示用户：「锁定的曲会让 step3 不平滑，是否调整」
- **曲目池被过滤到 < song_count** → 警告并询问放宽哪个约束
- **用户想换 1 首** → 提供 `swap N "新曲"` 微调命令
- **时长 > 120 分钟** → 询问是否要分成上下半场
- **重复艺人合作**（同一作曲人 / 编曲人）→ 警告但允许

## References
- `references/curve-presets.json` — 5 个预置情绪曲线模板
- `references/lyrics-db/` — 曲库元数据（由 `scripts/sync-lyrics-db.sh` 同步）

## Companion Skills
- **SK4 mayday-mood** — E/V/Theme 评分体系
- **SK6 concert-prep** — 区别：concert-prep 预测官方曲单，setlist-craft 自排
- **SK8 mayday-data** — 可叠加 popularity 加权
- **SK9 mayday-radio** — 编完的 setlist 可一键转 radio 节目
