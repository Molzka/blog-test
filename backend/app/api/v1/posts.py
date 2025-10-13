from app.core.database import get_async_session
from app.core.dependencies import get_post_service
from app.schemas.post import PostCreate
from app.services.post_service import PostService
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/")
async def get_posts(
    db: AsyncSession = Depends(get_async_session),
    service: PostService = Depends(get_post_service),
):
    return await service.get_all_posts(db)


@router.post("/")
async def create_post(
    data: PostCreate,
    db: AsyncSession = Depends(get_async_session),
    service: PostService = Depends(get_post_service),
):
    return await service.create_post(db, data)
