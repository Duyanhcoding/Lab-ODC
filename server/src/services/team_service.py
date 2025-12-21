from sqlalchemy.orm import Session
from infrastructure.repositories import team_repository
from api.schemas.team_schema import TeamCreate, TeamMemberCreate

def create_new_team(db: Session, team: TeamCreate):
    return team_repository.create_team(db, team)

def add_member_to_team(db: Session, team_id: int, member: TeamMemberCreate):
    # Có thể thêm logic kiểm tra: user có tồn tại không? user đã vào team chưa?
    return team_repository.add_member(db, team_id, member)