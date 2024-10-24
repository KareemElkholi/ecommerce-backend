from sqlalchemy import CheckConstraint, Column, DateTime, ForeignKey, Integer, String, Text, text

from app.config.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    category_id = Column(ForeignKey("categories.id", ondelete="CASCADE"))
    name = Column(String(60))
    description = Column(Text)
    stock = Column(Integer, CheckConstraint("stock >= 0"))
    price = Column(Integer)
    discount = Column(Integer)
    created_at = Column(DateTime, server_default=text("NOW()"))
    updated_at = Column(DateTime, server_default=text("NOW() ON UPDATE NOW()"))
