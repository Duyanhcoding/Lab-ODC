"""Mô-đun: Project model
Lưu trữ thông tin dự án (project).
"""

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base


class Project(Base):
    # Bảng projects
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    # Tiêu đề dự án
    title = Column(String(255), nullable=False)
    # Mô tả chi tiết (text)
    description = Column(Text)
    # Trạng thái (PENDING, ACTIVE, DONE...)
    status = Column(String(50), default="PENDING")
    # Nếu project thuộc về một enterprise (user), để FK
    enterprise_id = Column(Integer, ForeignKey("users.id"))

