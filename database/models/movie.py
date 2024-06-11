from sqlalchemy import (CheckConstraint, Column, ForeignKey, Integer,
                        SmallInteger, String)
from sqlalchemy.orm import relationship, validates

from database.base import Base
from utils.exceptions import InvalidRateValueError


class Movie(Base):
    """
        subclasses Base class
        each object represents a row in Movie table
        Columns:
            -id
            -name
            -age_limit
            -rate {between 0 and 5}
    """

    __tablename__ = 'movies'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(length=100), nullable=False)
    age_limit = Column("age_limit", SmallInteger, nullable=False, default=1)
    rate = Column("rate", SmallInteger, default=None)

    comments = relationship("Comment",back_populates="movie")


    def __repr__(self): 
        return f"<Movie(name='{self.name}', age_limit='{self.age_limit}', rate='{self.rate}'>"
    

    @validates('rate')
    def validate_rate(self,value):
        if not 0 <= value <=5 :
            raise InvalidRateValueError(f'Invalid rate {value}')
        return value
    
