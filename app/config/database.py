from pymongo import MongoClient
# from .settings import settings
from typing import Any


def client() -> MongoClient:
    return MongoClient("mongodb://localhost:27017")


def get_db() -> Any:
    db = client()["KACPER_WŁODARCZYK"]
    yield db


def get_categories_collection() -> Any:
    db = get_db()
    yield db["categories"]


def get_parts_collection() -> Any:
    db = get_db()
    yield db["parts"]
