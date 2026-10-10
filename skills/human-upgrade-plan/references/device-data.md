# 设备数据与 COROS MCP

训练建议默认可用文字反馈完成。手表与 MCP 是可选增强，不把设备当作开训门槛。

## 首次必须询问

在基础建档问题之后、排正式计划之前，补问：

> 你平时用什么手表或运动设备？（高驰 COROS / 佳明 Garmin / 苹果 Apple Watch / 华为 / 颂拓 / 没有 / 其他）

记录品牌、是否同步到官方 App、用户是否愿意授权 AI 读数据。不愿授权时继续用自述与手动日志。

高驰且愿意授权时，**再问一句客户端**（决定走哪条接法，不要直接丢链接）：

> 你现在是在哪个 AI 里用这个计划？ChatGPT / Claude 网页，还是 Cursor、OpenClaw、WorkBuddy，或其他要在自己电脑上装东西的国内客户端？

## 分支

| 设备情况 | 做法 |
|---|---|
| 高驰 COROS，且当前 AI 能接 MCP | 按下方「先选方式」给出可照做的步骤；接通后优先用 MCP 核对近期负荷、睡眠、恢复与计划日程 |
| 高驰 COROS，但客户端暂无 MCP / 用户不想装 | 说明配置步骤；未接通前用手动反馈；可请用户导出摘要或口述关键课 |
| Garmin / Apple / 华为 / 颂拓 / 其他 | 说明本 skill 当前内置的官方 MCP 路径是 COROS；其他品牌可用手动日志、截图摘要或用户自行提供的导出 |
| 无手表 | 用时间、距离感受、RPE、症状与睡眠自述排课；不因缺设备降低可执行性 |

不要假设用户已授权。未确认接入成功前，不声称“已读取你的手表数据”。

## 官方 COROS MCP（必须按客户端说清楚）

官方说明：[Connect Your COROS to AI](https://support.coros.com/hc/en-us/articles/50841795180948-Connect-Your-COROS-to-AI) · [COROS MCP GitHub](https://github.com/coroslab/COROS-MCP)

准备两样：**COROS 账号**（App 能正常登录、已有可看的数据）+ **支持 MCP 的 AI**。COROS MCP 本身免费；多数 AI 平台的 MCP / 开发者模式 / 高级模型需要该平台的付费套餐。

本 skill 默认服务大陆用户。远程 URL 只用大陆节点 `https://mcpcn.coros.com/mcp`，不主动引导欧/美节点。

### 先选方式（助手必须先判断，再给步骤）

| 用户的 AI | 走哪条 |
|---|---|
| ChatGPT、Claude 网页、Codex 等能在设置里**直接粘贴 MCP 链接**的云端平台 | **方式一：填 URL** |
| Cursor、Claude Code、OpenClaw、WorkBuddy、Hermes，以及多数**国内要在本机装扩展**的 AI | **方式二：本地安装**（国内默认这条） |
| 说不清 | 先问清楚客户端；在国内、又不是 ChatGPT 网页 → 默认按方式二讲 |

---

### 方式一：ChatGPT 等云端平台，直接添加 MCP URL

适合能在设置里填「MCP 服务器地址」的平台。下面以 ChatGPT 为例，其它能填 URL 的平台只换菜单位置，链接相同。

**步骤 1：复制大陆链接**

```text
https://mcpcn.coros.com/mcp
```

（本 skill 默认大陆账号。若客户端报 URL 无效，可再试官方总入口 `https://mcp.coros.com/mcp`。仍失败则改方式二或手动反馈，不要让用户改填欧/美节点。）

**步骤 2：在 AI 里添加（ChatGPT）**

1. 打开 ChatGPT → 左下角头像 → **设置**
2. **应用** → **高级设置**
3. 打开**开发人员模式**，点**创建应用**
4. 在 **MCP 服务器**里粘贴上面的链接，身份验证选 **OAuth**
5. 授权登录你的 **COROS** 账号（用大陆 App 同一套账号）
6. 回到聊天窗口，用下方「接通后说一句」验证

其它云端平台：在 MCP / Connector / 自定义工具里粘贴同一 URL，认证选 OAuth，完成 COROS 登录即可。

---

### 方式二：国内 / 本机 AI，本地安装（默认给大陆用户）

国内常见客户端往往**不能只贴一条网址**，要在你这台电脑上装 COROS 的本地 MCP，再在客户端里授权。OpenClaw、WorkBuddy、Hermes 等支持对话安装；Cursor 等则在本机装好后，到 MCP 设置里加本地服务器。

**A. 能在对话框里装 Skill 的（OpenClaw、WorkBuddy、Hermes 等）**

把下面整句发给那个 AI：

```text
npm install -g coros-mcp
```

然后按它的提示安装 COROS MCP 相关 Skill，登录并授权你的 COROS 账号。

**B. Cursor 等要本机配置的客户端**

1. 电脑已安装 [Node.js](https://nodejs.org/)（终端能运行 `npm -v`）。
2. 打开终端，执行：

```bash
npm install -g coros-mcp
```

3. 打开该 AI 的 **MCP / 工具 / 扩展** 设置，添加**本地 MCP 服务器**。
   - 命令填安装后的 `coros-mcp`（或按该客户端提示选择 COROS Skill）。
   - 具体按钮名称以当前软件界面为准，不要让用户去填欧/美 URL。
4. 按提示用浏览器登录并授权 **COROS** 账号。
5. 回到对话，用下方「接通后说一句」验证。

若以后提示会话过期或旧 Skill 连不上，再执行：

```bash
npm install -g coros-mcp@latest
```

然后重新授权一次。

---

### 接通后说一句（两种方式通用）

请用户复制到**已经接好 MCP 的那个对话窗口**：

> 请调用 COROS MCP，把过去两周的跑步训练和睡眠发给我。能读到数据后再给我本周计划。

读到活动/睡眠即成功。读不到时：确认数据已同步到 COROS App → 新开对话再问 → 明确说「请调用 COROS MCP」。仍失败则改手动反馈，不要反复让用户换境外链接。

官方示例也可以是：「请把过去两周的训练记录发给我。」

## 接入后本 skill 应调用的数据类型

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
