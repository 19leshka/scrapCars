import aiohttp
from bs4 import BeautifulSoup

from app.services.av import AVbyService


async def scrape(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            body = await resp.text()
            soup = BeautifulSoup(body, 'html.parser')
            listing_items = soup.findAll(class_="listing-item")
            cars = await AVbyService.parse_items(listing_items)
            return cars
