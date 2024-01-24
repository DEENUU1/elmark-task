from pymongo import MongoClient
from .settings import settings


db_connection = MongoClient("mongodb+srv://rekrutacja:BZijŌwEru0oELxT@cluster11.yxu8n2k.mongodb.net/")
database = db_connection["KACPER_WŁODARCZYK"]
# collection_parts = database["parts"]
# collection_categories = database["categories"]
