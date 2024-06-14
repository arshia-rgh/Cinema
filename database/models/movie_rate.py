from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship, validates

from database.base import Base
from utils.exceptions import InvalidRateValueError


class MovieRate(Base):
    """
    A MovieRate entity representing a rate given to a movie in the database.
    - Attributes:
        - id (int): The unique identifier of the movierate.
        - customer_id (int): FK(customer.id) customer of the movierate.
        - movie_id (int): FK(Movie.id) movie id of the movieratez.
        - stars (int): customer given stars for the movie.
    - Relationships:
        - movie: the Movie which the movierate belongs to
        - customer: the customer which the movierate belongs to
        
    """

    __tablename__ = 'movie_rates'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    movie_id = Column("movie_id", Integer, ForeignKey("movies.id", ondelete='CASCADE'))
    customer_id = Column("customer_id", Integer, ForeignKey("customers.id", ondelete='CASCADE'))
    stars = Column("stars", Integer, default=0)

    movie = relationship("Movie", back_populates="stars")
    customer = relationship("Customer", back_populates="movie_rates")

    def __repr__(self):
        return f"<MovieRate(id= '{self.id}', customer= '{self.customer_id}', movie= '{self.movie_id}', stars= '{self.stars}'>"

    @validates('stars')
    def validate_stars(self, value):
        valid_stars = [0, 1, 2, 3, 4, 5]
        if value not in valid_stars:
            raise InvalidRateValueError(f'Invalid stars {value}')
        return value
