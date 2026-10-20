# 佳明恢复指标怎么查

HRV、压力、Body Battery、训练准备度、负荷、VO2max、比赛预测。按问题选工具，不要每次拉全套。排课仍走知识大脑；这些是厂商模型，不单独决定间歇。

日期一律 `YYYY-MM-DD`。单日用 `date`，范围用 `startDate`/`endDate`，含首尾。MCP 不传 `account`。

| 问题 | 工具 |
|---|---|
| 某晚 HRV、基线、夜间点 | `get_garmin_hrv` |
| 一周或数周 HRV 趋势 | `get_garmin_hrv_summaries` |
| 某天压力 | `get_garmin_stress` |
| 一段时间压力 | `get_garmin_stress_summaries` |
| Body Battery | `get_garmin_body_battery` |
| 当天训练准备度 | `get_garmin_training_readiness` |
| 某天训练状态、急慢性负荷 | `get_garmin_daily_training_status` |
| 聚合训练状态 | `get_garmin_training_status` |
| 四周负荷平衡 | `get_garmin_training_load_balance` |
| 单日 / 一段时间 Max Metrics | `get_garmin_max_metrics` / `get_garmin_max_metrics_range` |
| 当前比赛预测 | `get_garmin_race_predictions`（无日期） |
| 预测历史 | `get_garmin_race_predictions_range`（首尾差 ≤366 天） |

「最近一周 HRV」先 summaries，某一晚再 `get_garmin_hrv`。`weeklyAvg`、`lastNightAvg`、`lastNight5MinHigh` 不要混用。没有状态不等于恢复差。

「今天能不能上质量」：准备度 + 完整睡眠日 + 近期活动 + 主观。准备度快照要标明时间（起床 / 运动前 / 后），旧快照不能叫「现在」。

`null`、空数组不是零。缺工具就说当前连接没有这项，继续用已有数据。认证错误走登录，不要写成「无数据」。不要从心率推算 HRV，不要自制恢复分。
