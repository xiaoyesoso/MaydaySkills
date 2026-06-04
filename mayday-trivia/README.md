# mayday-trivia · 五月天 Trivia Master

> 回答关于五月天 1997 年至今全部历史的事实性问题，支持 10 题挑战赛模式。

## 这个 Skill 能做什么

- **直答模式**：回答关于成员、专辑、演唱会、MV、奖项、合作等任何事实问题。
- **挑战赛模式**：从题库随机抽 10 题，按难度（easy / medium / hard / nightmare）计分。
- **结果评级**：10/10 → 第五位团员；7-9 → 资深五迷；4-6 → 路人粉；0-3 → 还不快去听歌。

## 适合什么场景

- 五迷聚会比拼冷知识。
- 写五月天相关稿件 / PPT / 推文需要事实核对。
- 想系统了解乐队历史。

## 怎么触发我

| 中文 | English |
|------|---------|
| 阿信几岁 / 怪兽生日 | when is monster's birthday |
| 倔强收录在哪张专辑 | which album is 倔强 in |
| 考考我 / 出题 / 挑战 | quiz me / trivia |

## 目录结构

```
mayday-trivia/
├── SKILL.md
├── README.md
└── references/
    ├── trivia-db.json                # 题库（id / domain / difficulty / Q / A / source）
    └── knowledge-base/               # 事实核对底稿
        ├── band-members.md
        ├── album-history.md
        ├── concert-archives.md
        └── timeline.md
```

## 题库格式

```json
{
  "id": "Q001",
  "domain": "members",
  "difficulty": "easy",
  "question": "...",
  "answer": "...",
  "accepted_variants": ["..."],
  "source": "references/knowledge-base/...",
  "background": "..."
}
```

## 注意事项

- ⚠️ 当前题库 8 题为示例；目标产线 500+ 题。
- ⚠️ 模糊问题会主动反问，不会随便猜。
- ⚠️ 数据库未覆盖的近期事件会走外部搜索并明确标注。
