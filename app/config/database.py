from pymongo import MongoClient
# from .settings import settings
from typing import Any


def client() -> MongoClient:
    return MongoClient("mongodb://localhost:27017")


def get_db() -> Any:
    db = client()["KACPER_WŁODARCZYK"]
    yield db
