# 附录 · 变更记录

> 隶属：[Mayday Skills SDD](../README.md)
> Semantic Versioning

## v1.1 — 2026-06-04

### Added
- SDD 文档从单文件 `mayday-skills-sdd.md` 拆分为 `docs/sdd/` 文档集
- 新增 5 个 Skill 的 SDD 规划：
  - SK9 [mayday-radio](../skills/sk9-mayday-radio.md) — AI 电台节目编排
  - SK10 [mayday-karaoke](../skills/sk10-mayday-karaoke.md) — K 歌教练
  - SK11 [mayday-fanfic](../skills/sk11-mayday-fanfic.md) — 同人短篇
  - SK12 [setlist-craft](../skills/sk12-setlist-craft.md) — 自定义 Setlist
  - SK13 [mayday-dictionary](../skills/sk13-mayday-dictionary.md) — 五迷词典
- Roadmap 新增 Phase 6/7/8/9
- 新增 [`appendix/trigger-matrix.md`](trigger-matrix.md)

### Changed
- 原 `mayday-skills-sdd.md` 归档到 [`archive/v1.0.md`](../archive/v1.0.md)
- 根 README 中的 SDD 链接从 `mayday-skills-sdd.md` → `docs/sdd/`

### Deprecated
- 无

### Removed
- 无（原文件保留，仅迁移路径）

## v1.0.1 — 2026-06-04（Phase 4 数据扩充）

### Added
- 9 张录音室专辑 / 120 首歌曲的 lyrics-db 元数据
- 762 题题库（trivia-db.json），由 `scripts/gen-trivia.py` 生成
- Spotify Web API + YouTube Data API 接入（`mayday-data/scripts/data-fetcher.py`）
- `scripts/sync-lyrics-db.sh` 多 skill 数据同步

### Changed
- `mayday-data` `compatibility` 字段从 "requires matplotlib+requests" 改为 "stdlib only"

## v1.0 — 2026-06-04

### Added
- 初稿：8 个 Skill 的 SDD 规格（单文件）
- Phase 0–3 全部脚手架交付