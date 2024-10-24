from sqlalchemy.orm import Session

from app.models.review import Review
from app.schemas.review import ReviewCreate, ReviewUpdate


class CRUDReview():
    def create_review(db: Session, user_id: int, review: ReviewCreate):
        db_review = db.query(Review).filter(Review.user_id == user_id, Review.product_id == review.product_id).first()
        if db_review:
            raise ValueError
        db_review = Review(
            user_id=user_id,
            product_id=review.product_id,
            rating=review.rating,
            title=review.title,
            comment=review.comment
        )
        try:
            db.add(db_review)
            db.commit()
            return db_review
        except Exception:
            db.rollback()
            raise

    def get_reviews(db: Session, user_id: int):
        return db.query(Review).filter(Review.user_id == user_id).all()

    def get_product_reviews(db: Session, product_id: int):
        return db.query(Review).filter(Review.product_id == product_id).all()

    def get_review(db: Session, user_id: int, product_id: int):
        db_review = db.query(Review).filter(Review.user_id == user_id, Review.product_id == product_id).first()
        if db_review is None:
            raise ValueError
        return db_review

    def update_review(db: Session, user_id: int, product_id: int, review: ReviewUpdate):
        db_review = CRUDReview.get_review(db, user_id, product_id)
        try:
            for key, value in review.model_dump(exclude_unset=True).items():
                setattr(db_review, key, value)
            db.commit()
            return db_review
        except Exception:
            db.rollback()
            raise

    def delete_review(db: Session, user_id: int, product_id: int):
        db_review = CRUDReview.get_review(db, user_id, product_id)
        try:
            db.delete(db_review)
            db.commit()
            return db_review
        except Exception:
            db.rollback()
            raise
