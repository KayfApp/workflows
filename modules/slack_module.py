import requests
from credentials import SlackCredentials

class SlackModule:
    def __init__(self, credentials: SlackCredentials):
        self.credentials = credentials

    def send_message(self, channel: str, message: str):
        payload = {"channel": channel, "message": message}
        try:
            res = requests.post(self.credentials.webhook_url, json=payload)
            res.raise_for_status()
            return res.json()
        except requests.RequestException as e:
            print(f"Slack Fehler: {e}")
            return None
