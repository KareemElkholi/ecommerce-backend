from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate


class CRUDCategory():
    def create_category(db: Session, category: CategoryCreate):
        db_category = Category(
            parent_id=category.parent_id,
            name=category.name,
            description=category.description
        )
        try:
            db.add(db_category)
            db.commit()
            return db_category
        except Exception:
            db.rollback()
            raise

    def get_categories(db: Session, parent_id: int):
        if parent_id is None:
            return db.query(Category).all()
        return db.query(Category).filter(Category.parent_id == parent_id).all()

    def get_category(db: Session, id: int):
        db_category = db.query(Category).filter(Category.id == id).first()
        if db_category is None:
            raise ValueError
        return db_category

    def update_category(db: Session, id: int, category: CategoryUpdate):
        db_category = CRUDCategory.get_category(db, id)
        try:
            for key, value in category.model_dump(exclude_unset=True).items():
                setattr(db_category, key, value)
            db.commit()
            return db_category
        except Exception:
            db.rollback()
            raise

    def delete_category(db: Session, id: int):
        db_category = CRUDCategory.get_category(db, id)
        try:
            db.delete(db_category)
            db.commit()
            return db_category
        except Exception:
            db.rollback()
            raise
