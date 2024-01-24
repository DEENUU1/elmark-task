from typing import Dict, Optional
from models.categories import Category


def get_category_serializer(category: Category) -> Dict[str, Optional[str]]:
    return {
        "id": str(category["_id"]),
        "name": category["name"],
        "parent_name": category["parent_name"],
    }
