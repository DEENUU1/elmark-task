from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()


class Settings(BaseSettings):
    # FastAPI
    DEBUG: bool = os.getenv("DEBUG") == "True"
    TITLE: str = os.getenv("TITLE")

    # Mongodb
    MONGO_DATABASE_NAME: str = os.getenv("MONGO_DATABASE_NAME")
    MONGO_USERNAME: Optional[str] = os.getenv("MONGO_USERNAME")
    MONGO_PASSWORD: Optional[str] = os.getenv("MONGO_PASSWORD")
    MONGO_CONNECTION_STRING: str = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.quwsqxx.mongodb.net/?retryWrites=true&w=majority"


settings = Settings()
