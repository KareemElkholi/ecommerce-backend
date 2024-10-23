from typing import List

from fastapi import APIRouter, Depends

from app.config.auth import verify_token
from app.config.database import get_db
from app.config.exceptions import not_found_exception, server_exception
from app.crud.address import CRUDAddress
from app.schemas.address import Address, AddressCreate, AddressUpdate

router = APIRouter(prefix="/addresses", tags=["Address"])


@router.post("/", response_model=Address)
def create_address(address: AddressCreate, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDAddress.create_address(db, payload["sub"], address)
    except Exception:
        raise server_exception


@router.get("/", response_model=List[Address])
def get_addresses(db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDAddress.get_addresses(db, payload["sub"])
    except Exception:
        raise server_exception


@router.get("/{id}", response_model=Address)
def get_address(id: int, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDAddress.get_address(db, payload["sub"], id)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception


@router.put("/{id}", response_model=Address)
def update_address(id: int, address: AddressUpdate, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDAddress.update_address(db, payload["sub"], id, address)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception


@router.delete("/{id}", response_model=Address)
def delete_address(id: int, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDAddress.delete_address(db, payload["sub"], id)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception
