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
from schemas.categories import CategorySchema, CategoryCreateSchema, CategoryUpdateSchema
from fastapi import status


router = APIRouter(
    prefix="/category",
    tags=["category"]
)


@router.post("/", response_model=CategoryCreateSchema, status_code=status.HTTP_201_CREATED)
def create_category(
        category: CategoryCreateSchema,
        collection: Any = Depends(get_categories_collection)
) -> CategoryCreateSchema:
    """
    Create a new category.

    Args:
        category (Category): The category data to be created.
        collection (Any): Dependency to get the categories' collection.

    Returns:
        CategoryCreateSchema: The created category.

    Raises:
        HTTPException: If there is an error in the creation process.
    """
    return create_category_object(category, collection)


@router.get("/{id}", response_model=CategorySchema, status_code=status.HTTP_200_OK)
def get_category(
        id: str,
        collection: Any = Depends(get_categories_collection)
) -> CategorySchema:
    """
    Get a category by name.

    Args:
        id (str): The id of the category to retrieve.
        collection (Any): Dependency to get the categories' collection.

    Returns:
        CategorySchema: The retrieved category.

    Raises:
        HTTPException: If the category is not found.
    """
    return get_category_object(id, collection)


@router.put("/{id}", response_model=CategoryUpdateSchema, status_code=status.HTTP_200_OK)
def update_category(
        id: str,
        category: CategoryUpdateSchema,
        collection: Any = Depends(get_categories_collection)
) -> CategoryUpdateSchema:
    """
    Update a category by name.

    Args:
        id (str): The id of the category to update.
        category (CategoryUpdateSchema): The updated category data.
        collection (Any): Dependency to get the categories' collection.

    Returns:
        CategoryUpdateSchema: The updated category.

    Raises:
        HTTPException: If the category is not found or there is an error in the update process.
    """
    return update_category_object(id, category, collection)


@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=Dict[str, str])
def delete_category(
        id: str,
        collection: Any = Depends(get_categories_collection),
        collection_part: Any = Depends(get_parts_collection)
) -> Dict[str, str]:
    """
    Delete a category by name.

    Args:
        id (str): The id of the category to delete.
        collection (Any): Dependency to get the categories' collection.
        collection_part (Any): Dependency to get the parts' collection.

    Returns:
        Dict[str, str]: A dictionary indicating the success of the deletion.

    Raises:
        HTTPException: If the category is not found or there is an error in the deletion process.
    """
    return delete_category_object(id, collection, collection_part)
