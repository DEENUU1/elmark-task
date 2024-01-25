from typing import Dict, Any, Optional
from fastapi import APIRouter, Depends, Query
from config.database import get_parts_collection, get_categories_collection
from models.parts import Part, Location
from services.parts import (
    create_part_object,
    get_part_object,
    update_part_object,
    delete_part_object,
    search_part
)


router = APIRouter(
    prefix="/part",
    tags=["part"],
)


@router.post("/")
def create_part(part: Part, collection: Any = Depends(get_parts_collection), collection_category: Any = Depends(get_categories_collection)) -> Dict[str, Any]:
    return create_part_object(part, collection, collection_category)


@router.get("/{serial_number}")
def get_part(serial_number: str, collection: Any = Depends(get_parts_collection)) -> Dict[str, Any]:
    return get_part_object(serial_number, collection)


@router.post("/{serial_number}")
def update_part(serial_number: str, part: Part, collection: Any = Depends(get_parts_collection)) -> Dict[str, Any]:
    return update_part_object(serial_number, part, collection)


@router.delete("/{serial_number}")
def delete_part(serial_number: str, collection: Any = Depends(get_parts_collection)) -> Dict[str, Any]:
    return delete_part_object(serial_number, collection)


@router.get("/search")
def search_part(
    serial_number: Optional[str] = Query(None, alias="serial-number"),
    name: Optional[str] = None,
    description: Optional[str] = None,
    category: Optional[str] = None,
    quantity: Optional[int] = None,
    price: Optional[float] = None,
    location: Optional[Location] = None,
    collection: Any = Depends(get_parts_collection)
):
    query_params = {
        "serial_number": serial_number,
        "name": name,
        "description": description,
        "category": category,
        "quantity": quantity,
        "price": price,
        "location": location.dict() if location else None
    }

    results = search_part(query_params, collection)
    return results
