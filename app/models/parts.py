from pydantic import BaseModel, Field, BeforeValidator
from typing import Union, Optional, Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]


class Location(BaseModel):
    room: Optional[Union[str, int]] = None
    bookcase: Optional[Union[str, int]] = None
    shelf: Optional[Union[str, int]] = None
    cuvette: Optional[Union[str, int]] = None
    column: Optional[Union[str, int]] = None
    row: Optional[Union[str, int]] = None


class Part(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    serial_number: str = Field(unique=True)
    name: str
    description: str
    category: str
    quantity: int = Field(ge=0)
    price: float = Field(ge=0)
    location: Location


class SearchParams(BaseModel):
    serial_number: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    room: Optional[str] = None
    bookcase: Optional[str] = None
    shelf: Optional[str] = None
    cuvette: Optional[str] = None
    column: Optional[str] = None
    row: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    min_quantity: Optional[int] = None
    max_quantity: Optional[int] = None

