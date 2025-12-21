from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from api.schemas.user_schema import UserCreate, UserResponse
from services import user_service

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return user_service.register_new_user(db, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))