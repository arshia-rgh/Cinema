from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship,validates

from database.base import Base
from utils.exceptions import InvalidRateValueError

class MovieRate(Base):
    """
    A MovieRate entity representing a rate given to a movie in the database.
    - Attributes:
        - id (int): The unique identifier of the movierate.
        - user_id (int): FK(User.id) user of the movierate.
        - movie_id (int): FK(Movie.id) movie id of the movieratez.
        - stars (int): user given stars for the movie.
    - Relationships:
        - movie: the Movie which the movierate belongs to
        - user: the User which the movierate belongs to
        
    """
    
    __tablename__ = 'movie_rates'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    movie_id = Column("movie_id", Integer, ForeignKey("movies.id", ondelete='CASCADE'))
    user_id = Column("user_id", Integer, ForeignKey("users.id", ondelete='CASCADE'))
    stars = Column("stars", Integer, default=0)

    movie = relationship("Movie", back_populates="stars")
    user = relationship("User", back_populates="movie_rates")

    def __repr__(self): 
        return f"<MovieRate(id= '{self.id}', User= '{self.user_id}', movie= '{self.movie_id}', stars= '{self.stars}'>"
    
    @validates('stars')
    def validate_stars(self,value):
        valid_stars= [0,1,2,3,4,5]
        if value not in valid_stars:
            raise InvalidRateValueError(f'Invalid stars {value}')
        return value