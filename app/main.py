from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.core import database
from app import models

app = FastAPI(
    title="Lab-ODC Backend API"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to LabODC System"}

@app.get("/users")
def get_users(db: Session = Depends(database.get_db)):
    return db.query(models.User).all()
