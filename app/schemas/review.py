from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    product_id: int
    rating: int = Field(ge=1, le=5)
    title: Optional[str] = Field(None, min_length=1, max_length=60)
    comment: Optional[str] = None


class Review(ReviewCreate):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime


class ReviewUpdate(BaseModel):
    product_id: int
    rating: Optional[int] = Field(None, ge=1, le=5)
    title: Optional[str] = Field(None, min_length=1, max_length=60)
    comment: Optional[str] = None
