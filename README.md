# 农历传感器 (Lunar Calendar Sensor)

🌙 Home Assistant 农历传感器集成 - 显示农历日期、生肖、干支年、传统节日倒计时

[![hacs][hacs-badge]][hacs-url]
![GitHub release](https://img.shields.io/github/v/release/D1ts1337/ha-lunar-sensor)
![Home Assistant](https://img.shields.io/badge/Home_Assistant-2023.1+-blue)

## 功能特性

- 🌙 农历日期显示 (如：正月廿六)
- 🐴 生肖计算
- 📅 干支纪年 (如：丙午)
- 🏮 传统节日倒计时 (春节、端午、中秋等)
- ⏰ 自动更新 (每小时)

## 安装方法

### 方法 1: HACS 安装 (推荐)

1. 打开 HACS
2. 点击右上角 **⋮** → **自定义存储库**
3. 添加：
   - **存储库**: `https://github.com/D1ts1337/ha-lunar-sensor`
   - **类型**: `集成`
4. 搜索 `Lunar Calendar` 或 `农历` 并安装
5. 重启 Home Assistant
6. **设置** → **设备与服务** → **添加集成** → 搜索 `农历`

### 方法 2: 手动安装

```bash
# 通过 SSH 或 Samba 复制文件
cd /config/custom_components
git clone https://github.com/D1ts1337/ha-lunar-sensor.git lunar_calendar

# 或者手动下载并解压到 /config/custom_components/lunar_calendar
```

### 方法 3: 使用脚本安装

```bash
# 在 HA 终端执行
cd /config/custom_components
wget https://github.com/D1ts1337/ha-lunar-sensor/archive/refs/heads/main.zip
unzip main.zip
mv ha-lunar-sensor-main lunar_calendar
rm main.zip
```

## 提供的传感器

| 传感器 | 实体 ID | 说明 | 示例 |
|--------|---------|------|------|
| 农历日期 | `sensor.lunar_date` | 农历日期 | `正月廿六` |
| 农历年份 | `sensor.lunar_year` | 农历年份 | `2026` |
| 农历月份 | `sensor.lunar_month` | 农历月份 | `1` |
| 农历日期 | `sensor.lunar_day` | 农历日期 (数字) | `26` |
| 生肖 | `sensor.lunar_zodiac` | 生肖 | `马` |
| 干支年 | `sensor.lunar_gz_year` | 干支纪年 | `丙午` |
| 下一个节日 | `sensor.lunar_next_festival` | 下一个传统节日 | `龙抬头` |
| 节日倒计时 | `sensor.lunar_festival_countdown` | 倒计时天数 | `5` |

## Lovelace 卡片示例

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

## 支持的节日

### 传统节日 (农历)
- 春节 (正月初一)
- 元宵节 (正月十五)
- 龙抬头 (二月初二)
- 端午节 (五月初五)
- 七夕节 (七月初七)
- 中元节 (七月十五)
- 中秋节 (八月十五)
- 重阳节 (九月初九)
- 腊八节 (腊月初八)
- 小年 (腊月廿三)
- 除夕 (腊月三十)

## 依赖

- Python 3.8+
- lunardate >= 0.2.0 (自动安装)

## 故障排除

### 传感器不显示
1. 检查 `custom_components/lunar_calendar` 目录是否存在
2. 检查 `manifest.json` 文件格式
3. 查看 Home Assistant 日志

### 依赖安装失败
```bash
# 手动安装依赖
pip3 install lunardate
```

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 PR！

---

[hacs-badge]: https://img.shields.io/badge/HACS-Custom-orange.svg
[hacs-url]: https://github.com/hacs/integration
