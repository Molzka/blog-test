import asyncio
import logging

from app.core.config import settings
from app.core.database import engine
from app.models.user import User
from app.schemas.user import UserCreate
from app.services.user_service import UserService
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user_service = UserService()


async def init() -> None:
    async with AsyncSession(engine) as session:
        user = (
            await session.execute(
                select(User).where(User.email == settings.FIRST_SUPERUSER)
            )
        ).first()
        if not user:
            user_in = UserCreate(
                email=settings.FIRST_SUPERUSER,
                password=settings.FIRST_SUPERUSER_PASSWORD,
                full_name=settings.FIRST_SUPERUSER_NAME,
                username=settings.FIRST_SUPERUSER_NAME,
                is_superuser=True,
            )
            user = await user_service.create_user(db=session, user_create=user_in)


async def main() -> None:
    logger.info("Creating initial data...")
    await init()
    logger.info("Initial data created successfully.")


if __name__ == "__main__":
    asyncio.run(main())
