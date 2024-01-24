from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # FastAPI
    DEBUG: bool = os.getenv("DEBUG") == "True"
    TITLE: str = os.getenv("TITLE")

    # Mongodb
    MONGO_CONNECTION_STRING: str = os.getenv("MONGO_CONNECTION_STRING")
    MONGO_DATABASE_NAME: str = os.getenv("MONGO_DATABASE_NAME")


settings = Settings()