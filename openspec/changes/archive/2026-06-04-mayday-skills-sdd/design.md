## Context

MaydaySkills 是一套围绕五月天乐队的 Agent Skills 生态（13 个 Skill），遵循 agentskills.io v1.0 规范。当前状态：

- SK1–SK8 已实现（含 SKILL.md、references、scripts）
- SK9–SK13 仅有 SDD 规划文档（`docs/sdd/skills/`），未实现
- 公共数据：lyrics-db（9 专辑 / 120 首元数据）、knowledge-base（4 文件）、persona（阿信人设）
- 同步脚本：`scripts/sync-lyrics-db.sh`、`scripts/gen-trivia.py`
- API 集成：Spotify Web API + YouTube Data API（SK8 data-fetcher.py）

约束：每个 Skill 必须自包含（不依赖仓库其他 skill 目录），歌词仅存 1–2 句引用片段，离线优先。

## Goals / Non-Goals

**Goals:**
- 将 13 个 Skill 的需求规格以 OpenSpec spec 格式落地到 `openspec/specs/`
- 统一描述跨 Skill 的数据依赖和交互关系
- 为 SK9–SK13 的实施提供可直接执行的任务清单
- 保留 docs/sdd/ 下的横向文档（overview/architecture/roadmap/quality）作为人类可读入口

**Non-Goals:**
- 不重新实现已有的 SK1–SK8 代码
- 不引入新的外部 API 或数据源（除 SK9–SK13 规划中已定义的）
- 不修改 agentskills.io 规范本身
- 不做跨平台打包或发布流程（Phase 9 范畴）

## Decisions

### D1: Spec 按 Skill 独立组织

每个 Skill 对应 `openspec/specs/<skill-name>/spec.md`，内含 Requirements + Scenarios。选择此方案而非"按功能域合并"是因为 Skill 天然是独立安装单元，一个 spec 对应一个 Skill 符合 agentskills.io 的"独立可安装"理念。

**Alternative**: 按功能域（创作陪伴/知识问答/互动陪伴/实用工具）合并 spec → 拒绝，因为同一个域的 Skill 实现和部署节奏不同，合并会制造不必要的耦合。

### D2: 新 Skill 数据依赖走现有 sync 机制

SK9–SK13 中需要 lyrics-db 的 Skill 仍然通过 `scripts/sync-lyrics-db.sh` 获取数据副本。选择此方案是因为它已被 SK1–SK8 验证，且满足"自包含"原则。

**Alternative**: 引入共享引用或 npm workspace 式依赖 → 拒绝，因为 Skill 打包后需独立运行，引用会破坏自包含性。

### D3: SK9 mood 匹配引擎复用而非重写

SK9 mayday-radio 的曲目筛选逻辑直接复用 SK4 mayday-mood 的三轴公式（`score = -sqrt(ΔE²+ΔV²) + 2·|theme_overlap|`），通过在 `references/mood-taxonomy.md` 中描述公式实现"文档级复用"。运行时两个 Skill 各自实现，不跨目录调用。

### D4: SK10 难度评分基于启发式公式

MVP 阶段使用 `0.4×highest_note + 0.2×bpm + 0.2×key_change + 0.2×continuous_singing` 的加权公式，数据全部来自 lyrics-db 已有字段。不引入 librosa 等音频分析库。

**Alternative**: 接入 pitch detection API → 延后到 Phase 9+。

### D5: SK11 同人创作红线以 spec 约束强制执行

在 `openspec/specs/mayday-fanfic/spec.md` 中用 SHALL/MUST 语句明确定义禁止行为（R18/丑化真人/伪造引语/完整歌词），而非仅靠 SKILL.md 中的建议。这样 OpenSpec 的 validate 命令可自动检查 spec 合规性。

## Risks / Trade-offs

- **[Spec 膨胀]** → 13 个 spec 文件可能产生大量交叉引用。缓解：每个 spec 限定在 ≤200 行，跨 Skill 依赖仅在 Requirements 中引用对方 spec 名而非内联内容。
- **[数据一致性]** → sync 脚本只同步 lyrics-db，knowledge-base 和 persona 仍靠手工拷贝。缓解：Phase 9 中加入 `scripts/sync-knowledge-base.sh`。
- **[SK10 准确度]** → 启发式难度评分可能不准。缓解：先对 30 首重点曲目人工校准，标注误差范围。
- **[SK11 版权风险]** → 同人内容可能被滥用。缓解：spec 中强制要求输出末尾附「创作声明」，且 SKILL.md 的 Edge Cases 明确拒绝商业用途请求。
