# LabOdc Backend

## 1. Giới thiệu

Đây là **Backend service** của dự án **Lab-ODC** – hệ thống kết nối doanh nghiệp và sinh viên UTH trong các dự án CNTT thực tế.

Backend được xây dựng nhằm:

* Cung cấp **RESTful APIs** cho hệ thống LabOdc.
* Quản lý dữ liệu: người dùng, dự án, mentor, báo cáo.
* Kết nối và thao tác với **PostgreSQL Database**.

Phiên bản hiện tại là **Backend Skeleton** phục vụ mục đích học tập trong môn **Công nghệ Phần mềm** (sinh viên năm 2).

---

## 2. Công nghệ sử dụng

* **Python 3.9+**
* **FastAPI** – Framework backend
* **SQLAlchemy** – ORM
* **PostgreSQL** – Database
* **Uvicorn** – ASGI Server
* **Docker & Docker Compose** – Môi trường chạy thống nhất

---

## 3. Cấu trúc thư mục Backend

```
LAB-ODC-BACKEND/
│
├── app/                    # Thư mục chính của source code
│   ├── __init__.py
│   │
│   ├── main.py             # Entry point của ứng dụng (FastAPI / Flask)
│   │
│   ├── core/               # Các cấu hình cốt lõi
│   │   ├── __init__.py
│   │   ├── config.py       # Load biến môi trường, config chung
│   │   ├── database.py     # Kết nối database
│   │   └── security.py     # Auth, JWT, hashing (nếu có)
│   │
│   ├── models/             # Định nghĩa model (ORM / schema)
│   │   ├── __init__.py
│   │   └── user.py         # Ví dụ model User
│   │
│   │
│   │
│   └── Dockerfile          # Dockerfile cho app
│
├── venv/                   # Virtual Environment (không khuyến khích commit)
│
├── .env                    # Biến môi trường (DB, SECRET_KEY…)
├── .gitignore              # Bỏ qua file không cần commit
├── docker-compose.yml      # Chạy nhiều service (app, db…)
├── requirements.txt        # Danh sách thư viện Python
└── README.md               # Mô tả project

```

---

## 4. Chuẩn bị môi trường

### 4.1. Yêu cầu

* Python >= 3.9
* PostgreSQL (nếu chạy local)
* Docker & Docker Compose (nếu chạy bằng Docker)

---

## 5. Chạy Backend trên máy cá nhân (Local)

### 5.1. Tạo môi trường ảo

```bash
cd backend
python -m venv venv
```

Kích hoạt môi trường ảo:

* **Windows**:

```bash
venv\Scripts\activate
```

* **Mac / Linux**:

```bash
source venv/bin/activate
```

---

### 5.2. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

### 5.3. Cấu hình Database

Tạo file `.env` trong thư mục `backend/`:

```env
DATABASE_URL=postgresql://postgres:150306@localhost:5432/labodc_db
```

---

### 5.4. Chạy server

```bash
uvicorn app.main:app --reload
```

Truy cập:

* API base: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 6. Kiểm tra kết nối Database

* Mở Swagger UI
* Chạy API:

```
GET /check-db
```

Nếu trả về:

```json
{
  "status": "Database Connected Successfully!"
}
```

=> Backend đã kết nối thành công với PostgreSQL.

---

## 7. Chạy Backend bằng Docker (Khuyến nghị cho nhóm)

### 7.1. Cách chạy

Tại thư mục gốc `LabOdc-Project`:

```bash
docker-compose up --build
```

Docker sẽ tự động:

* Build backend
* Khởi tạo PostgreSQL container
* Kết nối backend với database

---

## 8. Quy ước phát triển Backend

### 8.1. Branch

* `main`: code ổn định
* `develop`: code chính
* `feature/<ten>`: chức năng riêng

---

### 8.2. Commit message (gợi ý)

* `feat:` thêm API / chức năng
* `fix:` sửa lỗi
* `refactor:` chỉnh cấu trúc code
* `docs:` cập nhật tài liệu


---

## 9. Lưu ý quan trọng

* **Không push file `.env` lên GitHub**.
* Đây là backend học tập, chưa cấu hình production.
* Mọi thay đổi lớn cần báo với nhóm trưởng.

---

## 10. Liên hệ

* Nhóm thực hiện: Lab-ODC Team
* Môn học: Công nghệ Phần mềm
* Trường: Đại học Giao thông Vận tải TP.HCM (UTH)
>>>>>>> d01defb99187870942c9bfc4b9916952269237b4
