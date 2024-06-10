import enum
import datetime
import sqlalchemy as db
from sqlalchemy.orm import relationship

from database.base import Base


class MyEnum(enum.Enum):
    """
    An enumeration representing the types of subscriptions.

    Attributes:
        bronze: Represents a bronze subscription.
        silver: Represents a silver subscription.
        gold: Represents a gold subscription.
    """
    bronze = 'bronze'
    silver = 'silver'
    gold = 'gold'


class Subscription(Base):
    """
      A Subscription entity representing a customer's subscription in the database.

      Attributes:
          id (int): The unique identifier of the subscription.
          customer_id (int): The unique identifier of the customer who owns the subscription.
          type (MyEnum): The type of the subscription (bronze, silver, gold).
          expire_date (datetime): The expiration date of the subscription.

      Relationships:
          customer: The Customer entity that owns the subscription.
      """
    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    type = db.Column(db.Enum(MyEnum), nullable=False, default=MyEnum.bronze)
    expire_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now() + datetime.timedelta(days=30))

    customer = relationship('Customer', back_populates='subscription')
