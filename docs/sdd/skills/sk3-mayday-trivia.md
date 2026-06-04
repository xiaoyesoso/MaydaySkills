# SK3 · mayday-trivia

> 隶属：[Mayday Skills SDD](../README.md) · Skill 状态：✅ v1.0 / Phase 4 已扩充至 **762 题**
> 实现位置：[`/mayday-trivia/`](../../../mayday-trivia/)

## 1. 一句话定义

直答五月天 28 年历史的任意冷知识，并支持 10 题闯关 Quiz 模式。

## 2. 用户故事

- 「冠佑的本名是什么？」
- 「考考我，10 题中等难度」
- 「《倔强》是哪一年发的？什么背景？」

## 3. SKILL.md 关键字段

| 字段 | 内容 |
|------|------|
| `name` | `mayday-trivia` |
| `category` | `knowledge-qa` |
| `compatibility` | No external dependencies |

## 4. 输入

| 字段 | 必填 | 说明 |
|------|------|------|
| question | ✅ (Direct Q&A) | 自由文本 |
| difficulty | ✅ (Quiz) | easy / medium / hard / nightmare |

## 5. 输出

- Direct：简洁答案 + source 引用 + 背景故事 1–3 句
- Quiz：1 题/轮，10 轮总结评分 + 五月天主题等级

## 6. 数据依赖

- `references/trivia-db.json`（762 题，由 `scripts/gen-trivia.py` 重新生成）
- `references/knowledge-base/`（band-members / album-history / concert-archives / timeline）
- `references/lyrics-db/`（题源之一）

## 7. 流程

### Direct Q&A
1. 识别 domain
2. 在 trivia-db 查匹配条目
3. 简答 + source 标注；缺失则联网兜底并标记外部来源

### Quiz Mode
1. 询问难度
2. 随机抽 10 题
3. 一题一轮，逐题给反馈
4. 终极评分：
   - 10/10 第五位团员
   - 7–9 资深五迷
   - 4–6 路人粉
   - 0–3 还不快去听歌

## 8. Edge Cases

- 模糊问题 → 1 个澄清回合
- 时效性问题（如最新巡演场次） → 标注数据截止日期
- 谣言/未证实 → 拒绝断言，注明 "unverified"
- Quiz 答案变体 → 接受合理同义（"玛莎" = "蔡升晏"）

## 9. 与其它 Skill 协作

- trivia-db 由 lyrics-db + knowledge-base 一键再生成（脚本：`scripts/gen-trivia.py`）
- SK13 mayday-dictionary 与本 Skill 互补：dictionary 解释词条，trivia 验证认知