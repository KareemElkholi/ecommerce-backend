from datetime import datetime

from pydantic import BaseModel


class CartItemCreate(BaseModel):
    product_id: int
    quantity: int


class CartItem(CartItemCreate):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime


class CartItemUpdate(BaseModel):
    product_id: int
    quantity: int
