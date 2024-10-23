from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    parent_id: Optional[int] = None
    name: str = Field(min_length=1, max_length=30)
    description: Optional[str] = None


class Category(CategoryCreate):
    id: int
    created_at: datetime
    updated_at: datetime


class CategoryUpdate(BaseModel):
    parent_id: Optional[int] = None
    name: Optional[str] = Field(None, min_length=1, max_length=30)
    description: Optional[str] = None
