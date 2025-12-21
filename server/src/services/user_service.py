from sqlalchemy.orm import Session
from src.infrastructure.repositories import user_repository
from src.schemas.user_schema import UserCreate

def register_new_user(db: Session, user_data: UserCreate):
    # 1. Kiểm tra user tồn tại chưa
    existing_user = user_repository.get_user_by_email(db, user_data.email)
    if existing_user:
        raise Exception("Email already registered")
    
    # 2. Gọi repo để tạo user (sau này thêm logic hash pass ở đây)
    return user_repository.create_user(db, user_data)