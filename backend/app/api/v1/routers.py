from app.api.v1.posts import router as posts_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(posts_router)
