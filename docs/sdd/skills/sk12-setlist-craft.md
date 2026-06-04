# SK12 · setlist-craft

> 隶属：[Mayday Skills SDD](../README.md) · 状态：⏳ v1.1 规划中 · 优先级 P2
> 计划实现位置：`/setlist-craft/`

## 1. 一句话定义

让用户**自己当艺术总监**，按情绪曲线 + 必选 / 必避约束，编出一份个人定制版五月天 Setlist。

## 2. 用户故事

- 「帮我编一份生日趴用的五月天 setlist，20 首，要从平静嗨到爆」
- 「给爷爷生日做一份温柔向 setlist，避开重摇滚」
- 「自我和解之后写一份属于我的人生告别巡演 setlist」
- 「跟伴侣的纪念日，10 首歌从甜到酸到甜」

## 3. SKILL.md 关键字段

| 字段 | 内容 |
|------|------|
| `name` | `setlist-craft` |
| `category` | `event-planning` |
| `compatibility` | No external dependencies; optional PDF export needs reportlab |

## 4. 输入

| 字段 | 必填 | 说明 |
|------|------|------|
| occasion | ✅ | 用途场景（生日 / 婚礼 / 个人仪式 …）|
| song_count | ✅ | 期望曲目数 |
| mood_curve | ⏸️ | 自定义情绪曲线（如 `[5,6,8,9,7,5]`）或选预置 |
| must_include | ⏸️ | 必选曲列表 |
| must_exclude | ⏸️ | 必避曲列表 |
| max_high_energy | ⏸️ | 高能曲上限（避免太累）|

## 5. 输出

```
🎤 [用户取名] Setlist — 共 X 首 / 约 Y 分钟
━━━━━━━━━━━━━━━━━

01. 《[曲名]》  E5/V6  ⏱ 4:30
02. 《[曲名]》  E6/V7  ⏱ 4:00
…
20. 《[曲名]》  E8/V9  ⏱ 5:10

📈 情绪曲线：    
   E ▇▇▇▇▇▇▇▇▇▇                                                
                ▇▇▇▇▇▇▇▇▇                                              
   ▇▇▇▇▇▇                                                         

🎁 Encore（备选）：《[曲名]》《[曲名]》
```

可选导出为 PDF 卡片（`scripts/render-pdf.py`）。

## 6. 数据依赖

- `references/lyrics-db/`（取 E/V/themes/duration）
- `references/curve-presets.json`（预置情绪曲线模板）
- `scripts/build-setlist.py`（约束求解：满足 must_include / exclude / curve 的最优组合）

## 7. 流程

1. 询问 occasion + song_count
2. 提供 5 个预置曲线供选，或允许自定义
3. 用 `build-setlist.py` 执行：
   - 按 curve 把每个时间槽位的目标 E/V 算出来
   - 在 lyrics-db 中按相似度填入候选
   - 检查约束（必选/必避/总时长/重复艺人合作）
   - 输出最优解
4. 渲染 ASCII 情绪曲线
5. 询问是否导出 PDF

## 8. Edge Cases

- 必选曲目情绪与目标曲线冲突 → 提示用户：「锁定的曲会让 step3 不平滑，是否调整」
- 曲目池被过滤到 < song_count → 警告并询问放宽哪个约束
- 用户编完想换 1 首 → 提供 `swap N "新曲"` 的微调命令

## 9. 与其它 Skill 协作

- 与 SK6 concert-prep 区别：concert-prep 是"预测官方曲单"，setlist-craft 是"自己排自己的"
- 与 SK4 mood：mood 的 E/V/theme 是 setlist-craft 的核心输入
- 与 SK8 data：可选用 Spotify popularity 加权，避免全是冷门
- 与 SK9 radio：编完的 setlist 可一键转 radio 节目（加上 DJ 串场）

## 10. 预置曲线（curve-presets.json 草案）

| 名称 | E 曲线 | V 曲线 | 适用 |
|------|--------|--------|------|
| 平到嗨 | 4→6→8→9 | 5→6→7→8 | 派对 / 倒计时 |
| 抒情之夜 | 3→4→3→2 | 5→6→7→6 | 安静晚宴 |
| 情绪过山车 | 5→8→3→9→5 | 6→8→2→8→7 | 个人仪式 |
| 治愈 wave | 7→4→2→4→7 | 4→3→5→7→8 | 失恋恢复期 |
| 巡演级 | 6→9→7→9→5 | 7→8→6→9→7 | 真实演唱会逻辑 |