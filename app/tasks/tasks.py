import logging

from app.core.celery_config import celery
from app.core.setup import setup
from app.scraper.bs import scrape
from database.repositories.chat import ChatRepository



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@celery.task
async def avby_task():
    users = ChatRepository.get_all(setup.DB)
    logger.info(users)
    # res = await scrape()
