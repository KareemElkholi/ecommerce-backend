from datetime import datetime

from pydantic import BaseModel, Field


class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)


class CartItem(CartItemCreate):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime


class CartItemUpdate(BaseModel):
    quantity: int = Field(ge=1)
