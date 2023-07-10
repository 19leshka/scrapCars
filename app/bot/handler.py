import logging

from aiogram import Dispatcher
from aiogram.types import Message
from motor.motor_asyncio import AsyncIOMotorClient

from database.crud.chat import create_chat, get_chat_by_id

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def registration(message: Message, client: AsyncIOMotorClient):
    chat_is = await get_chat_by_id(client, message.chat.id)
    if not chat_is:
        chat = await create_chat(client, message.chat)
        await message.answer(text=f'Добро пожаловать {chat["first_name"]} {chat["last_name"]}.')
    else:
        await message.answer(text='Вы уже зарегистрированы.')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(registration, commands=['start', ])
