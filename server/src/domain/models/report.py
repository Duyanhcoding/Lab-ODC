"""Mô-đun: Report model
Báo cáo liên quan đến project.
"""

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from database import Base
import datetime


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    # Tiêu đề báo cáo
    title = Column(String(255), nullable=False)
    # Nội dung báo cáo
    content = Column(Text)
    # FK tới project
    project_id = Column(Integer, ForeignKey("projects.id"))
    # Thời điểm tạo
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

