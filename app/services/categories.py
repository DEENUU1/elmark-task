from typing import Dict, Optional, Any

from fastapi import HTTPException

from models.categories import Category
from serializers.categories import get_category_serializer
from pymongo import MongoClient


def create_category_object(
        category: Category,
        db: MongoClient
) -> Dict[str, Optional[str]]:
    if db.categories.find_one({"name": category.name}):
        raise HTTPException(status_code=400, detail="Category already exists")

    if category.parent_name and not db.categories.find_one({"name": category.parent_name}):
        raise HTTPException(status_code=400, detail="Parent category does not exist")
    
    _id = db.categories.insert_one(category.dict()).inserted_id
    inserted_category = db.categories.find_one({"_id": _id})
    return get_category_serializer(inserted_category)


def get_category_object(
        category_name: str,
        db: MongoClient
) -> Dict[str, Optional[str]]:
    inserted_category = db.categories.find_one({"name": category_name})
    return get_category_serializer(inserted_category)


def update_category_object(
        category_name: str,
        category: Category,
        db: MongoClient
) -> Dict[str, Optional[str]]:
    db.categories.update_one({"category_name": category_name}, {"$set": category.dict()})
    inserted_category = db.categories.find_one({"category_name": category_name})
    return get_category_serializer(inserted_category)


def delete_category_object(
        category_name: str,
        collection: Any,
        collection_parts: Any
) -> Dict[str, Optional[str]]:
    pass
