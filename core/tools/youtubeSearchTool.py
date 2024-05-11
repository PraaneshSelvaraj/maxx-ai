import json
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
from typing import Type
from youtube_search import YoutubeSearch
from . import tool_temp

class QueryInput(BaseModel):
    query : str = Field(description='query to be searched in youtube')

class YoutubeSearchTool(BaseTool):
    name = 'YoutubeSearchTool'
    description = 'useful for searching videos in youtube and returns the search result. The results are not visible to the human. Dont add links in final answer'
    description += "  args : {'query' :{'required':True, 'description': 'query to be searched in youtube', 'type': 'string'}, }"
    args_schema: Type[BaseModel] = QueryInput

    def _run(self, query : str, **kwargs) -> dict:
        results = YoutubeSearch(query, max_results=3).to_json()
        results = json.loads(results)
        
        videos = results['videos']
        formatted_results = []

        for video in videos:
            formatted_video = {
                'title': video.get('title', ''),
                'url': 'https://www.youtube.com'+ video.get('url_suffix', ''),
                'channel': video.get('channel', '')
            }
            formatted_results.append(formatted_video)
        data = {"results" : formatted_results}
        tool_temp.tools_used.append({"tool": "YoutubeSearchTool", "resp" : data})
        return data

    def _arun(self, query: str, **kwargs):
        raise NotImplementedError("This tool does not support async")