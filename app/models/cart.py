from sqlalchemy import Column, DateTime, ForeignKey, Integer, text

from app.config.database import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    product_id = Column(ForeignKey("products.id", ondelete="CASCADE"))
    quantity = Column(Integer)
    created_at = Column(DateTime, server_default=text("NOW()"))
    updated_at = Column(DateTime, server_default=text("NOW() ON UPDATE NOW()"))
