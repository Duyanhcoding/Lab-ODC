from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from .base import BaseModel

class Mentor(BaseModel):
    """
    Model Mentor - Quản lý thông tin người hướng dẫn
    Mentor có thể hướng dẫn nhiều dự án
    Liên kết với: User, Project
    """
    __tablename__ = "mentors"
    
    # Khóa ngoại tới User
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    
    # Thông tin chuyên môn
    expertise = Column(Text)  # Lĩnh vực chuyên môn (JSON string hoặc text)
    years_of_experience = Column(Integer)  # Số năm kinh nghiệm
    current_position = Column(String(255))  # Vị trí hiện tại
    company = Column(String(255))  # Công ty hiện tại
    bio = Column(Text)  # Tiểu sử
    linkedin_url = Column(String(500))
    github_url = Column(String(500))
    
    # Thống kê
    total_projects = Column(Integer, default=0)  # Tổng số dự án đã hướng dẫn
    rating_average = Column(Integer, default=0)  # Đánh giá trung bình (0-5)
    
    # Relationships
    user = relationship("User", back_populates="mentor")
    projects = relationship("Project", back_populates="mentor")
    
    def __repr__(self):
        return f"<Mentor {self.user.full_name if self.user else 'Unknown'}>"