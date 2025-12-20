from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey, DateTime
from database import Base
import datetime


class Fund(Base):
    __tablename__ = "funds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    amount = Column(Numeric, default=0)
    description = Column(Text)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
