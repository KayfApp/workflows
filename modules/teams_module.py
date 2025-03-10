import requests
from credentials import TeamsCredentials

class TeamsModule:
    def __init__(self, credentials: TeamsCredentials):
        self.credentials = credentials

    def send_message(self, message: str, title: str = "Benachrichtigung"):
        payload = {
            "title": title,
            "text": message
        }
        try:
            response = requests.post(self.credentials.webhook_url, json=payload)
            response.raise_for_status()
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"Teams send_message Fehler: {e}")
            return False
