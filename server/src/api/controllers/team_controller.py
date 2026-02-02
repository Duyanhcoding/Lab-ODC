from fastapi import APIRouter, HTTPException, status
from dependency_container import get_db_session
from services.team_service import TeamService
from api.schemas.team_schema import team_to_dict

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_team(name: str, description: str = None, lead_id: int = None):
    with get_db_session() as db:
        svc = TeamService(db)
        team = svc.create(name=name, description=description, lead_id=lead_id)
        return team_to_dict(team)

@router.get("/")
def list_teams(skip: int = 0, limit: int = 100):
    with get_db_session() as db:
        svc = TeamService(db)
        teams = svc.list(skip=skip, limit=limit)
        return [team_to_dict(t) for t in teams]

@router.get("/{team_id}")
def get_team(team_id: int):
    with get_db_session() as db:
        svc = TeamService(db)
        team = svc.get(team_id)
        if not team:
            raise HTTPException(status_code=404, detail="Team không tồn tại")
        return team_to_dict(team)

@router.post("/{team_id}/members", status_code=status.HTTP_201_CREATED)
def add_member(team_id: int, user_id: int, role: str = "MEMBER"):
    with get_db_session() as db:
        svc = TeamService(db)
        try:
            svc.add_member(team_id=team_id, user_id=user_id, role=role)
            return {"message": "Tham gia dự án thành công"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

@router.post("/{team_id}/projects/{project_id}")
def assign_project(team_id: int, project_id: int, role: str = "SUPPORT"):
    with get_db_session() as db:
        svc = TeamService(db)
        svc.assign_project(team_id=team_id, project_id=project_id, role=role)
        return {"message": "Giao dự án thành công"}