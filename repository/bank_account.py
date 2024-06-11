from typing import Type

from sqlalchemy.orm import Session

from database.base import session
from database.models.bank_account import BankAccount
from repository.base import BaseRepository


class BankAccountRepository(BaseRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Type[BankAccount]] | None:
        bank_accounts = self.db.query(BankAccount).all()
        return bank_accounts

    def get_by_id(self, id: int) -> Type[BankAccount] | None:
        bank_account = self.db.query(BankAccount).filter(BankAccount.id == id).first()
        if bank_account:
            return bank_account
        return None

    def get_by_customer_id(self, customer_id: int) -> list[Type[BankAccount]] | None:
        bank_accounts = self.db.query(BankAccount).filter(BankAccount.customer_id == customer_id).all()
        return bank_accounts

    def create(self, item: BankAccount) -> BankAccount:  # TODO should handle exceptions later
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def update(self, item: Type[BankAccount]) -> Type[BankAccount]:  # TODO should handle exceptions later
        bank_account = self.db.query(BankAccount).filter(BankAccount.id == item.id).first()
        if bank_account:
            bank_account = item
            self.db.commit()
            self.db.refresh(bank_account)
            return bank_account
        return None

    def delete(self, id: int) -> bool:
        bank_account = self.db.query(BankAccount).filter(BankAccount.id == id).first()
        if bank_account:
            self.db.delete(bank_account)
            self.db.commit()
            return True
        return False


bank_account_repository = BankAccountRepository(session)
