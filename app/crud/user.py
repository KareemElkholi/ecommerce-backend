from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser():
    def create_user(db: Session, user: UserCreate):
        db_user = User(
            username=user.username,
            name=user.name,
            password=user.password
        )
        try:
            db.add(db_user)
            db.commit()
            return db_user
        except Exception:
            db.rollback()
            raise

    def get_user(db: Session, id: int):
        db_user = db.query(User).filter(User.id == id).first()
        if db_user is None:
            raise ValueError
        return db_user

    def update_user(db: Session, id: int, user: UserUpdate):
        db_user = CRUDUser.get_user(db, id)
        try:
            for key, value in user.model_dump(exclude_unset=True).items():
                setattr(db_user, key, value)
            db.commit()
            return db_user
        except Exception:
            db.rollback()
            raise

    def delete_user(db: Session, id: int):
        db_user = CRUDUser.get_user(db, id)
        try:
            db.delete(db_user)
            db.commit()
            return db_user
        except Exception:
            db.rollback()
            raise
