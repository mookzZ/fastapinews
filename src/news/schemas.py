from datetime import datetime

from pydantic import BaseModel

class CategoryReadSchema(BaseModel):
    id: int
    name: str
    created: datetime

    class Config:
        orm_mode = True


class CategoryCreateSchema(BaseModel):
    name: str