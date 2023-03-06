from fastapi import APIRouter
from views.auth import router as auth_router
from views.author import router as author_router
from views.book import router as book_router
from views.order import router as order_router
from views.user import router as user_router

router =  APIRouter()

router.include_router(auth_router)
router.include_router(user_router)
router.include_router(book_router)
router.include_router(order_router)
router.include_router(author_router)