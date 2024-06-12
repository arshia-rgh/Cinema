from typing import Type

from sqlalchemy.orm import Session

from database.base import session
from database.models.bank_account import BankAccount
from repository.base import BaseRepository


class BankAccountRepository(BaseRepository):
    """
    A repository for managing BankAccount entities in the database.

    Attributes:
        db (Session): The database session to use for queries.

    Methods:
        get_all(): Returns all BankAccount entities from the database.
        get_by_id(id: int): Returns the BankAccount entity with the given id.
        get_by_card_number(card_number: str): Returns the BankAccount entity with the given card number.
        get_by_customer_id(customer_id: int): Returns all BankAccount entities associated with the given customer id.
        create(item: BankAccount): Adds a new BankAccount entity to the database.
        update(item: BankAccount): Updates an existing BankAccount entity in the database.
        delete(id: int): Deletes the BankAccount entity with the given id from the database.
    """
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

    def get_by_card_number(self, card_number: str) -> Type[BankAccount] | None:
        bank_account = self.db.query(BankAccount).filter(BankAccount.card_number == card_number).first()
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
