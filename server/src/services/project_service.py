from infrastructure.repositorties.project_repository import ProjectRepository


class ProjectService:
    def __init__(self, db_session):
        self.repo = ProjectRepository(db_session)

    def get(self, project_id: int):
        return self.repo.get_project_by_id(project_id)

    def list(self, skip: int = 0, limit: int = 100):
        return self.repo.list_projects(skip=skip, limit=limit)

    def create(self, title: str, description: str = None, enterprise_id: int = None):
        return self.repo.create_project(title=title, description=description, enterprise_id=enterprise_id)

    def update(self, project_id: int, db_session, **fields):
        project = self.repo.get_project_by_id(project_id)
        if not project:
            return None
        return self.repo.update_project(project, **fields)

    def delete(self, project_id: int):
        project = self.repo.get_project_by_id(project_id)
        if not project:
            return False
        return self.repo.delete_project(project)
