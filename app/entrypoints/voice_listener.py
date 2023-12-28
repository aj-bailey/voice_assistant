import os
from gtts import gTTS
import speech_recognition as sr


class VoiceListener():
  def listen_for_trigger() -> bool:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for 'Hey Raspberry'...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        spoken_text = recognizer.recognize_google(audio).lower()
        
        print(f"You said: {spoken_text}")
        if "hey raspberry" in spoken_text:
            speech = gTTS(text="what bitch?", tld='com.au', lang='en')
            speech_file = "speech.mp3"
            speech.save(speech_file)
            os.system('afplay '+ speech_file)
            return True
        else:
            return False
    except sr.UnknownValueError:
        return False
    except sr.RequestError as e:
        print(f"Error: {e}")
        return False
