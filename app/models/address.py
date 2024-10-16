from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text

from app.config.database import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    building = Column(String(60))
    street = Column(String(60))
    district = Column(String(60))
    city = Column(String(60))
    governorate = Column(String(60))
    country = Column(String(60))
    phone = Column(String(15))
    created_at = Column(DateTime, server_default=text("NOW()"))
    updated_at = Column(DateTime, server_default=text("NOW() ON UPDATE NOW()"))
