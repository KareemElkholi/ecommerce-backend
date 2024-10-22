from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class CRUDProduct():
    def create_product(db: Session, product: ProductCreate):
        db_product = Product(
            category_id=product.category_id,
            name=product.name,
            description=product.description,
            stock=product.stock,
            price=product.price,
            discount=product.discount
        )
        try:
            db.add(db_product)
            db.commit()
            return db_product
        except Exception:
            db.rollback()
            raise

    def get_products(db: Session, category_id: int):
        if category_id is None:
            return db.query(Product).all()
        return db.query(Product).filter(Product.category_id == category_id).all()

    def update_product(db: Session, product: ProductUpdate):
        db_product = db.query(Product).filter(Product.id == product.id).first()
        if db_product is None:
            raise ValueError
        try:
            for key, value in product.model_dump(exclude_unset=True).items():
                setattr(db_product, key, value)
            db.commit()
            return db_product
        except Exception:
            db.rollback()
            raise

    def delete_product(db: Session, id: int):
        db_product = db.query(Product).filter(Product.id == id).first()
        if db_product is None:
            raise ValueError
        try:
            db.delete(db_product)
            db.commit()
            return db_product
        except Exception:
            db.rollback()
            raise
