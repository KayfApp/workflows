import smtplib
from email.mime.text import MIMEText
from credentials import EmailCredentials

class EmailModule:
    def __init__(self, credentials: EmailCredentials):
        self.credentials = credentials

    def send_email(self, recipient: str, subject: str, body: str):
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = self.credentials.username
        msg['To'] = recipient

        try:
            with smtplib.SMTP(self.credentials.smtp_server, self.credentials.smtp_port) as server:
                server.starttls()
                server.login(self.credentials.username, self.credentials.password)
                server.sendmail(self.credentials.username, recipient, msg.as_string())
            return True
        except Exception as e:
            print(f"Fehler beim E-Mail senden: {e}")
            return False
