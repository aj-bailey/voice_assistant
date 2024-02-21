from app.utils.voice_transmitter import VoiceTransmitter

import speech_recognition as sr


class VoiceListener():
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_for_trigger(self) -> bool:
        with sr.Microphone() as source:
            print("Listening for 'Hey Raspberry'...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            spoken_text = self.recognizer.recognize_google(audio).lower()

            print(f"You said: {spoken_text}")
            if "hey raspberry" in spoken_text:
                VoiceTransmitter.transmit(message="Hi")
                return True
            else:
                return False
        except sr.UnknownValueError:
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    def record_phrase(self):
        with sr.Microphone() as source:
            print("Recording next phrase...")

            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=5)  # Record for up to 5 seconds

        try:
            spoken_text = self.recognizer.recognize_google(audio)
            print(f"Recorded phrase: {spoken_text}")

            return spoken_text
        except sr.UnknownValueError:
            print("Unable to understand the recorded phrase.")
            VoiceTransmitter.transmit(message="I didn't catch that")
        except sr.RequestError as e:
            print(f"Error: {e}")

            return None
