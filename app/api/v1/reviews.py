from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError

from app.config.auth import verify_token
from app.config.database import get_db
from app.config.exceptions import exists_exception, not_found_exception, server_exception
from app.crud.review import CRUDReview
from app.schemas.review import Review, ReviewCreate, ReviewUpdate

router = APIRouter(prefix="/reviews", tags=["Review"])


@router.post("/", response_model=Review)
def create_review(review: ReviewCreate, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDReview.create_review(db, payload["sub"], review)
    except IntegrityError:
        raise not_found_exception
    except ValueError:
        raise exists_exception
    except Exception:
        raise server_exception


@router.get("/", response_model=List[Review])
def get_reviews(db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDReview.get_reviews(db, payload["sub"])
    except Exception:
        raise server_exception


@router.get("/product/{product_id}", response_model=List[Review])
def get_product_reviews(product_id: int, db=Depends(get_db)):
    try:
        return CRUDReview.get_product_reviews(db, product_id)
    except Exception:
        raise server_exception


@router.get("/{product_id}", response_model=Review)
def get_review(product_id: int, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDReview.get_review(db, payload["sub"], product_id)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception


@router.put("/{product_id}", response_model=Review)
def update_review(product_id: int, review: ReviewUpdate, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDReview.update_review(db, payload["sub"], product_id, review)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception


@router.delete("/{product_id}", response_model=Review)
def delete_review(product_id: int, db=Depends(get_db), payload=Depends(verify_token)):
    try:
        return CRUDReview.delete_review(db, payload["sub"], product_id)
    except ValueError:
        raise not_found_exception
    except Exception:
        raise server_exception
