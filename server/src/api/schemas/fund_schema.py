from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FundCreate(BaseModel):
    amount: float

class FundResponse(BaseModel):
    id: int
    project_id: int
    amount: float
    payment_status: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True

def fund_to_dict(fund):
    if not fund:
        return None
    return {
        "id": fund.id,
        "project_id": fund.project_id,
        "amount": fund.amount,
        "payment_status": fund.payment_status,
        "created_at": fund.created_at.isoformat() if fund.created_at else None
    }