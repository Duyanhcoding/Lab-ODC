from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime


team_members = Table(
    "team_members",
    Base.metadata,
    Column("team_id", Integer, ForeignKey("teams.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("role", String(50), default="MEMBER"),
    Column("joined_at", DateTime, default=datetime.datetime.utcnow),
)

project_teams = Table(
    "project_teams",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
    Column("team_id", Integer, ForeignKey("teams.id"), primary_key=True),
    Column("role", String(50), default="SUPPORT"),
    Column("assigned_at", DateTime, default=datetime.datetime.utcnow),
)


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    lead_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    members = relationship("User", secondary=team_members, backref="teams")
    projects = relationship("Project", secondary=project_teams, backref="teams")
