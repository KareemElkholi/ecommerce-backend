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

    def get_address(db: Session, user_id: int, id: int):
        db_address = db.query(Address).filter(Address.user_id == user_id, Address.id == id).first()
        if db_address is None:
            raise ValueError
        return db_address

    def update_address(db: Session, user_id: int, id: int, address: AddressUpdate):
        db_address = CRUDAddress.get_address(db, user_id, id)
        try:
            for key, value in address.model_dump(exclude_unset=True).items():
                setattr(db_address, key, value)
            db.commit()
            return db_address
        except Exception:
            db.rollback()
            raise

    def delete_address(db: Session, user_id: int, id: int):
        db_address = db_address = CRUDAddress.get_address(db, user_id, id)
        try:
            db.delete(db_address)
            db.commit()
            return db_address
        except Exception:
            db.rollback()
            raise
