from database import User
from repository.user import UserRepository, user_repository
from utils.password_hash import get_password_hash, verify_password


class AuthService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, username: str, email: str, password: str, phone: str | None = None) -> User:
        user = User(
            username=username,
            email=email,
            password=get_password_hash(password)
        )
        if phone:
            user.phone = phone
        registered_user = self.user_repository.create(user)
        return registered_user

    def login_with_username(self, username: str, password: str) -> bool:
        user = self.user_repository.get_by_username(username)
        if verify_password(password, user.password):
            self.user_repository.set_last_login_now(user.id)
            return True
        return False

    def login_with_email(self, email: str, password: str) -> bool:
        user = self.user_repository.get_by_email(email)
        if verify_password(password, user.password):
            self.user_repository.set_last_login_now(user.id)
            return True
        return False


auth_service = AuthService(user_repository)
