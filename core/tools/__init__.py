from .timeTool import TimeTool
from .dateTool import DateTool
from .openWeatherMapTool import OpenWeatherMapTool

def get_tools():
    return [
            TimeTool(),
            DateTool(),
            OpenWeatherMapTool(),
        ]