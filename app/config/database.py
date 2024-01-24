from pymongo import MongoClient
# from .settings import settings
from typing import Any


def client() -> MongoClient:
    return MongoClient("mongodb://localhost:27017")


def db() -> Any:
    return client()["KACPER_WŁODARCZYK"]


def get_parts_collection() -> Any:
    return db()["parts"]


def get_categories_collection() -> Any:
    return db()["categories"]
