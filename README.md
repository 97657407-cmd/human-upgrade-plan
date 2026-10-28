# 人类耐力变强计划

版本 **1.3.6**（`skills/human-upgrade-plan/SKILL.md` 的 `version` 字段）。

面向不同训练基础的跑步、力量与恢复辅助 skill，支持 100m 至马拉松及越野、工作日训练、反馈分析、教练学习，以及（可选）高驰 COROS、佳明 Garmin MCP 数据接入。

## 使用

将 `skills/human-upgrade-plan` 文件夹复制到支持 SKILL.md 的工具的技能目录，例如 Codex 的 `~/.codex/skills/` 或 Claude Code 的 `~/.claude/skills/`；不同工具的加载方式请遵循各自说明。也可直接阅读该目录的 SKILL.md 与 references。

初次可说：

> 使用人类耐力变强计划。先问我怎么称呼，再了解我是学生还是上班、运动史、场地（能不能力量）、目标、伤病和手表，然后给我一周课表。

训练建议应包含：可执行课表、为什么这么设计、科学原理、相关文献及外推边界。更新训练时提供实际完成内容、主观强度、症状、睡眠与可用时间；高驰 / 佳明用户可先接入对应 MCP 再让助手读取近期数据；其他手表用 App 最近记录截图或口述三行。

### 公共包与私人档案

这个仓库只保存通用 skill、证据卡、模板和检查脚本。真实用户档案、训练日志、手表原始数据和个体课表应放在用户自己指定的私人目录，使用时在对话里授权读取。公共包更新方法和证据，私人目录更新个人历史；两者是同一个 skill 的两层数据，不需要做两个版本。

给别人使用时只发仓库链接即可。对方可以克隆或下载本仓库，把 `skills/human-upgrade-plan` 放进其 AI 客户端支持的 skill 目录。之后公共包更新时，对方用 `git pull` 或重新下载覆盖即可；私人档案不会随公共包同步。

### 手表绑定（可选 · 高驰 / 佳明）

排课不强制绑表。绑上了，助手会先读**最近一次运动 + 睡眠**再开口。接了几块就读几块；人难受听身体，不听恢复百分比。密码、验证码不要发到对话。完整步骤：[设备数据](skills/human-upgrade-plan/references/device-data.md)、[佳明](skills/human-upgrade-plan/references/garmin-mcp.md)。

**高驰 COROS（中国区）**

先看你用的是哪种 AI，不要所有人只贴一条网址。禁止 `mcpus` / `mcpeu`。

方式一 · ChatGPT 等能直接填 MCP 链接：复制 `https://mcp.coros.com/mcp`（无效再 `https://mcpcn.coros.com/mcp`），认证选 OAuth，登录大陆 COROS。也可在连接器里搜 COROS。然后说：「请调用 COROS MCP，把过去两周的跑步和睡眠发给我。」

方式二 · Cursor / OpenClaw / WorkBuddy 本机：

```bash
npm install -g coros-mcp
coros-mcp --issuer https://mcpcn.coros.com login-start
```

