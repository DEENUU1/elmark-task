from pymongo import MongoClient
# from .settings import settings


db_connection = MongoClient("mongodb://localhost:27017")
database = db_connection["KACPER_WŁODARCZYK"]
collection_parts = database["parts"]
collection_categories = database["categories"]
