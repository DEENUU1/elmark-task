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
    existing_category = get_category_object(part.category, category_collection)
    if not existing_category:
        raise HTTPException(status_code=404, detail="Category not found")

    if not existing_category["parent_name"]:
        raise HTTPException(status_code=400, detail="Cannot assign part to 'base' category")

    existing_part = collection.find_one({"serial_number": part.serial_number})
    if existing_part:
        raise HTTPException(status_code=400, detail="Part with this serial_number already exists")

    _id = collection.insert_one(part.dict()).inserted_id
    inserted_part = collection.find_one({"_id": _id})
    return inserted_part


def get_part_object(
        serial_number: str,
        collection: Any
) -> PartSchema:
    inserted_part = collection.find_one({"serial_number": serial_number})
    if not inserted_part:
        raise HTTPException(status_code=404, detail="Part not found")

    return inserted_part


def update_part_object(
        serial_number: str,
        part: Part,
        collection: Any
) -> PartSchema:
    # Todo create model for update method
    collection.update_one({"serial_number": serial_number}, {"$set": part.dict()})
    inserted_part = collection.find_one({"serial_number": serial_number})
    return inserted_part


def delete_part_object(
        serial_number: str,
        collection: Any
) -> Dict[str, str]:
    part = collection.find_one({"serial_number": serial_number})
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")

    collection.delete_one({"serial_number": serial_number})
    return {"message": "Part deleted successfully"}


def list_search_part_objects(
        query_params: Dict[str, Any],
        collection: Any
) -> List[PartSchema]:
    filter_query = {}
    for key, value in query_params.items():
        if value is not None:
            filter_query[key] = {"$regex": str(value), "$options": "i"}

    inserted_parts = list(collection.find(filter_query))
    if not inserted_parts:
        raise HTTPException(status_code=404, detail="Part not found")

    return inserted_parts
