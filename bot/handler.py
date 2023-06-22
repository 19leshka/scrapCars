from aiogram import Dispatcher
from aiogram.types import Message


async def registration(message: Message):
    chat_id = message.chat.id


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(registration, commands=['start', ])
