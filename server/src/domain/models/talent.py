from sqlalchemy import Column, String, Integer, ForeignKey, Text, Date
from sqlalchemy.orm import relationship
from .base import BaseModel

class Talent(BaseModel):
    """
    Model Talent - Quản lý thông tin sinh viên/ứng viên
    Một sinh viên có thể tham gia nhiều dự án thông qua Team
    Liên kết với: User, Team
    """
    __tablename__ = "talents"
    
    # Khóa ngoại tới User
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    
    # Thông tin sinh viên
    student_id = Column(String(50), unique=True)  # Mã sinh viên UTH
    major = Column(String(100))  # Ngành học
    year_of_study = Column(Integer)  # Năm học (1, 2, 3, 4)
    expected_graduation = Column(Date)  # Ngày dự kiến tốt nghiệp
    
    # Kỹ năng và kinh nghiệm
    skills = Column(Text)  # JSON string: ["Python", "React", "PostgreSQL"]
    certifications = Column(Text)  # JSON string: chứng chỉ
    portfolio_url = Column(String(500))  # Link portfolio
    github_url = Column(String(500))
    linkedin_url = Column(String(500))
    cv_url = Column(String(500))  # Link CV từ Cloudinary
    bio = Column(Text)  # Giới thiệu bản thân
    
    # Thống kê
    total_projects_joined = Column(Integer, default=0)  # Tổng số dự án đã tham gia
    rating_average = Column(Integer, default=0)  # Đánh giá trung bình
    
    # Relationships
    user = relationship("User", back_populates="talent")
    teams = relationship("Team", back_populates="talent")
    
    def __repr__(self):
        return f"<Talent {self.student_id} - {self.user.full_name if self.user else 'Unknown'}>"