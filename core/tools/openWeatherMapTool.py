from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
from typing import Type
import pyowm
import os

owm = pyowm.OWM(os.getenv('owm_api_key'))
weatherManager = owm.weather_manager()

class CityInput(BaseModel):
    city : str = Field(description='used to the specify city')

class OpenWeatherMapTool(BaseTool):
    name='OpenWeatherMapTool'
    description = "use only when the human wants to know current weather of a city using open weather map api."
    description += " args : {'city' :{'required':True, 'description': 'used to specify the city', 'type': 'string'}, }"
    args_schema: Type[BaseModel] = CityInput

    def _run(self, city : str, **kwargs) -> dict:
        observation = weatherManager.weather_at_place(city)
        temperature = observation.weather.temperature("celsius")["temp"]
        humidity = observation.weather.humidity

        return {"temperature" : f"{temperature} degree celsius", "humidity" : f"{humidity}%"}

    def _arun(self, city: str, **kwargs):
        raise NotImplementedError("This tool does not support async")