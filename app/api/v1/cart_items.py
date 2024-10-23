from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError

from app.config.auth import verify_token
from app.config.database import get_db
from app.config.exceptions import exists_exception, not_found_exception, server_exception
from app.crud.cart_item import CRUDCartItem
from app.schemas.cart_item import CartItem, CartItemCreate, CartItemUpdate

router = APIRouter(prefix="/cart_items", tags=["CartItem"])


@router.post("/", response_model=CartItem)
def create_cart_item(cart_item: CartItemCreate, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDCartItem.create_cart_item(db, payload["sub"], cart_item)
    except IntegrityError:
        raise not_found_exception
    except ValueError:
        raise exists_exception
    except Exception:
        raise server_exception


@router.get("/", response_model=List[CartItem])
def get_cart_items(db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDCartItem.get_cart_items(db, payload["sub"])
    except Exception:
        raise server_exception


@router.get("/{product_id}", response_model=CartItem)
def get_cart_item(product_id: int, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDCartItem.get_cart_item(db, payload["sub"], product_id)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception


@router.put("/{product_id}", response_model=CartItem)
def update_cart_item(product_id: int, cart_item: CartItemUpdate, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDCartItem.update_cart_item(db, payload["sub"], product_id, cart_item)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception


@router.delete("/", response_model=CartItem)
def delete_cart_item(product_id: int, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDCartItem.delete_cart_item(db, payload["sub"], product_id)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception
