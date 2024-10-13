from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(getenv("DB_URI"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
