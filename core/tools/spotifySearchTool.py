import json
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
from typing import Type, Optional
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from . import tool_temp
import os
from dotenv import load_dotenv

load_dotenv()

class SpotifyQueryInput(BaseModel):
    query: str = Field(description='Song name to be searched on Spotify')
    artist: Optional[str] = Field(None, description='Artist name to refine the search')

class SpotifySearchTool(BaseTool):
    name = 'SpotifySearchTool'
    description = ('Useful for searching songs on Spotify and returning search results. '
                   'Does not display links or spotify ids to the user. '
                   "args: {'query': {'required': True, 'description': 'Song name to search on Spotify', 'type': 'string'}, "
                   "'artist': {'required': False, 'description': 'Artist name to refine the search', 'type': 'string'}}")
    args_schema: Type[BaseModel] = SpotifyQueryInput

    class Config:
        arbitrary_types_allowed = True

    def __init__(self):
        super().__init__()
        object.__setattr__(self, "sp", spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope="user-library-read",
            cache_path="token.json",

        )))

    def _run(self, query: str, artist: Optional[str] = None, **kwargs) -> dict:
        search_query = f"track:{query}"
        if artist:
            search_query += f" artist:{artist}"
        
        results = self.sp.search(q=search_query, limit=3, type="track")
        songs = []

        if results['tracks']['items']:
            for track in results['tracks']['items']:
                name = track["name"]
                track_artist = track["artists"][0]["name"]
                track_id = track["id"]
                
                songs.append({
                    "title": name,
                    "artist": track_artist,
                    "spotify_id": track_id
                })
        
        data = {"results": songs}
        tool_temp.tools_used.append({"tool": "SpotifySearchTool", "resp": data})
        return data

    def _arun(self, query: str, **kwargs):
        raise NotImplementedError("This tool does not support async")
