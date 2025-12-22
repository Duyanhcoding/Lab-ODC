from infrastructure.repositorties.report_repository import ReportRepository
from domain.models.report import Report
from datetime import datetime
from typing import Optional, List

class ReportService:
    def __init__(self, db_session):
        self.repo = ReportRepository(db_session)

    def get(self, report_id: int) -> Optional[Report]:
        return self.repo.get_report_by_id(report_id)

    def list(self, skip: int = 0, limit: int = 100) -> List[Report]:
        return self.repo.list_reports(skip=skip, limit=limit)

    def create(self, project_id: int, mentor_id: int, content: str, submitted_at: Optional[datetime] = None) -> Report:
        if submitted_at is None:
            submitted_at = datetime.utcnow()
        return self.repo.create_report(
            project_id=project_id,
            mentor_id=mentor_id,
            content=content,
            submitted_at=submitted_at
        )

    def update(self, report_id: int, **fields) -> Optional[Report]:
        report = self.repo.get_report_by_id(report_id)
        if not report:
            return None
        return self.repo.update_report(report, **fields)

    def delete(self, report_id: int) -> bool:
        report = self.repo.get_report_by_id(report_id)
        if not report:
            return False
        return self.repo.delete_report(report)

    # Method tiện ích cho controller: lấy báo cáo theo project
    def get_by_project(self, project_id: int) -> List[Report]:
        return self.repo.get_reports_by_project(project_id)