from fastapi import APIRouter, HTTPException, status
from dependency_container import get_db_session  
from services.project_service import ProjectService
from api.schemas.project_schema import project_to_dict  # giả sử có hàm convert

router = APIRouter(prefix="/projects", tags=["Projects"])

# Submit project
@router.post("/", status_code=status.HTTP_201_CREATED)
def submit_project(title: str, description: str, budget: float):
    with get_db_session() as db:
        svc = ProjectService(db)
        project = svc.create(title=title, description=description, budget=budget, enterprise_id=1)  # hardcode tạm
        return project_to_dict(project)

# View approved projects
@router.get("/")
def view_approved_projects():
    with get_db_session() as db:
        svc = ProjectService(db)
        projects = svc.get_approved_projects()
        return [project_to_dict(p) for p in projects]

# Get detail
@router.get("/{project_id}")
def get_project_detail(project_id: int):
    with get_db_session() as db:
        svc = ProjectService(db)
        project = svc.get(project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Dự án không tồn tại")
        return project_to_dict(project)