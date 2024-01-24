from services.categories import create_category_object
from models.categories import Category
from typing import Dict, Optional
from fastapi import APIRouter


router = APIRouter(
    prefix="/api/v1/category",
    tags=["category"]
)


@router.post("/")
def create_category(category: Category):
    return create_category_object(category)
