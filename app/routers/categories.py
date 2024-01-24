from fastapi import APIRouter

from models.categories import Category
from services.categories import (
    create_category_object,
    get_category_object,
    update_category_object,
    delete_category_object
)

router = APIRouter(
    prefix="/api/v1/category",
    tags=["category"]
)


@router.post("/")
def create_category(category: Category):
    return create_category_object(category)


@router.get("/{name}")
def get_category(name: str):
    return get_category_object(name)


@router.put("/{name}")
def update_category(name: str, category: Category):
    return update_category_object(name, category)


@router.delete("/{name}")
def delete_category(name: str):
    return delete_category_object(name)
