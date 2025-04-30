from modules import (
    SlackModule,
    # TeamsModule,
    EmailModule,
    OpenAIModule,
    SchedulerModule,
    EditorModule,
)
from credentials import (
    SlackCredentials,
    # TeamsCredentials,
    EmailCredentials,
    OpenAICredentials,
    EditorCredentials,
)


class WorkflowFacade:
    def __init__(
        self,
        slack_credentials: SlackCredentials,
        # teams_credentials: TeamsCredentials,
        email_credentials: EmailCredentials,
        openai_credentials: OpenAICredentials,
        editor_credentials: EditorCredentials,
    ):
        # Initialize modules
        self.slack = SlackModule(slack_credentials)
        # self.teams = TeamsModule(teams_credentials)
        self.email = EmailModule(email_credentials)
        self.openai = OpenAIModule(openai_credentials)
        self.editor = EditorModule(editor_credentials)
        self.scheduler = SchedulerModule()

    # ---------------------------
    # Slack
    # ---------------------------
    def send_slack(self, channel: str, message: str):
        return self.slack.send_message(channel, message)

    # ---------------------------
    # Teams
    # ---------------------------
    # def send_teams(self, message: str, title: str = "Automatisierte Nachricht"):
        # return self.teams.send_message(message, title)

    # ---------------------------
    # Email
    # ---------------------------
    def send_email(self, recipient: str, subject: str, body: str):
        return self.email.send_email(subject=subject, body=body, recipient=recipient)

    # ---------------------------
    # OpenAI
    # ---------------------------
    def openai_request(self, prompt: str, model: str = "gpt-4o-mini", **kwargs):
        return self.openai.generate_text(prompt=prompt, model=model, **kwargs)

    # ---------------------------
    # Scheduler
    # ---------------------------
    def schedule_slack_message(self, cron_expression: str, channel: str, message: str):
        self.scheduler.schedule_task(
            cron_expression=cron_expression,
            task_callable=self.send_slack,
            channel=channel,
            message=message,
        )

    def stop_all_scheduled_tasks(self):
        self.scheduler.stop_all_tasks()

    # ---------------------------
    # Editor (New)
    # ---------------------------
    def list_documents(self):
        return self.editor.list_documents()

    def get_document(self, doc_id: str):
        return self.editor.get_document(doc_id)

    def rename_document(self, doc_id: str, new_name: str):
        return self.editor.rename_document(doc_id, new_name)

    def delete_document(self, doc_id: str):
        return self.editor.delete_document(doc_id)
