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
            docs.append(doc)

        if docs:
            return {"chats": docs}

    @classmethod
    async def total_docs_in_db(cls, adapter: MongoAdapter):
        collection = await adapter.get_collection(settings.DB_NAME, cls.Collection)
        return await collection.count_documents({})

    @classmethod
    async def update_by_id(cls, adapter: MongoAdapter, key: int, update_data):
        collection = await adapter.get_collection(settings.DB_NAME, cls.Collection)
        result = await collection.update_one({'id': key}, {'$set': update_data})
        if result.modified_count > 0:
            return True
        return False
