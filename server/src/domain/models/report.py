from sqlalchemy import Column, String, Integer, ForeignKey, Text, Enum, Date
from sqlalchemy.orm import relationship
import enum
from .base import BaseModel

class ReportType(enum.Enum):
    """Loại báo cáo"""
    MONTHLY = "monthly"        # Báo cáo hàng tháng
    PHASE = "phase"            # Báo cáo theo giai đoạn
    FINAL = "final"            # Báo cáo kết thúc dự án
    EMERGENCY = "emergency"    # Báo cáo khẩn cấp/sự cố

class ReportStatus(enum.Enum):
    """Trạng thái báo cáo"""
    DRAFT = "draft"            # Nháp
    SUBMITTED = "submitted"    # Đã nộp
    APPROVED = "approved"      # Đã duyệt
    REJECTED = "rejected"      # Bị từ chối
    REVISION = "revision"      # Cần chỉnh sửa

class Report(BaseModel):
    """
    Model Report - Quản lý báo cáo dự án
    Mentor nộp báo cáo định kỳ, Lab admin duyệt
    Liên kết với: Project
    """
    __tablename__ = "reports"
    
    # Khóa ngoại
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    submitted_by = Column(Integer, ForeignKey("users.id"))  # Người nộp (Mentor)
    reviewed_by = Column(Integer, ForeignKey("users.id"))   # Người duyệt (Lab Admin)
    
    # Thông tin báo cáo
    report_type = Column(Enum(ReportType), nullable=False)
    title = Column(String(255), nullable=False)
    period_start = Column(Date)  # Ngày bắt đầu kỳ báo cáo
    period_end = Column(Date)    # Ngày kết thúc kỳ báo cáo
    
    # Nội dung
    summary = Column(Text)  # Tóm tắt
    progress_percentage = Column(Integer, default=0)  # Tiến độ (0-100%)
    achievements = Column(Text)  # Công việc đã hoàn thành
    challenges = Column(Text)  # Khó khăn gặp phải
    next_steps = Column(Text)  # Kế hoạch tiếp theo
    
    # Đánh giá team
    team_performance = Column(Text)  # JSON string: đánh giá từng thành viên
    
    # Tài liệu đính kèm
    attachment_urls = Column(Text)  # JSON string: links file từ Cloudinary
    excel_template_url = Column(String(500))  # Link file Excel breakdown tasks
    
    # Trạng thái
    status = Column(Enum(ReportStatus), default=ReportStatus.DRAFT)
    
    # Feedback
    review_comment = Column(Text)  # Nhận xét từ Lab Admin
    review_date = Column(Date)
    
    # Relationships
    project = relationship("Project", back_populates="reports")
    
    def __repr__(self):
        return f"<Report {self.title} - {self.report_type.value} - {self.status.value}>"