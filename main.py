import os

from app.adapters.open_ai_repository import OpenAIRepository
from app.entrypoints.voice_listener import VoiceListener
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_API_KEY = os.environ.get('OPEN_AI_API_KEY')

def main():
    vl = VoiceListener()
    open_ai_repository = OpenAIRepository()
    continue_listening = True

    while continue_listening:
        if vl.listen_for_trigger():
            phrase_recorded = False

            while not phrase_recorded:
                phrase = vl.record_phrase()
                
                if phrase:
                    if phrase == 'stop listening':
                        phrase_recorded = True
                    elif phrase == 'exit':
                        phrase_recorded = True
                        continue_listening = False
                    else:
                        response = open_ai_repository.query(phrase)
                        print(response)
                        phrase_recorded = True

    print("Exiting...")

if __name__ == "__main__":
    main()