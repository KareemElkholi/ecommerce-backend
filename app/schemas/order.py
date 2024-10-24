from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.models.order import Status


class OrderCreate(BaseModel):
    address_id: int


class Order(OrderCreate):
    id: int
    user_id: int
    total_amount: int
    status: Status
    created_at: datetime
    updated_at: datetime


class OrderUpdate(BaseModel):
    status: Status


class OrderItem(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    price: int
