from typing import Dict, Any

from config.database import collection_parts
from models.parts import Part
from serializers.parts import part_serializer


def create_part_object(part: Part) -> Dict[str, Any]:
    result = collection_parts.insert_one(dict(part))
    inserted_id = result.inserted_id
    inserted_part = collection_parts.find_one({"_id": inserted_id})
    serialized_part = part_serializer(inserted_part)
    return {"part": serialized_part}
