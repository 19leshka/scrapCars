from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DB_NAME: str = Field(..., env='DATABASE_NAME')
    MONGO_URL: str = Field(..., env='MONGO_URL')

    API_TOKEN: str = Field(..., env='TELEGRAM_API_TOKEN')

    class Config:
        env_file = '.env'


settings = Settings()
