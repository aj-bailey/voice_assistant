import os
from gtts import gTTS

class VoiceTransmitter():
    @classmethod
    def transmit(cls, message=None) -> None:
        speech_file = "speech.mp3"

        if message:
            speech = gTTS(text=message)
            speech.save(speech_file)

        os.system('afplay '+ speech_file)