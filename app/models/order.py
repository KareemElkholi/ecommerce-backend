from enum import Enum as PyEnum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, text

from app.config.database import Base


class Status(PyEnum):
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id", ondelete="SET NULL"))
    address_id = Column(ForeignKey("addresses.id", ondelete="SET NULL"))
    total_amount = Column(Integer)
    status = Column(Enum(Status), server_default="PROCESSING")
    created_at = Column(DateTime, server_default=text("NOW()"))
    updated_at = Column(DateTime, server_default=text("NOW() ON UPDATE NOW()"))


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey("orders.id", ondelete="CASCADE"))
    product_id = Column(ForeignKey("products.id", ondelete="SET NULL"))
    quantity = Column(Integer)
    price = Column(Integer)
