from infrastructure.repositorties.report_repository import ReportRepository


class ReportService:
    def __init__(self, db_session):
        self.repo = ReportRepository(db_session)

    def get(self, report_id: int):
        return self.repo.get_report_by_id(report_id)

    def list(self, skip: int = 0, limit: int = 100):
        return self.repo.list_reports(skip=skip, limit=limit)

    def create(self, title: str, content: str = None, project_id: int = None):
        return self.repo.create_report(title=title, content=content, project_id=project_id)

    def update(self, report_id: int, **fields):
        report = self.repo.get_report_by_id(report_id)
        if not report:
            return None
        return self.repo.update_report(report, **fields)

    def delete(self, report_id: int):
        report = self.repo.get_report_by_id(report_id)
        if not report:
            return False
        return self.repo.delete_report(report)
