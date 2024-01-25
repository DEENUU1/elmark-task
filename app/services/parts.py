from typing import Dict, Any, List

from fastapi import HTTPException
from pymongo import MongoClient

from models.parts import Part
from serializers.parts import get_part_serializer, get_parts_serializer
from .categories import get_category_object


def create_part_object(
        part: Part,
        db: MongoClient
) -> Dict[str, Any]:
    existing_category = get_category_object(part.category, db.categories)
    if not existing_category:
        raise HTTPException(status_code=404, detail="Category not found")

    if not existing_category["parent_name"]:
        raise HTTPException(status_code=400, detail="Cannot assign part to 'base' category")

    existing_part = db.parts.find_one({"serial_number": part.serial_number})
    if existing_part:
        raise HTTPException(status_code=400, detail="Part with this serial_number already exists")

    _id = db.parts.insert_one(part.dict()).inserted_id
    inserted_part = db.parts.find_one({"_id": _id})
    return get_part_serializer(inserted_part)


def get_part_object(
        serial_number: str,
        db: MongoClient
) -> Dict[str, Any]:
    inserted_part = db.parts.find_one({"serial_number": serial_number})
    if not inserted_part:
        raise HTTPException(status_code=404, detail="Part not found")

    return get_part_serializer(inserted_part)


def update_part_object(
        serial_number: str,
        part: Part,
        db: MongoClient
) -> Dict[str, Any]:
    # Todo create model for update method
    db.parts.update_one({"serial_number": serial_number}, {"$set": part.dict()})
    inserted_part = db.parts.find_one({"serial_number": serial_number})
    return get_part_serializer(inserted_part)


def delete_part_object(
        serial_number: str,
        db: MongoClient
) -> Dict[str, Any]:
    part = db.parts.find_one({"serial_number": serial_number})
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")

    db.parts.delete_one({"serial_number": serial_number})
    return get_part_serializer(part)


def list_search_part_objects(
        query_params: Dict[str, Any],
        db: MongoClient
) -> List[Dict[str, Any]]:
    filter_query = {}
    for key, value in query_params.items():
        if value is not None:
            filter_query[key] = value

    inserted_parts = list(db.parts.find(filter_query))
    if not inserted_parts:
        raise HTTPException(status_code=404, detail="Part not found")

    return get_parts_serializer(inserted_parts)
