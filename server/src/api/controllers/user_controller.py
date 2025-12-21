from fastapi import APIRouter
from api.routes.users import router as users_router

# Wrapper để export router dùng chung cấu trúc controllers
router = APIRouter()
router.include_router(users_router)
