from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship,validates

from database.base import Base
from utils.exceptions import InvalidRateValueError

class CinemaRate(Base):
    """
    A CinemaRate entity representing a rate given to a cinema in the database.
    - Attributes:
        - id (int): The unique identifier of the CinemaRate.
        - cinema_id (int): FK(Cinema.id) cinema id of the cinemarate.
        - customer_id (int): FK(customer.id) customer of the cinemarate.
        - stars (int): customer given stars for the cinema.
    - Relationships:
        - cinema: the Cinema which the cinemarate belongs to
        - customer: the customer which the cinemarate belongs to
        
    """
    
    __tablename__ = 'cinema_rates'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    cinema_id = Column("cinema_id", Integer, ForeignKey("cinemas.id", ondelete='CASCADE'))
    customer_id = Column("customer_id", Integer, ForeignKey("customers.id", ondelete='CASCADE'))
    stars = Column("stars", Integer, default=0)

    cinema = relationship("Cinema", back_populates="stars")
    customer = relationship("Customer", back_populates="cinema_rates")

    def __repr__(self): 
        return f"<CinemaRate(id= '{self.id}', customer= '{self.customer_id}', cinema= '{self.cinema_id}', stars= '{self.stars}'>"
    
    @validates('stars')
    def validate_stars(self,value):
        valid_stars= [0,1,2,3,4,5]
        if value not in valid_stars:
            raise InvalidRateValueError(f'Invalid stars {value}')
        return value