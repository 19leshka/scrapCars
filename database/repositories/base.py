from app.core.config import settings
from database.mongodb import MongoAdapter


class BaseRepository:
    Collection = None

    @classmethod
    async def create(cls, adapter: MongoAdapter, data):
        collection = await adapter.get_collection(settings.DB_NAME, cls.Collection)
        result = await collection.insert_one(dict(data))
        return data

    @classmethod
    async def get_one(cls, adapter: MongoAdapter, key: int):
        collection = await adapter.get_collection(settings.DB_NAME, cls.Collection)
        row = await collection.find_one({'id': key})
        return row

    @classmethod
    async def get_all(cls, adapter: MongoAdapter):
        collection = await adapter.get_collection(settings.DB_NAME, cls.Collection)
        docs = []
        async for doc in collection.find():
            docs.append(doc.dict())

        if docs:
            return {"chats": docs}

    @classmethod
    async def total_docs_in_db(cls, adapter):
        collection = await adapter.get_collection(settings.DB_NAME, cls.Collection)
        return await collection.count_documents({})
