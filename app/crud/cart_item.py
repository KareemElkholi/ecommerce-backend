from sqlalchemy.orm import Session

from app.models.cart_item import CartItem
from app.schemas.cart_item import CartItemCreate, CartItemUpdate


class CRUDCartItem():
    def create_cart_item(db: Session, user_id: int, cart_item: CartItemCreate):
        db_cart_item = db.query(CartItem).filter(CartItem.user_id == user_id, CartItem.product_id == cart_item.product_id).first()
        if db_cart_item:
            raise ValueError
        db_cart_item = CartItem(
            user_id=user_id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity
        )
        try:
            db.add(db_cart_item)
            db.commit()
            return db_cart_item
        except Exception:
            db.rollback()
            raise

    def get_cart_items(db: Session, user_id: int):
        db_cart_items = db.query(CartItem).filter(CartItem.user_id == user_id).all()
        if db_cart_items == []:
            raise ValueError
        return db_cart_items

    def get_cart_item(db: Session, user_id: int, product_id: int):
        db_cart_item = db.query(CartItem).filter(CartItem.user_id == user_id, CartItem.product_id == product_id).first()
        if db_cart_item is None:
            raise ValueError
        return db_cart_item

    def update_cart_item(db: Session, user_id: int, product_id: int, cart_item: CartItemUpdate):
        db_cart_item = CRUDCartItem.get_cart_item(db, user_id, product_id)
        try:
            for key, value in cart_item.model_dump(exclude_unset=True).items():
                setattr(db_cart_item, key, value)
            db.commit()
            return db_cart_item
        except Exception:
            db.rollback()
            raise

    def delete_cart_item(db: Session, user_id: int, product_id: int):
        db_cart_item = CRUDCartItem.get_cart_item(db, user_id, product_id)
        try:
            db.delete(db_cart_item)
            db.commit()
            return db_cart_item
        except Exception:
            db.rollback()
            raise
