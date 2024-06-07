from sqlalchemy.orm import Session

from database.base import session
from database.bank_account import BankAccount
from schema.bank_account import BankAccountInDB, BankAccountOutput


class BankAccountRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[BankAccountOutput] | None:
        bank_accounts_db = self.db.query(BankAccount).all()
        bank_accounts = [BankAccountOutput(**account.__dict__) for account in bank_accounts_db]
        return bank_accounts

    def get_by_id(self, id: int) -> BankAccountOutput | None:
        bank_account_db = self.db.query(BankAccount).filter(BankAccount.id == id).first()
        if bank_account_db:
            bank_account = BankAccountOutput(**bank_account_db.__dict__)
            return bank_account
        return None

    def get_by_customer_id(self, user_id: int) -> list[BankAccountOutput] | None:
        bank_accounts_db = self.db.query(BankAccount).filter(BankAccount.customer_id == user_id).all()
        bank_accounts = [BankAccountOutput(**account.__dict__) for account in bank_accounts_db]
        return bank_accounts

    def create(self, item: BankAccountInDB) -> BankAccountOutput:  # should handle exceptions later
        bank_account_db = BankAccount(**item.__dict__)
        self.db.add(bank_account_db)
        self.db.commit()
        self.db.refresh(bank_account_db)
        bank_account = BankAccountOutput(**bank_account_db.__dict__)
        return bank_account

    def update(self, item: BankAccountInDB) -> BankAccountOutput:  # should handle exceptions later
        bank_account_db = self.db.query(BankAccount).filter(BankAccount.id == item.id).first()
        if bank_account_db:
            for key, value in item.__dict__.items():
                setattr(bank_account_db, key, value)
            self.db.commit()
            self.db.refresh(bank_account_db)
            bank_account = BankAccountOutput(**bank_account_db.__dict__)
            return bank_account
        return None

    def delete(self, id: int) -> bool:
        bank_account_db = self.db.query(BankAccount).filter(BankAccount.id == id).first()
        if bank_account_db:
            self.db.delete(bank_account_db)
            self.db.commit()
            return True
        return False


bank_account_repository = BankAccountRepository(session)
