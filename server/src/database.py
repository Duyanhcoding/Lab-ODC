# src/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.config import settings

# Tạo engine kết nối
engine = create_engine(
    settings.DATABASE_URL,
    echo=True, # In SQL ra log để debug
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class cho các Models kế thừa
Base = declarative_base()

# Dependency để lấy DB session (dùng cho API sau này)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()