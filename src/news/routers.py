from typing import Sequence

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from .models import Category, News
from .schemas import CategoryReadSchema, CategoryCreateSchema, NewsCreateSchema, NewsReadSchema

from src.database import session as async_session

category_router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

news_router = APIRouter(
    prefix="/news",
    tags=["News"]
)

@category_router.get("", response_model=Sequence[CategoryReadSchema])
async def get_categories(offset: int = 0, limit: int = 50) -> Sequence[Category]:
    async with async_session() as session:
        query = select(Category).offset(offset).limit(limit)
        categories = await session.execute(query)
        categories = categories.scalars().all()
        return categories

@category_router.get("/{category_id}", response_model=CategoryReadSchema)
async def get_category(category_id: int) -> Category:
    async with async_session() as session:
        query = select(Category).where(Category.id == category_id)
        result = await session.execute(query)
        category = result.scalar_one_or_none()
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

@category_router.post("", response_model=CategoryReadSchema)
async def create_category(category: CategoryCreateSchema) -> Category:
    async with async_session() as session:
        new_category = Category(**category.dict())
        session.add(new_category)
        await session.commit()
        await session.refresh(new_category)
        return new_category

@category_router.delete("/{category_id}")
async def delete_category(category_id: int) -> str:
    async with async_session() as session:
        query = select(Category).where(Category.id == category_id)
        result = await session.execute(query)
        category = result.scalar_one_or_none()
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        await session.delete(category)
        await session.commit()
        return "deleted."

@category_router.put("", response_model=CategoryReadSchema)
async def update_category(category_id: int, category: CategoryCreateSchema) -> Category:
    async with async_session() as session:
        query = select(Category).where(Category.id == category_id)
        result = await session.execute(query)
        old_category = result.scalar_one_or_none()
        if old_category is None:
            raise HTTPException(status_code=404, detail="Category not found")

        for key, value in category.dict().items():
            setattr(old_category, key, value)

        await session.commit()
        await session.refresh(old_category)
        return old_category

@category_router.patch("", response_model=CategoryReadSchema)
async def patch_category(category_id: int, category: CategoryCreateSchema) -> Category:
    async with async_session() as session:
        query = select(Category).where(Category.id == category_id)
        result = await session.execute(query)
        old_category = result.scalar_one_or_none()
        if old_category is None:
            raise HTTPException(status_code=404, detail="Category not found")

        for key, value in category.dict().items():
            if value:
                setattr(old_category, key, value)

        await session.commit()
        await session.refresh(old_category)
        return old_category




""""""

@news_router.get("", response_model=Sequence[NewsReadSchema])
async def get_news(offset: int = 0, limit: int = 10) -> Sequence[News]:
    async with async_session() as session:
        query = select(News).offset(offset).limit(limit)
        news = await session.execute(query)
        news = news.scalars().all()
        return news

@news_router.get("/{news_id}", response_model=NewsReadSchema)
async def get_news(news_id: int) -> News:
    async with async_session() as session:
        query = select(News).where(News.id == news_id)
        result = await session.execute(query)
        news = result.scalar_one_or_none()
        if news is None:
            raise HTTPException(status_code=404, detail="News not found")
        return news

@news_router.post("", response_model=NewsReadSchema)
async def create_news(news: NewsCreateSchema) -> News:
    async with async_session() as session:
        new_news = News(**news.dict())
        session.add(new_news)
        await session.commit()
        await session.refresh(new_news)
        return new_news

@news_router.delete("/{news_id}")
async def delete_news(news_id: int) -> str:
    async with async_session() as session:
        query = select(News).where(News.id == news_id)
        result = await session.execute(query)
        news = result.scalar_one_or_none()
        if news is None:
            raise HTTPException(status_code=404, detail="Category not found")
        await session.delete(news)
        await session.commit()
        return "deleted."

@news_router.put("", response_model=NewsReadSchema)
async def update_news(news_id: int, news: NewsCreateSchema) -> News:
    async with async_session() as session:
        query = select(News).where(News.id == news_id)
        result = await session.execute(query)
        old_news = result.scalar_one_or_none()
        if old_news is None:
            raise HTTPException(status_code=404, detail="Category not found")

        for key, value in news.dict().items():
            setattr(old_news, key, value)

        await session.commit()
        await session.refresh(old_news)
        return old_news

@news_router.patch("", response_model=NewsReadSchema)
async def patch_news(news_id: int, news: NewsCreateSchema) -> News:
    async with async_session() as session:
        query = select(News).where(News.id == news_id)
        result = await session.execute(query)
        old_news = result.scalar_one_or_none()
        if old_news is None:
            raise HTTPException(status_code=404, detail="Category not found")

        for key, value in news.dict().items():
            if value:
                setattr(old_news, key, value)

        await session.commit()
        await session.refresh(old_news)
        return old_news