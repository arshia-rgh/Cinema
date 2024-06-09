from sqlalchemy import (CheckConstraint, Column, ForeignKey, Integer,
                        SmallInteger, String)
from sqlalchemy.orm import relationship, validates

from database.base import Base
from utils.exceptions import InvalidRateValueError

from .manager import Manager


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
    manager_id =("manager_id", Integer, ForeignKey("managers.id"))
    name = Column("name", String(length=50), nullable=False)
    rate = Column("rate", SmallInteger, default=None)

    manager = relationship("Manager", back_populates="cinemas")

    def __repr__(self): 
        return f"<Cinema(name='{self.name}', manager='{self.manager_id}', rate='{self.rate}'>"
    

    @validates('rate')
    def validate_rate(self,value):
        if not 0 <= value <=5 :
            raise InvalidRateValueError(f'Invalid rate {value}')
        return value
    
