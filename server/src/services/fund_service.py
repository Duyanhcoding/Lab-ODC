from infrastructure.repositorties.fund_repository import FundRepository


class FundService:
    def __init__(self, db_session):
        self.repo = FundRepository(db_session)

    def get(self, fund_id: int):
        return self.repo.get_fund_by_id(fund_id)

    def list(self, skip: int = 0, limit: int = 100):
        return self.repo.list_funds(skip=skip, limit=limit)

    def create(self, name: str, amount=None, description: str = None, project_id: int = None):
        return self.repo.create_fund(name=name, amount=amount, description=description, project_id=project_id)

    def update(self, fund_id: int, **fields):
        fund = self.repo.get_fund_by_id(fund_id)
        if not fund:
            return None
        return self.repo.update_fund(fund, **fields)

    def delete(self, fund_id: int):
        fund = self.repo.get_fund_by_id(fund_id)
        if not fund:
            return False
        return self.repo.delete_fund(fund)
