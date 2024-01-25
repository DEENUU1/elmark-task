from typing import Dict, Any, List
from fastapi import APIRouter, Depends
from config.database import get_parts_collection, get_categories_collection
from models.parts import Part, SearchParams
from services.parts import (
    create_part_object,
    get_part_object,
    update_part_object,
    delete_part_object,
    list_search_part_objects
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


@router.get("")
def list_search_parts(query_params: SearchParams = Depends(), collection: Any = Depends(get_parts_collection)) -> List[Dict[str, Any]]:
    results = list_search_part_objects(query_params.dict(exclude_unset=True), collection)
    return results
