## 1. OpenSpec Spec 迁移与同步

- [ ] 1.1 Archive 当前 change `mayday-skills-sdd` 以将 specs 同步到 `openspec/specs/`
- [ ] 1.2 验证 `openspec/specs/` 下 13 个 spec 目录已就位
- [ ] 1.3 在 `docs/sdd/README.md` 中添加 OpenSpec specs 的交叉链接
- [ ] 1.4 更新根 `AGENTS.md` 指向 `openspec/specs/` 作为 spec 来源

## 2. SK9 mayday-radio 实现（Phase 6）

- [ ] 2.1 创建 `mayday-radio/` 目录与 `SKILL.md`（name: mayday-radio, category: immersive-companion）
- [ ] 2.2 创建 `mayday-radio/README.md` 中文说明
- [ ] 2.3 编写 `references/dj-voice.md`（DJ 语调指南：warm / philosophical / playful / nostalgic）
- [ ] 2.4 编写 `references/program-templates.json`（4 个内置节目模板：失恋治愈 / 通勤励志 / 深夜疗愈 / 演唱会倒计时）
- [ ] 2.5 实现 `scripts/build-program.py`（输入：theme + duration + mood_arc → 输出：完整节目脚本 JSON）
- [ ] 2.6 运行 `scripts/sync-lyrics-db.sh` 同步 lyrics-db 到 mayday-radio
- [ ] 2.7 端到端测试：输入 "30分钟失恋电台" → 输出完整脚本（含曲目 + DJ 串场）

## 3. SK10 mayday-karaoke 实现（Phase 7 前半）

- [ ] 3.1 创建 `mayday-karaoke/` 目录与 `SKILL.md`（name: mayday-karaoke, category: vocal-coaching）
- [ ] 3.2 创建 `mayday-karaoke/README.md` 中文说明
- [ ] 3.3 编写 `references/karaoke-difficulty.json`（30 首重点曲目的手动校准难度数据）
- [ ] 3.4 实现 `scripts/score-pitch.py`（基于 lyrics-db 的 key/bpm/segments 计算难度评分 0–10）
- [ ] 3.5 实现曲目标注逻辑：🔴高音 / 🟡转音 / 💨换气点 / 🎯升key
- [ ] 3.6 实现按 vocal_range 过滤推荐逻辑
- [ ] 3.7 实现 N 天练习计划生成器
- [ ] 3.8 运行 sync-lyrics-db.sh 同步 lyrics-db
- [ ] 3.9 端到端测试：输入 "倔强 30天练唱计划" → 输出 day-by-day 计划

## 4. SK11 mayday-fanfic 实现（Phase 7 后半）

- [ ] 4.1 创建 `mayday-fanfic/` 目录与 `SKILL.md`（name: mayday-fanfic, category: creative-writing）
- [ ] 4.2 创建 `mayday-fanfic/README.md` 中文说明
- [ ] 4.3 编写 `references/fanfic-guidelines.md`（红线清单：禁止 R18 / 禁止丑化真人 / 禁止伪造引语 / 禁止完整歌词）
- [ ] 4.4 编写 `references/fanfic-templates.md`（5 个场景模板：初遇 / 兵役分别 / 鸟巢之夜 / 退役日常 / 大学 AU）
- [ ] 4.5 扩展 `references/persona/`：新增玛莎/怪兽/石头/冠佑 4 份人设文档
- [ ] 4.6 实现红线自检逻辑：输出前自动扫描 R18 关键词 / 完整歌词匹配 / 真人引语格式
- [ ] 4.7 实现创作声明自动追加
- [ ] 4.8 运行 sync-lyrics-db.sh 同步 lyrics-db
- [ ] 4.9 端到端测试：输入 "志明春娇重逢 800字" → 输出故事 + 声明

## 5. SK12 setlist-craft 实现（Phase 8 前半）

- [ ] 5.1 创建 `setlist-craft/` 目录与 `SKILL.md`（name: setlist-craft, category: event-planning）
- [ ] 5.2 创建 `setlist-craft/README.md` 中文说明
- [ ] 5.3 编写 `references/curve-presets.json`（5 个预置情绪曲线）
- [ ] 5.4 实现 `scripts/build-setlist.py`（约束求解器：must_include/exclude + curve + duration → 最优曲目序列）
- [ ] 5.5 实现 ASCII 情绪曲线可视化
- [ ] 5.6 实现 `scripts/render-pdf.py`（可选 PDF 导出，依赖 reportlab）
- [ ] 5.7 运行 sync-lyrics-db.sh 同步 lyrics-db
- [ ] 5.8 端到端测试：输入 "生日20首 平到嗨 必选干杯" → 输出 20 首曲单 + 情绪曲线

## 6. SK13 mayday-dictionary 实现（Phase 8 后半）

- [ ] 6.1 创建 `mayday-dictionary/` 目录与 `SKILL.md`（name: mayday-dictionary, category: knowledge-qa）
- [ ] 6.2 创建 `mayday-dictionary/README.md` 中文说明
- [ ] 6.3 编写 `references/dictionary.json`（200+ 词条，6 大分类，含 aliases/definition/origin/examples/related/tags）
- [ ] 6.4 实现精确匹配 + 模糊搜索逻辑
- [ ] 6.5 实现"每日一词"（日期哈希确定性随机选择）
- [ ] 6.6 端到端测试：输入 "升 key 战神" → 输出完整词条

## 7. 跨 Skill 同步与验证

- [ ] 7.1 更新 `scripts/sync-lyrics-db.sh` 添加 mayday-radio / mayday-karaoke / mayday-fanfic / setlist-craft 到 TARGETS
- [ ] 7.2 运行 `openspec validate mayday-skills-sdd` 验证所有 spec 合规
- [ ] 7.3 运行 `scripts/gen-trivia.py` 重新生成 trivia-db.json（确保新歌词数据已纳入题源）
- [ ] 7.4 更新根 README 的技能总览表（添加 SK9–SK13 链接指向实现目录）
- [ ] 7.5 更新 `docs/sdd/20-roadmap.md` 将 Phase 6–8 标记为进行中

## 8. 文档归档

- [ ] 8.1 将 `docs/sdd/skills/` 下 13 份手工 SDD 标记为 "已迁移到 openspec/specs/"
- [ ] 8.2 在 `docs/sdd/skills/` 各文件顶部加跳转链接到对应 openspec spec
- [ ] 8.3 最终 commit 并推送到 GitHub
