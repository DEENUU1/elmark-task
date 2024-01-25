from pymongo import MongoClient
from .settings import settings
from typing import Any, Mapping

from pymongo.database import Database


def client() -> MongoClient:
    return MongoClient(settings.MONGO_CONNECTION_STRING)


def get_db() -> Database[Mapping[str, Any] | Any]:
    db = client()[settings.MONGO_DATABASE_NAME]
    return db


def get_categories_collection() -> Any:
    db = get_db()
    return db["categories"]


def get_parts_collection() -> Any:
    db = get_db()
    return db["parts"]
