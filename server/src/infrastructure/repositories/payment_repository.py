from sqlalchemy.orm import Session
from domain.models.payment import Payment, FundTransaction

def create_payment_record(db: Session, amount: float, team_id: int, payer_id: int):
    db_payment = Payment(
        amount=amount,
        team_id=team_id,
        payer_id=payer_id,
        status="COMPLETED"
    )
    db.add(db_payment)
    db.flush() 
    return db_payment

def save_fund_distribution(db: Session, payment_id: int, team_amt: float, mentor_amt: float, lab_amt: float):
    transaction = FundTransaction(
        payment_id=payment_id,
        amount_team=team_amt,
        amount_mentor=mentor_amt,
        amount_lab=lab_amt
    )
    db.add(transaction)
    return transaction