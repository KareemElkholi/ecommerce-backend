from fastapi import APIRouter, Depends

from app.config.auth import verify_permission, verify_token
from app.config.database import get_db
from app.config.exceptions import not_found_exception, server_exception
from app.config.hashing import get_password_hash
from app.crud.user import CRUDUser
from app.schemas.user import User, UserCreate, UserUpdate, UserRole

router = APIRouter(prefix="/users", tags=["User"])


@router.post("/", response_model=User)
def create_user(user: UserCreate, db=Depends(get_db)):
    try:
        user.password = get_password_hash(user.password)
        return CRUDUser.create_user(db, user)
    except Exception:
        raise server_exception


@router.get("/", response_model=User)
def get_user(db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDUser.get_user(db, payload["sub"])
    except Exception:
        raise server_exception


@router.put("/", response_model=User)
def update_user(user: UserUpdate, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        if user.password:
            user.password = get_password_hash(user.password)
        return CRUDUser.update_user(db, payload["sub"], user)
    except Exception:
        raise server_exception


@router.delete("/")
def delete_user(db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDUser.delete_user(db, payload["sub"])
    except Exception:
        raise server_exception


@router.put("/{id}", response_model=User, dependencies=[Depends(verify_permission)])
def update_user_role(id: int, user: UserRole, db=Depends(get_db)):
    try:
        return CRUDUser.update_user(db, id, user)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception
