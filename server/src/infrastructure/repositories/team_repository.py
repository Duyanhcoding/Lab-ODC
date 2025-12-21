from sqlalchemy.orm import Session
from domain.models.team import Team, TeamMember
from api.schemas.team_schema import TeamCreate, TeamMemberCreate

def create_team(db: Session, team: TeamCreate):
    db_team = Team(name=team.name, project_id=team.project_id)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def add_member(db: Session, team_id: int, member: TeamMemberCreate):
    db_member = TeamMember(
        team_id=team_id,
        user_id=member.user_id,
        role=member.role
    )
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def get_team(db: Session, team_id: int):
    return db.query(Team).filter(Team.id == team_id).first()