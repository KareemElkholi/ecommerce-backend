from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError

from app.config.auth import verify_permission
from app.config.database import get_db
from app.config.exceptions import not_found_exception, server_exception
from app.crud.product import CRUDProduct
from app.schemas.product import Product, ProductCreate, ProductDelete, ProductUpdate

router = APIRouter(prefix="/products", tags=["Product"])


@router.post("/", response_model=Product)
def create_product(product: ProductCreate, db=Depends(get_db), payload=Depends(verify_permission)):
    try:
        return CRUDProduct.create_product(db, product)
    except IntegrityError:
        raise not_found_exception
    except Exception:
        raise server_exception


@router.get("/", response_model=List[Product])
def get_products(category_id: Optional[int] = None, db=Depends(get_db)):
    try:
        return CRUDProduct.get_products(db, category_id)
    except Exception:
        raise server_exception


@router.put("/", response_model=Product)
def update_product(product: ProductUpdate, db=Depends(get_db), payload=Depends(verify_permission)):
    try:
        return CRUDProduct.update_product(db, product)
    except (ValueError, IntegrityError):
        raise not_found_exception
    except Exception:
        raise server_exception


@router.delete("/", response_model=Product)
def delete_product(product: ProductDelete, db=Depends(get_db), payload=Depends(verify_permission)):
    try:
        return CRUDProduct.delete_product(db, product.id)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception
