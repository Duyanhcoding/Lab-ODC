# src/dependency_container.py
from sqlalchemy.orm import Session
from infrastructure.repositories import user_repository, team_repository, payment_repository
from services import user_service, team_service, payment_service

class DependencyContainer:
    """
    Lớp này dùng để quản lý việc gọi các service.
    Vì bạn dùng FastAPI và inject DB qua Depends(get_db), 
    nên container này sẽ giúp gom nhóm các logic lại.
    """
    
    def __init__(self, db: Session):
        self.db = db

    # --- USER ---
    def get_user_service(self):
        return user_service

    # --- TEAM ---
    def get_team_service(self):
        return team_service

    # --- PAYMENT & FUND (Quy tắc 70/20/10) ---
    def get_payment_service(self):
        # Service này xử lý logic chia tiền LabOdc
        return payment_service

# Hàm helper để khởi tạo nhanh trong controller
def get_container(db: Session):
    return DependencyContainer(db)