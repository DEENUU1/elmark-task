from typing import Dict, Any, Optional, List

from fastapi import HTTPException

from models.parts import Part
from serializers.parts import get_part_serializer
from .categories import get_category_object


def create_part_object(part: Part, collection: Any, category_collection: Any) -> Dict[str, Any]:
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


def delete_part_object(serial_number: str, collection: Any) -> Dict[str, Any]:
    part = collection.find_one({"serial_number": serial_number})
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")

    collection.delete_one({"serial_number": serial_number})
    return get_part_serializer(part)


def search_part(query_params: Dict[str, Any], collection: Any) -> List[Optional[Dict[str, Any]]]:
    filter_query = {}
    for key, value in query_params.items():
        if key == "location":
            for loc_key, loc_value in value.items():
                filter_query[f"location.{loc_key}"] = loc_value
        else:
            filter_query[key] = value

    result = list(collection.find(filter_query))

    return result
