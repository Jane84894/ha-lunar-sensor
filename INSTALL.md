# 快速安装指南

## 方法 1: HACS 安装 (最简单)

1. **打开 HACS**
   - 左侧菜单 → HACS

2. **添加自定义存储库**
   - 点击右上角 **⋮** (三个点)
   - 选择 **自定义存储库**
   - 输入：
     - 存储库：`https://github.com/Jane84894/ha-lunar-sensor`
     - 类型：`集成`
   - 点击 **添加**

3. **安装集成**
   - 搜索 `Lunar Calendar` 或 `农历`
   - 点击进入
   - 点击 **下载**
   - 选择最新版本

4. **重启 Home Assistant**
   - 设置 → 系统 → 重启

5. **添加集成**
   - 设置 → 设备与服务 → 添加集成
   - 搜索 `农历` 或 `Lunar`
   - 点击安装

---

## 方法 2: 手动安装

### 步骤 1: 下载文件

```bash
# SSH 到 Home Assistant
cd /config/custom_components
wget https://github.com/Jane84894/ha-lunar-sensor/archive/refs/heads/main.zip
```

### 步骤 2: 解压

```bash
unzip main.zip
mv ha-lunar-sensor-main lunar_calendar
rm main.zip
```

### 步骤 3: 安装依赖

```bash
# 在 HA 终端执行
pip3 install lunardate
```

### 步骤 4: 重启 HA

```bash
ha core restart
```

---

## 验证安装

1. 打开 **开发者工具** → **状态**
2. 搜索 `lunar`
3. 应该看到以下实体：
   - `sensor.lunar_date` - 农历日期
   - `sensor.lunar_zodiac` - 生肖
   - `sensor.lunar_gz_year` - 干支年
   - `sensor.lunar_next_festival` - 下一个节日
   - `sensor.lunar_festival_countdown` - 节日倒计时

---

## 常见问题

### Q: 传感器不显示？
A: 检查 `/config/custom_components/lunar_calendar` 目录是否存在

### Q: 提示缺少依赖？
A: 在 HA 终端执行 `pip3 install lunardate`

### Q: 数据不更新？
A: 传感器每小时更新一次，可以手动重启 HA

---

**仓库地址**: https://github.com/Jane84894/ha-lunar-sensor
