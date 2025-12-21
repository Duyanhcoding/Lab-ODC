from pydantic import BaseModel, EmailStr

# Schema để tạo user mới
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str

# Schema để trả về client (không trả về password)
class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    is_active: bool

    class Config:
        from_attributes = True # Cho phép đọc dữ liệu từ ORM model