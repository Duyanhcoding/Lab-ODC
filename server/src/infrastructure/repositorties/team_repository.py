from sqlalchemy.orm import Session
from domain.models.team import Team, team_members, project_teams
from domain.models.user import User
from domain.models.project import Project
from sqlalchemy import select, insert, delete


class TeamRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_team_by_id(self, team_id: int):
        return self.db.query(Team).filter(Team.id == team_id).first()

    def list_teams(self, skip: int = 0, limit: int = 100):
        return self.db.query(Team).offset(skip).limit(limit).all()

    def create_team(self, name: str, description: str = None, lead_id: int = None):
        team = Team(name=name, description=description, lead_id=lead_id)
        self.db.add(team)
        self.db.commit()
        self.db.refresh(team)
        return team

    def update_team(self, team: Team, **fields):
        for key, value in fields.items():
            setattr(team, key, value)
        self.db.add(team)
        self.db.commit()
        self.db.refresh(team)
        return team

    def delete_team(self, team: Team):
        self.db.delete(team)
        self.db.commit()
        return True

    # Members
    def add_member(self, team_id: int, user_id: int, role: str = "MEMBER"):
        stmt = insert(team_members).values(team_id=team_id, user_id=user_id, role=role)
        self.db.execute(stmt)
        self.db.commit()
        return True

    def remove_member(self, team_id: int, user_id: int):
        stmt = delete(team_members).where(
            (team_members.c.team_id == team_id) & (team_members.c.user_id == user_id)
        )
        self.db.execute(stmt)
        self.db.commit()
        return True

    def list_members(self, team_id: int):
        team = self.get_team_by_id(team_id)
        return team.members if team else []

    # Project assignments
    def assign_project(self, team_id: int, project_id: int, role: str = "SUPPORT"):
        stmt = insert(project_teams).values(project_id=project_id, team_id=team_id, role=role)
        self.db.execute(stmt)
        self.db.commit()
        return True

    def unassign_project(self, team_id: int, project_id: int):
        stmt = delete(project_teams).where(
            (project_teams.c.team_id == team_id) & (project_teams.c.project_id == project_id)
        )
        self.db.execute(stmt)
        self.db.commit()
        return True

    def list_projects(self, team_id: int):
        team = self.get_team_by_id(team_id)
        return team.projects if team else []
