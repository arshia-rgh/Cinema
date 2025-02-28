from typing import Type

from sqlalchemy.orm import Session
from sqlalchemy import desc
from database.base import session
from database.models.movie import Movie
from repository.base import BaseRepository


class MovieRepository(BaseRepository):
    """
        All queries needed on movies are here. methods:
        - get_all
        - get_by_id
        - get_by_name
        - get_top_rated
        - create
        - update
        - update_rate (movie_id, rate)
        - delete
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Type[Movie]] | None:
        movies : list[Type[Movie]] = self.db.query(Movie).all()
        return movies

    def get_by_id(self, id: int) -> Type[Movie] | None:
        movie = self.db.query(Movie).filter(Movie.id == id).first()
        if movie:
            return movie
        return None

    def get_by_name(self, name: str) -> Type[Movie] | None:
        movie = self.db.query(Movie).filter(Movie.name.like(name)).all()
        if movie:
            return movie
        return None
    
    def get_top_rated(self, nums: int) -> list[Type[Movie]] | None:
        movies : list[Type[Movie]] =self.db.query(Movie).all().order_by(desc(Movie.rate))
        return movies[0:nums]

    def create(self, item: Movie) -> Movie:
        try:
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return item
        except Exception as e :
            self.db.rollback()
            # TODO: handle exceptions for rate and name values
            pass

    def update(self, item: Type[Movie]) -> Type[Movie]:
        movie = self.db.query(movie).filter(movie.id == item.id).first()
        if movie:
            try:
                movie = item
                self.db.commit()
                self.db.refresh(movie)
                return movie
            except Exception as e:
                self.db.rollback()
                # TODO: handle exceptions for rate and name values
                pass

        else:
            # TODO: raise appropriate exception, Not found movie
            pass

    def update_rate(self, movie_id: int, rate: float) -> bool:
        movie = self.get_by_id(movie_id)
        if movie:
            movie.rate = rate
            self.update(movie)
            return True
        return False
    
    def delete(self, id: int) -> bool:
        movie = self.db.query(Movie).filter(Movie.id == id).first()
        if movie:
            self.db.delete(movie)
            self.db.commit()
            return True
        return False

movie_repository = MovieRepository(session)
