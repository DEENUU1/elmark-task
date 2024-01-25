from pymongo import MongoClient
# from .settings import settings
from typing import Any, Mapping, Collection

from pymongo.database import Database


def client() -> MongoClient:
    return MongoClient("mongodb://localhost:27017")


def get_db() -> Database[Mapping[str, Any] | Any]:
    db = client()["KACPER_WŁODARCZYK"]
    return db


def get_categories_collection() -> Any:
    db = get_db()
    return db["categories"]


def get_parts_collection() -> Any:
    db = get_db()
    return db["parts"]
