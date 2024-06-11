from repository.bank_account import BankAccountRepository, bank_account_repository
from repository.customer import CustomerRepository, customer_repository
from database import BankAccount


class BankService:  # TODO: Add exception handling
    def __init__(self, bank_account_repository: BankAccountRepository, customer_repository: CustomerRepository):
        self.bank_account_repository = bank_account_repository
        self.customer_repository = customer_repository

    def add_new_bank_account(self, customer_id: int, card_number: str, password: str, cvv2: str, balance: float) -> bool:
        bank_account = self.bank_account_repository.get_by_card_number(card_number)
        if bank_account:
            return False
        new_bank_account = BankAccount(
            customer_id=customer_id,
            card_number=card_number,
            password=password,
            cvv2=cvv2,
            balance=balance
        )
        self.bank_account_repository.create(new_bank_account)
        return True

    def deposit_to_wallet(self, bank_account_id: int, password: str, amount: float) -> bool:
        bank_account = self.bank_account_repository.get_by_id(bank_account_id)
        if not bank_account or bank_account.password != password:
            return False

        if amount > bank_account.balance:
            return False

        customer = self.customer_repository.get_by_id(bank_account.customer_id)

        bank_account.balance -= amount
        customer.wallet += amount

        self.bank_account_repository.update(bank_account)
        self.customer_repository.update(customer)

        return True

    def withdraw_from_wallet(self, bank_account_id: int, amount: float) -> bool:
        bank_account = self.bank_account_repository.get_by_id(bank_account_id)
        if not bank_account:
            return False
        customer = self.customer_repository.get_by_id(bank_account.customer_id)
        if amount > customer.wallet:
            return False

        bank_account.balance += amount
        customer.wallet -= amount
        return True

    def transfer_to_another_account(self, sender_id: int, sender_password: str, receiver_id: int, amount: float) -> bool:
        sender = self.bank_account_repository.get_by_id(sender_id)
        receiver = self.bank_account_repository.get_by_id(receiver_id)
        if not sender or not receiver or sender.password != sender_password:
            return False
        if amount > sender.balance:
            return False
        sender.balance -= amount
        receiver.balance += amount
        return True


bank_service = BankService(bank_account_repository, customer_repository)
