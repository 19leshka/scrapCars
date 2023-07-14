from datetime import timedelta

from app.core.config import settings
from celery import Celery
from celery.schedules import crontab


broker_url = 'redis://redis:6379/0'

app = Celery("application", include=["app.tasks.scrap", ])
app.conf.broker_url = settings.CELERY_BROKER_URL
app.conf.result_backend = settings.CELERY_RESULT_BACKEND
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'scrap_cars': {
        'task': 'app.tasks.scrap.avby_task',
        'schedule': timedelta(seconds=30),
    },
}

app.conf.timezone = 'UTC'


if __name__ == '__main__':
    app.start()
