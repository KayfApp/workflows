import os
from dotenv import load_dotenv
from credentials import SlackCredentials, TeamsCredentials, EmailCredentials, OpenAICredentials
from facade import WorkflowFacade
import time

def main():
    # Lade Umgebungsvariablen (.env-Datei)
    load_dotenv()

    # Credentials aus .env laden
    slack_creds = SlackCredentials(webhook_url=os.getenv("SLACK_WEBHOOK_URL"))
    teams_creds = TeamsCredentials(webhook_url=os.getenv("TEAMS_WEBHOOK_URL"))
    email_creds = EmailCredentials(
        smtp_server=os.getenv("EMAIL_SMTP_SERVER"),
        smtp_port=int(os.getenv("EMAIL_SMTP_PORT")),
        username=os.getenv("EMAIL_USER"),
        password=os.getenv("EMAIL_APP_PASSWORD")
    )
    openai_creds = OpenAICredentials(api_key=os.getenv("OPENAI_API_KEY"))

    # Workflow-Fassade erstellen
    workflow = WorkflowFacade(
        slack_credentials=slack_creds,
        teams_credentials=teams_creds,
        email_credentials=email_creds,
        openai_credentials=openai_creds
    )

    # Teste Slack-Nachricht
    slack_response = workflow.send_slack("#general", "Slack-Nachricht via WorkflowFacade ✅")
    print("Slack-Antwort:", slack_creds)

    # Teste Teams-Nachricht
    #teams_success = workflow.send_teams("Teams-Nachricht via WorkflowFacade ✅", title="Testnachricht")
    #print("Teams erfolgreich:", teams_success)

    # E-Mail testen
    email_success = workflow.send_email(
        recipient="gioia@frolik.at",
        subject="Workflow Test 📧",
        body="Dies ist ein Test der E-Mail-Funktion via WorkflowFacade."
    )
    print("Email erfolgreich gesendet:", email_success)

    # OpenAI testen
    openai_response = workflow.openai_request(prompt="Was ist modularer Code?")
    print("OpenAI Antwort:", openai_response)

    # Test Scheduler-Modul (Cron-Job, alle 2 Min.)
    workflow.schedule_slack_message(
        cron_expression="*/2 * * * *",
        channel="#kayf-business-lunch",
        message="📅 Cron-Test-Nachricht alle 2 Min via WorkflowFacade!"
    )

    try:
        print("Scheduler läuft, zum Beenden: Ctrl+C")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        workflow.stop_all_scheduled_tasks()
        print("Scheduler beendet ✅")

if __name__ == "__main__":
    main()
