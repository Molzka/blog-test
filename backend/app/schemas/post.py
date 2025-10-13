from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostOut(PostBase):
    id: int
    slug: str
    created_at: datetime
    author_id: int

    class Config:
        orm_mode = True
