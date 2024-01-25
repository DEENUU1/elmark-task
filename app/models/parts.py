from pydantic import BaseModel


class Part(BaseModel):
    serial_number: str
    name: str
    description: str
    category: str
    quantity: int
    price: float
    location: dict

# Todo validate location field (room, bookcase, shelf, cuveƩe, column, row)
# Input validaƟon for both datasets, with special aƩenƟon to the new 'locaƟon' field and category relationship