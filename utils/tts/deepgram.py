import os
from utils.sounds import play_sound
import subprocess
import requests

class DeepgramTTS:
    def __init__(self, voice='aura-asteria-en'):
        self.voice = voice
        self.deepgram_api_key = os.getenv("deepgram_api_key")
        
    
    def stream(self, text: str):
        DEEPGRAM_URL = f"https://api.deepgram.com/v1/speak?model={self.voice}&performance=some&encoding=linear16&sample_rate=24000"
        headers = {
            "Authorization": f"Token {self.deepgram_api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "text": text
        }

        player_command = ["ffplay", "-autoexit", "-", "-nodisp"]
        player_process = subprocess.Popen(
            player_command,
            stdin=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        with requests.post(DEEPGRAM_URL, stream=True, headers=headers, json=payload) as r:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    player_process.stdin.write(chunk)
                    player_process.stdin.flush()
                    
        if player_process.stdin:
            player_process.stdin.close()
        player_process.wait()
    
    def speak(self, text:str):
        url = f"https://api.deepgram.com/v1/speak?model={self.voice}"
        headers = {
            "Authorization": f"Token {self.deepgram_api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "text": text
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            with open("temp_speech.mp3", "wb") as f:
                f.write(response.content)
            f.close()

            play_sound('temp_speech.mp3')
            os.remove("temp_speech.mp3")

        else:
            print(response.content, response.status_code)