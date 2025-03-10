from modules import SlackModule, TeamsModule, EmailModule, OpenAIModule, SchedulerModule
from credentials import SlackCredentials, TeamsCredentials, EmailCredentials, OpenAICredentials

class WorkflowFacade:
    def __init__(
        self,
        slack_credentials: SlackCredentials,
        teams_credentials: TeamsCredentials,
        email_credentials: EmailCredentials,
        openai_credentials: OpenAICredentials
    ):
        # Module initialisieren
        self.slack = SlackModule(slack_credentials)
        self.teams = TeamsModule(teams_credentials)
        self.email = EmailModule(email_credentials)
        self.openai = OpenAIModule(openai_credentials)
        self.scheduler = SchedulerModule()

    # Slack-Nachricht senden
    def send_slack(self, channel: str, message: str):
        return self.slack.send_message(channel, message)

    # Teams-Nachricht senden
    def send_teams(self, message: str, title: str = "Automatisierte Nachricht"):
        return self.teams.send_message(message, title)

    # Email senden
    def send_email(self, recipient: str, subject: str, body: str):
        return self.email.send_email(subject=subject, body=body, recipient=recipient)

    # OpenAI-Anfrage
    def openai_request(self, prompt: str, model: str = "gpt-4o-mini", **kwargs):
        return self.openai.generate_text(prompt=prompt, model=model, **kwargs)

    # Cron-basierte Slack-Nachricht planen
    def schedule_slack_message(self, cron_expression: str, channel: str, message: str):
        self.scheduler.schedule_task(cron_expression=cron_expression,
                                    task_callable=self.send_slack,
                                    channel=channel,
                                    message=message)

    # Cron-Job stoppen (alle geplanten Tasks stoppen)
    def stop_all_scheduled_tasks(self):
        self.scheduler.stop_all_tasks()
