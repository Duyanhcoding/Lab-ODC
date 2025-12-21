import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import domain.models.base
from api.controllers import user_controller, team_controller, payment_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LabOdc System API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_controller.router, prefix="/api/v1", tags=["Users"])
app.include_router(team_controller.router, prefix="/api/v1", tags=["Teams"])
app.include_router(payment_controller.router, prefix="/api/v1", tags=["Payments"])

@app.get("/")
def root():
    return {"status": "Running", "docs": "/docs"}