from pydantic import BaseModel


class Part(BaseModel):
    serial_number: str
    name: str
    description: str
    category: str
    quantity: int
    price: float
    location: dict
