"""
CRUD Operations for Chat Endpoint
"""
import logging
from dataclasses import asdict

from aiogram.types import Chat

from database.mongodb import AsyncIOMotorClient, MongoAdapter
from database.models.chat import BaseChatCreate, BaseChat, ChatSchema
from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mongo_collection = 'Users'


async def total_docs_in_db(conn: AsyncIOMotorClient) -> int:
    """
    Get total documents in the database
    :param conn: AsyncIOMotorClient connection
    :return: INT count of the total docs in mongodb or 0 if none
    """
    return await conn[settings.DB_NAME][mongo_collection].count_documents({})


async def get_all(conn: AsyncIOMotorClient) -> dict:
    """
    Get all users and their information
    :param conn: AsyncIOMotorClient connection
    :return: dict of all users
    """
    total_docs = await total_docs_in_db(conn)
    docs = []
    async for doc in conn[settings.DB_NAME][mongo_collection].find():
        docs.append(BaseChat(**doc).dict())

    if docs:
        return {'total_chats': total_docs, "chats": docs}


async def get_chat_by_id(
        adapter: MongoAdapter,
        chat_id: int
) -> ChatSchema:
    """Get user info
    :param adapter: MongoAdapter
    :param chat_id: Telegram chat id
    :return: BaseChat of a chat found or None
    """
    collection = await adapter.get_collection(settings.DB_NAME, mongo_collection)
    row = await collection.find_one({'id': chat_id})
    logger.info(f"Find one: {row}")
    if row:
        return ChatSchema(**row)


async def create_chat(
        adapter: MongoAdapter,
        chat: Chat
) -> ChatSchema:
    """Create a New API User.
    Created API Key is not stored in the database. It will be sent to browser and an email
    sent to the email id provided, for the user to confirm the email id.
    :param adapter: MongoAdapter
    :param chat: Chat model
    :return: NEW API KEY as STR or None
    """
    api_chat = dict(chat)
    collection = await adapter.get_collection(settings.DB_NAME, mongo_collection)
    result = await collection.insert_one(api_chat)
    return api_chat

