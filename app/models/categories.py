from pydantic import BaseModel
from typing import Optional


class Categories(BaseModel):
    name: str
    parent_name: Optional[str] = None