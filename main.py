import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.core.config import settings
from app.core.setup import setup
from app.bot.handler import register_handlers
from app.scraper.bs import scrape
from database.mongodb import MongoAdapter
from app.middlewares.middleware import MongoMiddleware


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    bot = Bot(token=settings.API_TOKEN)
    dp = Dispatcher(bot)
    setup.DB = MongoAdapter()
    dp.middleware.setup(MongoMiddleware(setup.DB))
    logger.info(type(setup.DB))
    register_handlers(dp)
    session = await bot.get_session()
    try:
        await dp.start_polling()
    finally:
        await session.close()


if __name__ == '__main__':
    asyncio.run(main())

