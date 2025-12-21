from sqlalchemy.orm import Session
from domain.models.report import Report


class ReportRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_report_by_id(self, report_id: int):
        return self.db.query(Report).filter(Report.id == report_id).first()

    def list_reports(self, skip: int = 0, limit: int = 100):
        return self.db.query(Report).offset(skip).limit(limit).all()

    def create_report(self, title: str, content: str = None, project_id: int = None):
        report = Report(title=title, content=content, project_id=project_id)
        self.db.add(report)
        self.db.commit()
        self.db.refresh(report)
        return report

    def update_report(self, report: Report, **fields):
        for k, v in fields.items():
            setattr(report, k, v)
        self.db.add(report)
        self.db.commit()
        self.db.refresh(report)
        return report

    def delete_report(self, report: Report):
        self.db.delete(report)
        self.db.commit()
        return True