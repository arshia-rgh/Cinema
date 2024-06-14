from sqlalchemy import Column, Integer, String, Float, SmallInteger
from sqlalchemy.orm import relationship, validates

from database.base import Base
from utils.exceptions import InvalidRateValueError


class Movie(Base):
    """
    A Movie entity representing a movie in the database.
    - Attributes:
        - id (int): The unique identifier of the movie.
        - name (str): name of the movie.
        - age_limit (int): customers above the age limit are allowed to reserve a ticket.
        - rate(int): average rate o the movie which is drieved from movie_rates table.
    - Relationships:
        - comments: a list of comments to the movie
        - stars: stars given to the movie
    """

    __tablename__ = 'movies'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(length=100), nullable=False)
    age_limit = Column("age_limit", SmallInteger, nullable=False, default=1)
    rate = Column("rate", Float, default=None)

    comments = relationship("Comment", back_populates="movie", cascade="all, delete")
    stars = relationship("MovieRate", back_populates='movie')

    def __repr__(self):
        return f"<Movie(name='{self.name}', age_limit='{self.age_limit}', rate='{self.rate}'>"

    @validates('rate')
    def validate_rate(self, value):
        if not 0.0 <= value <= 5.0 or None:
            raise InvalidRateValueError(f'Invalid rate {value}')
        return value
