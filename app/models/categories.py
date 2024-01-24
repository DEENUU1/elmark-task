from typing import Optional

from pydantic import BaseModel


class Categorie(BaseModel):
    name: str
    parent_name: Optional[str] = None
