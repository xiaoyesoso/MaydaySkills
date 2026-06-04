# mayday-mood · 五月天歌词情绪数据库

> 用「能量 / 极性 / 主题」三轴标注五月天歌曲，根据你的心情推荐最合适的歌单。

## 这个 Skill 能做什么

- 给定一句心情描述，返回 3-5 首贴合心境的五月天歌曲。
- 输出每首歌的：能量分（0-10）、极性分（0-10）、主题标签、锚句、推荐理由。
- 支持「活动序列歌单」：例如「通勤 → 上班 → 午休 → 下班 → 夜跑」生成 5 首过渡顺序合理的歌单。

## 适合什么场景

- 失恋 / 加班崩溃 / 备考 / 毕业 / 通勤 等具体情境的选歌。
- 不知道想听什么，只想说「现在心情很复杂」。
- 制作主题歌单（婚礼前奏、求婚、生日趴等）。

## 怎么触发我

| 中文 | English |
|------|---------|
| 推荐心情对应的五月天 | recommend mayday by mood |
| 失恋听什么 | what mayday song fits sadness |
| 帮我做歌单 | make me a playlist |

## 目录结构

```
mayday-mood/
├── SKILL.md
├── README.md
└── references/
    ├── mood-taxonomy.md              # 三轴情绪分类体系与关键词词典
    └── lyrics-db/                    # 含 mood 标签的歌词库
```

## 三轴情绪模型

| 轴 | 范围 | 含义 |
|----|------|------|
| Energy 能量 | 0-10 | 听感与编曲强度 |
| Valence 极性 | 0-10 | 正向 / 负向情绪 |
| Theme 主题 | 枚举 | love / friendship / dream-chasing / loss / nostalgia / rebellion / growth / celebration |

完整评分规则见 `references/mood-taxonomy.md`。

## 注意事项

- ⚠️ 推荐基于 `lyrics-db` 中已标注的歌曲；样本数据需逐步扩充。
- ⚠️ 仅输出锚句（一两句），不输出歌词全文。
- ⚠️ 当用户描述模糊时，会主动追问一句而不是猜。
