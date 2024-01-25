from typing import Dict, Any, List
from fastapi import APIRouter, Depends
from config.database import get_parts_collection, get_categories_collection
from models.parts import SearchParams
from services.parts import (
    create_part_object,
    get_part_object,
    update_part_object,
    delete_part_object,
    list_search_part_objects
)
from schemas.parts import PartSchema, PartCreateSchema, PartUpdateSchema
from fastapi import status


router = APIRouter(
    prefix="/part",
    tags=["part"],
)


@router.post("/", response_model=PartCreateSchema, status_code=status.HTTP_201_CREATED)
def create_part(
        part: PartCreateSchema,
        collection: Any = Depends(get_parts_collection),
        collection_category: Any = Depends(get_categories_collection),
) -> PartCreateSchema:
    """
    Create a new part.

    Args:
        part (PartCreateSchema): The part data to be created.
        collection (Any): Dependency to get the parts collection.
        collection_category (Any): Dependency to get the categories collection.

    Returns:
        PartSchema: The created part.

    Raises:
        HTTPException: If there is an error in the creation process.
    """
    return create_part_object(part, collection, collection_category)


@router.get("/{id}", response_model=PartSchema, status_code=status.HTTP_200_OK)
def get_part(
        id: str,
        collection: Any = Depends(get_parts_collection)
) -> PartSchema:
    """
    Get a part by serial number.

    Args:
        id (str): The id of the part to retrieve.
        collection (Any): Dependency to get the parts' collection.

    Returns:
        PartSchema: The retrieved part.

    Raises:
        HTTPException: If the part is not found.
    """
    return get_part_object(id, collection)


@router.put("/{id}", response_model=PartUpdateSchema, status_code=status.HTTP_200_OK)
def update_part(
        id: str,
        part: PartUpdateSchema,
        collection: Any = Depends(get_parts_collection),
        category_collection: Any = Depends(get_categories_collection)
) -> PartUpdateSchema:
    """
    Update a part by serial number.

    Args:
        id (str): The id of the part to update.
        part (PartUpdateSchema): The updated part data.
        collection (Any): Dependency to get the parts collection.
        category_collection (Any): Dependency to get the categories collection.

    Returns:
        PartSchema: The updated part.

    Raises:
        HTTPException: If the part is not found or there is an error in the update process.
    """
    return update_part_object(id, part, collection, category_collection)


@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=Dict[str, str])
def delete_part(
        id: str,
        collection: Any = Depends(get_parts_collection)
) -> Dict[str, str]:
    """
    Delete a part by serial number.

    Args:
        id (str): The id of the part to delete.
        collection (Any): Dependency to get the parts' collection.

    Returns:
        Dict[str, str]: A dictionary indicating the success of the deletion.

    Raises:
        HTTPException: If the part is not found or there is an error in the deletion process.
    """
    return delete_part_object(id, collection)


@router.get("/", response_model=List[PartSchema], status_code=status.HTTP_200_OK)
def list_search_parts(
        query_params: SearchParams = Depends(),
        collection: Any = Depends(get_parts_collection)
) -> List[PartSchema]:
    """
    List and search for parts based on the provided query parameters.

    Args:
        query_params (SearchParams): The search parameters for filtering parts.
        collection (Any): Dependency to get the parts' collection.

    Returns:
        List[PartSchema]: A list of parts that match the search criteria.
    """
    results = list_search_part_objects(query_params.dict(exclude_unset=True), collection)
    return results
