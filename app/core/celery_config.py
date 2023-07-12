from app.core.config import settings
from celery import Celery
from celery.schedules import crontab


broker_url = 'redis://redis:6379/0'

celery = Celery(__name__)
celery.conf.broker_url = settings.CELERY_BROKER_URL
celery.conf.result_backend = settings.CELERY_RESULT_BACKEND


celery.conf.beat_schedule = {
    'scrap_cars': {
        'task': 'app.tasks.tasks.avby_task',
        'schedule': crontab(minute='1'),
    },
}

celery.conf.timezone = 'UTC'
