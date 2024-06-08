from datetime import datetime
from typing import Type

from sqlalchemy.orm import Session

from database.base import session
from database.models.user import User
from repository.base import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Type[User]] | None:
        users: list[Type[User]] = self.db.query(User).all()
        return users

    def get_by_id(self, id: int) -> Type[User] | None:
        user = self.db.query(User).filter(User.id == id).first()
        if user:
            return user
        return None

    def get_by_username(self, username: str) -> Type[User] | None:
        user = self.db.query(User).filter(User.username == username).first()
        if user:
            return user
        return None

    def get_by_email(self, email: str) -> Type[User] | None:
        user = self.db.query(User).filter(User.email == email).first()
        if user:
            return user
        return None

    def create(self, item: User) -> User:
        try:
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return user
        except Exception as e:
            self.db.rollback()
            # TODO raise appropriate exception, Duplicate Email or username
            pass

    def update(self, item: Type[User]) -> Type[User]:
        user = self.db.query(User).filter(User.id == item.id).first()
        if user:
            try:
                user = item
                self.db.commit()
                self.db.refresh(user)
                return user
            except Exception as e:
                self.db.rollback()
                # TODO raise appropriate exception, Duplicate Email or username
                pass

        else:
            # TODO raise appropriate exception, Not found user
            pass

    def delete(self, id: int) -> bool:
        user = self.db.query(User).filter(User.id == id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False

    def set_last_login_now(self, id: int):
        user: User = self.db.query(User).get(id)
        user.last_login = datetime.now()
        self.db.commit()


user_repository = UserRepository(session)
