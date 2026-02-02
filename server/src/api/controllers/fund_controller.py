from fastapi import APIRouter, HTTPException, status
from dependency_container import get_db_session
from services.fund_service import FundService
from api.schemas.fund_schema import fund_to_dict

router = APIRouter(prefix="/funds", tags=["Funds"])

# Thanh toán
@router.post("/projects/{project_id}/payments", status_code=status.HTTP_201_CREATED)
def make_payment(project_id: int, amount: float):
    with get_db_session() as db:
        svc = FundService(db)
        payment = svc.make_payment(project_id=project_id, amount=amount)
        return fund_to_dict(payment)

# Phân bổ 70/20/10
@router.put("/projects/{project_id}/allocate")
def allocate_funds(project_id: int):
    with get_db_session() as db:
        svc = FundService(db)
        allocation = svc.allocate_funds(project_id=project_id)
        return {"message": "Phân bổ thành công", "detail": allocation}