from datetime import datetime
from typing import List

from pydantic import BaseModel

class CategoryReadSchema(BaseModel):
    id: int
    name: str
    created: datetime

    class Config:
        from_attributes = True


class CategoryCreateSchema(BaseModel):
    name: str


""""""

class NewsReadSchema(BaseModel):
    id: int
    title: str
    content: str | None = None
    images: List[str] | None = None
    created: datetime
    updated: datetime
    category_id: int | None = None

    class Config:
        from_attributes = True


class NewsCreateSchema(BaseModel):
    title: str
    content: str | None = None
    images: List[str] | None = None
    category_id: int | None = None