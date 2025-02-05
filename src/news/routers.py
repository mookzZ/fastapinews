from typing import Sequence

from fastapi import APIRouter
from sqlalchemy import select

from .models import Category
from .schemas import CategoryReadSchema, CategoryCreateSchema

from src.database import session as async_session

category_router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@category_router.get("", response_model=Sequence[CategoryReadSchema])
async def get_categories(offset: int = 0, limit: int = 10) -> Sequence[Category]:
    async with async_session() as session:
        query = select(Category).offset(offset).limit(limit)
        categories = await session.execute(query)
        categories = categories.scalars().all()
        return categories


@category_router.post("", response_model=CategoryReadSchema)
async def create_category(category: CategoryCreateSchema) -> Category:
    async with async_session() as session:
        new_category = Category(**category.dict())
        session.add(new_category)
        await session.commit()
        await session.refresh(new_category)
        return new_category