# 华为运动健康 MCP

本机 stdio MCP，直连大陆华为云 `hihealthbase-drcn.things.dbankcloud.cn`，不经第三方转发。社区实现（MIT），**不是华为官方 SDK**。不能装在手机上。不要在对话里要密码、验证码、完整 `Bearer`、Cookie。

排课仍走知识大脑。跑力、预测配速、VO2、训练负荷只当厂商模型，不单独开间歇。主观差或疼痛优先。空数据、401、请求失败要分开说，不把空当成零。`activityType` 是整数，不要擅自起中文名。HRV 数值原样返回，不换单位。

## 接入（Cursor）

本 skill **不实现登录、不刷新 token、不绕过权限**。必填环境变量（只放本机，不进 git、不进对话）：

- `HTC_AUTHORIZATION`：网页已登录会话的 `Authorization`（以 `Bearer ` 开头）
- `HTC_CLIENT_ID`：同一请求的 `x-client-id`

可选：`HTC_VERSION`、`HTC_COOKIE`。建议集中写在 `~/.huawei-training-camp/credentials.env`，MCP 用 `envFile` 或启动时 `source`，**不要把 Bearer 写进公共仓库或 `mcp.json` 正文**。

取凭证（用户自己在电脑浏览器做）：

1. 打开 https://health.huawei.com ，能看见自己的训练。
2. F12 → Network → 刷新。
3. 找 `activityRecord` 且状态 200，从 Request Headers 复制上面两行到本机 env 文件。
4. 重载 MCP，**新开对话**再拉数据。

过期会 401：按同样步骤换新值后重载。不要把 `127.0.0.1` 或完整 token 发到手机或聊天。

Cursor 会话里常见 server 名 `huawei-training-camp` / `user-huawei-training-camp`。先读当前 schema，禁止猜工具名。接通后先 `health_check`（可不带凭证，只探通路），再拉活动。

`~/.cursor/mcp.json` 形状（路径换成这台电脑；凭证走 env 文件）：

```json
"huawei-training-camp": {
  "command": "/absolute/path/to/python",
  "args": ["/absolute/path/to/huawei-training-camp-mcp/server.py"],
  "envFile": "/absolute/private/path/credentials.env"
}
```

## 排课前读什么

已接通则在写今日/本周课之前拉：最近活动 + 睡眠（有则加 HRV）。和高驰/佳明同时接了就都读，冲突时主观和症状优先。读不到就说未读到，改口述，禁止伪造。不要一次拉全库。位置采样不要复述坐标。

| 用途 | 工具 |
|---|---|
| 通不通 | `health_check` |
| 最近练了什么 | `get_recent_activities`（默认 `limit` 5，`lookback_days` 30，最大 730） |
| 某堂课曲线 / 摘要 | 先列表拿到 `activity_id`，再 `get_activity_detail` / `get_training_summary` / `get_session_metrics`。详情要在列表窗口里定位，窗口不够就把 `lookback_days` 调大 |
| 一周/一月总量 | `get_training_period_summary` |
| 近 N 天 vs 前 N 天 | `get_training_period_comparison` |
| 周趋势 / 环比 | `get_training_weekly_trend`、`get_training_weekly_trend_delta` |
| 睡眠 | `get_sleep_records`（默认近 14 天） |
| 静息心率 | `get_resting_heart_rate` |
| HRV | `get_hrv_stats`（默认 28 天；夜间 avgHrv 原样） |
| 跑力与预测配速 | `get_athletic_performance`（秒数原样） |
| PB | `get_personal_bests`（旧 PB 不是现能力） |

列表 `limit` 最大 100。排课默认：`get_recent_activities` 最近若干条 + `get_sleep_records` 昨晚到近几天。课表头三句：上次练了什么、身体/手表是否打架、因此今天执行 / 降档 / 休息。

本连接器**没有写回课表**工具。建议怎么练仍由本 skill 排；要进华为 App 日历请用户自己建。
