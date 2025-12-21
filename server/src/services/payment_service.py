from sqlalchemy.orm import Session
from src.infrastructure.repositories import payment_repository, team_repository
from src.schemas.payment_schema import PaymentCreate

def process_payment(db: Session, data: PaymentCreate):
    # 1. Tạo bản ghi thanh toán (Payment)
    payment = payment_repository.create_payment(db, data)
    
    # 2. Logic chia tiền (70/20/10 Rule)
    # LabOdc rule: Team 70%, Mentor 20%, Lab 10%
    total = data.amount
    
    team_share = total * 0.70
    mentor_share = total * 0.20
    lab_share = total * 0.10
    
    # 3. Cập nhật ví (Cộng tiền vào ví Team)
    team = team_repository.get_team(db, data.team_id)
    if team:
        team.wallet_balance += team_share
        db.add(team) # Đánh dấu cập nhật
    
    # (Lưu ý: Mentor share và Lab share sẽ cộng vào ví user tương ứng, 
    # ở đây tạm thời mình chỉ lưu log giao dịch để đơn giản hóa)
    
    # 4. Lưu log phân chia
    payment_repository.save_distribution(
        db, payment.id, team_share, mentor_share, lab_share
    )
    
    # 5. Cập nhật trạng thái Payment thành công
    payment.status = "COMPLETED"
    db.commit()
    db.refresh(payment)
    
    return payment
