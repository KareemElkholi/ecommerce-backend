from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.models.user import Role


class UserBase(BaseModel):
    username: str = Field(pattern=r"^[A-Za-z0-9_]{1,30}$")
    name: str = Field(min_length=1, max_length=60)


class UserCreate(UserBase):
    password: str = Field(min_length=8)


class User(UserBase):
    id: int
    role: Role
    created_at: datetime
    updated_at: datetime


class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, pattern=r"^[A-Za-z0-9_]{1,30}$")
    name: Optional[str] = Field(None, min_length=1, max_length=60)
    password: Optional[str] = Field(None, min_length=8)
