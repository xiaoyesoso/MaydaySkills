## Context

mayday-radio 是第 9 个 Skill，定位为「沉浸陪伴」。它消费 lyrics-db（120 首/9 专辑）和 mood-taxonomy.md 中的三轴匹配公式，输出一档完整的文本格式电台节目脚本。

已有资产：
- lyrics-db（主源在 mayday-mood/references/lyrics-db/）
- mood-taxonomy.md（定义 E/V/Themes 三轴与评分公式）
- sync-lyrics-db.sh（同步机制已验证）

## Goals / Non-Goals

**Goals:**
- 实现完整的 mayday-radio Skill（SKILL.md + references + scripts）
- 支持输入 theme + duration → 输出完整节目脚本（含 DJ 串场）
- 4 个内置节目模板覆盖失恋治愈 / 通勤励志 / 深夜疗愈 / 演唱会倒计时
- 支持 skip_songs 和自定义 mood arc

**Non-Goals:**
- 不做 TTS 音频渲染（纯文本输出）
- 不做实时流媒体播放
- 不修改 mayday-mood 的代码或 spec

## Decisions

### D1: build-program.py 用 Python stdlib 实现
与 data-fetcher.py 保持一致：stdlib-only HTTP，无第三方依赖，6h 磁盘缓存。虽然本 Skill 不调外部 API，但保持风格统一。

### D2: DJ 串场文本在 SKILL.md 指令中生成，不在脚本中硬编码
build-program.py 只负责曲目编排（输出 JSON：曲目列表 + 时间戳 + 每段目标 E/V），DJ 串场文本由 LLM 按 dj-voice.md 指南实时生成。这样 DJ 文本更自然，且避免脚本膨胀。

### D3: mood 匹配公式直接内嵌到 build-program.py
不跨目录 import mayday-mood，而是在 build-program.py 中重新实现 `score = -sqrt(ΔE²+ΔV²) + 2·|theme_overlap|`，保持 Skill 自包含。

## Risks / Trade-offs

- **[节目时长估算不准]** → 歌曲实际时长未入库（lyrics-db 无 duration_seconds），用 BPM × 经验系数估算。缓解：在 lyrics-db schema 中标注 duration 为已知限制。
- **[DJ 文本质量依赖 LLM]** → 低质量 prompt 可能产出千篇一律的串场。缓解：dj-voice.md 提供多样化范例和"避免"清单。
- **[mood 公式重复实现]** → 如果公式未来修改，需同步两处。缓解：在两处代码注释中互相引用源文件。
