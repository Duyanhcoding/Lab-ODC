from fastapi import FastAPI
from database import test_connection, Base, engine
from database import init_db
from fastapi.responses import HTMLResponse

init_db()  # Tạo bảng khi khởi động

# Tạo bảng tự động nếu chưa có (dev only)
Base.metadata.create_all(bind=engine)

# Test kết nối DB khi khởi động
test_connection()

app = FastAPI(
    title="LabOdc API",
    description="Hệ thống quản lý kết nối doanh nghiệp - sinh viên UTH",
    version="1.0"
)

# Include các router (controller)
from api.controllers.project_controller import router as project_router
from api.controllers.team_controller import router as team_router
from api.controllers.fund_controller import router as fund_router
from api.controllers.report_controller import router as report_router

app.include_router(project_router, prefix="/api/v1")
app.include_router(team_router, prefix="/api/v1")
app.include_router(fund_router, prefix="/api/v1")
app.include_router(report_router, prefix="/api/v1")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>LabOdc API</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 100px; background: #f0f2f5; }
                h1 { color: #1a5fb4; }
                a { font-size: 20px; color: #1a5fb4; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <h1>Chào mừng đến với LabOdc API! 🚀</h1>
            <p>Hệ thống quản lý kết nối doanh nghiệp - sinh viên UTH</p>
            <p><a href="/docs" target="_blank">👉 Nhấp vào đây để mở Swagger Documentation</a></p>
            <p>Hoặc truy cập trực tiếp: <a href="/redoc">ReDoc</a></p>
        </body>
    </html>
    """