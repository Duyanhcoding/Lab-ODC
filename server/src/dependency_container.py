"""Dependency container và helpers cho ứng dụng

Chức năng:
- Cung cấp context manager `get_db_session()` để lấy SQLAlchemy session
- Hàm `init_application_db()` để gọi `init_db()` tạo bảng (dev only)
- `RepositoryContainer` chứa các repository được lazy-initialized

Lưu ý: KHÔNG sửa file `database.py` hay `config.py` theo yêu cầu.
"""
from contextlib import contextmanager
from typing import Optional

from database import SessionLocal, init_db


def init_application_db() -> None:
    """Khởi tạo (create_all) các bảng trong DB (dùng cho dev).
    Gọi hàm này lúc startup nếu cần đảm bảo bảng đã được tạo.
    """
    init_db()


@contextmanager
def get_db_session():
    """Context manager để cung cấp SQLAlchemy session và đảm bảo commit/rollback/close.

    Usage:
        with get_db_session() as db:
            # use db (Session)
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


class RepositoryContainer:
    """Container để khởi tạo các repository lazily. Sử dụng khi cần truyền nhiều repo.

    Ví dụ:
        with get_db_session() as db:
            container = RepositoryContainer(db)
            user_repo = container.user
    """

    def __init__(self, db_session):
        self.db = db_session
        self._user = None
        self._project = None
        self._team = None
        self._fund = None
        self._report = None

    @property
    def user(self):
        if self._user is None:
            from infrastructure.repositorties.user_repository import UserRepository

            self._user = UserRepository(self.db)
        return self._user

    @property
    def project(self):
        if self._project is None:
            from infrastructure.repositorties.project_repository import ProjectRepository

            self._project = ProjectRepository(self.db)
        return self._project

    @property
    def team(self):
        if self._team is None:
            from infrastructure.repositorties.team_repository import TeamRepository

            self._team = TeamRepository(self.db)
        return self._team

    @property
    def fund(self):
        if self._fund is None:
            from infrastructure.repositorties.fund_repository import FundRepository

            self._fund = FundRepository(self.db)
        return self._fund

    @property
    def report(self):
        if self._report is None:
            from infrastructure.repositorties.report_repository import ReportRepository

            self._report = ReportRepository(self.db)
        return self._report


def get_repository_container(db_session) -> RepositoryContainer:
    """Helper để tạo RepositoryContainer"""
    return RepositoryContainer(db_session)


__all__ = ["get_db_session", "init_application_db", "RepositoryContainer", "get_repository_container"]