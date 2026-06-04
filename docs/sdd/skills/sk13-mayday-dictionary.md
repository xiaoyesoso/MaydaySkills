# SK13 · mayday-dictionary

> 隶属：[Mayday Skills SDD](../README.md) · 状态：⏳ v1.1 规划中 · 优先级 P2
> 计划实现位置：`/mayday-dictionary/`

## 1. 一句话定义

五迷黑话/术语/典故/彩蛋的语义词典：可查可解释，也可"每日一词"科普。

## 2. 用户故事

- 「五迷术语『升 key 战神』什么意思」
- 「『拥抱』在五迷文化里有什么特殊含义」
- 「OAOA 到底唱的是啥」
- 「今天教我一个新的五迷术语」

## 3. SKILL.md 关键字段

| 字段 | 内容 |
|------|------|
| `name` | `mayday-dictionary` |
| `category` | `knowledge-qa` |
| `compatibility` | No external dependencies |

## 4. 输入

| 字段 | 必填 | 说明 |
|------|------|------|
| term | ☑️ | 查询的词条 |
| mode | ⏸️ | `lookup` / `daily` / `search` / `random` |

## 5. 输出

### Lookup
```
📚 升 key 战神
分类：演唱会术语
释义：能在阿信副歌升 key 之后仍稳稳跟唱到底的五迷
出处：常用于《倔强》《突然好想你》后段副歌升 key 时
相关：升 key / 副歌升 / A→B
近义：高音 KO / 副歌之神
例句：「她副歌完没破音，是升 key 战神」
```

### Daily（每日一词）
- 随机 1 个 + 详细解读 + 1 个真实使用场景

### Search（模糊搜索）
- 输入「升」→ 返回 升 key / 升 key 战神 / 升 key 段位 / …

## 6. 数据依赖

- `references/dictionary.json`（核心：~200 词条）
- `references/knowledge-base/`（用于交叉验证术语相关的历史事件）

## 7. 词条结构（dictionary.json 草案）

```json
{
  "id": "term-001",
  "term": "升 key 战神",
  "aliases": ["升key战神", "高音KO"],
  "category": "concert-slang",
  "definition": "能在副歌升 key 之后仍稳稳跟唱到底的五迷",
  "origin": "源自《倔强》《突然好想你》副歌升 key 现象",
  "examples": [
    "她副歌完没破音，是升 key 战神"
  ],
  "related": ["term-002", "term-005"],
  "tags": ["concert", "fan-culture"]
}
```

## 8. 词条分类（计划）

| 类目 | 示例 |
|------|------|
| concert-slang | 升 key 战神、安可拳头、灯海蓝 |
| song-easter-egg | T1213121 的真正含义、转眼 MV 的递归镜头 |
| band-nickname | 信哥、温团、石老师、玛大学、佑哥 |
| timeline-event | 168 场、复出之夜、鸟巢首唱、人无 4 周年 |
| meme | 平凡很伟大、为爱而生、我们都有觉悟要疯狂到日出 |
| era-tag | 滚石时期 / 相信音乐时期 / 五人合体期 |

## 9. 流程

### Lookup
1. 接受 term
2. 在 dictionary.json 精确匹配 → 否则触发模糊搜索 → 列出候选请用户挑

### Daily
1. 当日哈希取一个稳定的随机词条
2. 输出完整释义 + 例句

### Random / Search
- 直接走 dictionary.json 的索引

## 10. Edge Cases

- 用户输入半个词 → 模糊搜索给候选
- 词条不存在 → 提示「未收录，要不要联网查」+ 引导用户贡献
- 多义词 → 列出不同义项，问用户哪一个

## 11. 与其它 Skill 协作

- 与 SK3 trivia 互补：trivia 出"题"，dictionary 提供"答"背后的术语注释
- 与 SK11 fanfic：写作时遇到术语 → 调用 dictionary 确保用法准确
- 与 SK6 concert-prep：演唱会备战时插入"今天值得知道的演唱会黑话"
- 与 SK5 chat-ashin：聊到术语时引用词典作信息源