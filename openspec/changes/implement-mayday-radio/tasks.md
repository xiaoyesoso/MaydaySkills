## 1. Skill 脚手架

- [ ] 1.1 创建 `mayday-radio/` 目录结构
- [ ] 1.2 编写 `mayday-radio/SKILL.md`（name: mayday-radio, category: immersive-companion, 含完整 Instruction Flow）
- [ ] 1.3 编写 `mayday-radio/README.md` 中文说明

## 2. 参考资源

- [ ] 2.1 编写 `references/dj-voice.md`（DJ 语调指南：warm/philosophical/playful/nostalgic 四种风格定义 + 范例 + 避免清单）
- [ ] 2.2 编写 `references/program-templates.json`（4 个内置模板：失恋治愈/通勤励志/深夜疗愈/演唱会倒计时，每个含 target_duration/mood_arc/dj_style）
- [ ] 2.3 运行 `scripts/sync-lyrics-db.sh` 同步 lyrics-db 到 mayday-radio

## 3. 节目编排引擎

- [ ] 3.1 实现 `scripts/build-program.py`（输入：theme/duration/mood_arc/skip_songs → 输出：JSON 含曲目列表+时间戳+每段 E/V 目标）
- [ ] 3.2 内嵌 mood 匹配公式 `score = -sqrt(ΔE²+ΔV²) + 2·|theme_overlap|`
- [ ] 3.3 实现时长估算逻辑（BPM → 歌曲时长 ≈ verse_count × 30s + chorus_count × 25s）
- [ ] 3.4 实现 skip_songs 过滤
- [ ] 3.5 实现 mood arc 插值（给定 N 首、起始 E/V、终止 E/V → 每首目标 E/V）

## 4. 集成与同步

- [ ] 4.1 更新 `scripts/sync-lyrics-db.sh` TARGETS 添加 mayday-radio
- [ ] 4.2 端到端测试：输入 "30分钟失恋电台" → 输出完整脚本（含曲目 + DJ 串场占位）

## 5. 提交

- [ ] 5.1 Git commit 并推送到 origin/main
