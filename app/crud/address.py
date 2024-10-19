from sqlalchemy.orm import Session

from app.models.address import Address
from app.schemas.address import AddressCreate, AddressUpdate


class CRUDAddress():
    def create_address(db: Session, user_id: int, address: AddressCreate):
        db_address = Address(
            user_id=user_id,
            building=address.building,
            street=address.street,
            district=address.district,
            city=address.city,
            governorate=address.governorate,
            country=address.country,
            phone=address.phone
        )
        try:
            db.add(db_address)
            db.commit()
            return db_address
        except Exception:
            db.rollback()
            raise

    def get_addresses(db: Session, user_id: int):
        return db.query(Address).filter(Address.user_id == user_id).all()

    def update_address(db: Session, user_id: int, address: AddressUpdate):
        db_address = db.query(Address).filter(Address.id == address.id, Address.user_id == user_id).first()
        if db_address is None:
            raise ValueError
        try:
            for key, value in address.model_dump(exclude_unset=True).items():
                setattr(db_address, key, value)
            db.commit()
            return db_address
        except Exception:
            db.rollback()
            raise

    def delete_address(db: Session, user_id: int, id: int):
        db_address = db.query(Address).filter(Address.id == id, Address.user_id == user_id).first()
        if db_address is None:
            raise ValueError
        try:
            db.delete(db_address)
            db.commit()
            return db_address
        except Exception:
            db.rollback()
            raise
