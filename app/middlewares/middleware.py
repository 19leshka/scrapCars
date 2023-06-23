from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from database.mongodb import MongoAdapter


class MongoMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, db: MongoAdapter):
        super().__init__()
        self.db = db

    async def pre_process(self, obj, data, *args):
        data["database"] = self.db

    async def post_process(self, obj, data, *args):
        del data["database"]
