from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    description = Column(String)
    status = Column(String, default="PENDING") # PENDING, COMPLETED
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Ai trả tiền (Enterprise)
    payer_id = Column(Integer, ForeignKey("users.id"))
    
    # Trả cho Team nào
    team_id = Column(Integer, ForeignKey("teams.id"))

class FundTransaction(Base):
    """Bảng này lưu lịch sử chia tiền 70/20/10 để minh bạch"""
    __tablename__ = "fund_transactions"

    id = Column(Integer, primary_key=True, index=True)
    payment_id = Column(Integer, ForeignKey("payments.id"))
    
    amount_team = Column(Float)   # 70%
    amount_mentor = Column(Float) # 20%
    amount_lab = Column(Float)    # 10%
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())