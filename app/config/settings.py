from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()


class Settings(BaseSettings):
    # FastAPI
    # Debug should be set to False on production
    DEBUG: bool = os.getenv("DEBUG") == "True"
    # Title is the name of application
    TITLE: str = os.getenv("TITLE")

    # Mongodb
    MONGO_DATABASE_NAME: str = os.getenv("MONGO_DATABASE_NAME")
    MONGO_CONNECTION_STRING: str = os.getenv("MONGO_CONNECTION_STRING")


settings = Settings()
