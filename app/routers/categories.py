from fastapi import APIRouter, Depends

from models.categories import Category
from services.categories import (
    create_category_object,
    get_category_object,
    update_category_object,
    delete_category_object
)
from config.database import get_db
from typing import Any, Dict
from pymongo import MongoClient

router = APIRouter(
    prefix="/category",
    tags=["category"]
)


@router.post("/")
def create_category(category: Category, db: MongoClient = Depends(get_db)):
    return create_category_object(category, db)


@router.get("/{name}")
def get_category(name: str, db: MongoClient = Depends(get_db)):
    return get_category_object(name, db)


@router.put("/{name}")
def update_category(name: str, category: Category, db: MongoClient = Depends(get_db)):
    return update_category_object(name, category, db)


# @router.delete("/{name}")
# def delete_category(name: str, db: MongoClient = Depends(get_db)) -> Dict[str, Any]:
#     return delete_category_object(name, db)
