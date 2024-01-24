from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_CONNECTION_STRING: str = "mongodb+srv://rekrutacja:BZijŌwEru0oELxT@cluster11.yxu8n2k.mongodb.net/"
    MONGO_DATABASE_NAME: str = 'KACPER_WŁODARCZYK'