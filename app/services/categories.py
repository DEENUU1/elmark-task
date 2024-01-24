from typing import Dict, Optional

from fastapi import HTTPException

from config.database import get_parts_collection, get_categories_collection
from models.categories import Category
from serializers.categories import get_category_serializer


def create_category_object(category: Category) -> Dict[str, Optional[str]]:
    _id = get_categories_collection().insert_one(category.dict()).inserted_id
    inserted_category = get_categories_collection().find_one({"_id": _id})
    return get_category_serializer(inserted_category)


def get_category_object(category_name: str) -> Dict[str, Optional[str]]:
    inserted_category = get_categories_collection().find_one({"name": category_name})
    return get_category_serializer(inserted_category)


def update_category_object(category_name: str, category: Category) -> Dict[str, Optional[str]]:
    get_categories_collection().update_one({"category_name": category_name}, {"$set": category.dict()})
    inserted_category = get_categories_collection().find_one({"category_name": category_name})
    return get_category_serializer(inserted_category)


def delete_category_object(category_name: str) -> Dict[str, Optional[str]]:
    category = get_categories_collection().find_one({"name": category_name})
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    parts_in_category = list(get_parts_collection().find({"category": category_name}))
    if len(parts_in_category) > 0:
        raise HTTPException(status_code=400, detail="Cannot delete a category with assigned parts")

    child_categories = get_categories_collection().find({"parent_name": category_name})
    for child_category in child_categories:
        child_category_parts = list(get_parts_collection().find({"category": child_category["name"]}))
        if len(child_category_parts) > 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot delete a parent category with child categories having assigned parts"
            )

    result = get_categories_collection().delete_one({"name": category_name})
    if result.deleted_count == 1:
        return {"message": "Category deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Category not found")
