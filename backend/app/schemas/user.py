from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    full_name: str
    username: str


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    username: str
    full_name: str
    is_superuser: bool
    created_at: datetime

    class Config:
        orm_mode = True
