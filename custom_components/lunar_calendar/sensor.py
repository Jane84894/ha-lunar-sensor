"""农历传感器平台"""
from datetime import timedelta
import logging
from lunardate import LunarDate
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import Entity
from homeassistant.util import dt as dt_util

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(hours=1)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """设置传感器平台"""
    sensors = [
        LunarDateSensor(),
        LunarYearSensor(),
        LunarMonthSensor(),
        LunarDaySensor(),
        ZodiacSensor(),
        GzYearSensor(),
        NextFestivalSensor(),
        FestivalCountdownSensor(),
    ]
    add_entities(sensors, True)


class LunarDateSensor(SensorEntity):
    """农历日期传感器"""
    
    _attr_name = "农历日期"
    _attr_icon = "mdi:calendar-star"
    _attr_unique_id = "lunar_date"
    
    def __init__(self):
        self._state = None
        self._attributes = {}
    
    @property
    def state(self):
        return self._state
    
    @property
    def extra_state_attributes(self):
        return self._attributes
    
    def update(self):
        lunar = LunarDate.today()
        month_cn = ["正", "二", "三", "四", "五", "六", "七", "八", "九", "十", "冬", "腊"]
        day_cn = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
                  "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十",
                  "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"]
        
        lunar_month_str = month_cn[lunar.month - 1] if lunar.month <= 12 else "腊月"
        lunar_day_str = day_cn[lunar.day - 1] if lunar.day <= 30 else "初一"
        
        self._state = f"{lunar_month_str}月{lunar_day_str}"
        self._attributes = {
            'lunar_year': lunar.year,
            'lunar_month': lunar.month,
            'lunar_day': lunar.day,
        }


class LunarYearSensor(Entity):
    """农历年份传感器"""
    
    _attr_name = "农历年份"
    _attr_icon = "mdi:calendar-month"
    _attr_unique_id = "lunar_year"
    
    def __init__(self):
        self._state = None
    
    @property
    def state(self):
        return self._state
    
    def update(self):
        lunar = LunarDate.today()
        self._state = lunar.year


class LunarMonthSensor(Entity):
    """农历月份传感器"""
    
    _attr_name = "农历月份"
    _attr_icon = "mdi:calendar-month"
    _attr_unique_id = "lunar_month"
    
    def __init__(self):
        self._state = None
    
    @property
    def state(self):
        return self._state
    
    def update(self):
        lunar = LunarDate.today()
        self._state = lunar.month


class LunarDaySensor(Entity):
    """农历日期传感器"""
    
    _attr_name = "农历日期"
    _attr_icon = "mdi:calendar-day"
    _attr_unique_id = "lunar_day"
    
    def __init__(self):
        self._state = None
    
    @property
    def state(self):
        return self._state
    
    def update(self):
        lunar = LunarDate.today()
        self._state = lunar.day


class ZodiacSensor(Entity):
    """生肖传感器"""
    
    _attr_name = "生肖"
    _attr_icon = "mdi:zodiac"
    _attr_unique_id = "lunar_zodiac"
    
    def __init__(self):
        self._state = None
    
    @property
    def state(self):
        return self._state
    
    def update(self):
        lunar = LunarDate.today()
        zodiacs = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
        branch_idx = (lunar.year - 4) % 12
        self._state = zodiacs[branch_idx]


class GzYearSensor(Entity):
    """干支年传感器"""
    
    _attr_name = "干支年"
    _attr_icon = "mdi:calendar-text"
    _attr_unique_id = "lunar_gz_year"
    
    def __init__(self):
        self._state = None
    
    @property
    def state(self):
        return self._state
    
    def update(self):
        lunar = LunarDate.today()
        stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        stem_idx = (lunar.year - 4) % 10
        branch_idx = (lunar.year - 4) % 12
        self._state = f"{stems[stem_idx]}{branches[branch_idx]}"


class NextFestivalSensor(Entity):
    """下一个传统节日传感器"""
    
    _attr_name = "下一个传统节日"
    _attr_icon = "mdi:celebration"
    _attr_unique_id = "lunar_next_festival"
    
    def __init__(self):
        self._state = None
        self._attributes = {}
    
    @property
    def state(self):
        return self._state
    
    @property
    def extra_state_attributes(self):
        return self._attributes
    
    def update(self):
        lunar = LunarDate.today()
        festivals = {
            "春节": (1, 1), "元宵节": (1, 15), "龙抬头": (2, 2),
            "端午节": (5, 5), "七夕节": (7, 7), "中元节": (7, 15),
            "中秋节": (8, 15), "重阳节": (9, 9), "腊八节": (12, 8),
            "小年": (12, 23), "除夕": (12, 30),
        }
        
        next_festival = None
        min_days = 9999
        
        for name, (month, day) in festivals.items():
            if (lunar.month < month) or (lunar.month == month and lunar.day < day):
                days = (month - lunar.month) * 29 + (day - lunar.day)
            else:
                days = (12 - lunar.month + month) * 29 + (day - lunar.day)
            
            if 0 < days < min_days:
                min_days = days
                next_festival = name
        
        self._state = next_festival
        self._attributes = {'days_until': min_days if min_days < 9999 else None}


class FestivalCountdownSensor(Entity):
    """节日倒计时传感器"""
    
    _attr_name = "节日倒计时"
    _attr_icon = "mdi:timer-sand"
    _attr_unique_id = "lunar_festival_countdown"
    _attr_native_unit_of_measurement = "天"
    
    def __init__(self):
        self._state = None
    
    @property
    def state(self):
        return self._state
    
    def update(self):
        lunar = LunarDate.today()
        festivals = {
            "春节": (1, 1), "元宵节": (1, 15), "龙抬头": (2, 2),
            "端午节": (5, 5), "七夕节": (7, 7), "中元节": (7, 15),
            "中秋节": (8, 15), "重阳节": (9, 9), "腊八节": (12, 8),
            "小年": (12, 23), "除夕": (12, 30),
        }
        
        min_days = 9999
        
        for name, (month, day) in festivals.items():
            if (lunar.month < month) or (lunar.month == month and lunar.day < day):
                days = (month - lunar.month) * 29 + (day - lunar.day)
            else:
                days = (12 - lunar.month + month) * 29 + (day - lunar.day)
            
            if 0 < days < min_days:
                min_days = days
        
        self._state = min_days if min_days < 9999 else None
