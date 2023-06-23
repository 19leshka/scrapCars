"""
CRUD Operations for Chat Endpoint
"""

from database.mongodb import AsyncIOMotorClient
from database.models.chat import BaseChatCreate, BaseChat
from app.core.config import mongo_db

mongo_collection = "api_chat"  # the collection for the chat model


async def total_docs_in_db(conn: AsyncIOMotorClient) -> int:
    """
    Get total documents in the database
    :param conn: AsyncIOMotorClient connection
    :return: INT count of the total docs in mongodb or 0 if none
    """
    return await conn[mongo_db][mongo_collection].count_documents({})


async def get_all(conn: AsyncIOMotorClient) -> dict:
    """
    Get all users and their information
    :param conn: AsyncIOMotorClient connection
    :return: dict of all users
    """
    total_docs = await total_docs_in_db(conn)
    docs = []
    async for doc in conn[mongo_db][mongo_collection].find():
        docs.append(BaseChat(**doc).dict())

    if docs:
        return {'total_chats': total_docs, "chats": docs}


async def get_chat_by_id(
        conn: AsyncIOMotorClient,
        chat_id: int
) -> BaseChat:
    """Get user info
    :param chat_id: Telegram chat id
    :param conn: AsyncIOMotorClient connection
    :return: BaseChat of a chat found or None
    """
    row = await conn[mongo_db][mongo_collection].find_one({"chat_id": chat_id})
    if row:
        return BaseChat(**row)


async def create_chat(
        conn: AsyncIOMotorClient,
        chat: BaseChatCreate
) -> BaseChat:
    """Create a New API User.
    Created API Key is not stored in the database. It will be sent to browser and an email
    sent to the email id provided, for the user to confirm the email id.
    :param conn: AsyncIOMotorClient connection
    :param chat: BaseChatCreate model
    :return: NEW API KEY as STR or None
    """
    api_chat = BaseChat(**chat.dict())

    row = await conn[mongo_db][mongo_collection].insert_one(api_chat.dict())

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
