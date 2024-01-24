from fastapi import APIRouter, Depends

from models.categories import Category
from services.categories import (
    create_category_object,
    get_category_object,
    update_category_object,
    delete_category_object
)
from config.database import get_parts_collection, get_categories_collection
from typing import Any, Dict

router = APIRouter(
    prefix="/category",
    tags=["category"]
)


@router.post("/")
def create_category(category: Category, collection: Any = Depends(get_categories_collection)):
    return create_category_object(category, collection)


@router.get("/{name}")
def get_category(name: str, collection: Any = Depends(get_categories_collection)):
    return get_category_object(name, collection)


@router.put("/{name}")
def update_category(name: str, category: Category, collection: Any = Depends(get_categories_collection)):
    return update_category_object(name, category, collection)


@router.delete("/{name}")
def delete_category(name: str, collection: Any = Depends(get_categories_collection), collection_part: Any = Depends(get_parts_collection)) -> Dict[str, Any]:
    collection_part.delete_many({"category": name})
    return delete_category_object(name, collection, collection_part)
