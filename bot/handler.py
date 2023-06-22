from aiogram import Dispatcher
from aiogram.types import Message


async def echo(message: Message):

    await message.reply(f"Hi! {message.chat.id}")

async def register(message: Message):
    chat_id = message.chat.id


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(register, commands=['start', ])
