# 设备数据与手表 MCP

训练建议默认可用文字反馈完成。手表与 MCP 是可选增强，不把设备当作开训门槛。

## 首次必须询问

在基础建档问题之后、排正式计划之前，补问：

> 你平时用什么手表或运动设备？（高驰 COROS / 佳明 Garmin / 苹果 Apple Watch / 华为 / 颂拓 / 没有 / 其他）  
> 心率带有没有：胸带、上臂光学臂带，还是只有腕表？跑步豆（Stryd 或表厂脚豆）有没有？

配件用法、每堂佩戴提醒、气温分支：[硬件配件](hardware-kit-framework.md)。没有配件继续用 RPE，不推销。

记录品牌、是否同步到官方 App、用户是否愿意授权 AI 读数据。不愿授权时继续用自述与手动日志。

高驰且愿意授权时，**再问一句客户端**（决定走哪条接法，不要直接丢链接）：

> 你现在用的是哪个 AI？能在设置里粘贴 MCP 链接的（ChatGPT 等）走方式一；OpenClaw、WorkBuddy、Cursor 这类本机客户端走方式二。我们只接中国区。

佳明且愿意授权：抄下方分支和 [garmin-mcp](garmin-mcp.md)，不要先丢密码框。

华为且愿意授权：抄 [huawei-mcp](huawei-mcp.md)。先确认本机 MCP 在不在；不在就按「手表绑定」说明装。不要在对话里要 Bearer。

## 分支

| 设备情况 | 做法 |
|---|---|
| 高驰 COROS，且当前 AI 能接 MCP | 按下方「先选方式」给出可照做的步骤；接通后优先用 MCP 核对近期负荷、睡眠、恢复与计划日程 |
| 高驰 COROS，但客户端暂无 MCP / 用户不想装 | 说明配置步骤；未接通前用手动反馈；可请用户导出摘要或口述关键课 |
| 佳明 Garmin，且当前 AI 能接本机 MCP | 抄 [佳明 MCP](garmin-mcp.md)：中国区 `cn`，Chrome 登录，排课前拉活动+睡眠 |
| 华为手表 / 运动健康，且当前 AI 能接本机 MCP | 抄 [华为 MCP](huawei-mcp.md)：网页会话头放本机 env；排课前拉活动+睡眠 |
| 高驰 / 佳明 / 华为接了不止一块 | 接了几块读几块；主观/疼痛优先于任一块表的恢复分 |
| Apple / 颂拓 / 其他，或上述 MCP 未接 | **不要让用户导以前的 FIT**：一份 FIT 只覆盖那一次活动或那一天，看不到更早负荷和 HRV 基线。排课请他看 App **最近**：上次课 + 近 7 天睡眠 + 今天恢复/HRV 相对这周。截图或打三行即可（见下方最小集）。只有要拆某一堂间歇质量，才导**那一堂**的 FIT |
| 无手表 | 用时间、距离感受、RPE、症状与睡眠自述排课；不因缺设备降低可执行性 |

不要假设用户已授权。未确认接入成功前，不声称“已读取你的手表数据”。

仓库首页「手表绑定」三块（高驰 / 佳明 / 华为）和本文件是同一套，不要另发明第四种接法。

## 官方 COROS MCP（中国区默认只走这两条）

