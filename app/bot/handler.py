from aiogram import Dispatcher
from aiogram.types import Message

from database.mongodb import MongoAdapter


async def registration(message: Message):
    chat_id = message.chat.id
    # collection = db.get_collection("mydatabase", "users")
    # print(collection)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(registration, commands=['start', ])
