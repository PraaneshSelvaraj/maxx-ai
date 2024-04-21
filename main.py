from core.brain import Brain
from utils.stt import GoogleSpeechRecognition
from utils.tts import DeepgramTTS
from utils.systrayApp import SystemTrayRunner
from utils import sounds
import keyboard

stt = GoogleSpeechRecognition()
tts = DeepgramTTS(voice='aura-arcas-en')
brain = Brain(agentMode=True)

def awake():
    sounds.play_awake_sound()
    text = stt.synthesize()

    if text:
        sounds.play_process_sound()
        resp = brain.invoke(text)
        tts.speak(resp)

def on_key_press(event):
    if keyboard.is_pressed("ctrl+alt+space"):
        awake()

if __name__ == "__main__":
    keyboard.on_press(on_key_press)
    systemTrayRunner = SystemTrayRunner(awake)
    systemTrayRunner.run()