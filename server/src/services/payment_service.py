from sqlalchemy.orm import Session
from infrastructure.repositories import payment_repository, team_repository

def process_payment_logic(db: Session, amount: float, team_id: int):
    # Quy tắc 70/20/10 của LabOdc
    team_share = amount * 0.7
    mentor_share = amount * 0.2
    lab_share = amount * 0.1
    
    # Cập nhật số dư cho Team
    team = team_repository.get_team(db, team_id)
    if team:
        team.wallet_balance += team_share
        db.commit()
    
    return {
        "team_amount": team_share,
        "mentor_amount": mentor_share,
        "lab_amount": lab_share
    }