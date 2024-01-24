from typing import Dict, Optional

from config.database import collection_categories
from models.categories import Category
from serializers.categories import get_category_serializer


def create_category_object(category: Category) -> Dict[str, Optional[str]]:
    _id = collection_categories.insert_one(category.dict()).inserted_id
    inserted_category = collection_categories.find_one({"_id": _id})
    return get_category_serializer(inserted_category)
