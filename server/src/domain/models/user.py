"""Mô-đun: User model (SQLAlchemy)
Giải thích: Đây là bảng `users` lưu trữ thông tin user cơ bản.
Không thay đổi cấu hình database ở file `database.py` hay `config.py`.
"""

from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    # Tên bảng trong DB
    __tablename__ = "users"

    # Khóa chính
    id = Column(Integer, primary_key=True, index=True)
    # Tên người dùng
    name = Column(String(255), nullable=False)
    # Email (unique)
    email = Column(String(255), unique=True, index=True, nullable=False)
    # Vai trò (ví dụ: USER, ADMIN)
    role = Column(String(50), default="USER")