官方说明：[Connect Your COROS to AI](https://support.coros.com/hc/en-us/articles/50841795180948-Connect-Your-COROS-to-AI) · [COROS MCP GitHub](https://github.com/coroslab/COROS-MCP)

本 skill **只服务中国区**。高驰接入默认按官方两步，不要发明第三种，**禁止给北美/欧洲链接**（`mcpus.coros.com` / `mcpeu.coros.com`）。

准备两样：**COROS 账号**（大陆 App 能登录、已有可看的数据）+ **支持 MCP 的 AI**。COROS MCP 本身免费；多数 AI 平台的 MCP / 开发者模式需要该平台付费套餐。

### 先选方式

| 用户的 AI | 走哪条 |
|---|---|
| ChatGPT、Claude 网页等能在设置里**直接粘贴 MCP 链接** | **方式一** |
| OpenClaw、WorkBuddy，以及其他要在本机装 Skill 的客户端（含 Cursor） | **方式二** |
| 说不清 | 先问客户端；不是能填 URL 的网页 → 按方式二 |

---

### 方式一：ChatGPT 等平台，添加 MCP

官方 GitHub 的**默认入口**（2026-10 探测：从国内访问会落到 `mcp_cn_prod`，未登录返回 401 + OAuth，属于活接口）：

```text
https://mcp.coros.com/mcp
```

部分客户端不吃跳转、报「URL 无效」时，再填中国直连（不要一上来就填这条）：

```text
https://mcpcn.coros.com/mcp
```

不要填 `mcpus` / `mcpeu`。两条都失败则改方式二或手动反馈，不要让用户换区。

**ChatGPT / Claude 优先走官方连接器（可以不填 URL）**

- ChatGPT：设置 → Plugins → 搜索 **COROS** → 连接 → 授权大陆账号  
- Claude 桌面：Settings → Connectors → Discover → 搜索 **COROS** → Connect

**仍要手填 URL 时（Cursor 远程 MCP、ChatGPT 自定义 MCP 等）**

1. 粘贴 `https://mcp.coros.com/mcp`，认证选 **OAuth**
2. 授权大陆 **COROS** 账号
3. 报 URL 无效再改 `https://mcpcn.coros.com/mcp`
4. 用下方「接通后说一句」试问

---

### 方式二：OpenClaw、WorkBuddy 等，用 Skill 安装

本机客户端通常不能只贴网址。

**A. 能在对话框里装的（OpenClaw、WorkBuddy 等）**

把这句发给那个 AI：

```text
npm install -g coros-mcp
```

再按提示安装 COROS MCP 相关 Skill，登录并授权大陆 COROS 账号。

**B. Cursor / 本机：中国区必须走这条（已验证可进）**

中国区发证地址是 `https://mcpcn.coros.com`。授权页可能会跳到 `opencn.coros.com`，这是大陆 OAuth，正常。不要填欧美节点。

终端找不到 `coros-mcp` 时，先把本机 Node 的 `bin` 加进 PATH（`which node` 所在目录），需要的话再 `npm install -g coros-mcp`。

**1. 终端拿登录链接**

```bash
coros-mcp --issuer https://mcpcn.coros.com login-start
```

会打出一条 `https://mcpcn.coros.com/cli/login/...`

**2. 必须用谷歌浏览器打开（不要 Cursor 窗口）**

Mac：

```bash
open -a "Google Chrome" "把上一步完整链接贴这里"
```

助手若被要求打开这条链接：只许用本机 Shell 执行 `open -a "Google Chrome"`，**禁止** Cursor 内置浏览器、Simple Browser、浏览器 MCP。

**3. Chrome 里用和 App 同一套大陆高驰账号授权**

**4. 终端收尾**

```bash
coros-mcp --issuer https://mcpcn.coros.com login-finish
```

然后对新对话说：`请把过去两周的训练记录发给我。`

会话过期：`npm install -g coros-mcp@latest` 后再跑一遍 login-start → Chrome → login-finish。一次授权链接带 `state=`，用过即废，不要发到公共仓库。

---

### 接通后说一句（两种方式通用）

请复制到**已经接好 MCP 的那个窗口**：

> 请把过去两周的训练记录发给我。

读到活动/睡眠即成功。读不到：确认已同步到 COROS App → 新开对话 → 明确说请调用 COROS MCP。仍失败改手动反馈，不要改填境外链接。

## 排每一堂课之前（高驰已接通则强制）

不要等用户提醒。只要本轮要写「今天练什么 / 本周七天 / 赛日策略」，先拉数据再开口：

1. 最近 **1 次**运动记录：项目、时间、距离、配速或功率、心率相对近期是否偏高、是否中途掉速、是否按计划完成。优先 `querySportRecords`（最近若干条）→ 需要细节再 `getActivityDetail` / `analyzeActivityDetail`。  
2. 最近睡眠与恢复：`querySleepData`、`queryRecoveryStatus`（有则加 HRV）。  
3. 用三句话写进课表头：上次练了什么、身体/手表是否打架、因此今天是执行 / 降档 / 休息。

冲突规则：主观差或疼痛 > 恢复百分比；表预测成绩不单独开间歇或赛日配速。读不到数据时明确说「未读到手表」，改口述上次课，禁止伪造。

---

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

App 里可以自建力量课（选力量模式、选动作）。MCP 写接口目前只能新建跑步 / 骑行 / 越野。力量课：先查课表库里是否已有同一课型模板再排期；没有就请用户在 App 里建，不要用跑步/骑行占位。取消某一天：MCP 没有删除工具，请用户在 App 日历里删。

### 数据使用规则

- MCP 数据是外部负荷与部分恢复信号，不能单独诊断伤病或过度训练。
- 手表配速、心率区、恢复百分比与用户主观感受冲突时，两边都保留，并说明哪一侧驱动本次课表调整。
- 预测成绩、VO2max、阈值配速视为厂商模型输出，需标注来源与不确定性，不直接当处方配速。
- 仅访问当前授权用户自己的数据；禁止拿他人账号或混用档案。
- 不要把原始健康曲线、精确生日等敏感字段写入公共 skill 或待发布仓库。

## 佳明（已接通则排课前强制）

细节和写回：[garmin-mcp](garmin-mcp.md)。HRV/准备度工具表：[garmin-recovery](garmin-recovery.md)。

1. `get_garmin_profile`  
2. `get_garmin_activities`（最近若干条）  
3. `get_garmin_sleep`（昨晚到今天醒来日）  
4. 课表头三句：上次练了什么、身体/手表是否打架、因此今天执行 / 降档 / 休息。

写课表进佳明必须用户确认预览。不要密码进对话。登录必须 Google Chrome。

## 华为（已接通则排课前强制）

细节：[华为 MCP](huawei-mcp.md)。不实现登录；401 请用户自己在 https://health.cloud.huawei.com/TrainingCamp 换新请求头，不要把 Bearer 贴进对话。不要用 `health.huawei.com`。

1. `health_check`（探通路）  
2. `get_recent_activities`（最近若干条）  
3. `get_sleep_records`（昨晚到近几天；有则 `get_hrv_stats`）  
4. 课表头三句：上次练了什么、身体/手表是否打架、因此今天执行 / 降档 / 休息。

没有写回课表工具。跑力/预测配速不当处方。

---

## 非 MCP 用户的等价最小集（看最近，不导旧 FIT）

排今日/本周课之前，原句问（可整段复制）：

> 不用导以前的 FIT。打开 App 看最近：上次练了什么、昨晚睡眠、今天恢复/HRV 比这周高还是低。截图或打这三行就行。

三行模板：

```text
上次课：日期 · 项目 · 时长或距离 · 均配/均心率（有就写）· 完成/未完成 · 累不累 0–10
睡眠：昨晚大约 x 小时 · 差/一般/好
恢复/HRV：今天相对这周 偏高 / 差不多 / 偏低 · 测法（表夜间 / 晨起胸带 / 没有这个数）
```

没有恢复分就写主观和睡眠，继续排课。单日 HRV 只当参考：人难受或发烧优先听症状，不跟恢复分对着干。完整表格见 [training-log-template](../assets/training-log-template.md)。

FIT 只在用户明确要拆**这一堂**的圈段/功率时再要那一个文件；解码成摘要再进对话，不要把逐秒曲线贴进来。
