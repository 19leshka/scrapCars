import motor.motor_asyncio


async def main_async():
    mongo_uri = "mongodb://db:27017/mydatabase"
    client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
    db = client.get_database()
    return db
