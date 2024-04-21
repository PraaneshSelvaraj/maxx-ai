
from utils.sounds import play_sound
import requests
import os

class WitaiTTS:
    def __init__(self, voice = 'rebecca'):
        self._auth_token = os.getenv('wit_ai_key')
        self.voice= voice

    def speak(self, text : str):
        data = { 'q': text, 'voice': self.voice}

        audio= requests.post(
        'https://api.wit.ai/synthesize',
        params={
            'v': '20220622',
        },
        headers={
            'Authorization': f'Bearer {self._auth_token}',
        },
        json=data,
        )

        with open("temp_speech.mp3", "wb") as f:
            f.write(audio.content)
        f.close()

        play_sound('temp_speech.mp3')
        os.remove("temp_speech.mp3")