from pydantic import BaseModel, Field
from typing import Union, Optional


class Location(BaseModel):
    room: Optional[Union[str, int]] = None
    bookcase: Optional[Union[str, int]] = None
    shelf: Optional[Union[str, int]] = None
    cuvette: Optional[Union[str, int]] = None
    column: Optional[Union[str, int]] = None
    row: Optional[Union[str, int]] = None


class Part(BaseModel):
    serial_number: str = Field(unique=True)
    name: str
    description: str
    category: str
    quantity: int
    price: float
    location: Location


class SearchParams(BaseModel):
    serial_number: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None

