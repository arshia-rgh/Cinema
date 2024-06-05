# import User class
from enum import Enum

class BankAccount:
    def __init__(self, user: User, card_number, password, cvv2, balance) -> None:
       self.user = user
       self.card_number = card_number
       self.password = password
       self.cvv2 = cvv2
       self.balance = balance 


    def take_money(self, amount):
        pass


    def add_money(self, amount):
        pass


    def transfer_money(self, amount, bank_account_id):
        pass

    
class Transaction:
    def __init__(self, bank_account: BankAccount, user: User, type, status, transaction_date) -> None:
       self.bank_account = bank_account
       self.user = user
       self.type = type
       self.status = status
       self.transaction_date = transaction_date


class SubscriptionEnum(Enum):
    bronze = 1
    silver = 2
    gold = 3


class Subscription:
    def __init__(self, user: User, type: SubscriptionEnum, expiry_date) -> None:
       self.user = user
       self.type = type 
       self.expire_date = expiry_date
