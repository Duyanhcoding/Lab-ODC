from sqlalchemy.orm import Session
from src.domain.models.user import User
from src.schemas.user_schema import UserCreate

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    # Lưu ý: password nên được hash, ở đây làm đơn giản trước
    db_user = User(
        email=user.email,
        password=user.password, # Cần hash password ở Service
        full_name=user.full_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user