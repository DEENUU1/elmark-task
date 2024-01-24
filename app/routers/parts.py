from typing import List, Optional, Dict, Any
from fastapi import APIRouter
from services.parts import create_part_object
from models.parts import Part


router = APIRouter(
    prefix="/part",
    tags=["part"],
)


@router.post("/")
def create_part(part: Part) -> Dict[str, Any]:
    return create_part_object(part)
