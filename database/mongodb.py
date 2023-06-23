"""
MongoDB
"""
from motor.motor_asyncio import AsyncIOMotorClient


class MongoAdapter:
    def __init__(self, mongo_url: str) -> None:
        self.client = AsyncIOMotorClient(mongo_url)

    def on_shutdown(self):
        self.client.close()

    def get_collection(self, db_name: str, collection_name: str):
        return self.client.get_database(db_name).get_collection(collection_name)

