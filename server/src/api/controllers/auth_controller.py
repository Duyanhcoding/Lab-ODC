from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(payload: dict):
    """Đăng nhập giả lập - chỉ dùng để test. Replace bằng auth thật khi cần."""
    username = payload.get("username")
    password = payload.get("password")
    if not username or not password:
        raise HTTPException(status_code=400, detail="Missing credentials")
    # Trả về token giả
    return {"access_token": "fake-token-for-" + username, "token_type": "bearer"}
