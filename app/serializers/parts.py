from models.parts import Part
from typing import Dict, Any, List


def get_part_serializer(part: Part) -> Dict[str, Any]:
    return {
        "id": str(part["_id"]),
        "serial_number": part["serial_number"],
        "name": part["name"],
        "description": part["description"],
        "category": part["category"],
        "quantity": part["quantity"],
        "price": part["price"],
        "location": part["location"],
    }


def get_parts_serializer(parts: [Part]) -> List[Dict[str, Any]]:
    return [get_part_serializer(part) for part in parts]
