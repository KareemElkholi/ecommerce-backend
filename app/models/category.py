from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, text

from app.config.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    parent_id = Column(ForeignKey("categories.id", ondelete="CASCADE"))
    name = Column(String(30))
    description = Column(Text)
    created_at = Column(DateTime, server_default=text("NOW()"))
    updated_at = Column(DateTime, server_default=text("NOW() ON UPDATE NOW()"))
