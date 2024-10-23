from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    category_id: int
    name: str = Field(min_length=1, max_length=60)
    description: Optional[str] = None
    stock: int
    price: int
    discount: int


class Product(ProductCreate):
    id: int
    created_at: datetime
    updated_at: datetime


class ProductUpdate(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = Field(None, min_length=1, max_length=60)
    description: Optional[str] = None
    stock: Optional[int] = None
    price: Optional[int] = None
    discount: Optional[int] = None
