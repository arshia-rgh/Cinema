# import User class

class BankAccount:
    _id = 0
    def __init__(self, user: User, card_number, password, cvv2, balance) -> None:
       self.id = BankAccount._id
       self.user = user
       self.card_number = card_number
       self.password = password
       self.cvv2 = cvv2
       self.balance = balance 

       BankAccount._id += 1 


    def take_money(self, amount):
        pass


    def add_money(self, amount):
        pass


    def transfer_money(self, amount, destination_account_id):
        pass

    
class Transaction:
    _id = 0
    def __init__(self, bank_account: BankAccount, user: User, type, status, transaction_date) -> None:
       self.id = Transaction._id
       self.bank_account = bank_account
       self.user = user
       self.type = type
       self.status = status
       self.transaction_date = transaction_date

       Transaction._id += 1 


class Subscription:
    _id = 0
    def __init__(self, user: User, type, expiry_date) -> None:
       self.id = Subscription._id
       self.user = user
       self.type = type
       self.expire_date = expiry_date

       Subscription._id += 1 
