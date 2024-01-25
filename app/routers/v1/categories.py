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
from schemas.categories import CategorySchema, CategoryUpdateSchema
from fastapi import status


router = APIRouter(
    prefix="/category",
    tags=["category"]
)


@router.post("/", response_model=CategorySchema, status_code=status.HTTP_201_CREATED)
def create_category(
        category: Category,
        collection: Any = Depends(get_categories_collection)
) -> CategorySchema:
    return create_category_object(category, collection)


@router.get("/{name}", response_model=CategorySchema, status_code=status.HTTP_200_OK)
def get_category(
        name: str,
        collection: Any = Depends(get_categories_collection)
) -> CategorySchema:
    return get_category_object(name, collection)


@router.put("/{name}", response_model=CategoryUpdateSchema, status_code=status.HTTP_200_OK)
def update_category(
        name: str,
        category: CategoryUpdateSchema,
        collection: Any = Depends(get_categories_collection)
) -> CategoryUpdateSchema:
    return update_category_object(name, category, collection)


@router.delete("/{name}", status_code=status.HTTP_200_OK, response_model=Dict[str, str])
def delete_category(
        name: str,
        collection: Any = Depends(get_categories_collection),
        collection_part: Any = Depends(get_parts_collection)
) -> Dict[str, str]:
    return delete_category_object(name, collection, collection_part)
