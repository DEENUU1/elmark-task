from typing import Dict, Any

from fastapi import HTTPException

from config.database import collection_parts
from models.parts import Part
from serializers.parts import get_part_serializer


def create_part_object(part: Part) -> Dict[str, Any]:
    _id = collection_parts.insert_one(part.dict()).inserted_id
    inserted_part = collection_parts.find_one({"_id": _id})
    return get_part_serializer(inserted_part)


def get_part_object(serial_number: str) -> Dict[str, Any]:
    inserted_part = collection_parts.find_one({"serial_number": serial_number})
    if not inserted_part:
        raise HTTPException(status_code=404, detail="Part not found")

    return get_part_serializer(inserted_part)


def update_part_object(serial_number: str, part: Part) -> Dict[str, Any]:
    collection_parts.update_one({"serial_number": serial_number}, {"$set": part.dict()})
    inserted_part = collection_parts.find_one({"serial_number": serial_number})
    return get_part_serializer(inserted_part)


def delete_part_object(serial_number: str) -> Dict[str, Any]:
    part = collection_parts.find_one({"serial_number": serial_number})
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")

    collection_parts.delete_one({"serial_number": serial_number})
    return get_part_serializer(part)
