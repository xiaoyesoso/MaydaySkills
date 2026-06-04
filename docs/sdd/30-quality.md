# 30 · 质量门禁与版权策略

> 隶属：[Mayday Skills SDD](./README.md)
> 版本：v1.1

## 1. 合规检查表

每个 Skill 提交前必须通过以下逐项检查：

### 1.1 结构完整性

| # | 检查项 | 标准 |
|---|--------|------|
| 1 | `SKILL.md` 存在 | 顶层文件 |
| 2 | `README.md` 存在 | 中文说明 |
| 3 | YAML frontmatter 合法 | `---` 分隔，缩进正确 |
| 4 | `name` ↔ 目录名一致 | 小写+连字符 |
| 5 | `description` 含触发关键词 | 参考附录触发词矩阵 |
| 6 | 所有 `references/` 引用有效 | 路径可解析 |
| 7 | 所有 `scripts/` 引用合法 | 文件存在+可执行/可调用 |
| 8 | `compatibility` 与实际依赖一致 | 不夸大也不遗漏 |

### 1.2 内容质量

| # | 维度 | 标准 |
|---|------|------|
| 9 | 指令完整性 | Body 包含至少一个 `## Instruction Flow` 章节 |
| 10 | Token 预算 | Body ≤ 5000 tokens（参考：本文 ~5000）|
| 11 | Edge Cases | 至少列出 3 个边缘场景的处理方式 |
| 12 | 跨平台兼容 | 无 Trae/Claude/某平台专有指令 |
| 13 | 示例可得性 | 至少 1 个输入→输出范例 |

### 1.3 数据质量（仅数据型 Skill）

| # | 检查项 | 标准 |
|---|--------|------|
| 14 | JSON 合法 | `python3 -c "import json; json.load(open('...'))"` pass |
| 15 | schema 合规 | 与 `schema.json` 定义一致 |
| 16 | 无全文歌词 | `lyrics_excerpt` ≤ 2 行（见 §3）|
| 17 | 无空字段导致下游报错 | mood 字段缺失用 `{}` 而非跳过 |

## 2. 验证脚本

计划交付 [`scripts/validate-skill.sh`](../../scripts/validate-skill.sh) ← Phase 9。

## 3. 版权策略

### 3.1 歌词使用

- **可存放**：每首歌 1–2 句引用片段（`lyrics_excerpt`），作为情绪锚点或示例
- **不可存放**：任何一首歌的完整歌词、完整副歌、连续 3 行以上
- **不可存放**：整份和弦谱的完整转录（简要进行标注可接受，如 `I–V–vi–IV`）
- **例外**：instrumental 曲目（如《前传》《胎音》）标 `(instrumental)`，不存歌词

### 3.2 音乐录音

- 不可展示或分发任何 MP3/AAC/FLAC 格式的音频样本
- 可引用公开流媒体 URL（如 YouTube/Spotify 链接）

### 3.3 成员形象

- 不可生成或展示成员的深度伪造（deepfake）图像/声音
- 同人创作 ai 内容需在输出中明确标注「AI 生成，仅供娱乐」

### 3.4 商标

- 「五月天」「Mayday」「滚石唱片」「相信音乐」等商标仅用于描述目的
- 不暗示官方授权或与乐队有正式合作关系

## 4. 反模式（DO NOT）

- ❌ 不要为了凑数推荐主题完全无关的歌曲（SK4）
- ❌ 不要伪造未在数据库中标注的 mood 数值（SK4）
- ❌ 不要给所有失恋问题都推同一首歌（惰性匹配）（SK4）
- ❌ 不要逐字引用阿信在非公开场合的言论（SK5）
- ❌ 不要承诺"官方认证""乐队认可"等无法核实的关系（任何 Skill）

## 5. 版本控制

- Semantic Versioning（`v{Major}.{Minor}`），`README.md` 顶部标注
- 重大变更（BREAKING）必须留档到 `appendix/changelog.md`
- SKILL.md 中的 `metadata.version` 与 SDD 版本号同步