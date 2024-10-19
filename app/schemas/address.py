from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class AddressCreate(BaseModel):
    building: str = Field(min_length=1, max_length=60)
    street: str = Field(min_length=1, max_length=60)
    district: str = Field(min_length=1, max_length=60)
    city: str = Field(min_length=1, max_length=60)
    governorate: str = Field(min_length=1, max_length=60)
    country: str = Field(min_length=1, max_length=60)
    phone: str = Field(pattern=r"^\d{1,15}$")


class Address(AddressCreate):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime


class AddressUpdate(BaseModel):
    id: int
    building: Optional[str] = Field(None, min_length=1, max_length=60)
    street: Optional[str] = Field(None, min_length=1, max_length=60)
    district: Optional[str] = Field(None, min_length=1, max_length=60)
    city: Optional[str] = Field(None, min_length=1, max_length=60)
    governorate: Optional[str] = Field(None, min_length=1, max_length=60)
    country: Optional[str] = Field(None, min_length=1, max_length=60)
    phone: Optional[str] = Field(None, pattern=r"^\d{1,15}$")


class AddressDelete(BaseModel):
    id: int
