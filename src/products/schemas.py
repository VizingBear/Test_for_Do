from pydantic import BaseModel
import datetime
from typing import List


class Product(BaseModel):

    title: str
    content: str
    category: str | None = None
    published: bool = False


    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListNoteResponse(BaseModel):
    status: str
    results: int
    notes: List[Product]