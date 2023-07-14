import logging

import celery

from app.core.celery_config import app
from app.tasks.async_decorator import async_task
from database.mongodb import MongoAdapter
from database.repositories.chat import ChatRepository


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@async_task(app, bind=True)
async def avby_task(self: celery.Task):
    users = await ChatRepository.get_all(MongoAdapter())
    logger.info(users)
