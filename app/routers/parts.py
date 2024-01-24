from typing import Dict, Any

from fastapi import APIRouter

from models.parts import Part
from services.parts import (
    create_part_object,
    get_part_object,
    update_part_object,
    delete_part_object,
)

router = APIRouter(
    prefix="/part",
    tags=["part"],
)


@router.post("/")
def create_part(part: Part) -> Dict[str, Any]:
    return create_part_object(part)


@router.get("/{serial_number}")
def get_part(serial_number: str) -> Dict[str, Any]:
    return get_part_object(serial_number)


@router.post("/{serial_number}")
def update_part(serial_number: str, part: Part) -> Dict[str, Any]:
    return update_part_object(serial_number, part)


@router.delete("/{serial_number}")
def delete_part(serial_number: str) -> Dict[str, Any]:
    return delete_part_object(serial_number)
