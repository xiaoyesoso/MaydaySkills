# mayday-chords · 五月天和弦秘籍

> 拆解怪兽的编曲哲学 — 和弦进行、结构搭建、升 key 范式。

## 这个 Skill 能做什么

1. **和弦查询** — 输入歌名，输出主歌 / 副歌 / Bridge 的和弦谱（标准记号 + 罗马数字分析）。
2. **模式挖掘** — 找出五月天高频使用的进行（如 I-V-vi-IV 的多种变体）。
3. **升 Key 分析** — 解析爆发段落的转调逻辑（《倔强》全音升 key、《你不是真正的快乐》半音上行等）。
4. **学习路线图** — 根据你的水平推荐 3 步练习曲序。

## 适合什么场景

- 想练一首五月天但找不到合适的谱。
- 学吉他 / 钢琴想理解为什么这些和弦组合好听。
- 自己写歌想抄怪兽的「公式」。

## 怎么触发我

| 中文 | English |
|------|---------|
| 倔强和弦 | 倔强 chords |
| 五月天吉他谱 | mayday guitar tabs |
| 升 key 怎么做 | how does mayday do key changes |

## 目录结构

```
mayday-chords/
├── SKILL.md
├── README.md
├── references/
│   └── chord-patterns.md             # 高频进行 + 升 key 范式 + 编曲特征
└── scripts/
    └── chord-diagram.py              # ASCII 和弦图打印 CLI
```

## 脚本用法

```bash
python scripts/chord-diagram.py Am
python scripts/chord-diagram.py "F#m"
```

## 难度分级

- **入门**：温柔、知足、拥抱（仅 4 和弦循环）
- **中级**：突然好想你、后来的我们、倔强（加七和弦 / 转位）
- **进阶**：你不是真正的快乐、顽固、入阵曲（升 key / 复杂副属）

## 注意事项

- ⚠️ 谱不附歌词全文 — 仅做教学分析。
- ⚠️ 多种 voicing 会优先选 Live 常用版本，并附备选。
- ⚠️ 不会为不熟悉的歌曲编造和弦 — 会主动请你提供录音或歌词。
