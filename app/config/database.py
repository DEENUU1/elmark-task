from pymongo import MongoClient
from .settings import settings


db_connection = MongoClient(settings.MONGO_CONNECTION_STRING)
database = db_connection[settings.MONGO_DATABASE]
collection_parts = database["parts"]
collection_categories = database["categories"]
