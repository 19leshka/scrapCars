import asyncio

from aiogram import Bot, Dispatcher

from core.config import settings
from bot.handler import register_handlers
from db.mongodb import MongoAdapter
from middleware import MongoMiddleware


async def main():
    bot = Bot(token=settings.API_TOKEN)
    dp = Dispatcher(bot)
    db = MongoAdapter(mongo_url=f"{settings.MONGO_URL}{settings.DB_NAME}")
    dp.middleware.setup(MongoMiddleware(db))
    register_handlers(dp)
    session = await bot.get_session()
    try:
        await dp.start_polling()
    finally:
        await session.close()


if __name__ == '__main__':
    asyncio.run(main())

