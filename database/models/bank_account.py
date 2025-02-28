import sqlalchemy as db
from sqlalchemy.orm import relationship

from database.base import Base


class BankAccount(Base):
    """
    A BankAccount entity representing a customer's bank account in the database.

    Attributes:
        id (int): The unique identifier of the bank account.
        customer_id (int): The unique identifier of the customer who owns the bank account.
        card_number (str): The card number associated with the bank account.
        password (str): The password for the bank account.
        cvv2 (str): The CVV2 security code for the bank account.
        balance (float): The current balance of the bank account.

    Relationships:
        customer: The Customer entity that owns the bank account.
    """
    __tablename__ = 'bank_accounts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    card_number = db.Column(db.String(length=16), unique=True, nullable=False)
    password = db.Column(db.String(length=255), nullable=False)
    cvv2 = db.Column(db.String(length=3), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)

    customer = relationship('Customer', back_populates='bank_accounts')
