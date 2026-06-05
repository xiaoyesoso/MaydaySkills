## Why

SK9 mayday-radio 是 Phase 6 的核心交付。当前 SK4 mayday-mood 只推荐歌单，不提供沉浸式电台体验。用户在通勤、加班、失眠等场景需要的不只是歌曲列表，而是一档有 DJ 串场、情绪编排和开场/收尾的完整广播节目。

## What Changes

- 新增 `mayday-radio/` Skill 目录（SKILL.md + README.md）
- 新增 `references/dj-voice.md`（DJ 语调指南）
- 新增 `references/program-templates.json`（4 个内置节目模板）
- 新增 `scripts/build-program.py`（节目编排引擎）
- 同步 lyrics-db 到 mayday-radio
- 更新 sync-lyrics-db.sh 添加 mayday-radio 到 TARGETS

## Capabilities

### New Capabilities
- `mayday-radio`: SK9 AI 电台 DJ — 按主题/时长/心情编排完整的五月天主题广播节目

### Modified Capabilities
- `mayday-mood`: 无 spec 变更，但 build-program.py 运行时复用其 mood 匹配公式

## Impact

- 新目录 `mayday-radio/`（约 8 个文件）
- `scripts/sync-lyrics-db.sh` TARGETS 数组增加 1 项
- 无破坏性变更，不影响现有 SK1–SK8
