from . import tool_temp
from .timeTool import TimeTool
from .dateTool import DateTool
from .openWeatherMapTool import OpenWeatherMapTool
from .websiteOpener import WebsiteOpenerTool
from .youtubeSearchTool import YoutubeSearchTool
from .screenshotTool import ScreenshotTool
from .spotifySearchTool import SpotifySearchTool
from .spotifyPlayTool import SpotifyPlayTool

def get_tools():
    return [
            TimeTool(),
            DateTool(),
            OpenWeatherMapTool(),
            WebsiteOpenerTool(),
            YoutubeSearchTool(),
            ScreenshotTool(),
            SpotifySearchTool(),
            SpotifyPlayTool(),
        ]

def reset_all_tools():
    tool_temp.reset_all_temp()

def get_tools_used():
    return tool_temp.get_tools_used()