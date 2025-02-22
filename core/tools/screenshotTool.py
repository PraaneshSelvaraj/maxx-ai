from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
from typing import Type


class ScreenshotInput(BaseModel):
    fullscreen: bool = Field(description='True, for full screen screenshot', default=True)

class ScreenshotTool(BaseTool):
    name = "ScreenshotTool"
    description = "use only when the human wants to take screenshot"
    description += " args: {'fullscreen': {'required':True, 'description': 'True, for full screen screenshot', 'default': True, 'type': 'boolean'},}"
    args_schema: Type[BaseModel] = ScreenshotInput

    def _run(self, fullscreen: bool, **kwargs) -> str: 
        return {"message" : "Screenshot has successfully captured."}


    def _arun(self, fullscreen: bool, **kwargs) -> str:
        raise NotImplementedError("This tool does not support async")