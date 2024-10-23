from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError

from app.config.auth import verify_permission
from app.config.database import get_db
from app.config.exceptions import not_found_exception, server_exception
from app.crud.category import CRUDCategory
from app.schemas.category import Category, CategoryCreate, CategoryUpdate

router = APIRouter(prefix="/categories", tags=["Category"])


@router.post("/", response_model=Category, dependencies=[Depends(verify_permission)])
def create_category(category: CategoryCreate, db=Depends(get_db)):
    try:
        return CRUDCategory.create_category(db, category)
    except IntegrityError:
        raise not_found_exception
    except Exception:
        raise server_exception


@router.get("/", response_model=List[Category])
def get_categories(parent_id: Optional[int] = None, db=Depends(get_db)):
    try:
        return CRUDCategory.get_categories(db, parent_id)
    except Exception:
        raise server_exception


@router.get("/{id}", response_model=Category)
def get_category(id: int, db=Depends(get_db)):
    try:
        return CRUDCategory.get_category(db, id)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception


@router.put("/{id}", response_model=Category, dependencies=[Depends(verify_permission)])
def update_category(id: int, category: CategoryUpdate, db=Depends(get_db)):
    try:
        return CRUDCategory.update_category(db, id, category)
    except (ValueError, IntegrityError):
        raise not_found_exception
    except Exception:
        raise server_exception


@router.delete("/{id}", response_model=Category, dependencies=[Depends(verify_permission)])
def delete_category(id: int, db=Depends(get_db)):
    try:
        return CRUDCategory.delete_category(db, id)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception
