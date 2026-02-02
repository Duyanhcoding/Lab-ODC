from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

# Hardcode DATABASE_URL để chạy chắc chắn (bỏ qua config và .env)
DATABASE_URL = "postgresql://postgres:150306@localhost:5432/labodc_db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
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

def init_db():
    """Tạo tất cả bảng nếu chưa tồn tại"""
    Base.metadata.create_all(bind=engine)
    print("✅ Đã tạo tất cả bảng trong database")