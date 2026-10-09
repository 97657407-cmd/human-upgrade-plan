# 人类变强计划

面向不同训练基础的跑步、力量与恢复辅助 skill，支持 100m 至马拉松及越野、工作日训练、反馈分析、教练学习，以及（可选）高驰 COROS 官方 MCP 数据接入。

## 使用

将 `skills/human-upgrade-plan` 文件夹复制到支持 SKILL.md 的工具的技能目录，例如 Codex 的 `~/.codex/skills/` 或 Claude Code 的 `~/.claude/skills/`；不同工具的加载方式请遵循各自说明。也可直接阅读该目录的 SKILL.md 与 references。

初次可说：

> 使用人类变强计划，根据我的目标和最近训练帮我安排一周，先问必要信息，并问我用什么手表。

训练建议应包含：可执行课表、为什么这么设计、科学原理、相关文献及外推边界。更新训练时提供实际完成内容、主观强度、症状、睡眠与可用时间；高驰用户可先接入 COROS MCP 再让助手读取近期数据。

### 高驰 COROS MCP（可选）

1. 在 AI 客户端添加 MCP，URL：`https://mcp.coros.com/mcp`（中国大陆账号若重定向失败可用 `https://mcpcn.coros.com/mcp`）。
2. 用 COROS 账号 OAuth 授权。
3. 对助手说：「已连接 COROS，请读取最近 14 天跑步与睡眠，再给我本周计划。」

说明见 skill 内 [device-data.md](skills/human-upgrade-plan/references/device-data.md) 与 [COROS 官方文档](https://support.coros.com/hc/en-us/articles/50841795180948-Connect-Your-COROS-to-AI)。

## 结构

- 用户建档与日志：仅提供空白模板，真实数据保存在用户指定的私人目录。
- 对话流程：基础问题 → 手表/MCP → 跟进具体需求 → 计划 + 原理与文献 → 反馈。
- 决策协议与输出：阶段判断、每日/周计划、反馈、进阶/减量与学习模式。
- 项目框架：11 个项目的能力需求、课型选择与评估重点。
- 恢复与工作：睡眠、精神疲劳、坐站工作、组间休息、力量与耐力组合。
- 证据：6 张已注明阅读深度的恢复卡。
- 设备：COROS MCP 接入与读写边界；其他品牌走手动反馈。
- 维护：公共文件白名单与隐私检查，个人数据不随包发布。

这是教练决策辅助资料，不保证无伤或必达成绩，也不替代必要的现场教学与医学评估。尚未完成所有项目的逐篇全文审校，不应宣称为世界级完整教材。

## 发布前检查

```sh
python3 skills/human-upgrade-plan/scripts/check_public.py --root .
```

检查包括文件白名单、空白模板、相对链接、常见个人路径及联系方式线索。识别词可用 `--deny-term` 追加。脚本通过后仍需人工复核内容和 Git 历史；其他分支、旧提交、发行附件与克隆不在当前文件检查范围。
