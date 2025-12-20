from contextlib import contextmanager
from database import SessionLocal, init_db


def init_application_db():
    """Initialize DB (create tables). Call once at startup."""
    init_db()


@contextmanager
def get_db_session():
    """Context manager that yields a SQLAlchemy session and ensures close/rollback."""
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

__all__ = ["get_db_session", "init_application_db"]
