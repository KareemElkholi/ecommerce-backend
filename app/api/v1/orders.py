from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.exc import OperationalError

from app.config.auth import verify_permission, verify_token
from app.config.database import get_db
from app.config.exceptions import not_found_exception, server_exception, shipped_exception, stock_exception
from app.crud.order import CRUDOrder
from app.schemas.order import Order, OrderCreate, OrderItem, OrderUpdate

router = APIRouter(prefix="/orders", tags=["Order"])


@router.post("/", response_model=Order)
def create_order(order: OrderCreate, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDOrder.create_order(db, payload["sub"], order)
    except ValueError:
        raise not_found_exception
    except OperationalError:
        raise stock_exception
    except Exception:
        raise server_exception


@router.get("/", response_model=List[Order])
def get_orders(db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDOrder.get_orders(db, payload["sub"])
    except Exception:
        raise server_exception


@router.get("/{id}", response_model=Order)
def get_order(id: int, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDOrder.get_order(db, payload["sub"], id)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception


@router.get("/{id}/items", response_model=List[OrderItem])
def get_order_items(id: int, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDOrder.get_order_items(db, payload["sub"], id)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception


@router.put("/{id}", response_model=Order, dependencies=[Depends(verify_permission)])
def update_order(id: int, order: OrderUpdate, db=Depends(get_db)):
    try:
        return CRUDOrder.update_order(db, id, order)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception


@router.delete("/{id}", response_model=Order)
def delete_order(id: int, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDOrder.delete_order(db, payload["sub"], id)
    except ValueError:
        raise not_found_exception
    except PermissionError:
        raise shipped_exception
    except Exception:
        raise server_exception
