from typing import Dict, Any

from fastapi import HTTPException

from models.parts import Part
from serializers.parts import get_part_serializer


def create_part_object(part: Part, collection: Any) -> Dict[str, Any]:
    # Todo ensure that part is not assigned to 'base' category
    # Todo part should be unique based on serial_number
    _id = collection.insert_one(part.dict()).inserted_id
    inserted_part = collection.find_one({"_id": _id})
    return get_part_serializer(inserted_part)


def get_part_object(serial_number: str, collection: Any) -> Dict[str, Any]:
    inserted_part = collection.find_one({"serial_number": serial_number})
    if not inserted_part:
        raise HTTPException(status_code=404, detail="Part not found")

    return get_part_serializer(inserted_part)


def update_part_object(serial_number: str, part: Part, collection: Any) -> Dict[str, Any]:
    # Todo create model for update method
    collection.update_one({"serial_number": serial_number}, {"$set": part.dict()})
    inserted_part = collection.find_one({"serial_number": serial_number})
    return get_part_serializer(inserted_part)


def delete_part_object(serial_number: str , collection: Any) -> Dict[str, Any]:
    part = collection.find_one({"serial_number": serial_number})
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")

    collection.delete_one({"serial_number": serial_number})
    return get_part_serializer(part)
