import os
from gtts import gTTS

class VoiceTransmitter():
    @classmethod
    def transmit(cls, message) -> None:
        speech = gTTS(text=message)
        speech_file = "speech.mp3"
        speech.save(speech_file)
        os.system('afplay '+ speech_file)