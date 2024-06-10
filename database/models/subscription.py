import enum
import datetime
import sqlalchemy as db
from sqlalchemy.orm import relationship

from database.base import Base


class MyEnum(enum.Enum):
    bronze = 'bronze'
    silver = 'silver'
    gold = 'gold'


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    type = db.Column(db.Enum(MyEnum), nullable=False, default=MyEnum.bronze)
    expire_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now() + datetime.timedelta(days=30))

    customer = relationship('Customer', back_populates='subscription')
