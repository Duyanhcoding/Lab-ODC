from sqlalchemy.orm import Session
from domain.models.project import Project


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_project_by_id(self, project_id: int):
        return self.db.query(Project).filter(Project.id == project_id).first()

    def list_projects(self, skip: int = 0, limit: int = 100):
        return self.db.query(Project).offset(skip).limit(limit).all()

    def create_project(self, title: str, description: str = None, enterprise_id: int = None):
        project = Project(title=title, description=description, enterprise_id=enterprise_id)
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def update_project(self, project: Project, **fields):
        for key, value in fields.items():
            setattr(project, key, value)
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def delete_project(self, project: Project):
        self.db.delete(project)
        self.db.commit()
        return True