"""农历传感器集成配置流程"""
from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol

from .const import DOMAIN


class LunarCalendarConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """农历传感器配置流程"""
    
    VERSION = 1
    
    async def async_step_user(self, user_input=None):
        """用户初始化配置"""
        if user_input is not None:
            return self.async_create_entry(title="农历传感器", data={})
        
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
            description_placeholders={},
        )
    
    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """获取选项流程"""
        return LunarCalendarOptionsFlow(config_entry)


class LunarCalendarOptionsFlow(config_entries.OptionsFlow):
    """农历传感器选项流程"""
    
    def __init__(self, config_entry):
        """初始化"""
        self.config_entry = config_entry
    
    async def async_step_init(self, user_input=None):
        """管理选项"""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({}),
        )
