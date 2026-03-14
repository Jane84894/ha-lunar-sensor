# Home Assistant 农历传感器

🌙 基于 Home Assistant 的农历日期显示 + 传统节日倒计时

![GitHub](https://img.shields.io/github/license/D1ts1337/ha-lunar-sensor)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Home Assistant](https://img.shields.io/badge/Home_Assistant-2023.1+-blue)

---

## 🎯 功能特性

- 🌙 **农历日期显示** - 格式：正月廿六
- 🐴 **生肖计算** - 自动计算生肖
- 📅 **干支纪年** - 丙午年
- 🏮 **传统节日倒计时** - 春节、端午、中秋等
- 🎉 **法定节假日倒计时** - 劳动节、国庆节等
- ⏰ **自动更新** - 每天午夜自动刷新

---

## 📦 安装方法

### 方法 1: 一键安装脚本 (推荐)

```bash
# 克隆仓库
git clone https://github.com/D1ts1337/ha-lunar-sensor.git
cd ha-lunar-sensor

# 运行安装脚本
bash install.sh
```

### 方法 2: 手动安装

```bash
# 1. 复制脚本到 HA 配置目录
cp lunar_sensor.py /config/python_scripts/

# 2. 安装依赖
pip3 install lunardate --break-system-packages

# 3. 在 configuration.yaml 中添加
python_script:

# 4. 重启 Home Assistant
ha core restart

# 5. 手动运行测试
python3 /config/python_scripts/lunar_sensor.py
```

### 方法 3: HACS 安装 (待支持)

> 后续会添加到 HACS 商店

---

## 🔧 配置

### 1️⃣ 添加自动化 (可选)

编辑 `automations.yaml`:

```yaml
automation:
  - alias: "🌙 每日更新农历"
    trigger:
      - platform: time
        hours: 0
        minutes: 0
    action:
      - service: python_script.lunar_sensor
```

或直接使用提供的 `lunar_automation.yaml`:

```bash
cp lunar_automation.yaml /config/automations/
```

### 2️⃣ 配置通知 (可选)

```yaml
notify:
  - platform: persistent_notification
```

---

## 📊 生成的实体

运行后自动创建:

### 主实体
```yaml
sensor.lunar_date
```

### 实体属性

| 属性 | 类型 | 示例值 | 说明 |
|------|------|--------|------|
| `state` | string | `正月廿六` | 农历日期 |
| `gregorian_date` | string | `2026-03-14` | 公历日期 |
| `lunar_year` | int | `2026` | 农历年份 |
| `lunar_month` | int | `1` | 农历月份 |
| `lunar_day` | int | `26` | 农历日期 |
| `gz_year` | string | `丙午` | 干支年 |
| `zodiac` | string | `马` | 生肖 |
| `week_cn` | string | `六` | 星期 (中文) |
| `next_traditional` | string | `龙抬头` | 下一个传统节日 |
| `next_traditional_days` | int | `5` | 节日倒计时 (天) |
| `next_traditional_date` | string | `2026 年二月初二` | 节日农历日期 |
| `next_public` | string | `劳动节` | 下一个法定节假日 |
| `next_public_days` | int | `48` | 法定节日倒计时 |

---

## 🖥️ 使用示例

### Lovelace 卡片

```yaml
type: entities
title: 🌙 农历
entities:
  - entity: sensor.lunar_date
    name: 农历日期
  - entity: sensor.lunar_date
    name: 公历
    attribute: gregorian_date
  - entity: sensor.lunar_date
    name: 生肖
    attribute: zodiac
  - entity: sensor.lunar_date
    name: 干支
    attribute: gz_year
  - type: divider
  - entity: sensor.lunar_date
    name: 🏮 下一个传统节日
    attribute: next_traditional
  - entity: sensor.lunar_date
    name: 倒计时
    attribute: next_traditional_days
    suffix: 天
```

### ESPHome 集成

```yaml
text_sensor:
  - platform: homeassistant
    id: ha_lunar_date
    entity_id: sensor.lunar_date
  
  - platform: homeassistant
    id: ha_zodiac
    entity_id: sensor.lunar_date
    attribute: zodiac

sensor:
  - platform: homeassistant
    id: ha_festival_days
    entity_id: sensor.lunar_date
    attribute: next_traditional_days
```

---

## 🏮 支持的节日

### 传统节日 (农历)
- 春节 (正月初一)
- 元宵节 (正月十五)
- 龙抬头 (二月初二)
- 上巳节 (三月初三)
- 端午节 (五月初五)
- 七夕节 (七月初七)
- 中元节 (七月十五)
- 中秋节 (八月十五)
- 重阳节 (九月初九)
- 下元节 (十月十五)
- 腊八节 (腊月初八)
- 小年 (腊月廿三)
- 除夕 (腊月三十)

### 法定节假日 (公历)
- 元旦 (1 月 1 日)
- 妇女节 (3 月 8 日)
- 劳动节 (5 月 1 日)
- 青年节 (5 月 4 日)
- 儿童节 (6 月 1 日)
- 建党节 (7 月 1 日)
- 建军节 (8 月 1 日)
- 教师节 (9 月 10 日)
- 国庆节 (10 月 1 日)

---

## 🔍 故障排除

### 脚本运行失败

```bash
# 检查 lunardate 是否安装
pip3 list | grep lunar

# 手动测试脚本
python3 /config/python_scripts/lunar_sensor.py

# 查看 HA 日志
ha core logs | grep lunar
```

### 实体未创建

1. 确认 `python_script:` 已在 `configuration.yaml` 中启用
2. 检查 HA 日志是否有错误
3. 手动运行脚本查看输出

### 农历日期不准确

- 脚本使用 `lunardate` 库计算，确保库是最新版
- 每天午夜自动更新，或手动调用服务刷新

---

## 📁 文件说明

```
ha-lunar-sensor/
├── README.md                 # 本文件
├── lunar_sensor.py           # 农历传感器脚本
├── lunar_automation.yaml     # HA 自动化配置
├── install.sh                # 一键安装脚本
└── requirements.txt          # Python 依赖
```

---

## 🤝 贡献

欢迎提交 Issue 和 PR!

- 🐛 Bug 报告
- 🎉 新功能建议
- 📝 文档完善
- 🔧 代码优化

---

## 📄 许可证

MIT License

---

## 🙏 致谢

- [lunardate](https://pypi.org/project/lunardate/) - 农历计算库
- [Home Assistant](https://www.home-assistant.io/) - 智能家居平台
- [ESPHome](https://esphome.io/) - ESP 设备配置

---

## 📬 联系方式

- GitHub: [@D1ts1337](https://github.com/D1ts1337)
- 问题反馈：[Issues](https://github.com/D1ts1337/ha-lunar-sensor/issues)

---

**⭐ 如果这个项目对你有帮助，请给个 Star!**
