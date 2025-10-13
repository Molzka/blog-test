from app.repositories.post_repository import PostRepository
from app.repositories.user_repository import UserRepository
from app.services.post_service import PostService
from app.services.user_service import UserService
from fastapi import Depends


def get_user_repository() -> UserRepository:
    return UserRepository()


def get_user_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(user_repository)


def get_post_repository() -> PostRepository:
    return PostRepository()


def get_post_service(
    post_repository: PostRepository = Depends(get_post_repository),
) -> PostService:
    return PostService(post_repository)
