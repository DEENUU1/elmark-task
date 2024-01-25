from typing import Optional

from pydantic import BaseModel, Field


class Category(BaseModel):
    name: str
    parent_name: Optional[str] = None
