from datetime import date, datetime

from database import User, Customer
from repository.customer import CustomerRepository, customer_repository
from repository.user import UserRepository, user_repository
from utils.password_hash import get_password_hash, verify_password


class AuthService:

    def __init__(self, user_repository: UserRepository, customer_repository: CustomerRepository):
        self.user_repository = user_repository
        self.customer_repository = customer_repository

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

    def create_customer(self, user: User, birth_date: date, registration_date: datetime) -> Customer:
        customer = Customer(
            user_id=user.id,
            wallet=0,
            birth_date=birth_date,
            registration_date=registration_date
        )
        customer = self.customer_repository.create(customer)
        return customer


auth_service = AuthService(user_repository, customer_repository)
