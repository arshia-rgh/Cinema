import sqlalchemy as db
from sqlalchemy.orm import relationship

from database.base import Base


class BankAccount(Base):
    __tablename__ = 'bank_accounts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.Foreingkey('customer.id'), nullable=False)
    card_number = db.Column(db.String(length=16), unique=True, nullable=False)
    password = db.Column(db.String(length=255), nullable=False)
    cvv2 = db.Column(db.String(length=3), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)

    customer = relationship('Customer', back_populates='bank_account')
