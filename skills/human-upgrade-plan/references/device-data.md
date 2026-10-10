# 设备数据与 COROS MCP

训练建议默认可用文字反馈完成。手表与 MCP 是可选增强，不把设备当作开训门槛。

## 首次必须询问

在基础建档问题之后、排正式计划之前，补问：

> 你平时用什么手表或运动设备？（高驰 COROS / 佳明 Garmin / 苹果 Apple Watch / 华为 / 颂拓 / 没有 / 其他）

记录品牌、是否同步到官方 App、用户是否愿意授权 AI 读数据。不愿授权时继续用自述与手动日志。

## 分支

| 设备情况 | 做法 |
|---|---|
| 高驰 COROS，且当前 AI 客户端支持 MCP | 引导接入官方 COROS MCP；接入后优先用 MCP 核对近期负荷、睡眠、恢复与计划日程 |
| 高驰 COROS，但客户端暂无 MCP | 说明配置步骤；未接通前用手动反馈；可请用户导出摘要或口述关键课 |
| Garmin / Apple / 华为 / 颂拓 / 其他 | 说明本 skill 当前内置的官方 MCP 路径是 COROS；其他品牌可用手动日志、截图摘要或用户自行提供的导出 |
| 无手表 | 用时间、距离感受、RPE、症状与睡眠自述排课；不因缺设备降低可执行性 |

不要假设用户已授权。未确认接入成功前，不声称“已读取你的手表数据”。

## 官方 COROS MCP（推荐分享给用户）

官方桥接说明：[Connect Your COROS to AI](https://support.coros.com/hc/en-us/articles/50841795180948-Connect-Your-COROS-to-AI) · [COROS MCP GitHub](https://github.com/coroslab/COROS-MCP)

### 接入提示词（可直接发给用户 · 默认中国大陆）

本 skill 面向大陆用户，**只走大陆节点**，不引导欧/美 MCP。

1. 在你的 AI 客户端里添加 MCP / Connector。
2. 服务器 URL 填：`https://mcpcn.coros.com/mcp`
3. 用 COROS 账号完成 OAuth 授权（大陆账号）。
4. 授权后回复：「已连接 COROS，请读取最近 14 天跑步、睡眠和恢复，再给我本周计划。」

若客户端报 URL 无效，可再试官方文档里的通用入口 `https://mcp.coros.com/mcp`；仍失败则改手动反馈，不要让用户折腾境外节点。

部分平台可用 Skill 安装：`npm install -g coros-mcp`（以 COROS 文档与本地客户端支持为准）。MCP 本身免费；AI 平台会员/配额按其规则。

### 接入后本 skill 应调用的数据类型

按任务选用，不一次拉全库。首次连接成功后先跑一次 `list_tools` 核对真实工具名再调用，禁止猜工具名硬调：

| 用途 | 优先工具方向 |
|---|---|
| 核对近期是否真练、练了什么 | `querySportRecords` → 必要时 `getActivityDetail` / `analyzeActivityDetail` |
| 间歇/配速质量 | 活动详情、圈段；大数据量时优先 FIT 下载而非整段逐秒塞进对话 |
| 睡眠与恢复 | `querySleepData`、`querySleepHrv`、`queryRecoveryStatus`、`queryDailyHealthData` |
| 负荷与阶段判断 | `queryTrainingLoadAssessment`、`queryFitnessAssessmentOverview` |
| 写入计划前先读日程 | `queryTrainingSchedule`、计划/课表库相关查询 |
| 用户明确要求同步到手表日历 | 创建/更新计划或 `scheduleWorkout` / `createScheduledWorkout` 等写接口 |

写回 COROS（创建计划、改课、排进日历）必须先得到用户明确同意；仅“给建议”不等于授权保存。先读再改；计划课与独立日程课用对应更新入口，不要用新建第二堂课伪装修改。

### 数据使用规则

- MCP 数据是外部负荷与部分恢复信号，不能单独诊断伤病或过度训练。
- 手表配速、心率区、恢复百分比与用户主观感受冲突时，两边都保留，并说明哪一侧驱动本次课表调整。
- 预测成绩、VO2max、阈值配速视为厂商模型输出，需标注来源与不确定性，不直接当处方配速。
- 仅访问当前授权用户自己的数据；禁止拿他人账号或混用档案。
- 不要把原始健康曲线、精确生日等敏感字段写入公共 skill 或待发布仓库。

## 非 COROS 用户的等价最小集

请用户每次反馈尽量包含：日期、运动类型、时间或距离、主观强度（0–10）、睡眠（差/一般/好）、症状、是否完成计划。模板见 [training-log-template](../assets/training-log-template.md)。
