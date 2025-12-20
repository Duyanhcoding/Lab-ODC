from infrastructure.repositorties.team_repository import TeamRepository


class TeamService:
    def __init__(self, db_session):
        self.repo = TeamRepository(db_session)

    def get(self, team_id: int):
        return self.repo.get_team_by_id(team_id)

    def list(self, skip: int = 0, limit: int = 100):
        return self.repo.list_teams(skip=skip, limit=limit)

    def create(self, name: str, description: str = None, lead_id: int = None):
        return self.repo.create_team(name=name, description=description, lead_id=lead_id)

    def update(self, team_id: int, db_session, **fields):
        team = self.repo.get_team_by_id(team_id)
        if not team:
            return None
        return self.repo.update_team(team, **fields)

    def delete(self, team_id: int):
        team = self.repo.get_team_by_id(team_id)
        if not team:
            return False
        return self.repo.delete_team(team)

    # Members
    def add_member(self, team_id: int, user_id: int, role: str = "MEMBER"):
        return self.repo.add_member(team_id=team_id, user_id=user_id, role=role)

    def remove_member(self, team_id: int, user_id: int):
        return self.repo.remove_member(team_id=team_id, user_id=user_id)

    def list_members(self, team_id: int):
        return self.repo.list_members(team_id=team_id)

    # Projects
    def assign_project(self, team_id: int, project_id: int, role: str = "SUPPORT"):
        return self.repo.assign_project(team_id=team_id, project_id=project_id, role=role)

    def unassign_project(self, team_id: int, project_id: int):
        return self.repo.unassign_project(team_id=team_id, project_id=project_id)

    def list_projects(self, team_id: int):
        return self.repo.list_projects(team_id=team_id)
