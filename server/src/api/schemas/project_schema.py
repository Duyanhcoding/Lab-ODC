from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProjectCreate(BaseModel):
    title: str
    description: str
    budget: float

class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    budget: float
    status: str
    created_at: Optional[datetime] = None
    enterprise_id: int

    class Config:
        from_attributes = True

def project_to_dict(project):
    if not project:
        return None
    return {
        "id": project.id,
        "title": project.title,
        "description": project.description,
        "budget": project.budget,
        "status": project.status,
        "created_at": project.created_at.isoformat() if project.created_at else None,
        "enterprise_id": project.enterprise_id
    }