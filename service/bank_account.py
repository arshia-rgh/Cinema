import logging

from repository.bank_account import BankAccountRepository, bank_account_repository
from repository.customer import CustomerRepository, customer_repository
from database import BankAccount

logging.basicConfig(filename='transaction.log', level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)


class BankService:  # TODO: Add exception handling
    """
       A service class that handles operations related to bank accounts and customers.

       Attributes:
           bank_account_repository (BankAccountRepository): A repository for accessing bank account data.
           customer_repository (CustomerRepository): A repository for accessing customer data.
       """

    def __init__(self, bank_account_repository: BankAccountRepository, customer_repository: CustomerRepository):
        self.bank_account_repository = bank_account_repository
        self.customer_repository = customer_repository

    def add_new_bank_account(self, customer_id: int, card_number: str, password: str, cvv2: str,
                             balance: float) -> bool:
        """
                Adds a new bank account.

                Args:
                    customer_id (int): The ID of the customer.
                    card_number (str): The card number of the bank account.
                    password (str): The password of the bank account.
                    cvv2 (str): The CVV2 of the bank account.
                    balance (float): The initial balance of the bank account.

                Returns:
                    bool: True if the bank account was successfully added, False otherwise.
                """

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
        """
        Deposits an amount from a bank account to the associated customer's wallet.

        Args:
            bank_account_id (int): The ID of the bank account.
            password (str): The password of the bank account.
            amount (float): The amount to deposit.

        Returns:
            bool: True if the deposit was successful, False otherwise.
        """

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

        logger.info(f'Deposited {amount} to wallet of customer {customer.id} from bank account {bank_account.id}')

        return True

    def withdraw_from_wallet(self, bank_account_id: int, amount: float) -> bool:
        """
              Withdraws an amount from the associated customer's wallet to a bank account.

              Args:
                  bank_account_id (int): The ID of the bank account.
                  amount (float): The amount to withdraw.

              Returns:
                  bool: True if the withdrawal was successful, False otherwise.
              """

        bank_account = self.bank_account_repository.get_by_id(bank_account_id)
        if not bank_account:
            return False
        customer = self.customer_repository.get_by_id(bank_account.customer_id)
        if amount > customer.wallet:
            return False

        bank_account.balance += amount
        customer.wallet -= amount

        logger.info(f'Withdrew {amount} from wallet of customer {customer.id} to bank account {bank_account.id}')

        return True

    def transfer_to_another_account(self, sender_id: int, sender_password: str, receiver_id: int,
                                    amount: float) -> bool:
        """
             Transfers an amount from one bank account to another.

             Args:
                 sender_id (int): The ID of the sender's bank account.
                 sender_password (str): The password of the sender's bank account.
                 receiver_id (int): The ID of the receiver's bank account.
                 amount (float): The amount to transfer.

             Returns:
                 bool: True if the transfer was successful, False otherwise.
             """

        sender = self.bank_account_repository.get_by_id(sender_id)
        receiver = self.bank_account_repository.get_by_id(receiver_id)
        if not sender or not receiver or sender.password != sender_password:
            return False
        if amount > sender.balance:
            return False
        sender.balance -= amount
        receiver.balance += amount

        logger.info(f'Transferred {amount} from bank account {sender.id} to bank account {receiver.id}')

        return True


bank_service = BankService(bank_account_repository, customer_repository)
