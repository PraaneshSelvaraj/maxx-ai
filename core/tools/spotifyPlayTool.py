import json
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
from typing import Type
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from . import tool_temp
import os
from dotenv import load_dotenv

load_dotenv()

class SpotifyPlayInput(BaseModel):
    spotify_id: str = Field(description="Spotify Track ID of the song to play. Use SpotifySearchTool to get this ID.")
    add_to_queue: bool = Field(default=False, description="Set to True if the song should be added to the queue instead of playing immediately.")

class SpotifyPlayTool(BaseTool):
    name = 'SpotifyPlayTool'
    description = ('Plays a song on Spotify using the track ID or adds it to the queue if explicitly requested. '
                   "You must first use SpotifySearchTool to get the song's ID. "
                   "args: {'spotify_id': {'required': True, 'description': 'Spotify Track ID of the song', 'type': 'string'}, "
                   "'add_to_queue': {'required': False, 'description': 'Set True to add to queue', 'type': 'boolean'}}")
    args_schema: Type[BaseModel] = SpotifyPlayInput

    class Config:
        arbitrary_types_allowed = True

    def __init__(self):
        super().__init__()
        object.__setattr__(self, "sp", spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope="user-modify-playback-state user-read-playback-state",
            cache_path="token.json",
        )))

    def _run(self, spotify_id: str, add_to_queue: bool = False, **kwargs) -> dict:
        devices = self.sp.devices()
        available_devices = devices.get("devices", [])

        if not available_devices:
            return {"error": "No active Spotify device found. Please open Spotify on a device."}

        device_id = available_devices[0]["id"]

        if add_to_queue:
            self.sp.add_to_queue(uri=f"spotify:track:{spotify_id}", device_id=device_id)
            response = {
                "status": "Queued",
                "spotify_id": spotify_id,
                "device_id": device_id,
                "message": "Song added to queue. If you didn't have the ID, use SpotifySearchTool first."
            }
        else:

            self.sp.start_playback(device_id=device_id, uris=[f"spotify:track:{spotify_id}"])
            response = {
                "status": "Playing",
                "spotify_id": spotify_id,
                "device_id": device_id,
                "message": "Playing song now. If you didn't have the ID, use SpotifySearchTool first."
            }

        tool_temp.tools_used.append({"tool": "SpotifyPlayTool", "resp": response})
        return response

    def _arun(self, spotify_id: str, add_to_queue: bool = False, **kwargs):
        raise NotImplementedError("This tool does not support async")
