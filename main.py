import asyncio

from bs import scrape
from database.database import main_async

URL = "https://cars.av.by/filter?price_usd[min]=10000&price_usd[max]=12500&transmission_type=2&body_type[0]=6&body_type[1]=4&engine_type[0]=5&seller_type[0]=1&mileage_km[max]=220000&sort=4"


async def main():
    tasks = []

    task = asyncio.create_task(scrape(URL))
    tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
