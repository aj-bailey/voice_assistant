from app.adapters.open_ai_repository import OpenAIRepository
from app.entrypoints.voice_listener import VoiceListener
from app.utils.voice_transmitter import VoiceTransmitter
from dotenv import load_dotenv

load_dotenv()


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
                        text_response = open_ai_repository.query(phrase)
                        open_ai_repository.audio_response(text_response)
                        print(text_response)
                        VoiceTransmitter.transmit()

                        phrase_recorded = True

    print("Exiting...")


if __name__ == "__main__":
    main()
