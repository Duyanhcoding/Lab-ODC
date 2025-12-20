from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    status = Column(String(50), default="PENDING")
    enterprise_id = Column(Integer, ForeignKey("users.id"))
