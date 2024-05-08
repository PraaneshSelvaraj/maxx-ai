from . import tool_temp
from .timeTool import TimeTool
from .dateTool import DateTool
from .openWeatherMapTool import OpenWeatherMapTool
from .websiteOpener import WebsiteOpenerTool

def get_tools():
    return [
            TimeTool(),
            DateTool(),
            OpenWeatherMapTool(),
            WebsiteOpenerTool(),
        ]

def reset_all_tools():
    tool_temp.reset_all_temp()