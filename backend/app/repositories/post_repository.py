from typing import List
from app.models.post import Post
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class PostRepository:
    async def get_all(self, db: AsyncSession) -> List[Post]:
        result = await db.execute(select(Post))
        return result.scalars().all()

    async def create(self, db: AsyncSession, post: str) -> Post:
        db.add(post)
        await db.commit()
        await db.refresh(post)
        return post
