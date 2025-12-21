from fastapi import APIRouter

router = APIRouter(prefix="/audit", tags=["audit"])


@router.get("/")
def list_audit_logs():
    """Sample audit log endpoint - trả về danh sách rỗng hiện tại."""
    return []
