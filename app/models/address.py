from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, text
from datetime import datetime


class Address(Base):
    __tablename__ = "addresses"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    building: Mapped[str] = mapped_column(String(60))
    street: Mapped[str] = mapped_column(String(60))
    district: Mapped[str] = mapped_column(String(60))
    city: Mapped[str] = mapped_column(String(60))
    governorate: Mapped[str] = mapped_column(String(60))
    phone: Mapped[str] = mapped_column(String(15))
    created_at: Mapped[datetime] = mapped_column(server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
