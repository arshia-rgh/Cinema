import sqlalchemy as db

from database.base import Base
# from database.customer import Customer


class BankAccount(Base):
    __tablename__ = 'bank_accounts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.Foreingkey('customer.id'), nullable=False)
    card_number = db.Column(db.String(length=16), unique=True, nullable=False)
    password = db.Column(db.String(length=255), nullable=False)
    cvv2 = db.Column(db.String(length=3), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)
