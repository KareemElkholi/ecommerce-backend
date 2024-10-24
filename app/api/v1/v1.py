from fastapi import APIRouter

from app.api.v1 import addresses, cart_items, categories, orders, products, reviews, users

router = APIRouter(prefix="/v1")
router.include_router(addresses.router)
router.include_router(cart_items.router)
router.include_router(categories.router)
router.include_router(orders.router)
router.include_router(products.router)
router.include_router(reviews.router)
router.include_router(users.router)
