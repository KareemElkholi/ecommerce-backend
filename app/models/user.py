from enum import Enum as PyEnum

from sqlalchemy import Column, DateTime, Enum, Integer, String, text

from app.config.database import Base


class Role(PyEnum):
    USER = "user"
    ADMIN = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, index=True)
    password = Column(String(120))
    name = Column(String(60))
    role = Column(Enum(Role), server_default="USER")
    created_at = Column(DateTime, server_default=text("NOW()"))
    updated_at = Column(DateTime, server_default=text("NOW() ON UPDATE NOW()"))
