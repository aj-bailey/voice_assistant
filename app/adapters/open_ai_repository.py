from openai import OpenAI

class OpenAIRepository():
    def __init__(self):
        self.client = OpenAI()

    def query(self, message):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return completion.choices[0].message.content
    
    def audio_response(self, message):
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=message,
        )

        response.stream_to_file("speech.mp3")