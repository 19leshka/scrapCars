from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DB_NAME: str = Field(..., env='DATABASE_NAME')
    USER: str = Field(..., env='USER')
    PASSWORD: str = Field(..., env='PASSWORD')
    HOST: str = Field(..., env='HOST')

    API_TOKEN: str = Field(..., env='TELEGRAM_API_TOKEN')

    CELERY_BROKER_URL: str = Field(..., env='CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND: str = Field(..., env='CELERY_RESULT_BACKEND')

    SCRAPE_URL: str = Field(..., env='SCRAPE_URL')

    class Config:
        env_file = '.env'


settings = Settings()
