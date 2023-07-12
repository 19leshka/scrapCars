import logging

from aiogram import Dispatcher
from aiogram.types import Message
from motor.motor_asyncio import AsyncIOMotorClient

from database.repositories.av_links import AVRepository
from database.repositories.chat import ChatRepository

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def registration(message: Message, client: AsyncIOMotorClient):
    chat_is = await ChatRepository.get_one(client, message.chat.id)
    if not chat_is:
        chat = await ChatRepository.create(client, message.chat)
        await message.answer(text=f'Добро пожаловать {chat["first_name"]} {chat["last_name"]}.')
    else:
        await message.answer(text='Вы уже зарегистрированы.')


async def get_link(message: Message, client: AsyncIOMotorClient):
    logger.info(message.text)
    elem = {
        'id': message.chat.id,
        'link': message.text,
        'latest_id': None
    }
    if await AVRepository.get_one(client, message.chat.id):
        await AVRepository.update_by_id(client, message.chat.id, elem)
        await message.answer(text='Ссылка обновлена.')
    else:
        user_link = await AVRepository.create(client, elem)
        await message.answer(text='Ссылка сохранена.')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(registration, commands=['start', ])
    dp.register_message_handler(get_link, lambda msg: msg.text.lower()[:15] == 'https://cars.av')
