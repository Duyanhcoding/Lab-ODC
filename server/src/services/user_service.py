from infrastructure.repositorties.user_repository import UserRepository


class UserService:
    def __init__(self, db_session):
        self.repo = UserRepository(db_session)

    def get(self, user_id: int):
        return self.repo.get_user_by_id(user_id)

    def list(self, skip: int = 0, limit: int = 100):
        return self.repo.list_users(skip=skip, limit=limit)

    def create(self, name: str, email: str, role: str = "USER"):
        # Prevent duplicate emails
        existing = self.repo.get_user_by_email(email)
        if existing:
            return None
        return self.repo.create_user(name=name, email=email, role=role)

    def update(self, user_id: int, **fields):
        user = self.repo.get_user_by_id(user_id)
        if not user:
            return None
        return self.repo.update_user(user, **fields)

    def delete(self, user_id: int):
        user = self.repo.get_user_by_id(user_id)
        if not user:
            return False
        return self.repo.delete_user(user)
