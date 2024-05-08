import webbrowser
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
from typing import Type
from . import tool_temp

class UrlInput(BaseModel):
    url : str = Field(description='url which needs to be opened in browser')

class WebsiteOpenerTool(BaseTool):
    name='WebsiteOpenerTool'
    description = 'This tool will open the url in browser.'
    description += " args : {'url' :{'required':True, 'description': 'url which needs to be opened in browser', 'type': 'string'}, }"
    description += "returns : {'success' : {'type':'bool', 'description':'True - when successfully opened. False - when failure.'} }"
    args_schema: Type[BaseModel] = UrlInput    

    def _run(self, url : str, **kwargs) -> str:
        print(tool_temp.opened_urls_website_opener)
        if url in tool_temp.opened_urls_website_opener:
            return {'success': False, 'message': f"The URL '{url}' has already been opened. give final answer"}
        webbrowser.open(url)
        tool_temp.opened_urls_website_opener.append(url)
        print(tool_temp.opened_urls_website_opener)
        data = {'success' : True}
        return data
    
    def _arun(self, url: str, **kwargs):
        raise NotImplementedError("This tool does not support async")