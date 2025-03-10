from apscheduler.schedulers.background import BackgroundScheduler

class SchedulerModule:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def schedule_task(self, cron_expression: str, task_callable, *args, **kwargs):
        cron_parts = cron_expression.split()
        if len(cron_parts) != 5:
            raise ValueError("Cron-Ausdruck ungültig. Erwartet: min hour day month day_of_week")

        self.scheduler.add_job(
            task_callable,
            'cron',
            args=args,
            kwargs=kwargs,
            minute=cron_parts[0],
            hour=cron_parts[1],
            day=cron_parts[2],
            month=cron_parts[3],
            day_of_week=cron_parts[4]
        )

    def stop_all_tasks(self):
        self.scheduler.shutdown(wait=False)
