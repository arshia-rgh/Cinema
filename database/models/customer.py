import sqlalchemy as db
from sqlalchemy.orm import relationship

from database.base import Base


class Customer(Base):
    """
    A Customer entity representing a customer in the database.
    - Attributes:
        - id (int): The UNIQUE identifier of the customer.
        - user_id (int): Fk(users.id).
        - wallet (float): The balance of the wallet.
        - birth_date (date): The date customer was born.
        - registration_date (date): The date customer was registered.
    - Relationships:
        - user: one-to-one relationship with user table.
        - bank_accounts: customer's bank accounts
        - subscription: one-to-one relationship indicating the customer's subscription level
        - cinema_rates: stars given by the customer to a cinema
        - movie_rates: stars given by the customer to a movie
    """

    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    wallet = db.Column(db.Float, nullable=False, default=0.0)
    birth_date = db.Column(db.Date)
    registration_date = db.Column(db.DateTime, default=db.func.now())

    user = relationship('User', back_populates='customer')
    movie_rates = relationship('MovieRate', back_populates='customer',cascade="all, delete")
    cinema_rates = relationship('CinemaRate', back_populates='customer',cascade="all, delete")
    bank_accounts = relationship('BankAccount', back_populates='customer')
    subscription = relationship('Subscription', back_populates='customer')