from sqlalchemy import Column, String, Integer, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
import enum
from .base import BaseModel

class EnterpriseStatus(enum.Enum):
    """Trạng thái của doanh nghiệp"""
    PENDING = "pending"        # Chờ xét duyệt
    APPROVED = "approved"      # Đã được phê duyệt
    REJECTED = "rejected"      # Bị từ chối
    SUSPENDED = "suspended"    # Bị tạm ngưng

class Enterprise(BaseModel):
    """
    Model Enterprise - Quản lý thông tin doanh nghiệp
    Một doanh nghiệp có thể đăng nhiều dự án
    Liên kết với: User, Project
    """
    __tablename__ = "enterprises"
    
    # Khóa ngoại tới User
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    
    # Thông tin doanh nghiệp
    company_name = Column(String(255), nullable=False)
    tax_code = Column(String(50), unique=True)  # Mã số thuế
    address = Column(Text)
    website = Column(String(255))
    industry = Column(String(100))  # Ngành nghề
    company_size = Column(String(50))  # Quy mô: Startup, SME, Enterprise
    description = Column(Text)
    
    # Trạng thái
    status = Column(Enum(EnterpriseStatus), default=EnterpriseStatus.PENDING)
    
    # Relationships
    user = relationship("User", back_populates="enterprise")
    projects = relationship("Project", back_populates="enterprise", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Enterprise {self.company_name} - {self.status.value}>"