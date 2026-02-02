from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReportCreate(BaseModel):
    content: str

class ReportResponse(BaseModel):
    id: int
    project_id: int
    mentor_id: int
    content: str
    submitted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

def report_to_dict(report):
    if not report:
        return None
    return {
        "id": report.id,
        "project_id": report.project_id,
        "mentor_id": report.mentor_id,
        "content": report.content,
        "submitted_at": report.submitted_at.isoformat() if report.submitted_at else None
    }