# 农历传感器 (Lunar Calendar Sensor)

🌙 Home Assistant 农历传感器集成 - 显示农历日期、生肖、干支年、传统节日倒计时

[![hacs][hacs-badge]][hacs-url]
![GitHub release](https://img.shields.io/github/v/release/Jane84894/ha-lunar-sensor)
![Home Assistant](https://img.shields.io/badge/Home_Assistant-2023.1+-blue)

## ✨ 功能特性

- 🌙 农历日期显示 (如：正月廿六)
- 🐴 生肖计算
- 📅 干支纪年 (如：丙午)
- 🏮 传统节日倒计时 (春节、端午、中秋等)
- ⏰ 自动更新 (每小时)
- ✅ **支持 UI 直接添加** (无需配置 yaml)

## 🚀 快速安装

### 方法 1: HACS 安装 (推荐) ⭐

1. **打开 HACS** → 左侧菜单
2. **点击右上角 ⋮** → **自定义存储库**
3. **添加存储库**:
   ```
   存储库：https://github.com/Jane84894/ha-lunar-sensor
   类型：集成
   ```
4. **搜索并安装**:
   - 搜索 `Lunar Calendar` 或 `农历`
   - 点击进入 → 点击 **下载**
5. **重启 Home Assistant**
6. **添加集成**:
   - 设置 → 设备与服务 → **添加集成**
   - 搜索 `农历` 或 `Lunar`
   - 点击提交 (无需配置)

### 方法 2: 手动安装

```bash
# SSH 到 Home Assistant
cd /config/custom_components
git clone https://github.com/Jane84894/ha-lunar-sensor.git lunar_calendar

# 重启 Home Assistant
ha core restart
```

### 方法 3: 下载 ZIP 安装

1. 下载：https://github.com/Jane84894/ha-lunar-sensor/archive/refs/heads/main.zip
2. 解压到 `/config/custom_components/lunar_calendar`
3. 重启 Home Assistant

## 📊 提供的传感器

安装后自动创建以下实体：

| 实体 ID | 说明 | 示例值 |
|--------|------|--------|
| `sensor.lunar_date` | 农历日期 | `正月廿六` |
| `sensor.lunar_year` | 农历年份 | `2026` |
| `sensor.lunar_month` | 农历月份 | `1` |
| `sensor.lunar_day` | 农历日期 (数字) | `26` |
| `sensor.lunar_zodiac` | 生肖 | `马` |
| `sensor.lunar_gz_year` | 干支年 | `丙午` |
| `sensor.lunar_next_festival` | 下一个传统节日 | `龙抬头` |
| `sensor.lunar_festival_countdown` | 节日倒计时 | `5` 天 |

## 🎨 Lovelace 卡片示例

### 基础卡片

```yaml
type: entities
title: 🌙 农历
entities:
  - entity: sensor.lunar_date
    name: 农历日期
  - entity: sensor.lunar_zodiac
    name: 生肖
  - entity: sensor.lunar_gz_year
    name: 干支
  - type: divider
  - entity: sensor.lunar_next_festival
    name: 下一个节日
  - entity: sensor.lunar_festival_countdown
    name: 倒计时
    suffix: 天
```

### 高级卡片 (带图标)

```yaml
type: glance
entities:
  - entity: sensor.lunar_date
    icon: mdi:calendar-star
  - entity: sensor.lunar_zodiac
    icon: mdi:dragon
  - entity: sensor.lunar_gz_year
    icon: mdi:calendar-text
  - entity: sensor.lunar_next_festival
    icon: mdi:celebration
```

## 🏮 支持的节日

### 传统节日 (农历)
- ✅ 春节 (正月初一)
- ✅ 元宵节 (正月十五)
- ✅ 龙抬头 (二月初二)
- ✅ 端午节 (五月初五)
- ✅ 七夕节 (七月初七)
- ✅ 中元节 (七月十五)
- ✅ 中秋节 (八月十五)
- ✅ 重阳节 (九月初九)
- ✅ 腊八节 (腊月初八)
- ✅ 小年 (腊月廿三)
- ✅ 除夕 (腊月三十)

## ❓ 常见问题

### Q: 集成无法通过 UI 添加？
**A**: 确保版本 >= 1.0.0，已支持 config_flow

### Q: 传感器不显示？
**A**: 
1. 检查 `/config/custom_components/lunar_calendar` 目录
2. 重启 Home Assistant
3. 查看 开发者工具 → 状态 → 搜索 `lunar`

### Q: 提示缺少依赖？
**A**: 
```bash
# SSH 到 HA 终端
pip3 install lunardate
```

### Q: 数据不更新？
**A**: 传感器每小时更新一次，可手动重启 HA

### Q: 如何卸载？
**A**: 
1. 设置 → 设备与服务 → 找到农历传感器
2. 点击三个点 → 删除
3. 删除 `/config/custom_components/lunar_calendar` 目录

## 📝 更新日志

### v1.0.0 (2026-03-14)
- ✅ 初始版本发布
- ✅ 支持 UI 直接添加 (config_flow)
- ✅ 农历日期显示
- ✅ 生肖计算
- ✅ 干支纪年
- ✅ 传统节日倒计时
- ✅ 自动更新

## 📄 许可证

MIT License

## 💖 贡献

欢迎提交 Issue 和 PR！

**仓库**: https://github.com/Jane84894/ha-lunar-sensor

---

[hacs-badge]: https://img.shields.io/badge/HACS-Custom-orange.svg
[hacs-url]: https://github.com/hacs/integration
