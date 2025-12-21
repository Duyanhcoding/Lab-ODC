from sqlalchemy.orm import Session
from src.domain.models.payment import Payment, FundTransaction

def create_payment(db: Session, payment_data):
    db_payment = Payment(
        amount=payment_data.amount,
        team_id=payment_data.team_id,
        payer_id=payment_data.payer_id,
        description=payment_data.description,
        status="PENDING"
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def save_distribution(db: Session, payment_id: int, team_amt: float, mentor_amt: float, lab_amt: float):
    # Lưu lịch sử chia tiền
    transaction = FundTransaction(
        payment_id=payment_id,
        amount_team=team_amt,
        amount_mentor=mentor_amt,
        amount_lab=lab_amt
    )
    db.add(transaction)
    db.commit()