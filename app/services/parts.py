from typing import Dict, Any

from config.database import collection_parts
from models.parts import Part
from serializers.parts import part_serializer


def create_part_object(part: Part) -> Dict[str, Any]:
    _id = collection_parts.insert_one(dict(part))
    part = part_serializer(collection_parts.find({"_id": _id.inserted_id}))
    return {"part": part}
