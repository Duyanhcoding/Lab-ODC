"""Mô-đun: Fund model
Lưu trữ quỹ/nguồn tài trợ liên quan tới project.
"""

from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey, DateTime
from database import Base
import datetime


class Fund(Base):
    __tablename__ = "funds"

    id = Column(Integer, primary_key=True, index=True)
    # Tên quỹ
    name = Column(String(255), nullable=False)
    # Số tiền (số thập phân)
    amount = Column(Numeric, default=0)
    # Ghi chú mô tả
    description = Column(Text)
    # Liên kết tới project (nếu có)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=True)
    # Thời điểm tạo (UTC)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

