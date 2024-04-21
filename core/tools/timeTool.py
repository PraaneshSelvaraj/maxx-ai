from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
from typing import Type
from datetime import datetime

class TimeInput(BaseModel):
    time_format : str = Field(description='used to specify the time format', default='%I:%M %p')

class TimeTool(BaseTool):
    name = "Get Current Time"
    description = "use only when the human wants to know the current time."
    # description = "Useful for when you need to get the current time."
    description += " args: {'time_format': {'required':True, 'description': 'used to specify the time format.', 'default': '%I:%M %p', 'type': 'string'},}"
    args_schema: Type[BaseModel] = TimeInput

    def _run(self, time_format: str, **kwargs) -> str: 
        return datetime.now().strftime(time_format)

    def _arun(self, time_format: str, **kwargs) -> str:
        raise NotImplementedError("This tool does not support async")