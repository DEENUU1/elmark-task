from pydantic import BaseModel


class Parts(BaseModel):
    serial_number: str
    name: str
    description: str
    category: str
    quantity: int
    price: float
    location: dict
