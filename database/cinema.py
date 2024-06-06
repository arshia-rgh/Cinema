from sqlalchemy import (CheckConstraint, Column, ForeignKey, Integer,
                        SmallInteger, String, orm)

from .base import Base
from .manager import Manager
from utils.exceptions import InvalidRateValueError

class Cinema(Base):
    """
    subclasses Base class
    each object represents a row in Cinema table
    Columns:
        - id
        - name
        - manager_id
        - rate {between 0 and 5}
    """

    __tablename__ = 'cinemas'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    manager_id =("manager_id", Integer, ForeignKey("Manager.id"))
    name = Column("name", String(length=50), nullable=False, unique=True)
    rate = Column("rate", SmallInteger, CheckConstraint('rate >= 0 AND rate <=5'), default=None)


    def __repr__(self): 
        return f"<Cinema(name='{self.name}', manager='{self.manager_id}', rate='{self.rate}'>"
    

    @orm.validates('rate')
    def validate_rate(self,value):
        if not 0 <= value <=5 :
            raise InvalidRateValueError(f'Invalid rate {value}')
        return value
    
