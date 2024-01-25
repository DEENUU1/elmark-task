from typing import Dict, Any

from fastapi import HTTPException

from models.categories import Category
from schemas.categories import CategorySchema, CategoryUpdateSchema


def create_category_object(
        category: Category,
        collection: Any
) -> CategorySchema:
    """
    Create a new category object in the specified collection.

    Parameters:
    - category (Category): The category object to be created.
    - collection (Any): The MongoDB collection where the category will be stored.

    Returns:
    - CategorySchema: The newly created category as a CategorySchema object.
    """

    # Check if a category with the same name already exists
    if collection.find_one({"name": category.name}):
        raise HTTPException(status_code=400, detail="Category already exists")

    # Check if the specified parent category exists
    if category.parent_name and not collection.find_one({"name": category.parent_name}):
        raise HTTPException(status_code=400, detail="Parent category does not exist")

    _id = collection.insert_one(category.dict()).inserted_id
    inserted_category = collection.find_one({"_id": _id})
    return CategorySchema(**inserted_category)


def get_category_object(
        category_name: str,
        collection: Any
) -> CategorySchema:
    """
    Retrieve a category object from the specified collection by its name.

    Parameters:
    - category_name (str): The name of the category to be retrieved.
    - collection (Any): The MongoDB collection where the category is stored.

    Returns:
    - CategorySchema: The retrieved category as a CategorySchema object.
    """
    inserted_category = collection.find_one({"name": category_name})

    # Raise an exception if the category is not found
    if inserted_category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return CategorySchema(**inserted_category)


def update_category_object(
        category_name: str,
        category: CategoryUpdateSchema,
        collection: Any
) -> CategoryUpdateSchema:
    """
    Update a category object in the specified collection by its name.

    Parameters:
    - category_name (str): The name of the category to be updated.
    - category (CategoryUpdateSchema): The updated data for the category.
    - collection (Any): The MongoDB collection where the category is stored.

    Returns:
    - CategoryUpdateSchema: The updated category as a CategoryUpdateSchema object.
    """

    # Check if the category with the specified name exists
    existing_category = collection.find_one({"name": category_name})
    if existing_category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    # Check if updating to the specified name would result in a duplicate category
    duplicated_category = get_category_object(category.name, collection)
    if duplicated_category:
        raise HTTPException(status_code=400, detail="Category already exists")

    update_data = {"$set": {"name": category.name}}
    collection.update_one({"name": category_name}, update_data)

    updated_category = collection.find_one({"name": category.name})
    return CategoryUpdateSchema(**updated_category)


def delete_category_object(
        category_name: str,
        collection: Any,
        collection_parts: Any
) -> Dict[str, str]:
    """
    Delete a category object from the specified collection and associated parts.

    Parameters:
    - category_name (str): The name of the category to be deleted.
    - collection (Any): The MongoDB collection where the category is stored.
    - collection_parts (Any): The MongoDB collection where parts related to categories are stored.

    Returns:
    - Dict[str, str]: A dictionary indicating the success of the deletion.
    """
    # Check if the category with the specified name exists
    category = collection.find_one({"name": category_name})
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    # Check if the category has assigned parts
    parts_in_category = list(collection_parts.find({"category": category_name}))
    if len(parts_in_category) > 0:
        raise HTTPException(status_code=400, detail="Cannot delete a category with assigned parts")

    # Check if a parent category has child categories with assigned parts
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

