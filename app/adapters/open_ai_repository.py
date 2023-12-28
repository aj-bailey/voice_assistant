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