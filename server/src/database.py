from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from config import settings


Base = declarative_base()


engine = create_engine(
    settings.DATABASE_URL,
    echo=True,          # In SQL ra console để học
    pool_pre_ping=True
)


SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✅ Kết nối PostgreSQL thành công:", result.scalar())
    except Exception as e:
        print("❌ Kết nối thất bại:", e)
