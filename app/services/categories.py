from typing import Dict, Optional, Any

from fastapi import HTTPException

from models.categories import Category
from serializers.categories import get_category_serializer


def create_category_object(category: Category, collection: Any) -> Dict[str, Optional[str]]:
    if collection.find_one({"name": category.name}):
        raise HTTPException(status_code=400, detail="Category already exists")

    if category.parent_name and not collection.find_one({"name": category.parent_name}):
        raise HTTPException(status_code=400, detail="Parent category does not exist")
    
    _id = collection.insert_one(category.dict()).inserted_id
    inserted_category = collection.find_one({"_id": _id})
    return get_category_serializer(inserted_category)


def get_category_object(category_name: str, collection: Any) -> Dict[str, Optional[str]]:
    inserted_category = collection.find_one({"name": category_name})
    return get_category_serializer(inserted_category)


def update_category_object(category_name: str, category: Category, collection: Any) -> Dict[str, Optional[str]]:
    collection.update_one({"category_name": category_name}, {"$set": category.dict()})
    inserted_category = collection.find_one({"category_name": category_name})
    return get_category_serializer(inserted_category)


def delete_category_object(category_name: str, collection: Any, collection_parts: Any) -> Dict[str, Optional[str]]:
    category = collection.find_one({"name": category_name})
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    parts_in_category = list(collection_parts.find({"category": category_name}))
    if len(parts_in_category) > 0:
        raise HTTPException(status_code=400, detail="Cannot delete a category with assigned parts")

    child_categories = collection.find({"parent_name": category_name})
    for child_category in child_categories:
        child_category_parts = list(collection_parts.find({"category": child_category["name"]}))
        if len(child_category_parts) > 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot delete a parent category with child categories having assigned parts"
            )

    result = collection.delete_one({"name": category_name})
    if result.deleted_count == 1:
        return {"message": "Category deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Category not found")
