import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Read connection URL from environment with a sensible default for local dev
# Format: postgresql://username:password@host:port/dbname
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:admin@localhost:5432/labodc")

# Create engine and session factory
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db():
	"""Create database tables. Call this at application startup."""
	Base.metadata.create_all(bind=engine)


__all__ = ["engine", "SessionLocal", "Base", "init_db"]