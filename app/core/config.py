import secrets
import urllib.parse

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME="APISpace"
    SQLALCHEMY_DATABASE_URI=""
    SECRET_KEY: str = secrets.token_urlsafe(32)

    class Config:
        env_file = ".env"


settings = Settings()