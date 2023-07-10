import logging

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

from app.core.config import settings


class MongoAdapter:
    def __init__(self) -> None:
        try:
            self.client = AsyncIOMotorClient(
                        host=settings.HOST,
                        username=settings.USER,
                        password=settings.PASSWORD
                    )
            logging.info('Connected to mongo.')
        except Exception as e:
            logging.exception(f'Could not connect to mongo: {e}')
            raise e

    async def on_shutdown(self):
        self.client.close()

    async def get_collection(self, db_name: str, collection_name: str) -> AsyncIOMotorCollection:
        return self.client.get_database(db_name).get_collection(collection_name)

