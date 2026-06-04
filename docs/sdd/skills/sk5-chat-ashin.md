# SK5 · chat-ashin

> 隶属：[Mayday Skills SDD](../README.md) · Skill 状态：✅ v1.0 已交付
> 实现位置：[`/chat-ashin/`](../../../chat-ashin/)

## 1. 一句话定义

以阿信人设回应用户：建议、安慰或闲聊，用他的口吻和价值观。

## 2. 用户故事

- 「我快撑不住了，阿信会怎么说」
- 「想换工作但不敢，如果是阿信他会怎么决定」
- 「跟阿信聊聊今晚的月亮」

## 3. SKILL.md 关键字段

| 字段 | 内容 |
|------|------|
| `name` | `chat-ashin` |
| `category` | `roleplay` |
| `compatibility` | No external dependencies |

## 4. 输入

| 字段 | 必填 | 说明 |
|------|------|------|
| message | ✅ | 用户原话 |
| intent | ⏸️ | `advice` / `comfort` / `casual` 自动识别 |

## 5. 输出

- 一段第一人称回应，结尾可附 1 句五月天歌词引用
- 对于编造内容，使用 "如果是阿信，他可能会说……" 前缀

## 6. 数据依赖

- `references/persona/ashin-persona.md`
- `references/ashin-voice.md`
- `references/conversation-examples.md`
- `references/knowledge-base/`
- `references/lyrics-db/`（提供锚句）

## 7. 流程

1. 加载 persona + voice + examples
2. 解析 message 的情绪意图
3. 按 intent 调用对应口吻策略：
   - advice：哲学 + 实用 + 锚句
   - comfort：先共情 → 提供新视角 → 温暖收尾
   - casual：轻松，可穿插乐团趣闻
4. 输出回应；若需引用歌词标明出处

## 8. Edge Cases

- 涉及政治 / 团内私事 / 财务 → 礼貌回避
- 用户要求扮演其他成员 → 解释当前仅支持阿信，建议下次扩展
- 编造引语 → 必须带 "如果是阿信" 等不确定语气

## 9. 与其它 Skill 协作

- v1.1 拟在 `references/persona/` 下扩展玛莎/怪兽/石头/冠佑 persona，供 SK11 同人使用
- 与 SK7 mayday-quotes 共享 lyrics-db 锚句机制