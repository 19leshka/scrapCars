from pydantic import BaseSettings

from database.mongodb import MongoAdapter


class AppSetup(BaseSettings):
    DB: MongoAdapter = None


setup = AppSetup()
