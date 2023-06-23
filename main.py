import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.core.config import settings
from app.bot.handler import register_handlers
from database.mongodb import MongoAdapter
from app.middlewares.middleware import MongoMiddleware


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.API_TOKEN)
    dp = Dispatcher(bot)
    db = MongoAdapter(db_host=settings.HOST, db_user=settings.USER, db_password=settings.PASSWORD)
    dp.middleware.setup(MongoMiddleware(db))
    register_handlers(dp)
    session = await bot.get_session()
    try:
        await dp.start_polling()
    finally:
        await session.close()


if __name__ == '__main__':
    asyncio.run(main())

