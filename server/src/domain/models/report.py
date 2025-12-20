from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from database import Base
import datetime


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text)
    project_id = Column(Integer, ForeignKey("projects.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
