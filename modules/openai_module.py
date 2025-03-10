from openai import OpenAI
from credentials import OpenAICredentials

class OpenAIModule:
    def __init__(self, credentials: OpenAICredentials):
        self.client = OpenAI(api_key=credentials.api_key)

    def generate_text(self, prompt: str, model: str = "gpt-3.5-turbo", **kwargs):
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI Fehler: {e}")
            return None
