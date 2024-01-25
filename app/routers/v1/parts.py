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
from schemas.parts import PartSchema


router = APIRouter(
    prefix="/part",
    tags=["part"],
)


@router.post("/", response_model=PartSchema)
def create_part(
        part: Part,
        collection: Any = Depends(get_parts_collection),
        collection_category: Any = Depends(get_categories_collection),
) -> PartSchema:
    return create_part_object(part, collection, collection_category)


@router.get("/{serial_number}", response_model=PartSchema)
def get_part(
        serial_number: str,
        collection: Any = Depends(get_parts_collection)
) -> PartSchema:
    return get_part_object(serial_number, collection)


@router.post("/{serial_number}", response_model=PartSchema)
def update_part(
        serial_number: str,
        part: Part,
        collection: Any = Depends(get_parts_collection)
) -> PartSchema:
    return update_part_object(serial_number, part, collection)


@router.delete("/{serial_number}")
def delete_part(
        serial_number: str,
        collection: Any = Depends(get_parts_collection)
) -> Dict[str, str]:
    return delete_part_object(serial_number, collection)


@router.get("/", response_model=List[PartSchema])
def list_search_parts(
        query_params: SearchParams = Depends(),
        collection: Any = Depends(get_parts_collection)
) -> List[PartSchema]:
    results = list_search_part_objects(query_params.dict(exclude_unset=True), collection)
    return results
