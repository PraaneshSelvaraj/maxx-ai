import speech_recognition as sr

class GoogleSpeechRecognition:
    def __init__(self):
        self.r = sr.Recognizer()

    def synthesize(self):
        with sr.Microphone() as source:
            self.r.pause_threshold =  1.5
            self.r.adjust_for_ambient_noise(source, duration=1)
            self.r.energy_threshold = 2000
            self.r.dynamic_energy_threshold = True
            audio = self.r.listen(source,timeout=10,phrase_time_limit=5)
            said = ""

            try:
                said = self.r.recognize_google(audio)
                said = said.lower()

            except Exception as e:
                print(e)

        return said