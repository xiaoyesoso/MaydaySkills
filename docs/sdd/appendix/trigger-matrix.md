# 附录 · 触发词矩阵

> 隶属：[Mayday Skills SDD](../README.md)
> 用途：为每个 Skill 列出推荐的中英文触发关键词，供 SKILL.md `description` 字段调优时参考。

## v1.0 既有 8 个 Skill

| Skill | 中文触发词 | 英文触发词 |
|-------|-----------|-----------|
| SK1 ashin-lyrics | 写歌词、模仿阿信、五月天风格写词、原创歌词 | write mayday lyrics, ashin style lyrics, original chinese lyric |
| SK2 mayday-chords | 和弦、吉他谱、怪兽编曲、升 key、和声分析 | mayday chords, guitar tab, key change, arrangement analysis |
| SK3 mayday-trivia | 冷知识、问答、考考我、五月天历史、阿信生日 | mayday trivia, quiz, facts, behind the scenes |
| SK4 mayday-mood | 心情、适合、歌单、推荐、失恋听什么、加班崩溃听啥 | mood, playlist, recommend, feeling, breakup song |
| SK5 chat-ashin | 阿信说、如果阿信、和阿信聊天、阿信会怎么劝 | chat ashin, what would ashin say, ashin advice |
| SK6 concert-prep | 演唱会、备战、setlist、安可、场馆、应援 | concert, setlist, encore, venue, fan chant |
| SK7 mayday-quotes | 金句、朋友圈、文案、辞职信、毕业感言 | quote, social post, copywriting, life moment |
| SK8 mayday-data | 数据、趋势、销量、统计、Spotify、YouTube | data, trends, statistics, charts, streaming numbers |

## v1.1 新增 5 个 Skill

| Skill | 中文触发词 | 英文触发词 |
|-------|-----------|-----------|
| SK9 mayday-radio | 电台、广播、DJ、节目、陪我加班、失恋电台 | radio, DJ program, late-night, breakup station |
| SK10 mayday-karaoke | KTV、K 歌、练唱、副歌破音、音域、唱不上去 | karaoke, vocal coaching, pitch range, practice |
| SK11 mayday-fanfic | 同人、短篇、AU、五月天宇宙、二创、虚构故事 | fanfic, fan fiction, AU, alternate universe |
| SK12 setlist-craft | 自定义 setlist、演唱会曲单、生日歌单、情绪曲线 | custom setlist, concert order, mood curve |
| SK13 mayday-dictionary | 五迷术语、黑话、典故、彩蛋、每日一词 | mayday slang, lingo, lore, easter egg, daily term |

## 设计原则

1. **覆盖率优先**：每个 Skill 至少 5 个中文 + 3 个英文触发词，覆盖该 Skill 的典型使用场景
2. **避免冲突**：相近 Skill 用不同关键词分开（如 SK6 用"演唱会预测"，SK12 用"自定义 setlist"）
3. **避免泛词**：不要单独使用「五月天」这种泛词作触发，必须组合上下文动词或场景
4. **双语并列**：保证英语助手也能正确识别意图