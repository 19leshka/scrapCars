from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DB_NAME: str = Field(..., env='DATABASE_NAME')
    USER: str = Field(..., env='USER')
    PASSWORD: str = Field(..., env='PASSWORD')
    HOST: str = Field(..., env='HOST')

    API_TOKEN: str = Field(..., env='TELEGRAM_API_TOKEN')

    class Config:
        env_file = '.env'


settings = Settings()
