from typing import List

from app.models.post import Post
from app.repositories.post_repository import PostRepository
from app.schemas.post import PostCreate
from sqlalchemy.ext.asyncio import AsyncSession


class PostService:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    async def create_post(self, db: AsyncSession, data: PostCreate) -> Post:
        post = Post(title=data.title, content=data.content)

        return await self.repo.create(db, post)

    async def get_all_posts(self, db: AsyncSession) -> List[Post]:
        posts = await self.repo.get_all(db)
        return posts
