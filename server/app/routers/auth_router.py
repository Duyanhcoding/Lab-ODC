from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.auth_schemas import UserRegister, UserLogin, Token
from app.services.auth import AuthService
from fastapi.security import OAuth2PasswordRequestForm
from app.core.deps import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=Token)
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    try:
        user = AuthService.register_user(db, user_data)
        token = AuthService.create_token(user)

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = AuthService.authenticate_by_email(
        db,
        form_data.username,   # Swagger dùng "username"
        form_data.password
    )

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = AuthService.create_token(user)
    return {
        "access_token": token,
        "token_type": "bearer"
    }
# auth_router.py

@router.post("/forgot-password")
async def forgot_password(payload: dict, db: Session = Depends(get_db)):
    email = payload.get("email")
    user = db.query(user).filter(user.email == email).first()
    
    if not user:
        return {"message": "link be sent"}

    # Tạo token tạm thời (15 phút)
    reset_token = AuthService.create_token(user) 
    
    print(f"DEBUG: Link: http://localhost:3000/reset-password?token={reset_token}")
    return {"message": "Email reset be sent"}

@router.post("/reset-password")
def reset_password(payload: dict, db: Session = Depends(get_db)):
    token = payload.get("token")
    new_password = payload.get("password")
    return {"message": "password has been updated"}