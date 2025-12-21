from sqlalchemy import Column, String, Integer, ForeignKey, Text, Enum, Numeric, Date
from sqlalchemy.orm import relationship
import enum
from .base import BaseModel

class ProjectStatus(enum.Enum):
    """Trạng thái của dự án"""
    DRAFT = "draft"                    # Nháp
    PENDING_APPROVAL = "pending"       # Chờ Lab phê duyệt
    APPROVED = "approved"              # Đã phê duyệt, chờ tuyển team
    IN_PROGRESS = "in_progress"        # Đang thực hiện
    COMPLETED = "completed"            # Hoàn thành
    CANCELLED = "cancelled"            # Đã hủy
    ON_HOLD = "on_hold"                # Tạm dừng

class ProjectCategory(enum.Enum):
    """Danh mục dự án"""
    WEB_DEVELOPMENT = "web_dev"
    MOBILE_APP = "mobile_app"
    DATA_SCIENCE = "data_science"
    AI_ML = "ai_ml"
    BLOCKCHAIN = "blockchain"
    IOT = "iot"
    GAME_DEVELOPMENT = "game_dev"
    DEVOPS = "devops"
    OTHER = "other"

class Project(BaseModel):
    """
    Model Project - Quản lý thông tin dự án
    Một dự án thuộc về một doanh nghiệp và được hướng dẫn bởi một mentor
    Liên kết với: Enterprise, Mentor, Team, Fund, Report
    """
    __tablename__ = "projects"
    
    # Khóa ngoại
    enterprise_id = Column(Integer, ForeignKey("enterprises.id"), nullable=False)
    mentor_id = Column(Integer, ForeignKey("mentors.id"))
    
    # Thông tin dự án
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(Enum(ProjectCategory))
    required_skills = Column(Text)  # JSON string: ["Python", "React"]
    expected_outcome = Column(Text)  # Kết quả mong đợi
    
    # Thời gian
    start_date = Column(Date)
    end_date = Column(Date)
    duration_months = Column(Integer)  # Thời gian dự kiến (tháng)
    
    # Tài chính
    budget = Column(Numeric(12, 2))  # Ngân sách dự án
    payment_status = Column(String(50), default="unpaid")  # unpaid, partial, paid
    
    # Quy mô team
    required_members = Column(Integer, default=3)  # Số lượng thành viên cần
    current_members = Column(Integer, default=0)   # Số lượng hiện tại
    
    # Trạng thái
    status = Column(Enum(ProjectStatus), default=ProjectStatus.DRAFT)
    
    # Tài liệu
    attachment_urls = Column(Text)  # JSON string: links tài liệu từ Cloudinary
    
    # Relationships
    enterprise = relationship("Enterprise", back_populates="projects")
    mentor = relationship("Mentor", back_populates="projects")
    teams = relationship("Team", back_populates="project", cascade="all, delete-orphan")
    funds = relationship("Fund", back_populates="project", cascade="all, delete-orphan")
    reports = relationship("Report", back_populates="project", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Project {self.title} - {self.status.value}>"