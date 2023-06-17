import aiohttp
from bs4 import BeautifulSoup

from services.av import AVbyService


async def scrape(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            body = await resp.text()
            soup = BeautifulSoup(body, 'html.parser')
            listing_items = soup.findAll(class_="listing-item")
            await AVbyService.parse_items(listing_items)
