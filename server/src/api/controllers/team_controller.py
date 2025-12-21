from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.team_schema import TeamCreate, TeamResponse, TeamMemberCreate
from src.services import team_service

router = APIRouter()

@router.post("/teams/", response_model=TeamResponse)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    return team_service.create_new_team(db, team)

@router.post("/teams/{team_id}/members")
def add_member(team_id: int, member: TeamMemberCreate, db: Session = Depends(get_db)):
    return team_service.add_member_to_team(db, team_id, member)