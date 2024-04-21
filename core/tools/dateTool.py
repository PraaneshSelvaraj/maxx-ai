from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
from typing import Type
from datetime import datetime

class DateInput(BaseModel):
    date_format: str = Field(description='used to specify the date format', default='%Y-%m-%d, %A')

class DateTool(BaseTool):
    name = "Get Current Date"
    description = "use only when the human wants to know the current date."
    # description = "Useful when you need to get the current date."
    description += " args: {'date_format': {'required':True, 'description': 'used to specify the date format', 'default': '%Y-%m-%d, %A', 'type': 'string'},}"
    args_schema: Type[BaseModel] = DateInput

    def _run(self, date_format: str, **kwargs) -> str: 

        return datetime.now().strftime(date_format)


    def _arun(self, date_format: str, **kwargs) -> str:
        raise NotImplementedError("This tool does not support async")