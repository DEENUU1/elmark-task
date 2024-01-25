from typing import Dict, Optional, Any

from fastapi import APIRouter, Depends
from pymongo import MongoClient

from config.database import get_db, get_categories_collection, get_parts_collection
from models.categories import Category
from services.categories import (
    create_category_object,
    get_category_object,
    update_category_object,
    delete_category_object
)

router = APIRouter(
    prefix="/category",
    tags=["category"]
)


@router.post("/")
def create_category(
        category: Category,
        db: MongoClient = Depends(get_db)
) -> Dict[str, Optional[str]]:
    return create_category_object(category, db)


@router.get("/{name}")
def get_category(
        name: str,
        db: MongoClient = Depends(get_db)
) -> Dict[str, Optional[str]]:
    return get_category_object(name, db)


@router.put("/{name}")
def update_category(
        name: str,
        category: Category,
        db: MongoClient = Depends(get_db)
) -> Dict[str, Optional[str]]:
    return update_category_object(name, category, db)


@router.delete("/{name}")
def delete_category(name: str, collection: Any = Depends(get_categories_collection), collection_part: Any = Depends(get_parts_collection)) -> Dict[str, Any]:
    return delete_category_object(name, collection, collection_part)
