from sqlalchemy.orm import Session
from domain.models.report import Report
from typing import List, Optional

class ReportRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_report_by_id(self, report_id: int) -> Optional[Report]:
        return self.db.query(Report).filter(Report.id == report_id).first()

    def list_reports(self, skip: int = 0, limit: int = 100) -> List[Report]:
        return self.db.query(Report).offset(skip).limit(limit).all()

    def create_report(self, project_id: int, mentor_id: int, content: str, submitted_at):
        new_report = Report(
            project_id=project_id,
            mentor_id=mentor_id,
            content=content,
            submitted_at=submitted_at
        )
        self.db.add(new_report)
        self.db.commit()
        self.db.refresh(new_report)
        return new_report

    def update_report(self, report: Report, **fields) -> Report:
        for key, value in fields.items():
            if hasattr(report, key):
                setattr(report, key, value)
        self.db.commit()
        self.db.refresh(report)
        return report

    def delete_report(self, report: Report) -> bool:
        self.db.delete(report)
        self.db.commit()
        return True

    def get_reports_by_project(self, project_id: int) -> List[Report]:
        return self.db.query(Report).filter(Report.project_id == project_id).order_by(Report.submitted_at.desc()).all()