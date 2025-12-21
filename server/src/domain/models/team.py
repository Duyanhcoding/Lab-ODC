from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Float
from sqlalchemy.orm import relationship
import enum
from src.database import Base

class TeamRole(str, enum.Enum):
    LEADER = "LEADER"
    MEMBER = "MEMBER"
    MENTOR = "MENTOR"

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    project_id = Column(Integer, nullable=True) # Link tới Project nếu có
    # Ví cho team (tổng tiền team nhận được)
    wallet_balance = Column(Float, default=0.0) 

    members = relationship("TeamMember", back_populates="team")

class TeamMember(Base):
    __tablename__ = "team_members"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    role = Column(String, default=TeamRole.MEMBER) # Lưu dạng string cho đơn giản

    team = relationship("Team", back_populates="members")
    # user = relationship("User") # Uncomment nếu muốn link ngược lại user