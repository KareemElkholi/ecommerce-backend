from sqlalchemy.orm import Session

from app.crud.address import CRUDAddress
from app.crud.cart_item import CRUDCartItem
from app.crud.product import CRUDProduct
from app.models.order import Order, OrderItem
from app.schemas.order import OrderCreate, OrderUpdate


class CRUDOrder():
    def create_order(db: Session, user_id: int, order: OrderCreate):
        try:
            address = CRUDAddress.get_address(db, user_id, order.address_id)
            db_order = Order(
                user_id=user_id,
                address_id=address.id,
                total_amount=0
            )
            db.add(db_order)
            db.flush()
            for item in CRUDCartItem.get_cart_items(db, user_id):
                product = CRUDProduct.get_product(db, item.product_id)
                product.stock -= item.quantity
                db_order.total_amount += item.quantity * product.price
                db_order_item = OrderItem(
                    order_id=db_order.id,
                    product_id=product.id,
                    quantity=item.quantity,
                    price=product.price
                )
                db.add(db_order_item)
                db.delete(item)
            db.commit()
            return db_order
        except Exception:
            db.rollback()
            raise

    def get_orders(db: Session, user_id: int):
        return db.query(Order).filter(Order.user_id == user_id).all()

    def get_order(db: Session, user_id: int, id: int):
        db_order = db.query(Order).filter(Order.user_id == user_id, Order.id == id).first()
        if db_order is None:
            raise ValueError
        return db_order

    def get_order_items(db: Session, user_id: int, id: int):
        db_order = CRUDOrder.get_order(db, user_id, id)
        return db.query(OrderItem).filter(OrderItem.order_id == db_order.id).all()

    def update_order(db: Session, id: int, order: OrderUpdate):
        db_order = db.query(Order).filter(Order.id == id).first()
        if db_order is None:
            raise ValueError
        try:
            for key, value in order.model_dump(exclude_unset=True).items():
                setattr(db_order, key, value)
            db.commit()
            return db_order
        except Exception:
            db.rollback()
            raise

    def delete_order(db: Session, user_id: int, id: int):
        db_order = CRUDOrder.get_order(db, user_id, id)
        if db_order.status.value != "processing":
            raise PermissionError
        items = db.query(OrderItem).filter(OrderItem.order_id == id).all()
        try:
            for item in items:
                product = CRUDProduct.get_product(db, item.product_id)
                product.stock += item.quantity
            db.delete(db_order)
            db.commit()
            return db_order
        except Exception:
            db.rollback()
            raise
