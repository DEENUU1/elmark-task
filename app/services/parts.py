from typing import Dict, Any, List

from fastapi import HTTPException

from .categories import get_category_object_by_name
from schemas.parts import PartSchema, PartCreateSchema, PartUpdateSchema
from bson import ObjectId


def create_part_object(
        part: PartCreateSchema,
        collection: Any,
        category_collection: Any
) -> PartCreateSchema:
    """
    Create a new part object in the specified collection.

    Parameters:
    - part (PartCreateSchema): The part object to be created.
    - collection (Any): The MongoDB collection where the part will be stored.
    - category_collection (Any): The MongoDB collection where categories are stored.

    Returns:
    - PartCreateSchema: The newly created part as a PartSchema object.
    """
    # Check if the specified category exists

    existing_category = get_category_object_by_name(part.category, category_collection)
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
    return PartCreateSchema(**inserted_part)


def get_part_object(
        part_id: str,
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
    inserted_part = collection.find_one({"_id": ObjectId(part_id)})

    # Raise an exception if the part is not found
    if not inserted_part:
        raise HTTPException(status_code=404, detail="Part not found")

    return PartSchema(**inserted_part)


def update_part_object(
        part_id: str,
        part: PartUpdateSchema,
        collection: Any,
        category_collection: Any
) -> PartUpdateSchema:
    """
    Update a part object in the specified collection by its serial number.

    Parameters:
    - serial_number (str): The serial number of the part to be updated.
    - part (PartCreateSchema): The updated data for the part.
    - collection (Any): The MongoDB collection where the part is stored.
    - category_collection (Any): The MongoDB collection where categories are stored.

    Returns:
    - PartCreateSchema: The updated part as a PartSchema object.
    """
    existing_part = collection.find_one({"_id": ObjectId(part_id)})

    # Check if the part with the specified serial number exists
    if not existing_part:
        raise HTTPException(status_code=404, detail="Part not found")

    # Check if the specified category exists
    existing_category = get_category_object_by_name(part.category, category_collection)
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

    collection.update_one({"_id": existing_part.get("_id")}, update_data)

    updated_part = collection.find_one({"serial_number": part.serial_number})
    return PartUpdateSchema(**updated_part)


def delete_part_object(
        part_id: str,
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
    part = collection.find_one({"_id": ObjectId(part_id)})

    # Raise an exception if the part is not found
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")

    collection.delete_one({"_id": part.get("_id")})
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

    location_params = {
        "room", "bookcase", "shelf", "cuvette", "column", "row"
    }

    for key, value in query_params.items():
        if value is not None:
            if key in location_params:
                filter_query[f"location.{key}"] = {"$regex": str(value), "$options": "i"}
            elif key == "min_price":
                filter_query["price"] = {"$gte": value}
            elif key == "max_price":
                filter_query["price"] = {"$lte": value}
            elif key == "min_quantity":
                filter_query["quantity"] = {"$gte": value}
            elif key == "max_quantity":
                filter_query["quantity"] = {"$lte": value}
            else:
                filter_query[key] = {"$regex": str(value), "$options": "i"}

    inserted_parts = list(collection.find(filter_query))

    # Raise an exception if no parts match the query parameters
    if not inserted_parts:
        raise HTTPException(status_code=404, detail="Part not found")

    return inserted_parts
