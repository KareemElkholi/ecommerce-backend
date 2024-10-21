from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError

from app.config.auth import verify_permission
from app.config.database import get_db
from app.config.exceptions import not_found_exception, server_exception
from app.crud.category import CRUDCategory
from app.schemas.category import Category, CategoryCreate, CategoryDelete, CategoryUpdate

router = APIRouter(prefix="/categories", tags=["Category"])


@router.post("/", response_model=Category)
def create_category(category: CategoryCreate, db=Depends(get_db), payload=Depends(verify_permission)):
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


@router.put("/", response_model=Category)
def update_category(category: CategoryUpdate, db=Depends(get_db), payload=Depends(verify_permission)):
    try:
        return CRUDCategory.update_category(db, category)
    except (ValueError, IntegrityError):
        raise not_found_exception
    except Exception:
        raise server_exception


@router.delete("/", response_model=Category)
def delete_category(category: CategoryDelete, db=Depends(get_db), payload=Depends(verify_permission)):
    try:
        return CRUDCategory.delete_category(db, category.id)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception
