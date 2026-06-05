# Mayday Dictionary · 五迷黑话 / 术语 / 典故词典

可查可解释的五迷文化词典：覆盖演唱会术语、歌曲彩蛋、乐队昵称、时代事件、Meme、年代标签。

## 快速使用

```bash
# 精确查询
python scripts/lookup.py --term "升 key 战神"

# 模糊搜索
python scripts/lookup.py --mode search --query "升"

# 每日一词（按日期稳定）
python scripts/lookup.py --mode daily

# 完全随机
python scripts/lookup.py --mode random

# 按分类列出
python scripts/lookup.py --mode list --category concert-slang
```

## 词条分类

| 类目 | 示例 |
|------|------|
| `concert-slang` | 升 key 战神、安可拳头、灯海蓝、点歌、纸飞机 |
| `song-easter-egg` | T1213121 的真正含义、转眼 MV 的递归镜头、突然好想你的副歌升 key |
| `band-nickname` | 信哥、温团（怪兽）、石老师（石头）、玛大学（玛莎）、佑哥（冠佑） |
| `timeline-event` | 168 场、复出之夜、鸟巢首唱、人无 4 周年、五月天 25 周年 |
| `meme` | 平凡很伟大、为爱而生、我们都有觉悟要疯狂到日出、自传 |
| `era-tag` | 滚石时期、相信音乐时期、五人合体期、复出演唱会期 |

## 词条结构

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

## 4 种模式

### 1. Lookup（精确查询）
输入完整 term，输出分类、释义、出处、相关词、例句。

### 2. Daily（每日一词）
按日期哈希取一个稳定的随机词条，每天不重复。

### 3. Search（模糊搜索）
输入关键字，返回所有匹配的词条列表。

### 4. Random（随机推荐）
完全随机一词。

## 输出示例

```bash
$ python scripts/lookup.py --term "升 key 战神"
```

```json
{
  "found": true,
  "term": {
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
}
```

## 依赖

- `references/dictionary.json`（核心词条库）
- `references/lyrics-db/`（通过 `scripts/sync-lyrics-db.sh` 同步，用于交叉验证）
- Python 3.12+（stdlib only）

## 关联 Skill

- **SK3 trivia** — 出题，dictionary 提供术语注释
- **SK5 chat-ashin** — 聊术语时引用作信息源
- **SK6 concert-prep** — 演唱会备战插入"今日黑话"
- **SK11 fanfic** — 写作时确保术语用法准确
