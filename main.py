import asyncio

from aiogram import Bot, Dispatcher

from bot.handler import register_handlers
from bs import scrape
from core.settings import API_TOKEN, mongo_url
from db.mongodb import MongoAdapter
from middleware import MongoMiddleware


URL = "https://cars.av.by/filter?price_usd[min]=10000&price_usd[max]=12500&transmission_type=2&body_type[0]=6&body_type[1]=4&engine_type[0]=5&seller_type[0]=1&mileage_km[max]=220000&sort=4"


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)
    db = MongoAdapter(mongo_url=mongo_url)
    dp.middleware.setup(MongoMiddleware(db))
    register_handlers(dp)
    session = await bot.get_session()
    try:
        await dp.start_polling()
    finally:
        await session.close()  # type: ignore


if __name__ == '__main__':
    asyncio.run(main())

