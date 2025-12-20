from sqlalchemy.orm import Session
from domain.models.fund import Fund


class FundRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_fund_by_id(self, fund_id: int):
        return self.db.query(Fund).filter(Fund.id == fund_id).first()

    def list_funds(self, skip: int = 0, limit: int = 100):
        return self.db.query(Fund).offset(skip).limit(limit).all()

    def create_fund(self, name: str, amount=None, description: str = None, project_id: int = None):
        fund = Fund(name=name, amount=amount or 0, description=description, project_id=project_id)
        self.db.add(fund)
        self.db.commit()
        self.db.refresh(fund)
        return fund

    def update_fund(self, fund: Fund, **fields):
        for k, v in fields.items():
            setattr(fund, k, v)
        self.db.add(fund)
        self.db.commit()
        self.db.refresh(fund)
        return fund

    def delete_fund(self, fund: Fund):
        self.db.delete(fund)
        self.db.commit()
        return True