登录链接必须用 **Google Chrome** 打开（Mac：`open -a "Google Chrome" "链接"`），不要用 Cursor 内置窗口。授权后：`coros-mcp --issuer https://mcpcn.coros.com login-finish`。会话过期则 `npm install -g coros-mcp@latest` 后再走一遍。官方说明：[Connect Your COROS to AI](https://support.coros.com/hc/en-us/articles/50841795180948-Connect-Your-COROS-to-AI)。

**佳明 Garmin（中国区）**

本机 MCP，不能只贴网址。`GARMIN_REGION=cn`。登录页是电脑 `127.0.0.1`，必须 Chrome，密码只打在佳明表单里。接通后先核账号，再拉活动和睡眠。点选见 [garmin-mcp.md](skills/human-upgrade-plan/references/garmin-mcp.md)。

## 结构

- 用户建档与日志：仅提供空白模板，真实数据保存在用户指定的私人目录。
- 对话流程：基础问题 → 手表/MCP → 跟进具体需求 → 计划 + 原理与文献 → 反馈。
- 决策协议与输出：阶段判断、每日/周计划、反馈、进阶/减量与学习模式。
- 决策大脑：[知识大脑](skills/human-upgrade-plan/references/knowledge-brain.md) — 给建议时先判断取舍，再写课表。
- 长期备赛：[备赛框架](skills/human-upgrade-plan/references/race-prep-framework.md) — 100m 至全马/越野，按大众、进阶、体测、上班族降级；证据见 [race-prep-core](skills/human-upgrade-plan/references/evidence/race-prep-core.md)。
- 训练产出：[框架手册](skills/human-upgrade-plan/references/framework-handbook.md)（金样课表、伤后树、项目、力量菜单）。课表不从论文堆出来。
- 项目框架：11 个项目（100m 至越野）的能力需求、课型选择与评估重点。
- 恢复与工作：睡眠、精神疲劳、坐站工作、组间休息、力量与耐力组合。
- 文献全库：[INDEX-all](skills/human-upgrade-plan/references/evidence/INDEX-all.md) — 约 358 条可检索入口。主题包细目见 [INDEX-core50](skills/human-upgrade-plan/references/evidence/INDEX-core50-2023-2026.md)。
- 青少年跑步：[youth-run-framework](skills/human-upgrade-plan/references/youth-run-framework.md) YR01–YR05。不抄成人周公里；默认不排超马。
- 赛道策略与补给：[race-fuel-framework](skills/human-upgrade-plan/references/race-fuel-framework.md) — 分段配速、补给站、能量胶、盐丸边界；证据 RF01–RF12。
- 碳板/比赛鞋：[carbon-shoe-framework](skills/human-upgrade-plan/references/carbon-shoe-framework.md) CS01–CS05。
- 热习服：[heat-acclimation-framework](skills/human-upgrade-plan/references/heat-acclimation-framework.md) HA01–HA05。
- 伤停交叉训练：[自行车与椭圆机手册](skills/human-upgrade-plan/references/cross-train-framework.md)。
- 间歇组间休息 + 控时：[interval-rest-framework](skills/human-upgrade-plan/references/interval-rest-framework.md) IR01–IR18 — 工作钟与休息钟一起定。
- 双阈值 / LGTIT：[double-threshold-framework](skills/human-upgrade-plan/references/double-threshold-framework.md) DT01–DT12 — 研究报告方法模板 + 爱好者降级。
- 间歇·控时·双阈值知识文：[interval-training-playbook](skills/human-upgrade-plan/references/interval-training-playbook.md) — 含方法卡与一千米速查。
- 顶级运动员案例：[elite-cases-framework](skills/human-upgrade-plan/references/elite-cases-framework.md) EC01–EC10 — 短跑/中跑/长跑；只借原则不借剂量。
- 赛日：[赛事预测与赛日策略](skills/human-upgrade-plan/references/race-day-strategy.md)（气温、身体、三档预测）。
- 手表绑定：README 本节高驰 / 佳明；细节 [device-data](skills/human-upgrade-plan/references/device-data.md)、[garmin-mcp](skills/human-upgrade-plan/references/garmin-mcp.md)。未接 MCP 走手动三行。
- 维护：公共文件白名单与隐私检查，个人数据不随包发布。

这是教练决策辅助资料，不保证无伤或必达成绩，也不替代必要的现场教学与医学评估。尚未完成所有项目的逐篇全文审校，不应宣称为世界级完整教材。

## 发布前检查

```sh
python3 skills/human-upgrade-plan/scripts/check_public.py --root .
```

检查包括文件白名单、空白模板、相对链接、常见个人路径及联系方式线索。识别词可用 `--deny-term` 追加。脚本通过后仍需人工复核内容和 Git 历史；其他分支、旧提交、发行附件与克隆不在当前文件检查范围。
