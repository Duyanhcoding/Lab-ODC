import sys
import os

from fastapi import FastAPI
from src.database import engine
from src.domain.models import base # Import này để tạo bảng
from src.api.controllers import user_controller

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
# Tự động tạo bảng (chỉ dùng cho dev, production nên dùng migration)
base.Base.metadata.create_all(bind=engine)

app = FastAPI(title="LabOdc API")

# Đăng ký router
app.include_router(user_controller.router, prefix="/api/v1", tags=["Users"])
app.include_router(team_controller.router, prefix="/api/v1", tags=["Teams"])
app.include_router(payment_controller.router, prefix="/api/v1", tags=["Payments"])

@app.get("/")
def root():
    return {"message": "Welcome to LabOdc System"}