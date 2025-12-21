from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.payment_schema import PaymentCreate, PaymentResponse
from src.services import payment_service

router = APIRouter()

@router.post("/payments/process", response_model=PaymentResponse)
def process_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    """API để Doanh nghiệp thanh toán, hệ thống tự chia 70/20/10"""
    return payment_service.process_payment(db, payment)