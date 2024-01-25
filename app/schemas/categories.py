from models.categories import Category
from pydantic import BaseModel
from typing import Optional


class CategorySchema(Category):
    pass


class CategoryCreateSchema(BaseModel):
    name: str
    parent_name: Optional[str] = None


class CategoryUpdateSchema(CategoryCreateSchema):
    pass
