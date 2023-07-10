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



# async def update_chat(
#         conn: AsyncIOMotorClient,
#         chat_id: int,
#         user: BaseUserUpdate
# ) -> BaseUserInDB:
#     """Update a user with new details
#     :param conn: AsyncIOMotorClient connection
#     :param chat_id: chat_id of the user to update details
#     :param user: BaseUserUpdate model
#     :return: BaseUserInDB of a user found or None
#     """
#     api_user = await get_chat_by_id(conn, chat_id)
#
#     api_user.salt = user.salt or api_user.salt
#     api_user.hashed_api_key = user.hashed_api_key or api_user.hashed_api_key
#
#     api_user.endpoint_access = user.endpoint_access or api_user.endpoint_access
#     api_user.is_active = user.is_active or api_user.is_active
#
#     if user.disabled is not None:
#         api_user.disabled = user.disabled
#
#     if user.is_active is not None:
#         api_user.is_active = user.is_active
#
#     if user.is_superuser is not None:
#         api_user.is_superuser = user.is_superuser
#
#     api_user.updated_at = datetime.utcnow()
#     updated_at = await conn[mongo_db][mongo_collection].update_one(
#         {"email": api_user.email}, {'$set': api_user.dict()}
#     )
#
#     return api_user
