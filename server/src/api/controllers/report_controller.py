from fastapi import APIRouter, HTTPException, status
from dependency_container import get_db_session
from services.report_service import ReportService
from api.schemas.report_schema import report_to_dict
from datetime import datetime

router = APIRouter(prefix="/reports", tags=["Reports"])

# Submit report
@router.post("/projects/{project_id}/reports", status_code=status.HTTP_201_CREATED)
def submit_report(project_id: int, content: str):
    with get_db_session() as db:
        svc = ReportService(db)
        report = svc.create(project_id=project_id, mentor_id=1, content=content, submitted_at=datetime.utcnow())
        return report_to_dict(report)

# View reports
@router.get("/projects/{project_id}/reports")
def get_reports(project_id: int):
    with get_db_session() as db:
        svc = ReportService(db)
        reports = svc.get_by_project(project_id)
        return [report_to_dict(r) for r in reports]