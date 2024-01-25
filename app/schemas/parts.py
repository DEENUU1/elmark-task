from models.parts import Part, Location
from pydantic import BaseModel, Field


class PartSchema(Part):
    pass


class PartCreateSchema(BaseModel):
    serial_number: str = Field(unique=True)
    name: str
    description: str
    category: str
    quantity: int = Field(ge=0)
    price: float = Field(ge=0)
    location: Location


class PartUpdateSchema(PartCreateSchema):
    pass


