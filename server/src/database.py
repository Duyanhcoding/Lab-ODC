import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Format example: postgresql+psycopg2://user:pass@host:port/dbname
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:admin@localhost:5432/labodc")
SQL_ECHO = os.getenv("SQL_ECHO", "False").lower() in ("1", "true", "yes")

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=SQL_ECHO, pool_pre_ping=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
Base = declarative_base()


def init_db():
    """Create database tables for development. Use Alembic for real migrations."""
    Base.metadata.create_all(bind=engine)


__all__ = ["engine", "SessionLocal", "Base", "init_db"]