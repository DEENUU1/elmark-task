from typing import Dict, Any

from fastapi import HTTPException

from config.database import get_parts_collection
from models.parts import Part
from serializers.parts import get_part_serializer


def create_part_object(part: Part) -> Dict[str, Any]:
    _id = get_parts_collection().insert_one(part.dict()).inserted_id
    inserted_part = get_parts_collection().find_one({"_id": _id})
    return get_part_serializer(inserted_part)


def get_part_object(serial_number: str) -> Dict[str, Any]:
    inserted_part = get_parts_collection().find_one({"serial_number": serial_number})
    if not inserted_part:
        raise HTTPException(status_code=404, detail="Part not found")

    return get_part_serializer(inserted_part)


def update_part_object(serial_number: str, part: Part) -> Dict[str, Any]:
    get_parts_collection().update_one({"serial_number": serial_number}, {"$set": part.dict()})
    inserted_part = get_parts_collection().find_one({"serial_number": serial_number})
    return get_part_serializer(inserted_part)


def delete_part_object(serial_number: str) -> Dict[str, Any]:
    part = get_parts_collection().find_one({"serial_number": serial_number})
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")

    get_parts_collection().delete_one({"serial_number": serial_number})
    return get_part_serializer(part)
