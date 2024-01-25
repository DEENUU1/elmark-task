from typing import Dict, Any, List

from fastapi import HTTPException

from models.parts import Part
from .categories import get_category_object
from schemas.parts import PartSchema


def create_part_object(
        part: Part,
        collection: Any,
        category_collection: Any
) -> PartSchema:
    """
    Create a new part object in the specified collection.

    Parameters:
    - part (Part): The part object to be created.
    - collection (Any): The MongoDB collection where the part will be stored.
    - category_collection (Any): The MongoDB collection where categories are stored.

    Returns:
    - PartSchema: The newly created part as a PartSchema object.
    """
    # Check if the specified category exists
    existing_category = get_category_object(part.category, category_collection)
    if not existing_category:
        raise HTTPException(status_code=404, detail="Category not found")

    # Check if the category is the 'base' category, and disallow assigning parts to it
    if existing_category.parent_name is None:
        raise HTTPException(status_code=400, detail="Cannot assign part to 'base' category")

    # Check if a part with the same serial number already exists
    existing_part = collection.find_one({"serial_number": part.serial_number})
    if existing_part:
        raise HTTPException(status_code=400, detail="Part with this serial_number already exists")

    _id = collection.insert_one(part.dict()).inserted_id
    inserted_part = collection.find_one({"_id": _id})
    return PartSchema(**inserted_part)


def get_part_object(
        serial_number: str,
        collection: Any
) -> PartSchema:
    """
    Retrieve a part object from the specified collection by its serial number.

    Parameters:
    - serial_number (str): The serial number of the part to be retrieved.
    - collection (Any): The MongoDB collection where the part is stored.

    Returns:
    - PartSchema: The retrieved part as a PartSchema object.
    """
    inserted_part = collection.find_one({"serial_number": serial_number})

    # Raise an exception if the part is not found
    if not inserted_part:
        raise HTTPException(status_code=404, detail="Part not found")

    return PartSchema(**inserted_part)


def update_part_object(
        serial_number: str,
        part: Part,
        collection: Any,
        category_collection: Any
) -> PartSchema:
    """
    Update a part object in the specified collection by its serial number.

    Parameters:
    - serial_number (str): The serial number of the part to be updated.
    - part (Part): The updated data for the part.
    - collection (Any): The MongoDB collection where the part is stored.
    - category_collection (Any): The MongoDB collection where categories are stored.

    Returns:
    - PartSchema: The updated part as a PartSchema object.
    """
    existing_part = collection.find_one({"serial_number": serial_number})

    # Check if the part with the specified serial number exists
    if not existing_part:
        raise HTTPException(status_code=404, detail="Part not found")

    # Check if the specified category exists
    existing_category = get_category_object(part.category, category_collection)
    if not existing_category:
        raise HTTPException(status_code=404, detail="Category not found")

    update_data = {
        "$set": {
            "serial_number": part.serial_number,
            "name": part.name,
            "description": part.description,
            "category": part.category,
            "quantity": part.quantity,
            "price": part.price,
            "location": part.location.model_dump(),
        }
    }

    collection.update_one({"serial_number": serial_number}, update_data)

    updated_part = collection.find_one({"serial_number": part.serial_number})
    return PartSchema(**updated_part)

def delete_part_object(
        serial_number: str,
        collection: Any
) -> Dict[str, str]:
    """
    Delete a part object from the specified collection by its serial number.

    Parameters:
    - serial_number (str): The serial number of the part to be deleted.
    - collection (Any): The MongoDB collection where the part is stored.

    Returns:
    - Dict[str, str]: A dictionary indicating the success of the deletion.
    """
    part = collection.find_one({"serial_number": serial_number})

    # Raise an exception if the part is not found
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")

    collection.delete_one({"serial_number": serial_number})
    return {"message": "Part deleted successfully"}


def list_search_part_objects(
        query_params: Dict[str, Any],
        collection: Any
) -> List[PartSchema]:
    """
    List and search part objects in the specified collection based on query parameters.

    Parameters:
    - query_params (Dict[str, Any]): A dictionary of query parameters for filtering parts.
    - collection (Any): The MongoDB collection where parts are stored.

    Returns:
    - List[PartSchema]: A list of part objects that match the query parameters.
    """
    filter_query = {}
    for key, value in query_params.items():
        if value is not None:
            filter_query[key] = {"$regex": str(value), "$options": "i"}

    inserted_parts = list(collection.find(filter_query))

    # Raise an exception if no parts match the query parameters
    if not inserted_parts:
        raise HTTPException(status_code=404, detail="Part not found")

    return inserted_parts
