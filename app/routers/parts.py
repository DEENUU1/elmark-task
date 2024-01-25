from typing import Dict, Any, List
from fastapi import APIRouter, Depends
from config.database import get_db
from pymongo import MongoClient
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
def create_part(part: Part, db: MongoClient = Depends(get_db)) -> Dict[str, Any]:
    return create_part_object(part, db)


@router.get("/{serial_number}")
def get_part(serial_number: str, db: MongoClient = Depends(get_db)) -> Dict[str, Any]:
    return get_part_object(serial_number, db)


@router.post("/{serial_number}")
def update_part(serial_number: str, part: Part, db: MongoClient = Depends(get_db)) -> Dict[str, Any]:
    return update_part_object(serial_number, part, db)


@router.delete("/{serial_number}")
def delete_part(serial_number: str, db: MongoClient = Depends(get_db)) -> Dict[str, Any]:
    return delete_part_object(serial_number, db)


@router.get("/")
def list_search_parts(query_params: SearchParams = Depends(), db: MongoClient = Depends(get_db)) -> List[Dict[str, Any]]:
    results = list_search_part_objects(query_params.dict(exclude_unset=True), db)
    return results
