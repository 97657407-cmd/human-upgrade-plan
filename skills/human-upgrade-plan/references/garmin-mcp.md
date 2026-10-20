# 佳明 Garmin MCP

本机 stdio MCP。不能装在手机上。登录页是电脑 `127.0.0.1`，必须用本机 **Google Chrome**，禁止 Cursor 内置窗口 / Simple Browser / 浏览器 MCP。不要在对话里要密码、验证码、会话令牌。

排课仍走知识大脑。手表分数、训练准备度、VO2max、比赛预测只当厂商模型，不单独开间歇。主观差或疼痛优先。空数据、认证失败、请求失败要分开说，不把空当成零。

## 接入（Cursor）

包名 `dsh-plugin-garmin-connect`，命令 `garmin-connect-mcp`。中国区 `GARMIN_REGION=cn`，国际区 `global`。不要把密码写进 MCP 配置。

`~/.cursor/mcp.json` 示例（路径换成这台电脑的绝对路径）：

```json
"garmin-connect": {
  "command": "/absolute/path/to/node",
  "args": ["/absolute/path/to/dsh-plugin-garmin-connect/lib/mcp.js"],
  "env": {
    "GARMIN_USERNAME": "换成佳明登录邮箱",
    "GARMIN_REGION": "cn",
    "GARMIN_ACCOUNT": "cursor-cn",
    "GARMIN_SESSION_TOKEN_FILE": "/absolute/private/path/cursor-cn.session.json",
    "GARMIN_FIT_DOWNLOAD_DIR": "/absolute/path/to/garmin-fit-parent"
  }
}
```

会话目录仅当前用户可读写。每个客户端用自己的 `GARMIN_ACCOUNT` 和会话文件，不要和高驰或其他 AI 共用一份。

登录（终端，中国区）：

```bash
export GARMIN_USERNAME='邮箱'
garmin-connect-auth serve --account cursor-cn --region cn --open --output /absolute/private/path/cursor-cn.session.json
```

Mac 若没自动打开 Chrome：`open -a "Google Chrome" "登录页 URL"`。密码只打在浏览器里的佳明表单。登完重载 MCP，新开对话再拉数据。手机 App 只负责同步手表；验证码可以看短信，不要把 `127.0.0.1` 链接发到手机浏览器。

接通后先 `get_garmin_profile` 核对账号。工具以当前会话 schema 为准，禁止猜工具名。

## 排课前读什么

已接通则在写今日/本周课之前拉：最近活动 + 睡眠（有则加 HRV/准备度）。两块表都接了就都读，冲突时主观和症状优先。读不到就说未读到，改口述，禁止伪造。

| 用途 | 工具 |
|---|---|
| 核对账号 | `get_garmin_profile` |
| 最近练了什么 | `get_garmin_activities`（默认 `detail=full`；用户要短摘要用 `compact`。full 可能含路线，只摘要不要复述坐标） |
| 睡眠 | `get_garmin_sleep` |
| 步数 / 心率 / 体重 | `get_garmin_steps` / `get_garmin_heart_rate` / `get_garmin_weight` |
| 课表库模板 | `get_garmin_workouts`（不是已完成训练） |
| 日历排期 | `get_garmin_scheduled_workouts`（最多 31 天，含首尾） |
| HRV / 压力 / Body Battery / 准备度 / 负荷 / VO2 / 预测 | 见 [garmin-recovery](garmin-recovery.md) |

相对日期换成 `YYYY-MM-DD`。睡眠、步数、心率、体重超过 30 天要分批。不要一次拉全库。

## 写回（必须用户确认）

只给建议 ≠ 写入。创建、删除模板、取消排期、下载 FIT 都要先预览再确认。`confirmationId` 一次性、约 10 分钟；失败不自动重放。

1. 创建：`create_garmin_workout` 先 `confirmed` 省略或 false → 展示名称和步骤 → 用户确认后同一内容 + `confirmed: true` + `confirmationId`。只进训练库，不自动排到某天、不自动推表。  
2. 删模板：`get_garmin_workouts` 拿 `workoutId` → `delete_garmin_workout`。不是删已完成活动。  
3. 取消某天排期：`get_garmin_scheduled_workouts` 拿 `scheduleId` → `unschedule_garmin_workout`（保留模板）。不要用模板 ID 代替排期 ID。  
4. 下载 FIT：用户明确要某次活动；先核 `activityId`；需已设 `GARMIN_FIT_DOWNLOAD_DIR`；不覆盖已有文件。不要把 FIT 二进制塞进对话。

课表怎么练仍由本 skill 排。不要用跑步壳冒充力量。
