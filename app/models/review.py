from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, text

from app.config.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    product_id = Column(ForeignKey("products.id", ondelete="CASCADE"))
    rating = Column(Integer)
    title = Column(String(60))
    comment = Column(Text)
    created_at = Column(DateTime, server_default=text("NOW()"))
    updated_at = Column(DateTime, server_default=text("NOW() ON UPDATE NOW()"))
